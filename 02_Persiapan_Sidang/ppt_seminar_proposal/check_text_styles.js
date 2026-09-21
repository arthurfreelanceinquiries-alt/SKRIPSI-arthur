const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { pathToFileURL } = require('url');

async function main() {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const slidesDir = path.resolve(__dirname, 'slides');
  const files = fs.readdirSync(slidesDir).filter(f => f.endsWith('.html')).sort();

  const textTags = ['P', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'UL', 'OL', 'LI', 'SPAN'];

  for (const file of files) {
    const filePath = path.join(slidesDir, file);
    await page.goto(pathToFileURL(filePath).href);

    const issues = await page.evaluate(() => {
      const textTags = ['P', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6'];
      const errors = [];
      document.querySelectorAll('*').forEach(el => {
        if (textTags.includes(el.tagName)) {
          const computed = window.getComputedStyle(el);
          const hasBg = computed.backgroundColor && computed.backgroundColor !== 'rgba(0, 0, 0, 0)';
          const hasBgImage = computed.backgroundImage && computed.backgroundImage !== 'none';
          const hasBorder = (computed.borderWidth && parseFloat(computed.borderWidth) > 0) ||
            (computed.borderTopWidth && parseFloat(computed.borderTopWidth) > 0) ||
            (computed.borderRightWidth && parseFloat(computed.borderRightWidth) > 0) ||
            (computed.borderBottomWidth && parseFloat(computed.borderBottomWidth) > 0) ||
            (computed.borderLeftWidth && parseFloat(computed.borderLeftWidth) > 0);
          const hasShadow = computed.boxShadow && computed.boxShadow !== 'none';

          if (hasBg || hasBgImage || hasBorder || hasShadow) {
            errors.push({
              tag: el.tagName,
              className: el.className,
              issue: hasBg ? 'bg' : hasBorder ? 'border' : 'shadow',
              text: el.textContent.trim().substring(0, 40)
            });
          }
        }
      });
      return errors;
    });

    if (issues.length > 0) {
      console.log(`[ISSUES] ${file}:`);
      for (const iss of issues) {
        console.log(`  - <${iss.tag} class="${iss.className}"> has ${iss.issue} ("${iss.text}")`);
      }
    } else {
      console.log(`[OK] ${file}`);
    }
  }

  await browser.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
