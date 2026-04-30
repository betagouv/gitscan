## Changelog : tchap-x-ios (30 derniers jours, au 28 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des espaces et des salons, notamment l'introduction de l'accès par lien aux salons, ainsi que des corrections et des ajustements d'interface utilisateur. Des efforts ont également été faits pour harmoniser la terminologie avec les standards Tchap.

### Évolutions fonctionnelles
- **Accès par lien aux salons :** Possibilité de générer un lien d'accès pour les salons, facilitant ainsi l'invitation de nouveaux participants. [#309](https://github.com/tchapgouv/tchap-x-ios/pull/309)
- **Gestion des espaces :** Amélioration de l'affichage et de la gestion des espaces, avec une action par défaut de filtrage des conversations. [#329](https://github.com/tchapgouv/tchap-x-ios/pull/329)
- **Création de salon :** Modification de l'interface de création de salon pour intégrer l'option d'accès par lien et masquer la sélection d'espace. [#325](https://github.com/tchapgouv/tchap-x-ios/pull/325)
- **Désactivation de l'épinglage des géolocalisations :** L'épinglage des données de géolocalisation a été temporairement désactivé. [#331](https://github.com/tchapgouv/tchap-x-ios/pull/331)
- **Taxonomie :** Mise à jour de la taxonomie. [#323](https://github.com/tchapgouv/tchap-x-ios/pull/323)
- **Écran de récupération :** L'écran de récupération s'ouvre maintenant en premier avant l'écran de confirmation d'identité. [#333](https://github.com/tchapgouv/tchap-x-ios/pull/333)

### Évolutions techniques
- **Mise à jour du SDK Matrix Rust :** Passage à la version v26.03.10 du SDK Matrix Rust.
- **Mise à jour de Compound Design Token :** Mise à jour vers la version 6.10-angelo.
- **Rebase :** Rebase de la branche Tchap sur ElementX-ios v26.03.3.
- **Formatage du code :** Le code a été formaté avec swiftformat v0.59.1 pour une meilleure lisibilité et cohérence.
- **Corrections de compilation des tests unitaires :** Résolution de problèmes de compilation des tests unitaires.

### Autres changements
- **Terminologie Tchap :** Utilisation de la terminologie spécifique à Tchap dans l'application.
- **Correction du gradient de la timeline :** Correction d'un problème d'affichage du gradient de la timeline.
- **Suppression de fichiers inutiles :** Suppression de fichiers hérités d'ElementX.
- **Amélioration de la gestion des autorisations :** Le bouton de bascule pour l'accès par lien est maintenant désactivé si l'activation de cette fonctionnalité n'est pas autorisée.
