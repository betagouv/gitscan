## Changelog : vao (30 derniers jours)

### Résumé
Ce changelog résume les améliorations et corrections apportées à l'application vao au cours des 30 derniers jours. Les modifications incluent des corrections de bugs liés à la gestion des organismes et des déclarations de séjour, l'ajout de fonctionnalités d'authentification à deux facteurs, l'amélioration de l'accessibilité, et des optimisations techniques pour le développement et la maintenance du projet.

### Évolutions fonctionnelles
- Ajout d'une page d'authentification à deux facteurs (2FA) (#1183)
- Amélioration de l'accessibilité avec l'ajout de boutons pour les tableaux, conformément aux directives RGAA (#1186)
- Correction d'un bug empêchant la disparition correcte du deuxième compte OVA (#1197)
- Correction d'un bug dans le filtre de liste des déclarations de séjour (DS) pour les organismes (#1196)
- Correction de l'affichage du message d'erreur "SIRET inexistant" (#1156, #1117)
- Correction du routage des emails lors de la mise à jour du SIRET (#1157)
- Correction de la copie d'une déclaration de séjour annulée (#1166)
- Correction de l'assignation de l'organisme lors de la création d'une déclaration de séjour (#1160)

### Évolutions techniques
- Migration vers pnpm et correction des problèmes de linting associés (#1125, #1191)
- Mise à jour de la dépendance `nuxt-maplibre` vers la version 1.2.2 (#1172)
- Amélioration de la configuration de développement, notamment pour les variables d'environnement (#1164, #1165, #1187)
- Correction de problèmes liés aux schémas de téléphone pour l'export (#1161, #1191)
- Ajout d'un composable pour la gestion des "toasters" (notifications) (#1158)
- Amélioration des scripts de CI/CD et de la configuration des conteneurs de développement (#1174, #1176)
- Correction de l'import manquant dans un composant (#1176)
- Ajout de vérifications de types dans le projet Nuxt (#1138)

### Autres changements
- Amélioration du template de pull request pour encourager des contributions de meilleure qualité (#1191, #1185)
- Correction de la configuration du bucket S3 pour les assets locaux (#1177)
- Suppression des applications de la configuration docker-compose (#1163)
