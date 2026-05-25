## Changelog : otelo (30 derniers jours, au 21 mai 2026)

### Résumé
Le mois écoulé a été marqué par d'importantes améliorations fonctionnelles et techniques sur l'application otelo. Les utilisateurs bénéficieront notamment de nouvelles fonctionnalités de comparaison de données, d'une meilleure gestion des millésimes et de l'ajout de données historiques. Des optimisations ont également été apportées à l'interface utilisateur et à l'infrastructure pour une expérience plus fluide et performante.

### Évolutions fonctionnelles
- Ajout de la comparaison en pourcentage entre les logements vacants et le parc résidentiel ([#42](https://github.com/MTES-MCT/otelo/pull/42)).
- Implémentation de la possibilité pour un administrateur d'usurper l'identité d'un autre utilisateur.
- Prévisualisation des résultats lors de la création ou de la mise à jour de formulaires.
- Amélioration de la gestion des millésimes et mise en cache des résultats pour une meilleure performance.
- Ajout de données historiques et du RP (Répertoire des Parc) pour le millésime 2022.
- Nouvelle méthode de calcul pour l'absence d'accommodation.
- Ajout d'une page de changelog pour une meilleure communication des évolutions.
- Implémentation d'un CLI (Command Line Interface) pour l'import de données.
- Ajout de la gestion des versions de données.
- Ajout de la gestion des clés API et de leurs consommateurs.
- Amélioration de la gestion des utilisateurs avec un nouveau type d'utilisateur.
- Ajout de la fonctionnalité "readonly-share" pour le partage de données en lecture seule.
- Amélioration de la page de pilotage avec l'ajout d'une carte.
- Ajout de la gestion des typologies d'utilisateurs.
- Amélioration de l'exportation des données au format Excel.
- Ajout de la gestion des projections et des wordings associés.
- Correction de l'affichage du taux de vacance.
- Correction de l'affichage des taux de logement dans Excel.
- Correction de la gestion des années de base dans les comparaisons.

### Évolutions techniques
- Mise à jour de Next.js.
- Amélioration de la gestion des erreurs et des injections de modules dans le CLI.
- Correction de problèmes de build et de linting.
- Amélioration de la gestion des configurations de millésime.
- Amélioration de la gestion des dépendances et des locks pnpm.
- Refonte de la structure de la disparition des données.
- Ajout de tests unitaires et corrections de bugs associés.
- Amélioration de la gestion des enums dans Swagger.

### Autres changements
- Corrections de typographie et d'UI.
- Amélioration de la documentation.
- Suppression de l'envoi d'emails en environnement local.
- Correction de bugs divers liés à l'interface utilisateur et à la construction de l'application.
- Amélioration de la gestion des groupes EPCI.
- Correction de problèmes de build web.
- Amélioration de la gestion des tests et du linting.
