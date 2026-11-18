## Changelog : mutafriches (30 derniers jours, au 17 novembre 2026)

### Résumé
Ce mois-ci, l'application a bénéficié de nouvelles capacités de consultation grâce à l'ajout d'une table des attributaires par commune. L'expérience utilisateur a été affinée par une amélioration de la lisibilité des infobulles et une mise en conformité des exports PDF. Parallèlement, la cartographie a été optimisée et la sécurité du pipeline de déploiement a été renforcée.

### Évolutions fonctionnelles
- Ajout d'une table permettant de consulter les attributaires des sites par commune [#262](https://github.com/incubateur-ademe/mutafriches/pull/262)
- Amélioration de la lisibilité des infobulles dans les modales de détail d'usage [#267](https://github.com/incubateur-ademe/mutafriches/pull/267)
- Mise en conformité des exports PDF avec les maquettes et correction de la typographie Marianne [#268](https://github.com/incubateur-ademe/mutafriches/pull/268)
- Rétablissement du bloc-marque République Française dans le pied de page [#276](https://github.com/incubateur-ademe/mutafriches/pull/276)

### Évolutions techniques
- Optimisation de la cartographie Metabase via l'hébergement du fond de carte EPCI et le retrait des zones d'outre-mer pour une meilleure clarté [#269](https://github.com/incubateur-ademe/mutafriches/pull/269), [#270](https://github.com/incubateur-ademe/mutafriches/pull/270)
- Correction de la récupération d'URL et ajout des identifiants de parcelles dans les iframes [#266](https://github.com/incubateur-ademe/mutafriches/pull/266)
- Résolution de vulnérabilités de sécurité bloquant le pipeline CI [#263](https://github.com/incubateur-ademe/mutafriches/pull/263)

### Autres changements
- Alignement de la documentation de l'algorithme, de l'API et des libellés d'usages [#265](https://github.com/incubateur-ademe/mutafriches/pull/265)
