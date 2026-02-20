## Changelog : vao (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à vao au cours des 30 derniers jours. Les modifications incluent des corrections de bugs, des améliorations de l'interface utilisateur, l'ajout de nouvelles fonctionnalités liées au module "fusager" et des optimisations techniques, notamment la migration vers pnpm et l'amélioration des outils de développement.

### Évolutions fonctionnelles
- Ajout d'une page d'authentification à deux facteurs (2FA) (#1183)
- Ajout de boutons pour améliorer l'accessibilité (RGAA) dans les tableaux (#1186)
- Correction d'un bug empêchant la copie des données du fusager dans les déclarations annulées (#1166)
- Correction d'un bug lié à la mise à jour du SIRET dans le fusager (#1184)
- Amélioration de l'affichage des messages d'erreur concernant le SIRET (#1156, #1117)
- Ajout d'un titre aux modales et modification de leur taille (#1150)
- Correction d'un problème d'export du schéma téléphonique (#1161, #1191)
- Correction de l'organisme dans le fusager pour les déclarations (#1160)

### Évolutions techniques
- Migration vers pnpm pour la gestion des dépendances et amélioration des outils de linting (#1125, #1185, #1174)
- Mise à jour de la dépendance `nuxt-maplibre` vers la version 1.2.2 (#1172)
- Amélioration de la configuration de l'environnement de développement (#1165, #1164)
- Ajout d'un composable pour la gestion des toasts (#1158)
- Amélioration des scripts de CI/CD et des tests (#1138)
- Correction de problèmes liés à la configuration de la carte en environnement de développement (#1187)

### Autres changements
- Amélioration du template de pull request (#1191)
- Correction de l'import manquant (#1176)
- Ajout de tests d'intégration pour l'acceptation des CGU (#1148)
- Nettoyage du code et des configurations.
