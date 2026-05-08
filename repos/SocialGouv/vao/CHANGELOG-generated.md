## Changelog : vao (30 derniers jours, au 07 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant le renouvellement des agréments, notamment au niveau de la saisie d'informations, de la gestion des fichiers et de l'accessibilité. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et l'expérience utilisateur. Des travaux ont été réalisés sur l'initialisation de la base de données avec l'ajout d'un Dockerfile dédié.

### Évolutions fonctionnelles
- **Renouvellement d'agréments :** Amélioration significative de l'étape 1 du processus de renouvellement d'agrément, incluant des correctifs sur les champs, les labels et la validation des données. [#1256, #1266, #1284]
- **Gestion des fichiers :** Correction de problèmes liés à l'upload de documents pour le renouvellement des agréments, notamment la gestion des doublons et la persistance des fichiers. [#1295, #1303]
- **Affichage des informations :** Correction de l'affichage des informations concernant les agréments (statut, dates) dans le back-office. [#1294]
- **Accès et permissions :** Correction d'un problème d'accès à la liste des EIG. [#1293]
- **Confirmation d'envoi :** Implémentation de l'envoi de mails de confirmation pour les demandes d'agrément. [#1286]
- **Fonctionnalités Fusager :** Ajout de nouvelles fonctionnalités liées au module Fusager, incluant la gestion des messages, des listes JDMA et la suppression du menu de renouvellement d'agrément. [#1266, #1267, #1269, #1273]
- **Gestion des activités :** Correction de la récupération des activités lors du renouvellement d'agrément. [#1265]

### Évolutions techniques
- **Initialisation de la base de données :** Ajout d'un Dockerfile pour faciliter l'initialisation de la base de données. [#1283, #1304, #1305]
- **Tests :** Amélioration de la couverture de tests, notamment avec l'ajout de tests frontend à la CI et l'amélioration des tests existants. [#1307, #1309]
- **Refactoring :** Passage de certains composants en TypeScript pour une meilleure maintenabilité.
- **CI/CD :** Corrections et améliorations des actions de build de l'image database-init.
- **Sécurité :** Correction d'une vulnérabilité liée à la déconnexion et au refresh token. [#1310]

### Autres changements
- Amélioration de l'accessibilité de l'étape 1 du processus de demande d'agrément (RGAA). [#1183, #1281]
- Corrections de coquilles et améliorations de la lisibilité du code.
- Suppression de branches inutilisées.
- Correction de problèmes de formattage d'adresse. [#1101]
- Correction de problèmes de validation en brouillon. [#1085]
