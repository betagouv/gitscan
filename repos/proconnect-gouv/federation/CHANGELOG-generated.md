## Changelog : federation (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la robustesse de la plateforme, notamment en renforçant la validation des emails, en affinant la gestion des rôles et des accès, et en optimisant les contrôles de santé de l'application. Des améliorations d'accessibilité et des corrections de bugs ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de la gestion des rôles : Seuls les utilisateurs ayant les rôles appropriés peuvent accéder aux informations sensibles via les SP [#1158](https://github.com/proconnect-gouv/federation/issues/1158).
- Ajout de rôles par défaut dans l'interface d'administration [#1161](https://github.com/proconnect-gouv/federation/issues/1161).
- Ajout d'une bannière d'avertissement pour l'environnement de test [#1141](https://github.com/proconnect-gouv/federation/issues/1141).
- Amélioration de l'accessibilité : Ajout d'un lien vers la déclaration d'accessibilité et amélioration de la structure HTML [#1142](https://github.com/proconnect-gouv/federation/issues/1142).
- Ajout d'un indicateur pour activer/désactiver la validation des emails via un flag de fonctionnalité [#1144](https://github.com/proconnect-gouv/federation/issues/1144).

### Évolutions techniques
- Refonte de la validation des emails pour utiliser DNS-over-HTTPS [#1159](https://github.com/proconnect-gouv/federation/issues/1159).
- Amélioration des contrôles de santé (healthchecks) :
    - Implémentation d'un pattern ping/pong pour le broker [#1117](https://github.com/proconnect-gouv/federation/issues/1117).
    - Ajout de contrôles de santé spécifiques pour le CSM et le core-fca [#1114](https://github.com/proconnect-gouv/federation/issues/1114), [#1116](https://github.com/proconnect-gouv/federation/issues/1116).
    - Suppression des healthchecks inutiles et simplification de la configuration [#1119](https://github.com/proconnect-gouv/federation/issues/1119), [#1120](https://github.com/proconnect-gouv/federation/issues/1120).
- Correction d'un bug empêchant la reconnaissance correcte des valeurs ACR (Action Claim Request) [#1122](https://github.com/proconnect-gouv/federation/issues/1122).
- Amélioration de la gestion des exclusions pour le readiness probe du core-fca [#1121](https://github.com/proconnect-gouv/federation/issues/1121), [#1154](https://github.com/proconnect-gouv/federation/issues/1154).
- Utilisation de HTTPS pour la récupération du core-fca [#1118](https://github.com/proconnect-gouv/federation/issues/1118).
- Mise à jour de diverses dépendances : Mongoose, FastAPI, Axios, etc.

### Autres changements
- Ajout de logs pour faciliter le débogage des valeurs ACR [#1139](https://github.com/proconnect-gouv/federation/issues/1139).
- Ajout des champs `isEntraId` et `hyyyperbridge` à Grist pour une meilleure traçabilité [#1115](https://github.com/proconnect-gouv/federation/issues/1115).
- Corrections de linting et renommage de variables pour améliorer la lisibilité du code [#1157](https://github.com/proconnect-gouv/federation/issues/1157), [#1125](https://github.com/proconnect-gouv/federation/issues/1125).
