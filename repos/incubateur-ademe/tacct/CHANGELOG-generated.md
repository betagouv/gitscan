## Changelog : tacct (30 derniers jours, au 18 juin 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations de l'accessibilité du site, notamment via l'implémentation des critères RGAA. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées, ainsi que l'ajout de nouvelles données territoriales et de nouvelles pages thématiques.

### Évolutions fonctionnelles
- Ajout de nouveaux territoires : 977, 978, 988 et 987 [#71909b45](https://github.com/incubateur-ademe/tacct/commit/71909b45).
- Ajout d'une page thématique et d'un article MEAP (Maison de l'Environnement et des Paysages) [#40ba6f9f](https://github.com/incubateur-ademe/tacct/commit/40ba6f9f).
- Amélioration de l'accessibilité des indicateurs avec des ancres [#4862f421](https://github.com/incubateur-ademe/tacct/commit/4862f421).
- Amélioration de l'accessibilité des collections avec la navigation au clavier [#33a6c487](https://github.com/incubateur-ademe/tacct/commit/33a6c487).
- Ajout de données sur les prélèvements en eau [#9297b4d9](https://github.com/incubateur-ademe/tacct/commit/9297b4d9).
- Correction de l'affichage des tooltips pour les diagrammes circulaires (agriculture) [#456661b7](https://github.com/incubateur-ademe/tacct/commit/456661b7) et en général [#d0c2f005](https://github.com/incubateur-ademe/tacct/commit/d0c2f005).
- Correction de l'affichage des tooltips pour les feux de forêt [#a9aa50a6](https://github.com/incubateur-ademe/tacct/commit/a9aa50a6).

### Évolutions techniques
- Mise à jour de Next.js [#2d9ac829](https://github.com/incubateur-ademe/tacct/commit/2d9ac829).
- Génération de Prisma [#0cfae0a8](https://github.com/incubateur-ademe/tacct/commit/0cfae0a8) et [#f1e2b4c6](https://github.com/incubateur-ademe/tacct/commit/f1e2b4c6).
- Correction de l'utilisation de `useSearchParams` en mode suspense [#560d66a6](https://github.com/incubateur-ademe/tacct/commit/560d66a6) et [#e609c69f](https://github.com/incubateur-ademe/tacct/commit/e609c69f) et [#48e1af21](https://github.com/incubateur-ademe/tacct/commit/48e1af21).
- Suppression de logs de console inutiles [#22c2dee0](https://github.com/incubateur-ademe/tacct/commit/22c2dee0).

### Autres changements
- Amélioration de l'accessibilité : implémentation de nombreux critères RGAA (1 à 12) [#c278d3d1](https://github.com/incubateur-ademe/tacct/commit/c278d3d1), [#753ea966](https://github.com/incubateur-ademe/tacct/commit/753ea966), [#b90dc203](https://github.com/incubateur-ademe/tacct/commit/b90dc203), [#454244e5](https://github.com/incubateur-ademe/tacct/commit/454244e5), [#01cb8131](https://github.com/incubateur-ademe/tacct/commit/01cb8131), [#d03223d3](https://github.com/incubateur-ademe/tacct/commit/d03223d3), [#8539cd5b](https://github.com/incubateur-ademe/tacct/commit/8539cd5b), [#dfd8f5c8](https://github.com/incubateur-ademe/tacct/commit/dfd8f5c8).
- Suppression d'une notice de maintenance [#9d257a0d](https://github.com/incubateur-ademe/tacct/commit/9d257a0d) et [#b3bf3bf0](https://github.com/incubateur-ademe/tacct/commit/b3bf3bf0) et [#6f490774](https://github.com/incubateur-ademe/tacct/commit/6f490774).
- Correction de coquilles textuelles [#f92793b2](https://github.com/incubateur-ademe/tacct/commit/f92793b2).
- Amélioration du style des cartes slider [#8c8d7cd1](https://github.com/incubateur-ademe/tacct/commit/8c8d7cd1).
- Correction de l'intégrité du SHA pour les fichiers XLSX [#61e1c16b](https://github.com/incubateur-ademe/tacct/commit/61e1c16b).
