const fs = require('fs');
const path = require('path');
const { chromium } = require('playwright');
const { pathToFileURL } = require('url');

async function main() {
  const browser = await chromium.launch();
  const page = await browser.newPage();
  const slidesDir = path.resolve(__dirname, 'slides');
  const files = fs.readdirSync(slidesDir).filter(f => f.endsWith('.html')).sort();

  for (const file of files) {
    const filePath = path.join(slidesDir, file);
    await page.goto(pathToFileURL(filePath).href);

    await page.evaluate(() => {
      const textTags = ['P', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6'];
      
      // We repeatedly find text tags that have bg/border/shadow and convert them to div + inner p
      let changed = true;
      while (changed) {
        changed = false;
        const elements = Array.from(document.querySelectorAll('*'));
        for (const el of elements) {
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
              // Convert this text element to a div, with an internal p
              const div = document.createElement('div');
              div.className = el.className;
              if (el.id) div.id = el.id;
              if (el.getAttribute('style')) div.setAttribute('style', el.getAttribute('style'));

              const p = document.createElement('p');
              while (el.firstChild) {
                p.appendChild(el.firstChild);
              }
              div.appendChild(p);

              el.parentNode.replaceChild(div, el);
              changed = true;
              break; // restart querySelectorAll
            }
          }
        }
      }
    });

    const updatedHtml = await page.content();
    fs.writeFileSync(filePath, updatedHtml, 'utf8');
    console.log(`Processed style fixes for ${file}`);
  }

  await browser.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
