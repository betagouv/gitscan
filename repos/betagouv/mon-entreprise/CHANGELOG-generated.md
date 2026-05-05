## Changelog : mon-entreprise (30 derniers jours, au 4 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la précision des calculs, notamment pour les auto-entrepreneurs et les cotisations sociales. Des corrections ont été apportées pour tenir compte des dernières réglementations et des spécificités des différents régimes. Des refactorings importants ont été réalisés pour améliorer la maintenabilité du code et l'expérience développeur, ainsi que des améliorations de l'infrastructure CI/CD. Enfin, le simulateur RGCP a été décommissionné.

### Évolutions fonctionnelles
- Correction du calcul de l'IR pour les auto-entrepreneurs [#4105](https://github.com/betagouv/mon-entreprise/issues/4105).
- Décommissionnement du simulateur RGCP, avec des modifications des règles associées et des messages affichés.
- Ajout du PASS mahorais pour les travailleurs indépendants.
- Correction de la saisie des montants, quelle que soit l'unité utilisée.
- Correction de la navigation et de la prévisualisation de l'iframe en local et en production.
- Correction de l'affichage de la valeur de situation familiale pour le calcul de l'impôt.
- Mise à jour des plafonds de chiffre d'affaires pour l'auto-entreprise.
- Mise à jour des cotisations aux caisses de retraite (PLR).
- Correction des tests sur les DROM.
- Ajout d'un bandeau rouge pour signaler la présence de règles obsolètes.
- Ajout d'un bandeau de feedback pour indiquer quand une simulation est en cours de chargement [#4433](https://github.com/betagouv/mon-entreprise/issues/4433).

### Évolutions techniques
- Refonte complète des workflows GitHub Actions pour une meilleure gestion des tests et du déploiement.
- Séparation des tests E2E de production dans un workflow dédié.
- Amélioration de la gestion des secrets pour Algolia.
- Correction de références de workflow cassées.
- Refactor de la gestion des règles obsolètes pour une meilleure distinction des suppressions manuelles.
- Refactor de la fonction `safeSetSituation` pour une meilleure gestion des erreurs et découplage du cache engine.
- Correction d'un problème de FOUC (Flash of Unstyled Content) en SSR (Server-Side Rendering) causé par `navigator` dans Node 24.
- Mise à jour des versions de Node.js et des actions CI.
- Suppression de code commenté et amélioration du formatage du code avec Prettier.
- Export du type `OrigineSimulation` pour améliorer le typage.

### Autres changements
- Mise à jour des traductions (i18n).
- Correction de traductions manquantes.
- Mise à jour du budget 2025.
- Correction de tests unitaires.
- Suppression de règles inutiles dans le modèle AS.
- Déplacement des composants de réduction vers `lodeom`.
- Remplacement des chemins relatifs par des alias `@/`.
- Correction du formatage Prettier du test `safeSetSituation`.
- Correction de la valeur de situation de famille.
- Mise à jour du taux horaire minimum pour l'activité partielle.
- Correction du calcul des cotisations de début d'activité au régime micro-fiscal.
- Amélioration de la gestion des cotisations forfaitaires.
