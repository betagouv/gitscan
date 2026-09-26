## Changelog : react-dsfr-chart (30 derniers jours, au 22 septembre 2026)

### Résumé
La bibliothèque s'enrichit de nouveaux types de visualisations (graphiques en barres, en lignes et diagrammes circulaires) et offre une plus grande flexibilité de personnalisation des couleurs et des dimensions. Parallèlement, les processus de publication et la sécurité du projet ont été renforcés pour garantir des déploiements plus fiables.

### Évolutions fonctionnelles
- Ajout de nouveaux types de graphiques : barres, lignes et diagrammes circulaires (très légers, ~3,4 ko) [#15](https://github.com/betagouv/react-dsfr-chart/pull/15)
- Personnalisation accrue des couleurs par série ou par part via la propriété `colors` [#18](https://github.com/betagouv/react-dsfr-chart/pull/18)
- Meilleure gestion des dimensions avec la possibilité de définir une hauteur fixe ou par catégorie pour les graphiques en barres [#22](https://github.com/betagouv/react-dsfr-chart/pull/22)

### Évolutions techniques
- Optimisation du cycle de publication des versions candidates (RC) via un nouveau script [#19](https://github.com/betagouv/react-dsfr-chart/pull/19) et l'imposition d'une Pull Request pour ces publications [#21](https://github.com/betagouv/react-dsfr-chart/pull/21)
- Renforcement de la sécurité du dépôt et du processus de publication sur npm [#5](https://github.com/betagouv/react-dsfr-chart/pull/5)
- Possibilité d'installer le paquet directement depuis les archives de release GitHub avant sa publication officielle sur npm [#16](https://github.com/betagouv/react-dsfr-chart/pull/16)
