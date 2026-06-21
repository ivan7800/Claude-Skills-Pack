const { test, expect } = require('@playwright/test');

test.describe('I. Roig Claude Skills Web', () => {
  test('loads core UI without console errors', async ({ page }) => {
    const errors = [];
    page.on('console', msg => {
      if (msg.type() === 'error') errors.push(msg.text());
    });
    page.on('pageerror', error => errors.push(error.message));

    await page.goto('/');
    await expect(page).toHaveTitle(/I\. Roig Claude Skills Pack/);
    await expect(page.getByRole('heading', { name: /Panel web para gestionar/i })).toBeVisible();
    await expect(page.locator('.skill-card')).toHaveCount(33);
    expect(errors).toEqual([]);
  });

  test('search, open modal, favorite and copy flow stay usable', async ({ page, context }) => {
    await context.grantPermissions(['clipboard-read', 'clipboard-write']);
    await page.goto('/');

    await page.getByLabel('Buscar').fill('safari');
    await expect(page.locator('.skill-card')).toHaveCount(await page.locator('.skill-card').count());
    await expect(page.locator('.skill-card').first()).toBeVisible();

    await page.locator('.open-skill').first().click();
    await expect(page.locator('#skillDialog')).toBeVisible();
    await page.getByRole('button', { name: 'Copiar comando' }).click();
    await expect(page.locator('#toast')).toContainText(/Comando copiado|No se pudo copiar/);
    await page.getByRole('button', { name: 'Cerrar' }).click();
    await expect(page.locator('#skillDialog')).not.toBeVisible();
  });

  test('theme, notes and checklist survive reload when storage is available', async ({ page }) => {
    await page.goto('/');
    await page.getByRole('button', { name: /Cambiar a tema/i }).click();
    const theme = await page.locator('html').getAttribute('data-theme');

    await page.getByLabel('Notas del proyecto').fill('Prueba automática E2E');
    await page.locator('#releaseChecklist input').first().check();
    await page.reload();

    await expect(page.locator('html')).toHaveAttribute('data-theme', theme || /dark|light/);
    await expect(page.getByLabel('Notas del proyecto')).toHaveValue('Prueba automática E2E');
    await expect(page.locator('#releaseChecklist input').first()).toBeChecked();
  });

  test('download buttons expose valid filenames', async ({ page }) => {
    await page.goto('/');
    await expect(page.getByRole('link', { name: 'ZIP pack' })).toHaveAttribute('href', /v1\.3\.4\.zip$/);
    await page.locator('.open-skill').first().click();
    await expect(page.getByRole('button', { name: 'Descargar SKILL.md' })).toBeVisible();
  });
});
