## Changelog : tchap-x-ios (30 derniers jours, au 30 avril 2026)

### Résumé
Cette version apporte des améliorations à la gestion des espaces, notamment dans l'affichage et la création de salons. Des corrections ont été apportées pour résoudre des problèmes de connexion et d'affichage, ainsi qu'une gestion améliorée des erreurs de serveur. Une bannière d'alerte s'affiche désormais en cas d'indisponibilité du serveur.

### Évolutions fonctionnelles
- Amélioration de l'affichage des espaces et des salons : l'action par défaut pour les espaces est maintenant le filtrage des conversations. [#329](https://github.com/tchapgouv/tchap-x-ios/issues/329)
- Possibilité d'accéder à un salon via un lien. [#309](https://github.com/tchapgouv/tchap-x-ios/issues/309)
- Affichage d'une bannière d'alerte lorsque le serveur est inaccessible. [#338](https://github.com/tchapgouv/tchap-x-ios/issues/338)
- Modification du libellé pour utiliser la terminologie spécifique à Tchap. [#323](https://github.com/tchapgouv/tchap-x-ios/issues/323)
- Correction de l'affichage du gradient dans la timeline.
- Suppression temporaire de l'épinglage des données géographiques. [#331](https://github.com/tchapgouv/tchap-x-ios/issues/331)

### Évolutions techniques
- Mise à jour de la bibliothèque `matrix-rust-components-swift` vers la version 26.03.10.
- Mise à jour de `compound-design-token` vers la version 6.10-angelo.
- Intégration de la version 26.03.3 d'ElementX-ios.
- Correction de conflits de rebase lors de l'intégration d'ElementX-ios.
- Correction d'un problème de CA (Certificate Authority) en environnement de staging. [#335](https://github.com/tchapgouv/tchap-x-ios/issues/335)

### Autres changements
- Amélioration de la gestion des erreurs et de la robustesse de l'application.
- Corrections diverses et optimisations du code.
- Mise à jour de la configuration pour désactiver l'épinglage des données géographiques. [#336](https://github.com/tchapgouv/tchap-x-ios/issues/336)
