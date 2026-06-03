## Changelog : api-engagement (30 derniers jours, au 2 juin 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en termes de sécurité, de performance et d'expérience utilisateur. Des corrections ont été apportées pour améliorer l'accessibilité, notamment sur le formulaire d'authentification et le quiz. L'architecture interne a été refactorisée pour une meilleure gestion des règles de diffusion et une plus grande robustesse.

### Évolutions fonctionnelles
- **Authentification:** Amélioration de l'accessibilité des formulaires d'authentification et de gestion de compte, avec ajout d'attributs d'autocomplétion et d'associations de labels aux champs. [#1086](https://github.com/betagouv/api-engagement/issues/1086) [#1087](https://github.com/betagouv/api-engagement/issues/1087) [#1088](https://github.com/betagouv/api-engagement/issues/1088) [#1089](https://github.com/betagouv/api-engagement/issues/1089)
- **Quiz:** Amélioration de l'interface utilisateur du quiz, notamment en termes d'accessibilité avec des patterns de barre de progression et de boîtes de dialogue accessibles. [#1053](https://github.com/betagouv/api-engagement/issues/1053) [#1054](https://github.com/betagouv/api-engagement/issues/1054) [#1055](https://github.com/betagouv/api-engagement/issues/1055) [#1057](https://github.com/betagouv/api-engagement/issues/1057) [#1058](https://github.com/betagouv/api-engagement/issues/1058) [#1084](https://github.com/betagouv/api-engagement/issues/1084)
- **Plateforme:** Amélioration de l'affichage du nom du département. [#1072](https://github.com/betagouv/api-engagement/issues/1072)
- **API:** Possibilité pour les diffuseurs d'utiliser l'endpoint `v2/activity`. [#1091](https://github.com/betagouv/api-engagement/issues/1091)
- **Missions:** Ajout de la possibilité d'activer les missions de service civique dans Grimpio. [#977](https://github.com/betagouv/api-engagement/issues/977)
- **Cartographie des missions:** Corrections pour améliorer l'accessibilité (RGAA). [#1103](https://github.com/betagouv/api-engagement/issues/1103)

### Évolutions techniques
- **Refactorisation:** Remplacement du système d'exclusion de publication par un moteur basé sur des règles. [#1078](https://github.com/betagouv/api-engagement/issues/1078)
- **Sécurité:** Implémentation d'une limitation du taux de requêtes (IP rate limit) sur les routes de l'API plateforme. [#1075](https://github.com/betagouv/api-engagement/issues/1075)
- **Base de données:** Ajout d'un index unique pour `mission_enrichment` sur `missionId` et `promptVersion`. [#1092](https://github.com/betagouv/api-engagement/issues/1092)
- **Infrastructure:** Configuration de Typesense pour la production. [#1068](https://github.com/betagouv/api-engagement/issues/1068)
- **Tests:** Ajout de tests unitaires et de workflows linting pour le package plateforme. [#1085](https://github.com/betagouv/api-engagement/issues/1085)
- **Architecture:** Suppression du modèle de taxonomie hérité. [#1079](https://github.com/betagouv/api-engagement/issues/1079)
- **Performance:** Suppression de l'expiration du score utilisateur. [#1105](https://github.com/betagouv/api-engagement/issues/1105)
- **CI/CD:** Correction de problèmes liés à la construction des jobs. [#1018](https://github.com/betagouv/api-engagement/issues/1018)

### Autres changements
- **Documentation:** Ajout d'un fichier `AGENTS.md`. [#1082](https://github.com/betagouv/api-engagement/issues/1082)
- **Corrections:** Correction de variables manquantes dans la configuration Terraform. [#1106](https://github.com/betagouv/api-engagement/issues/1106)
- **Versionning:** Publication des versions v1.5.0, v1.5.1, v1.6.0, v1.7.0 et v1.8.1.
- **Divers:** Suppression de l'ancienne logique de validation d'adresse IP Brevo. [#1027](https://github.com/betagouv/api-engagement/issues/1027)
