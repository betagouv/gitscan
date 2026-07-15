## Changelog : egapro (30 derniers jours, au 9 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la plateforme, notamment concernant la conformité aux règles de déclaration des écarts de rémunération, la gestion des notifications, la sécurité de l'authentification et l'amélioration de l'expérience utilisateur sur le parcours de conformité. Des corrections ont également été apportées pour améliorer l'accessibilité et la fiabilité de l'application.

### Évolutions fonctionnelles
- Implémentation de la signature des écarts de rémunération conformément aux règles GIP. [#3868](https://github.com/SocialGouv/egapro/issues/3868)
- Affichage correct de la proportion de bénéficiaires dans l'étape 6 de la déclaration et dans le PDF généré. [#3869](https://github.com/SocialGouv/egapro/issues/3869)
- Amélioration du contenu des emails de rappel et définition des règles d'envoi. [#3671](https://github.com/SocialGouv/egapro/issues/3671) [#3857](https://github.com/SocialGouv/egapro/issues/3857)
- Mise en place d'un canal de prépublication "alpha" avec déclenchement automatique des releases. [#3736](https://github.com/SocialGouv/egapro/issues/3736) [#3799](https://github.com/SocialGouv/egapro/issues/3799) [#3858](https://github.com/SocialGouv/egapro/issues/3858)
- Possibilité de purger les données des déclarations. [#3134](https://github.com/SocialGouv/egapro/issues/3134) [#3828](https://github.com/SocialGouv/egapro/issues/3828)
- Intégration des contenus et des règles d'envoi des emails de confirmation. [#3670](https://github.com/SocialGouv/egapro/issues/3670) [#3849](https://github.com/SocialGouv/egapro/issues/3849)
- Mise en place d'une API publique pour la déclaration de rémunération. [#3172](https://github.com/SocialGouv/egapro/issues/3172) [#3839](https://github.com/SocialGouv/egapro/issues/3839)
- Demande d'authentification à deux facteurs (EIDAS2) sur ProConnect. [#3829](https://github.com/SocialGouv/egapro/issues/3829)
- Lecture seule de la déclaration après la date limite de modification. [#3716](https://github.com/SocialGouv/egapro/issues/3716) [#3798](https://github.com/SocialGouv/egapro/issues/3798)
- Verrouillage du parcours de conformité pour éviter les modifications simultanées. [#3556](https://github.com/SocialGouv/egapro/issues/3556) [#3753](https://github.com/SocialGouv/egapro/issues/3753)
- Amélioration de la conservation de l'URL cible lors de la redirection après la connexion. [#3718](https://github.com/SocialGouv/egapro/issues/3718)

### Évolutions techniques
- Migration des builds d'images de buildkit-service vers buildkit-operator. [#3844](https://github.com/SocialGouv/egapro/issues/3844)
- Refactorisation de l'unification de l'impersonation et du verrou collaboratif dans LockContext. [#3794](https://github.com/SocialGouv/egapro/issues/3794)
- Ajout d'un gate de fidélité visuelle avec design-validator (Figma ↔ rendu). [#3749](https://github.com/SocialGouv/egapro/issues/3749)
- Ajout d'un agent e2e-dev en fin de pipeline. [#3654](https://github.com/SocialGouv/egapro/issues/3654)
- Ajout d'un check monotone pour éviter le skip silencieux des migrations. [#3557](https://github.com/SocialGouv/egapro/issues/3557) [#3560](https://github.com/SocialGouv/egapro/issues/3560)

### Autres changements
- Correction du seed des données Matomo en local. [#3787](https://github.com/SocialGouv/egapro/issues/3787)
- Amélioration du contraste du tag "élevé" et des encarts d'avertissement pour l'accessibilité. [#3720](https://github.com/SocialGouv/egapro/issues/3720) [#3758](https://github.com/SocialGouv/egapro/issues/3758)
- Ajout de statistiques sur l'engagement des CSE et le nombre d'utilisateurs par entreprise. [#3756](https://github.com/SocialGouv/egapro/issues/3756)
- Ajout de scripts pour tester les graphiques statistiques en local. [#3569](https://github.com/SocialGouv/egapro/issues/3569)
- Mise en place d'un plan de tracking Matomo (événements client + documentation). [#3625](https://github.com/SocialGouv/egapro/issues/3625)
- Refonte des pages avis CSE. [#3476](https://github.com/SocialGouv/egapro/issues/3476) [#3639](https://github.com/SocialGouv/egapro/issues/3639)
- Ajout d'un diagramme de flux du parcours CSE 2027 avec superposition des étapes FSM. [#3433](https://github.com/SocialGouv/egapro/issues/3433)
- Implémentation de l'exemption de consentement CNIL pour Matomo. [#3655](https://github.com/SocialGouv/egapro/issues/3655)
- Ajout d'événements Matomo pour l'indicateur 7 et suivi des liens d'aide. [#3707](https://github.com/SocialGouv/egapro/issues/3707)
- Amélioration des graphiques Matomo /admin/stats (usage modèle, liens d'aide, split appareil). [#3658](https://github.com/SocialGouv/egapro/issues/3658)
