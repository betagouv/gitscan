## Changelog : vao (30 derniers jours)

### Résumé
Ce changelog présente les évolutions récentes de l'application Vao, un système d'information dédié à la dématérialisation des procédures liées aux séjours pour personnes handicapées. Les dernières améliorations concernent la correction de bugs, l'ajout de nouvelles fonctionnalités comme l'authentification à deux facteurs et l'intégration S3, ainsi que des optimisations techniques et des améliorations de l'expérience utilisateur.

### Évolutions fonctionnelles
- Correction d'une erreur lors de la désactivation d'un hébergement [#1204](https://github.com/SocialGouv/vao/issues/1204).
- Correction d'un problème d'affichage des utilisateurs OVA secondaires [#1197](https://github.com/SocialGouv/vao/issues/1197).
- Correction d'un bug dans le filtre de liste des déclarations de séjour (DS) par organisation [#1196](https://github.com/SocialGouv/vao/issues/1196).
- Implémentation de la page d'authentification à deux facteurs (2FA) [#1183](https://github.com/SocialGouv/vao/issues/1183).
- Ajout de boutons pour améliorer l'accessibilité (RGAA) dans les tableaux [#1186](https://github.com/SocialGouv/vao/issues/1186).
- Correction du problème d'affichage du SIRET lors de la mise à jour d'un fusager, avec ajout de tests liés à la restriction GDPR [#1184](https://github.com/SocialGouv/vao/issues/1184).

### Évolutions techniques
- Ajout de *feature flags* pour une gestion plus flexible des fonctionnalités [#1205](https://github.com/SocialGouv/vao/issues/1205).
- Intégration de S3 (étape 2) pour le stockage des données [#1198](https://github.com/SocialGouv/vao/issues/1198).
- Amélioration du workflow SonarQube pour une meilleure analyse de la qualité du code [#1202](https://github.com/SocialGouv/vao/issues/1202).
- Mise à jour de la configuration de pnpm pour ajuster l'âge minimum des versions publiées [#1185](https://github.com/SocialGouv/vao/issues/1185).
- Correction d'un doublon de requête SQL dans le middleware de permission pour les hébergements [#1204](https://github.com/SocialGouv/vao/issues/1204).
- Correction d'une erreur dans le middleware de permission pour les hébergements [#1204](https://github.com/SocialGouv/vao/issues/1204).

### Autres changements
- Amélioration du template de pull request pour une meilleure collaboration [#1191](https://github.com/SocialGouv/vao/issues/1191).
- Correction de la configuration de la carte en environnement de développement [#1187](https://github.com/SocialGouv/vao/issues/1187).
- Publication des versions 1.26.0 [#1192](https://github.com/SocialGouv/vao/issues/1192) et 1.26.1 [#1200](https://github.com/SocialGouv/vao/issues/1200).
