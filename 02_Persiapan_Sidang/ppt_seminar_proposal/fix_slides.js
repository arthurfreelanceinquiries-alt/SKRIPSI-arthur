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
      const blockTags = new Set(['P', 'H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'UL', 'OL', 'TABLE', 'FORM', 'BLOCKQUOTE']);
      const divs = Array.from(document.querySelectorAll('div'));

      for (const div of divs) {
        let hasDirectText = false;
        for (const node of div.childNodes) {
          if (node.nodeType === Node.TEXT_NODE && node.textContent.trim()) {
            hasDirectText = true;
            break;
          }
        }

        if (hasDirectText) {
          // If the div only contains text or inline tags (span, strong, em, a, etc.), wrap its contents in <p>
          const hasBlockChild = Array.from(div.children).some(c => blockTags.has(c.tagName));
          if (!hasBlockChild) {
            const p = document.createElement('p');
            while (div.firstChild) {
              p.appendChild(div.firstChild);
            }
            div.appendChild(p);
          } else {
            // It has both direct text and block children. Wrap individual direct text nodes in <p>
            const nodes = Array.from(div.childNodes);
            for (const node of nodes) {
              if (node.nodeType === Node.TEXT_NODE && node.textContent.trim()) {
                const p = document.createElement('p');
                p.textContent = node.textContent;
                div.insertBefore(p, node);
                div.removeChild(node);
              }
            }
          }
        }
      }
    });

    const updatedHtml = await page.content();
    fs.writeFileSync(filePath, updatedHtml, 'utf8');
    console.log(`Updated ${file}`);
  }

  await browser.close();
}

main().catch(err => {
  console.error(err);
  process.exit(1);
});
