import re

with open("01_Naskah_Utama/Proposal_Arthur_PokemonTCG.tex", encoding="utf-8") as f:
    tex = f.read()

cites = re.findall(r"\\cite[a-z]*\{([^}]+)\}", tex)
all_cites = set()
for c in cites:
    for k in c.split(","):
        k = k.strip()
        if k:
            all_cites.add(k)

with open("01_Naskah_Utama/references.bib", encoding="utf-8") as f:
    bib = f.read()
keys = set(re.findall(r"@\w+\{([^,]+),", bib))

print("Total unique cites in TeX:", len(all_cites))
print("Total keys in Bib:", len(keys))
print("Cites not in Bib:", all_cites - keys)
print("Bib not in Cites:", keys - all_cites)
