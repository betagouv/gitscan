## Changelog : tchap-x-ios (30 derniers jours, au 9 avril 2026)

### Résumé
Cette version apporte des améliorations de sécurité en désactivant les salons privés non chiffrés et en masquant l'option de connexion par QR code sur l'écran d'accueil. Des corrections et des ajustements ont été effectués pour améliorer la stabilité et la compatibilité de l'application, notamment concernant la gestion des instances Matrix et la réouverture de l'écran de récupération.

### Évolutions fonctionnelles
- Désactivation des salons privés non chiffrés pour renforcer la sécurité des conversations. [#318](https://github.com/tchapgouv/tchap-x-ios/pull/318)
- Masquage du bouton de connexion par QR code sur l'écran d'accueil pour simplifier l'expérience utilisateur et potentiellement améliorer la sécurité. [#316](https://github.com/tchapgouv/tchap-x-ios/pull/316)
- Autorisation de la connexion à toutes les instances Matrix, offrant une plus grande flexibilité aux utilisateurs. [#311](https://github.com/tchapgouv/tchap-x-ios/pull/311)
- L'écran de récupération s'ouvre maintenant avant l'écran de confirmation d'identité, améliorant le flux de récupération de compte. [#324](https://github.com/tchapgouv/tchap-x-ios/pull/324)

### Évolutions techniques
- Mise à jour du SDK Matrix Rust pour bénéficier des dernières corrections et améliorations. [#322](https://github.com/tchapgouv/tchap-x-ios/pull/322), [#4d3d9b903](https://github.com/tchapgouv/tchap-x-ios/commit/4d3d9b903)
- Refactorisation du code pour supprimer du code BWI (Business Workflow Integration) inutilisé, améliorant la maintenabilité. [#304](https://github.com/tchapgouv/tchap-x-ios/pull/304)
- Mise en place d'un système de build basé sur les dépendances GitHub pour une meilleure gestion des dépendances. [#314](https://github.com/tchapgouv/tchap-x-ios/pull/314)
- Désactivation de Sentry pour des raisons de configuration et de conformité. [#308](https://github.com/tchapgouv/tchap-x-ios/pull/308), [#f19b077d8](https://github.com/tchapgouv/tchap-x-ios/commit/f19b077d8)

### Autres changements
- Modification du libellé du bouton "Sign in manually" en "Sign in" pour une meilleure clarté. [#315](https://github.com/tchapgouv/tchap-x-ios/pull/315)
- Incrémentation de la version de l'application à v0.9.10. [#322](https://github.com/tchapgouv/tchap-x-ios/commit/637c99daf)
