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
    
    const unwrapped = await page.evaluate(() => {
      const issues = [];
      const divs = document.querySelectorAll('div');
      for (const div of divs) {
        for (const node of div.childNodes) {
          if (node.nodeType === Node.TEXT_NODE) {
            const txt = node.textContent.trim();
            if (txt) {
              issues.push({
                className: div.className,
                id: div.id,
                text: txt,
                html: div.outerHTML.substring(0, 100)
              });
            }
          }
        }
      }
      return issues;
    });

    if (unwrapped.length > 0) {
      console.log(`[ISSUES] ${file}:`);
      for (const item of unwrapped) {
        console.log(`  - class="${item.className}": "${item.text}"`);
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
