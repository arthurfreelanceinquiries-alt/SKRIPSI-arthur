# Graph Report - Skripsi  (2026-08-30)

## Corpus Check
- Large corpus: 291 files · ~1,308,240 words. Semantic extraction will be expensive (many Claude tokens). Consider running on a subfolder.

## Summary
- 18 nodes · 24 edges · 5 communities (4 shown, 1 thin omitted)
- Extraction: 92% EXTRACTED · 8% INFERRED · 0% AMBIGUOUS · INFERRED: 2 edges (avg confidence: 0.85)
- Token cost: 0 input · 0 output

## Community Hubs (Navigation)
- Website UI & Navigation
- Website Counter Animation

## God Nodes (most connected - your core abstractions)
1. `init()` - 11 edges
2. `initMobileMenu()` - 2 edges
3. `updateActiveNavLink()` - 2 edges
4. `handleNavbarScroll()` - 2 edges
5. `initRevealAnimations()` - 2 edges
6. `animateCountUp()` - 2 edges
7. `initStatAnimations()` - 2 edges
8. `initBarAnimations()` - 2 edges
9. `initSmoothScroll()` - 2 edges
10. `handleResize()` - 2 edges

## Surprising Connections (you probably didn't know these)
- None detected - all connections are within the same source files.

## Import Cycles
- None detected.

## Communities (5 total, 1 thin omitted)

### Community 0 - "Website UI & Navigation"
Cohesion: 0.28
Nodes (11): handleNavbarScroll(), handleResize(), init(), initBackToTop(), initBarAnimations(), initDynamicYear(), initMobileMenu(), initRevealAnimations() (+3 more)

## Knowledge Gaps
- **1 thin communities (<3 nodes) omitted from report** — run `graphify query` to explore isolated nodes.

## Suggested Questions
_Questions this graph is uniquely positioned to answer:_

- **Why does `animateCountUp()` connect `Website Counter Animation` to `Website UI & Navigation`?**
  _High betweenness centrality (0.096) - this node is a cross-community bridge._