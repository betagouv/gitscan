## Changelog : egapro (30 derniers jours, au 2026-07-09)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de la conformité aux règles de déclaration, l'intégration de nouvelles fonctionnalités pour la gestion des notifications et des données, ainsi que des corrections d'interface et de sécurité. Des améliorations ont également été apportées à l'infrastructure de déploiement et à la collecte de données analytiques.

### Évolutions fonctionnelles
- Implémentation de la signature des écarts de rémunération conformément aux règles GIP. [#3868](https://github.com/SocialGouv/egapro/issues/3868)
- Affichage correct de la proportion de bénéficiaires dans l'étape 6 de la déclaration et dans le PDF généré. [#3869](https://github.com/SocialGouv/egapro/issues/3869)
- Mise en place de contenus de mails de rappel et définition des règles d'envoi pour les notifications. [#3671](https://github.com/SocialGouv/egapro/issues/3671) et [#3857](https://github.com/SocialGouv/egapro/issues/3857)
- Création d'un canal de prépublication alpha avec déclenchement automatique des déploiements. [#3736](https://github.com/SocialGouv/egapro/issues/3736), [#3799](https://github.com/SocialGouv/egapro/issues/3799) et [#3858](https://github.com/SocialGouv/egapro/issues/3858)
- Implémentation de la purge des données des déclarations. [#3134](https://github.com/SocialGouv/egapro/issues/3134) et [#3828](https://github.com/SocialGouv/egapro/issues/3828)
- Intégration des contenus et des règles d'envoi des emails de confirmation. [#3670](https://github.com/SocialGouv/egapro/issues/3670) et [#3849](https://github.com/SocialGouv/egapro/issues/3849)
- Publication d'une API publique pour la déclaration de rémunération. [#3172](https://github.com/SocialGouv/egapro/issues/3172) et [#3839](https://github.com/SocialGouv/egapro/issues/3839)
- Demande du niveau EIDAS2 (authentification forte) sur ProConnect. [#3829](https://github.com/SocialGouv/egapro/issues/3829)
- Lecture seule de la déclaration après la date limite de modification. [#3716](https://github.com/SocialGouv/egapro/issues/3716) et [#3798](https://github.com/SocialGouv/egapro/issues/3798)
- Mise en place d'un lock pour le parcours de déclaration. [#3556](https://github.com/SocialGouv/egapro/issues/3556) et [#3753](https://github.com/SocialGouv/egapro/issues/3753)

### Évolutions techniques
- Migration des builds d'images de buildkit-service vers buildkit-operator. [#3844](https://github.com/SocialGouv/egapro/issues/3844)
- Refactorisation de l'unification de l'impersonation et du verrou collaboratif dans LockContext. [#3794](https://github.com/SocialGouv/egapro/issues/3794)
- Ajout d'un gate de fidélité visuelle (design-validator) au pipeline CI/CD. [#3749](https://github.com/SocialGouv/egapro/issues/3749)
- Amélioration de la gestion des erreurs et des migrations SQL avec un check de journal monotone. [#3557](https://github.com/SocialGouv/egapro/issues/3557) et [#3560](https://github.com/SocialGouv/egapro/issues/3560)
- Ajout d'un agent e2e-dev en fin de pipeline. [#3654](https://github.com/SocialGouv/egapro/issues/3654)

### Autres changements
- Correction du seed des données Matomo en local. [#3787](https://github.com/SocialGouv/egapro/issues/3787)
- Amélioration du contraste des tags "élevé" et des encarts d'avertissement pour l'accessibilité. [#3720](https://github.com/SocialGouv/egapro/issues/3720) et [#3758](https://github.com/SocialGouv/egapro/issues/3758)
- Ajout de statistiques Matomo pour le suivi de l'engagement des CSE et des utilisateurs par entreprise. [#3756](https://github.com/SocialGouv/egapro/issues/3756)
- Implémentation du plan de tracking Matomo (événements client et documentation). [#3625](https://github.com/SocialGouv/egapro/issues/3625)
- Ajout de seed-demo-stats pour les tests des graphiques statistiques en local. [#3569](https://github.com/SocialGouv/egapro/issues/3569)
- Ajout d'un diagramme de flux du parcours CSE avec les étapes FSM. [#3433](https://github.com/SocialGouv/egapro/issues/3433)
- Mise à jour de la documentation pour refléter les changements.
- Correction de divers problèmes d'interface utilisateur et d'alignement visuel avec Figma.
- Amélioration de la gestion des URLs de redirection après authentification. [#3718](https://github.com/SocialGouv/egapro/issues/3718)
