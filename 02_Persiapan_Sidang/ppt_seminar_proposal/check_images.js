const fs = require('fs');
const path = require('path');
const slidesDir = path.resolve(__dirname, 'slides');
const assetsDir = path.resolve(__dirname, 'assets');

fs.readdirSync(slidesDir).filter(f => f.endsWith('.html')).sort().forEach(f => {
  const content = fs.readFileSync(path.join(slidesDir, f), 'utf8');
  const regex = /src=["']([^"']+)["']/g;
  let m;
  while ((m = regex.exec(content)) !== null) {
    const src = m[1];
    if (src.includes('assets/')) {
      const base = path.basename(src);
      const exists = fs.existsSync(path.join(assetsDir, base));
      console.log(`${f}: ${base} -> ${exists ? 'OK' : 'MISSING'}`);
      if (!exists && base === 'gambar1_1_media_franchises_ranking.png') {
        const fixed = content.replace(/gambar1_1_media_franchises_ranking\.png/g, 'gambar1_1_media_franchise_ranking.png');
        fs.writeFileSync(path.join(slidesDir, f), fixed, 'utf8');
        console.log(`  Fixed in ${f}!`);
      }
    }
  }
});
