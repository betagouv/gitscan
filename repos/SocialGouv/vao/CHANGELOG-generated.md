## Changelog : vao (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à l'application, notamment des corrections de bugs concernant la gestion des organismes et des déclarations de séjour, ainsi que l'ajout de nouvelles fonctionnalités comme la page d'authentification à deux facteurs et des boutons pour l'accessibilité (RGAA). Des optimisations techniques ont également été réalisées, notamment concernant la configuration du projet et l'intégration de nouveaux outils de développement.

### Évolutions fonctionnelles
- Ajout d'une page d'authentification à deux facteurs (2FA) (#1183)
- Amélioration de l'accessibilité avec l'ajout de boutons pour les tableaux, conformément aux normes RGAA (#1186)
- Correction d'un bug empêchant la disparition correcte du deuxième compte OVA lors de la fusion (#1197)
- Correction d'un bug dans le filtre de liste des DS pour les organisations (#1196)
- Correction d'un bug concernant la mise à jour du SIRET et l'ajout d'un test sur la restriction RGPD (#1184)
- Correction d'un bug lié à la copie des déclarations de séjour annulées (#1166)
- Correction d'un bug concernant la gestion des organismes pour les déclarations de séjour (#1160)
- Correction d'un bug lié à l'export du schéma téléphonique (#1161)

### Évolutions techniques
- Mise à jour de la configuration SonarQube pour l'analyse du code (#1202)
- Amélioration du template de pull request pour une meilleure collaboration (#1191)
- Mise à jour de la configuration pnpm pour la gestion des dépendances (#1185, #1177)
- Migration vers pnpm et correction des erreurs de linting (#1125)
- Mise à jour de la dépendance `nuxt-maplibre` vers la version 1.2.2 (#1172)
- Ajout d'un composable pour la gestion des notifications "toasters" (#1158)
- Correction d'une erreur d'import (#1176)

### Autres changements
- Configuration de l'environnement de développement (#1165, #1164, #1163)
- Suppression des applications du fichier `docker-compose` pour simplifier le développement local (#1163)
- Correction de la configuration de la carte en environnement de développement (#1187, #1187)
