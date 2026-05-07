## Changelog : espace-membre-next (30 derniers jours, au 06 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des startups et de l'onboarding/offboarding des membres. Des corrections ont été apportées pour améliorer la stabilité et la fiabilité de l'application, ainsi que des optimisations techniques pour la performance et la maintenance du code.

### Évolutions fonctionnelles
- Ajout d'un champ de recherche combiné pour les startups dans l'interface de recherche. [#1324](https://github.com/betagouv/espace-membre-next/issues/1324)
- Les agents des startups peuvent désormais modifier les informations des membres. [#1303](https://github.com/betagouv/espace-membre-next/issues/1303)
- Amélioration de l'email envoyé lors des départs d'une équipe, avec des instructions claires pour le membre sortant. [#1290](https://github.com/betagouv/espace-membre-next/issues/1290)
- Un panneau d'offboarding est maintenant affiché dans le tableau de bord lorsque l'expiration d'un membre approche. [#1289](https://github.com/betagouv/espace-membre-next/issues/1289)
- Mise à niveau des phases (sans détails supplémentaires dans le commit). [#1304](https://github.com/betagouv/espace-membre-next/issues/1304)
- Correction : Création d'un email même en l'absence d'adresse email principale définie. [#1342](https://github.com/betagouv/espace-membre-next/issues/1342)
- Correction : Suppression de l'exportation de l'email secondaire. [#1327](https://github.com/betagouv/espace-membre-next/issues/1327)
- Correction : Simplification du routage et utilisation accrue du rendu côté serveur (SSR). [#1326](https://github.com/betagouv/espace-membre-next/issues/1326)
- Correction : Suppression de variables d'environnement inutiles. [#1329](https://github.com/betagouv/espace-membre-next/issues/1329)
- Correction : Suppression du fichier `.env`. [#1339](https://github.com/betagouv/espace-membre-next/issues/1339)
- Correction : Problème lié à l'utilisation de ESM en production. [#1337](https://github.com/betagouv/espace-membre-next/issues/1337)
- Correction : Utilisation du composant `DataVisualization` de DSFR au lieu d'un asset SVG supprimé. [#1351](https://github.com/betagouv/espace-membre-next/issues/1351)

### Évolutions techniques
- Migration vers MJML pour la gestion des templates d'emails. [#1350](https://github.com/betagouv/espace-membre-next/issues/1350)
- Amélioration de la journalisation (logging) de l'application. [#1300](https://github.com/betagouv/espace-membre-next/issues/1300) et [#1302](https://github.com/betagouv/espace-membre-next/issues/1302)
- Ajout de tests E2E pour le tableau de bord et les processus d'onboarding/offboarding. [#1299](https://github.com/betagouv/espace-membre-next/issues/1299)
- Suppression des éléments liés à Mattermost. [#1325](https://github.com/betagouv/espace-membre-next/issues/1325)
- Suppression de la fonctionnalité de suppression des comptes Matomo/Sentry. [#1322](https://github.com/betagouv/espace-membre-next/issues/1322)
- Amélioration de l'accessibilité (a11y) en activant le preset recommandé de jsx-a11y (RGAA). [#1355](https://github.com/betagouv/espace-membre-next/issues/1355)
- Suppression d'un TODO lié à l'authentification. [#1354](https://github.com/betagouv/espace-membre-next/issues/1354)
- Quelques mises à jour de dépendances. [#1331](https://github.com/betagouv/espace-membre-next/issues/1331)

### Autres changements
- Les attributaires ne se voient plus créer d'email lors de l'onboarding. [#1305](https://github.com/betagouv/espace-membre-next/issues/1305)
