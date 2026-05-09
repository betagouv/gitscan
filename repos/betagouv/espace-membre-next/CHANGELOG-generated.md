## Changelog : espace-membre-next (30 derniers jours, au 06 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des startups et de l'onboarding/offboarding des membres. Des corrections ont été apportées pour améliorer la stabilité et la robustesse de l'application, ainsi que des optimisations techniques pour simplifier le code et améliorer les performances.

### Évolutions fonctionnelles
- Ajout d'une recherche par combo pour les startups dans l'interface. [#1324](https://github.com/betagouv/espace-membre-next/issues/1324)
- Les agents des startups peuvent désormais modifier les informations des membres. [#1303](https://github.com/betagouv/espace-membre-next/issues/1303)
- Amélioration de l'email envoyé lors des départs d'une équipe, avec des instructions claires. [#1290](https://github.com/betagouv/espace-membre-next/issues/1290)
- Affichage d'un panneau d'offboarding sur le tableau de bord lorsqu'un membre arrive à expiration. [#1289](https://github.com/betagouv/espace-membre-next/issues/1289)
- Suppression de la création d'email pour les attributaires lors de l'onboarding. [#1305](https://github.com/betagouv/espace-membre-next/issues/1305)
- Mise à jour des phases (statuts) des membres. [#1304](https://github.com/betagouv/espace-membre-next/issues/1304)
- Correction d'un bug empêchant la création d'email si l'adresse email principale n'était pas définie. [#1342](https://github.com/betagouv/espace-membre-next/issues/1342)

### Évolutions techniques
- Migration du système de templates d'emails de MJML. [#1350](https://github.com/betagouv/espace-membre-next/issues/1350)
- Simplification du routage et utilisation accrue du rendu côté serveur (SSR) pour améliorer les performances. [#1326](https://github.com/betagouv/espace-membre-next/issues/1326)
- Amélioration de la configuration et suppression de variables d'environnement inutiles. [#1329](https://github.com/betagouv/espace-membre-next/issues/1329)
- Suppression des éléments liés à Mattermost. [#1325](https://github.com/betagouv/espace-membre-next/issues/1325)
- Correction de problèmes liés à l'exportation de l'adresse email secondaire. [#1327](https://github.com/betagouv/espace-membre-next/issues/1327)
- Amélioration du logging pour faciliter le débogage. [#1300](https://github.com/betagouv/espace-membre-next/issues/1300)
- Correction de problèmes liés à l'utilisation de modules ECMAScript (ESM) en production. [#1337](https://github.com/betagouv/espace-membre-next/issues/1337)
- Suppression d'un TODO lié à l'authentification obsolète. [#1354](https://github.com/betagouv/espace-membre-next/issues/1354)
- Utilisation du composant `DataVisualization` de DSFR au lieu d'un asset SVG supprimé. [#1351](https://github.com/betagouv/espace-membre-next/issues/1351)
- Activation du preset recommandé pour l'accessibilité JSX-A11Y (RGAA). [#1355](https://github.com/betagouv/espace-membre-next/issues/1355)

### Autres changements
- Ajout de tests E2E pour le tableau de bord et les processus d'onboarding/offboarding. [#1299](https://github.com/betagouv/espace-membre-next/issues/1299)
- Diverses mises à jour de dépendances. [#1331](https://github.com/betagouv/espace-membre-next/issues/1331)
- Suppression de code inutile. [#1338](https://github.com/betagouv/espace-membre-next/issues/1338) et [#1339](https://github.com/betagouv/espace-membre-next/issues/1339)
- Suppression de la possibilité de supprimer les comptes Matomo/Sentry. [#1322](https://github.com/betagouv/espace-membre-next/issues/1322)
