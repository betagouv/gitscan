## Changelog : tchap-web-v4 (30 derniers jours, au 2026-04-13)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'ajout de nouvelles fonctionnalités liées à la gestion des salons privés non chiffrés, ainsi que sur des corrections et des optimisations pour améliorer l'expérience utilisateur, notamment au niveau des notifications et de l'interface. Des mises à jour de dépendances et des corrections de bugs ont également été apportées.

### Évolutions fonctionnelles
- **Salons privés non chiffrés :** Ajout de la possibilité de créer des salons privés non chiffrés, avec un badge spécifique pour les identifier. [#1525](https://github.com/tchapgouv/tchap-web-v4/pull/1525)
- **Gestion de l'identité :** Refonte du flux de confirmation de réinitialisation d'identité pour une meilleure clarté et expérience utilisateur. [#1478](https://github.com/tchapgouv/tchap-web-v4/pull/1478)
- **Vérification des emojis :** Modification du libellé lié à la vérification des emojis. [#1546](https://github.com/tchapgouv/tchap-web-v4/pull/1546)
- **Appel audio/vidéo :** Intégration d'une version spécifique de `element-call` pour supporter l'Open Finance. [#1547](https://github.com/tchapgouv/tchap-web-v4/pull/1547)
- **Notifications (Desktop) :** Correction des notifications sur desktop (ajout d'un overlay icon et correction du nombre de notifications). [#1544](https://github.com/tchapgouv/tchap-web-v4/pull/1544)
- **Paramètres des salons chiffrés :** Ajout d'un flag pour les paramètres des salons chiffrés. [#1537](https://github.com/tchapgouv/tchap-web-v4/pull/1537)
- **SSO (Edge PWA) :** Correction d'un problème de redirection SSO dans Edge PWA. [#1247](https://github.com/tchapgouv/tchap-web-v4/pull/1247)

### Évolutions techniques
- **Mise à jour de Gaufre :** Mise à jour vers une nouvelle version de Gaufre. [#1525](https://github.com/tchapgouv/tchap-web-v4/pull/1525)
- **Utilisation de Feature Flags :** Utilisation de feature flags pour la création de salons non chiffrés au lieu de variables.
- **Refactoring :** Refactoring du code pour la gestion des salons privés non chiffrés.
- **Mise à jour de dépendances :** Mise à jour vers la version 4.19.3 puis 4.19.4. [#1550](https://github.com/tchapgouv/tchap-web-v4/pull/1550), [#1561](https://github.com/tchapgouv/tchap-web-v4/pull/1561)
- **Amélioration de la gestion des erreurs :** Correction d'un problème lié aux erreurs lors du changement de niveau de pouvoir dans les paramètres des salons.

### Autres changements
- **Tests :** Ajout de tests pour les types de salons Tchap et pour la gestion des accès aux salons.
- **Documentation :** Ajout de documentation pour la création de salons privés non chiffrés.
- **CSS :** Modifications du CSS pour l'apparence des badges et des boutons.
- **Suppression de code obsolète :** Suppression d'icônes et de logique liées aux avatars globes.
- **Correction d'un bug lié à l'affichage des toasts keystorage hors synchronisation.** [#1533](https://github.com/tchapgouv/tchap-web-v4/pull/1533)
- **Ajout du nom et de la version de l'application sur desktop.** [#1539](https://github.com/tchapgouv/tchap-web-v4/pull/1539)
