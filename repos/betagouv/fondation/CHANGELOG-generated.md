## Changelog : fondation (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, l'équipe a continué à améliorer l'application en se concentrant sur la refactorisation de l'architecture frontale vers une approche plus modulaire et maintenable. Des améliorations ont également été apportées à la gestion des fichiers, à l'interface utilisateur pour les magistrats et à la gestion des dates d'audition. Des corrections de sécurité et des mises à jour de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Ajout de la possibilité d'attacher des fichiers à un dossier de nomination. [#407](https://github.com/betagouv/fondation/issues/407)
- Ajout d'une date d'audition pour les magistrats. [#463](https://github.com/betagouv/fondation/issues/463)
- Refonte de l'affichage des observations des magistrats, avec un panneau latéral dédié. [#439](https://github.com/betagouv/fondation/issues/439)
- Possibilité de modifier les dates d'audition passées après confirmation. [#508](https://github.com/betagouv/fondation/issues/508)
- Ajout d'un bouton "+" pour ajouter des observations. [#497](https://github.com/betagouv/fondation/issues/497)
- Ajout d'un point d'extrémité d'autorisation M2M pour les magistrats. [#502](https://github.com/betagouv/fondation/issues/502)
- Les étiquettes des résultats des dossiers de nomination sont désormais servies par l'API. [#473](https://github.com/betagouv/fondation/issues/473)

### Évolutions techniques
- Refactorisation importante de l'architecture frontale vers une approche "feature-first", améliorant la modularité et la maintenabilité du code. (plusieurs commits [#430](https://github.com/betagouv/fondation/issues/430), [#431](https://github.com/betagouv/fondation/issues/431), [#432](https://github.com/betagouv/fondation/issues/432), [#433](https://github.com/betagouv/fondation/issues/433), [#427](https://github.com/betagouv/fondation/issues/427), [#428](https://github.com/betagouv/fondation/issues/428), [#429](https://github.com/betagouv/fondation/issues/429))
- Mise à jour de Prisma vers la version 7. [#481](https://github.com/betagouv/fondation/issues/481)
- Mise à jour de TypeScript vers la version 6. [#480](https://github.com/betagouv/fondation/issues/480)
- Migration des tests vers Vitest. [#437](https://github.com/betagouv/fondation/issues/437)
- Suppression des modèles partagés et internalisation des enums et types. (plusieurs commits [#499](https://github.com/betagouv/fondation/issues/499), [#496](https://github.com/betagouv/fondation/issues/496), [#495](https://github.com/betagouv/fondation/issues/495), [#492](https://github.com/betagouv/fondation/issues/492), [#490](https://github.com/betagouv/fondation/issues/490), [#491](https://github.com/betagouv/fondation/issues/491))
- Amélioration de la gestion du cache Vite. [#487](https://github.com/betagouv/fondation/issues/487), [#501](https://github.com/betagouv/fondation/issues/501), [#502](https://github.com/betagouv/fondation/issues/502)

### Autres changements
- Ajout de guides Storybook et mise à jour du fichier README. [#507](https://github.com/betagouv/fondation/issues/507)
- Amélioration de la documentation et des tests.
- Corrections de bugs mineurs et améliorations de la performance.
- Mise à jour de plusieurs dépendances (piscina, react-router, vite, etc.).
- Suppression de code obsolète.
- Amélioration de la configuration CI/CD.
- Ajout d'un ADR pour l'architecture frontale. [#434](https://github.com/betagouv/fondation/issues/434)
