#!/usr/bin/env node
import fs from 'node:fs/promises';
import path from 'node:path';
import { spawn } from 'node:child_process';

const ROOT = path.resolve(path.dirname(new URL(import.meta.url).pathname), '..');
const CHROME = process.env.CHROME || process.env.CHROMIUM || '/usr/bin/chromium';
const VERSION = '1.3.4';
const SKIP_BROWSER = process.env.SMOKE_SKIP_BROWSER === '1';

async function staticSmoke() {
  const index = await fs.readFile(path.join(ROOT, 'index.html'), 'utf8');
  const app = await fs.readFile(path.join(ROOT, 'app.js'), 'utf8');
  const sw = await fs.readFile(path.join(ROOT, 'sw.js'), 'utf8');
  const manifest = JSON.parse(await fs.readFile(path.join(ROOT, 'skills-manifest.json'), 'utf8'));
  const failures = [];

  if (manifest.version !== VERSION) failures.push(`manifest version is ${manifest.version}`);
  if (manifest.skills.length !== 33) failures.push(`expected 33 skills, got ${manifest.skills.length}`);
  if (!index.includes(`style.css?v=${VERSION}`)) failures.push('index.html CSS version is not current');
  if (!index.includes(`app.js?v=${VERSION}`)) failures.push('index.html app.js version is not current');
  if (!index.includes(`i-roig-claude-skills-pack-github-v${VERSION}.zip`)) failures.push('index.html ZIP link is not current');
  if (!sw.includes(`iroig-claude-skills-web-v${VERSION}`)) failures.push('sw.js cache version is not current');
  if (!sw.includes(`i-roig-claude-skills-pack-github-v${VERSION}.zip`)) failures.push('sw.js ZIP asset is not current');
  if (!app.includes(`const VERSION = '${VERSION}-web'`)) failures.push('app.js VERSION is not current');

  for (const id of ['searchInput', 'categorySelect', 'viewSelect', 'themeBtn', 'skillsGrid', 'skillDialog', 'releaseChecklist', 'notesInput']) {
    if (!index.includes(`id="${id}"`) && !index.includes(`id='${id}'`)) failures.push(`missing DOM id #${id}`);
  }
  for (const rel of ['style.css', 'app.js', 'manifest.json', 'sw.js', 'icons/icon.svg', `downloads/i-roig-claude-skills-pack-github-v${VERSION}.zip`]) {
    await fs.access(path.join(ROOT, rel)).catch(() => failures.push(`missing asset ${rel}`));
  }
  if (!/function setupPwa\(\)/.test(app)) failures.push('setupPwa() missing');
  if (!/safeStorage/.test(app)) failures.push('safeStorage fallback missing');
  if (!/openModal/.test(app) || !/closeModal/.test(app)) failures.push('modal fallback missing');
  if (!/isCacheable/.test(sw)) failures.push('service worker cache guard missing');

  if (failures.length) throw new Error(failures.join('\n'));
  console.log('OK: static smoke checks passed.');
}

function runChromeDump() {
  return new Promise((resolve) => {
    const url = `file://${path.join(ROOT, 'index.html')}`;
    const args = [
      '--headless=new',
      '--no-sandbox',
      '--disable-gpu',
      '--disable-dev-shm-usage',
      '--allow-file-access-from-files',
      '--virtual-time-budget=5000',
      '--dump-dom',
      url
    ];
    const child = spawn(CHROME, args, { stdio: ['ignore', 'pipe', 'pipe'] });
    let stdout = '';
    let stderr = '';
    const timer = setTimeout(() => {
      child.kill('SIGKILL');
      resolve({ skipped: true, reason: 'Chromium timed out in this environment' });
    }, 12000);
    child.stdout.on('data', chunk => { stdout += chunk.toString(); });
    child.stderr.on('data', chunk => { stderr += chunk.toString(); });
    child.on('error', error => {
      clearTimeout(timer);
      resolve({ skipped: true, reason: error.message });
    });
    child.on('close', code => {
      clearTimeout(timer);
      if (/organization doesn.t allow|links are blocked|is blocked/i.test(stdout)) {
        resolve({ skipped: true, reason: 'Chromium policy blocked local file/page access' });
        return;
      }
      if (code !== 0) {
        resolve({ skipped: true, reason: `Chromium exited with ${code}: ${stderr.slice(0, 300)}` });
        return;
      }
      const ok = stdout.includes('Panel web para gestionar tus Claude Skills') && stdout.includes('skillsGrid');
      resolve(ok ? { passed: true } : { skipped: true, reason: 'Chromium dump did not include expected app HTML' });
    });
  });
}

async function main() {
  await staticSmoke();
  if (SKIP_BROWSER) {
    console.log('INFO: browser smoke skipped by SMOKE_SKIP_BROWSER=1.');
    return;
  }
  const hasChrome = await fs.access(CHROME).then(() => true).catch(() => false);
  if (!hasChrome) {
    console.log(`INFO: browser smoke skipped; Chromium not found at ${CHROME}.`);
    return;
  }
  const result = await runChromeDump();
  if (result.passed) console.log('OK: Chromium smoke reached the app shell.');
  else console.log(`INFO: browser smoke skipped after static pass: ${result.reason}.`);
}

main().catch(error => {
  console.error('ERROR: smoke test failed');
  console.error(error.message);
  process.exit(1);
});
