## Changelog : tacct (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'accessibilité du site, l'ajout de nouvelles données territoriales (977, 978, 987, 988) et la correction de plusieurs bugs, notamment liés à la gestion des paramètres de recherche et des infobulles. Des améliorations de l'interface utilisateur et de la configuration ont également été apportées.

### Évolutions fonctionnelles
- Ajout de données pour les nouveaux territoires : 977, 978, 988 et 987. [#71909b45](https://github.com/incubateur-ademe/tacct/commit/71909b45)
- Ajout d'une page thématique et d'un article pour le MEp (Maison de l'Économie Publique). [#40ba6f9f](https://github.com/incubateur-ademe/tacct/commit/40ba6f9f)
- Amélioration de l'accessibilité : navigation au clavier pour les collections. [#33a6c487](https://github.com/incubateur-ademe/tacct/commit/33a6c487)
- Ajout d'ancres pour les indicateurs, améliorant l'accessibilité. [#4862f421](https://github.com/incubateur-ademe/tacct/commit/4862f421)
- Ajout des données de prélèvement en eau. [#9297b4d9](https://github.com/incubateur-ademe/tacct/commit/9297b4d9)
- Correction de l'affichage des infobulles pour les diagrammes circulaires (agriculture). [#456661b7](https://github.com/incubateur-ademe/tacct/commit/456661b7) et [#d0c2f005](https://github.com/incubateur-ademe/tacct/commit/d0c2f005)
- Amélioration de l'affichage des cartes slider. [#8c8d7cd1](https://github.com/incubateur-ademe/tacct/commit/8c8d7cd1)

### Évolutions techniques
- Mise à jour de Next.js. [#2d9ac829](https://github.com/incubateur-ademe/tacct/commit/2d9ac829)
- Génération de Prisma. [#0cfae0a8](https://github.com/incubateur-ademe/tacct/commit/0cfae0a8) et [#f1e2b4c6](https://github.com/incubateur-ademe/tacct/commit/f1e2b4c6)
- Correction de l'utilisation de `useSearchParams` en mode suspense. [#560d66a6](https://github.com/incubateur-ademe/tacct/commit/560d66a6) et [#e609c69f](https://github.com/incubateur-ademe/tacct/commit/e609c69f) et [#48e1af21](https://github.com/incubateur-ademe/tacct/commit/48e1af21)
- Suppression de logs de console inutiles. [#22c2dee0](https://github.com/incubateur-ademe/tacct/commit/22c2dee0)

### Autres changements
- Correction de coquilles textuelles. [#f92793b2](https://github.com/incubateur-ademe/tacct/commit/f92793b2)
- Suppression d'une notification de maintenance. [#9d257a0d](https://github.com/incubateur-ademe/tacct/commit/9d257a0d) et [#b3bf3bf0](https://github.com/incubateur-ademe/tacct/commit/b3bf3bf0)
- Mise à jour de la documentation concernant l'accessibilité. [#f2eb8088](https://github.com/incubateur-ademe/tacct/commit/f2eb8088)
- Travaux d'accessibilité : implémentation des critères RGAA (Référentiel Général d'Accessibilité des Applications). [#c278d3d1](https://github.com/incubateur-ademe/tacct/commit/c278d3d1) et autres commits liés à l'accessibilité.
- Suppression de contenu obsolète (facili des textes et metadata). [#2dd17bd5](https://github.com/incubateur-ademe/tacct/commit/2dd17bd5)
- Correction de l'heure de la notification d'information. [#6f490774](https://github.com/incubateur-ademe/tacct/commit/6f490774)
- Correction de l'intégrité du SHA pour les fichiers XLSX. [#61e1c16b](https://github.com/incubateur-ademe/tacct/commit/61e1c16b)
