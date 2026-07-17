## Changelog : egapro (30 derniers jours, au 2026-07-16)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'accessibilité, la correction de bugs et l'ajout de nouvelles fonctionnalités pour faciliter la déclaration de l'index de l'égalité professionnelle. Des améliorations ont également été apportées à la sécurité, à la gestion des données et aux outils de suivi analytique.

### Évolutions fonctionnelles
- Implémentation d'un système d'accessibilité (ultra11y) pour améliorer l'expérience utilisateur pour tous, notamment les personnes handicapées. [#3817](https://github.com/SocialGouv/egapro/issues/3817)
- Amélioration de l'affichage de la proportion de bénéficiaires dans l'étape 6 du parcours de déclaration et dans le PDF exporté. [#3869](https://github.com/SocialGouv/egapro/issues/3869)
- Ajout de contenu et de règles d'envoi pour les notifications par email de rappel. [#3671](https://github.com/SocialGouv/egapro/issues/3671)
- Mise en place d'un canal de prépublication alpha avec déclenchement automatique des releases. [#3736](https://github.com/SocialGouv/egapro/issues/3736)
- Possibilité de purger les données des déclarations. [#3134](https://github.com/SocialGouv/egapro/issues/3134)
- Intégration des contenus et des règles d'envoi des emails de confirmation. [#3670](https://github.com/SocialGouv/egapro/issues/3670)
- Ajout d'une API publique pour la déclaration de rémunération. [#3172](https://github.com/SocialGouv/egapro/issues/3172)
- Demande du niveau Eidas2 (authentification forte) sur ProConnect. (Annulé suite à un problème, réactivation à venir) [#3829](https://github.com/SocialGouv/egapro/issues/3829)
- Amélioration de la gestion du verrouillage du parcours de déclaration pour la collaboration. [#3556](https://github.com/SocialGouv/egapro/issues/3556)
- Lecture seule du parcours de conformité après la date limite de modification. [#3494](https://github.com/SocialGouv/egapro/issues/3494)
- Amélioration des libellés et de l'affichage dans l'espace personnel (My Space). [#3761](https://github.com/SocialGouv/egapro/issues/3761)
- Implémentation de règles de conformité GIP pour les écarts de rémunération. [#3868](https://github.com/SocialGouv/egapro/issues/3868)

### Évolutions techniques
- Correction des permissions OIDC sur le workflow de promotion des environnements de test. [#3908](https://github.com/SocialGouv/egapro/issues/3908)
- Correction d'un problème de création de tag GPG lors des releases. [#3906](https://github.com/SocialGouv/egapro/issues/3906)
- Mise en place d'environnements de test persistants déployables uniquement depuis des releases (pour les tests RGAA et de performance). [#3904](https://github.com/SocialGouv/egapro/issues/3904)
- Correction d'un problème de protection de branche sur le canal de prépublication alpha. [#3905](https://github.com/SocialGouv/egapro/issues/3905)
- Rétrogradation d'une fonctionnalité d'authentification (demande Eidas2) suite à un problème. [#3907](https://github.com/SocialGouv/egapro/issues/3907)
- Migration des builds d'images de buildkit-service vers buildkit-operator. [#3844](https://github.com/SocialGouv/egapro/issues/3844)
- Ajout d'un check de fidélité visuelle (design-validator) dans le pipeline CI. [#3749](https://github.com/SocialGouv/egapro/issues/3749)
- Ajout d'un agent e2e-dev en fin de pipeline. [#3654](https://github.com/SocialGouv/egapro/issues/3654)
- Ajout d'un check pour éviter le skip silencieux des migrations de base de données. [#3557](https://github.com/SocialGouv/egapro/issues/3557)
- Refactoring de la gestion de l'impersonation et du verrou collaboratif dans le contexte de déclaration. [#3794](https://github.com/SocialGouv/egapro/issues/3794)
- Implémentation de Matomo pour le suivi analytique (avec exemption de consentement CNIL). [#3655](https://github.com/SocialGouv/egapro/issues/3655)

### Autres changements
- Réalignement du workflow Figma sur le serveur MCP officiel. [#3848](https://github.com/SocialGouv/egapro/issues/3848)
- Correction du seed des données Matomo en local. [#3787](https://github.com/SocialGouv/egapro/issues/3787)
- Ajout de seed pour les stats en local pour les tests. [#3569](https://github.com/SocialGouv/egapro/issues/3569)
- Ajout de diagrammes de parcours pour le CSE. [#3433](https://github.com/SocialGouv/egapro/issues/3433)
- Amélioration de la documentation.
- Corrections de contraste et d'accessibilité (RGAA). [#3800](https://github.com/SocialGouv/egapro/issues/3800) et [#3720](https://github.com/SocialGouv/egapro/issues/3720)
