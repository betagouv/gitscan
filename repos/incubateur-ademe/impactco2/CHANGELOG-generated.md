## Changelog : impactco2 (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de fonctionnalités et de qualité. De nouveaux éléments de calcul ont été ajoutés, notamment des repas, et des corrections ont été apportées à l'affichage et à l'accessibilité de l'application. Des améliorations techniques ont également été réalisées pour optimiser les performances et la stabilité, notamment concernant l'intégration de tests visuels et la gestion des erreurs.

### Évolutions fonctionnelles
- Ajout de nouveaux repas pour le calcul de l'impact carbone. [#879](https://github.com/incubateur-ademe/impactco2/issues/879)
- Amélioration de l'affichage des étiquettes (étiquette LR, étiquette de livraison) avec des ajustements de hauteur, de libellés et de largeur maximale.
- Correction de l'adresse du Bioparc. [#876](https://github.com/incubateur-ademe/impactco2/issues/876)
- Ajout de nouvelles statistiques. [#873](https://github.com/incubateur-ademe/impactco2/issues/873)
- Gestion du temps d'engagement en fonction du simulateur. [#873](https://github.com/incubateur-ademe/impactco2/issues/873)

### Évolutions techniques
- Intégration d'Integrabook pour les tests d'intégration visuels. [#878](https://github.com/incubateur-ademe/impactco2/issues/878)
- Amélioration de la gestion des erreurs dans les composants Notion avec l'ajout de *error boundaries*.
- Optimisation de l'appel de la carte (callgmap) dans une fonction serveur. [#874](https://github.com/incubateur-ademe/impactco2/issues/874)
- Suppression du rendu côté serveur (SSR) sur la page Notion.
- Correction de valeurs dans le *iframe checker*.
- Mise à jour de npm. [#875](https://github.com/incubateur-ademe/impactco2/issues/875)

### Autres changements
- Ajout de logs pour le suivi de l'API.
- Suppression de logs inutiles.
- Ajout de tests sur le Bioparc.
- Correction du zoom sur les logos du footer.
- Amélioration de l'accessibilité des étiquettes.
- Correction de petits problèmes de wording sur les étiquettes.
