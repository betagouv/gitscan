## Changelog : nosgestesclimat (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, nosgestesclimat a connu une évolution significative avec l'ajout de nombreuses nouvelles actions, notamment dans les domaines de la mobilité, du logement, de la vie quotidienne et de la consommation. Des améliorations ont également été apportées à la précision des calculs, à la gestion des actions et à l'expérience utilisateur, notamment via des corrections de traduction et des ajustements suite aux retours des utilisateurs.

### Évolutions fonctionnelles
- Ajout d'actions liées à la mobilité : nouvelles actions pour les mobilités, notamment des actions de reconditionnement [#2775](https://github.com/incubateur-ademe/nosgestesclimat/issues/2775).
- Ajout d'actions liées au logement : ajout d'actions pour l'amélioration de l'isolation via le DPE, le chauffage collectif et l'adaptation des actions en fonction du type de logement [#2781](https://github.com/incubateur-ademe/nosgestesclimat/issues/2781).
- Ajout d'actions liées à la vie quotidienne : intégration de nouvelles actions pour la vie quotidienne [#2782](https://github.com/incubateur-ademe/nosgestesclimat/issues/2782).
- Ajout d'une action pour réduire la consommation de viande [#97e6bda4](https://github.com/incubateur-ademe/nosgestesclimat/commit/97e6bda4).
- Amélioration de la description des repas avec ajout de la portion [#2785](https://github.com/incubateur-ademe/nosgestesclimat/issues/2785).
- Correction de l'impact de la piscine sur l'empreinte eau [#13683ec4](https://github.com/incubateur-ademe/nosgestesclimat/commit/13683ec4).
- Correction de la vitesse des avions pour une meilleure précision des calculs [#2778](https://github.com/incubateur-ademe/nosgestesclimat/issues/2778).
- Suppression des suggestions de vacances. [#df6d5d71](https://github.com/incubateur-ademe/nosgestesclimat/commit/df6d5d71)
- Désactivation des actions v2 pour le mode jeune. [#2762](https://github.com/incubateur-ademe/nosgestesclimat/issues/2762)

### Évolutions techniques
- Refonte de la gestion des dates de péremption (DLUO) pour l'écobalyse et l'agribalyse [#48d8c9c4](https://github.com/incubateur-ademe/nosgestesclimat/commit/48d8c9c4).
- Mise à jour de l'interface utilisateur pour l'affichage des données Agribalyse [#331ac51a](https://github.com/incubateur-ademe/nosgestesclimat/commit/331ac51a).
- Correction de la gestion de la désactivation des actions pour l'évaluation des émissions différées (ED) [#f9a5211c](https://github.com/incubateur-ademe/nosgestesclimat/commit/f9a5211c).
- Corrections et ajustements suite aux retours des phases de tests (MEP) [#a7b6ba2a](https://github.com/incubateur-ademe/nosgestesclimat/commit/a7b6ba2a).
- Gestion de la cohabitation des nouvelles et anciennes actions [#55fc9821](https://github.com/incubateur-ademe/nosgestesclimat/commit/55fc9821).
- Corrections de namespace pour les actions logement [#92f8a861](https://github.com/incubateur-ademe/nosgestesclimat/commit/92f8a861).

### Autres changements
- Corrections de traductions et d'orthographe [#cb2b54c9](https://github.com/incubateur-ademe/nosgestesclimat/commit/cb2b54c9), [#dd5763eb](https://github.com/incubateur-ademe/nosgestesclimat/commit/dd5763eb), [#19e71a58](https://github.com/incubateur-ademe/nosgestesclimat/commit/19e71a58), [#9b6a98ad](https://github.com/incubateur-ademe/nosgestesclimat/commit/9b6a98ad).
- Publication des versions 4.13.0-rc.1, 4.13.0-rc.2 et 4.13.1 [#006715d4](https://github.com/incubateur-ademe/nosgestesclimat/commit/006715d4), [#f1c9d809](https://github.com/incubateur-ademe/nosgestesclimat/commit/f1c9d809), [#6d01b87b](https://github.com/incubateur-ademe/nosgestesclimat/commit/6d01b87b).
- Ajout des identifiants manquants [#0b06e539](https://github.com/incubateur-ademe/nosgestesclimat/commit/0b06e539).
- Corrections de conditions d'actions [#c4bb9d68](https://github.com/incubateur-ademe/nosgestesclimat/commit/c4bb9d68), [#c03c0a82](https://github.com/incubateur-ademe/nosgestesclimat/commit/c03c0a82), [#14ebcefa](https://github.com/incubateur-ademe/nosgestesclimat/commit/14ebcefa).
- Correction d'une action légumineuse non quantifiable [#099d95fd](https://github.com/incubateur-ademe/nosgestesclimat/commit/099d95fd).
