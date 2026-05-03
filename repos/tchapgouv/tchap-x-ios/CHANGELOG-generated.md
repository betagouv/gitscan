## Changelog : tchap-x-ios (30 derniers jours, au 30 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à l'expérience utilisateur, notamment l'ajout de la fonctionnalité d'accès par lien aux salons, une meilleure gestion des espaces et des corrections pour une utilisation plus stable de l'application, y compris en cas de perte de connexion au serveur. Des ajustements spécifiques à Tchap ont également été effectués pour une meilleure cohérence avec les besoins de l'administration.

### Évolutions fonctionnelles
- **Accès par lien aux salons:** Implémentation de la fonctionnalité permettant de générer et d'utiliser des liens pour accéder directement à un salon [#309](https://github.com/tchapgouv/tchap-x-ios/pulls/309).
- **Gestion des espaces:** Amélioration de l'affichage et de l'interaction avec les espaces, avec une action par défaut de filtrage des conversations dans les espaces [#329](https://github.com/tchapgouv/tchap-x-ios/pulls/329).
- **Affichage des salons:** Modification de l'affichage des salons pour une meilleure clarté.
- **Indication de perte de connexion:** Affichage d'une bannière informative lorsque le serveur est inaccessible [#338](https://github.com/tchapgouv/tchap-x-ios/pulls/338).
- **Taxonomie:** Améliorations liées à la taxonomie (détails non spécifiés) [#323](https://github.com/tchapgouv/tchap-x-ios/pulls/323).
- **Récupération de compte:** Amélioration du flux de récupération de compte, affichant d'abord l'écran de récupération avant la confirmation d'identité.

### Évolutions techniques
- **Mise à jour des dépendances:**
    - Mise à jour de `compound-design-token` vers la version 6.10-angelo [#4eac3a73a](https://github.com/tchapgouv/tchap-x-ios/commit/4eac3a73a).
    - Mise à jour de `matrix-rust-components-swift` vers la version 26.03.10 [#09afa20b9](https://github.com/tchapgouv/tchap-x-ios/commit/09afa20b9).
- **Rebase:** Rebase de la branche ElementX-ios v26.03.3 dans la branche Tchap.
- **Désactivation du pinning géolocalisation:** Désactivation du pinning pour les données géolocalisées, à la fois dans le code et dans la configuration du projet [#331](https://github.com/tchapgouv/tchap-x-ios/pulls/331), [#325](https://github.com/tchapgouv/tchap-x-ios/pulls/325).
- **Correction de conflits de rebase:** Résolution des conflits de rebase lors de l'intégration de ElementX-ios v26.03.3.
- **Correction de compilation des tests unitaires:** Correction d'erreurs de compilation des tests unitaires.

### Autres changements
- Ajustements spécifiques à Tchap pour l'utilisation de la terminologie appropriée.
- Correction de typos dans les tests unitaires.
- Suppression de fichiers inutiles provenant d'ElementX.
- Amélioration de la gestion de l'état du bouton bascule pour l'accès par lien.
- Ajout de chaînes de caractères générées.
