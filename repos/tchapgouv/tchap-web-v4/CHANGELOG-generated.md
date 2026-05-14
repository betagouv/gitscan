## Changelog : tchap-web-v4 (30 derniers jours, au 2026-05-13)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'invitation d'utilisateurs externes, la gestion des appels groupés et l'ajout de fonctionnalités liées à la sécurité et à la conformité, notamment l'implémentation d'une "red list" configurable. Des corrections de bugs et des optimisations ont également été apportées pour améliorer l'expérience utilisateur.

### Évolutions fonctionnelles
- **Invitation d'utilisateurs externes :** Amélioration du flux d'invitation d'utilisateurs externes avec des vérifications supplémentaires pour garantir la sécurité et la conformité [#1573](https://github.com/tchapgouv/tchap-web-v4/pull/1573).
- **Liste rouge (Red List) :** Ajout d'une fonctionnalité configurable permettant de gérer une liste rouge, probablement pour restreindre l'accès à certains domaines ou utilisateurs [#1586](https://github.com/tchapgouv/tchap-web-v4/pull/1586).
- **Appels groupés :** Activation progressive des appels groupés pour différents types d'organisations (collectivités, intérieur) via des flags de configuration [#1568](https://github.com/tchapgouv/tchap-web-v4/pull/1568), [#1569](https://github.com/tchapgouv/tchap-web-v4/pull/1569), [#1579](https://github.com/tchapgouv/tchap-web-v4/pull/1579).
- **Authentification :** Refonte du processus de connexion et d'enregistrement pour utiliser un pré-check par email, améliorant ainsi l'expérience utilisateur et la sécurité [#1583](https://github.com/tchapgouv/tchap-web-v4/pull/1583).
- **Accès aux rooms :** Modification des règles d'accès aux rooms lors de l'invitation d'utilisateurs [#1560](https://github.com/tchapgouv/tchap-web-v4/pull/1560).
- **Cryptage de bout en bout :** Ajout d'un flag de fonctionnalité pour permettre l'utilisation du cryptage de bout en bout dans les conversations directes [#1563](https://github.com/tchapgouv/tchap-web-v4/pull/1563).

### Évolutions techniques
- **Mise à jour de Compound-web :** Mise à jour de la librairie Compound-web vers la version 5.0.5 et 5.0.6 [#1585](https://github.com/tchapgouv/tchap-web-v4/pull/1585), [#1564](https://github.com/tchapgouv/tchap-web-v4/pull/1564), [#1574](https://github.com/tchapgouv/tchap-web-v4/pull/1574), [#1584](https://github.com/tchapgouv/tchap-web-v4/pull/1584).
- **Mise à jour de la version :** Passage à la version 4.19.6 et 4.19.7 [#1580](https://github.com/tchapgouv/tchap-web-v4/pull/1580), [#1592](https://github.com/tchapgouv/tchap-web-v4/pull/1592).
- **Suppression de code obsolète :** Suppression du code lié à l'ancienne fonctionnalité MAS (Multi-Account Support) [#1575](https://github.com/tchapgouv/tchap-web-v4/pull/1575).
- **Amélioration de la configuration :** Ajout de la configuration du schéma de deep link personnalisé pour l'application desktop [#1571](https://github.com/tchapgouv/tchap-web-v4/pull/1571).

### Autres changements
- **Corrections de tests :** Correction de plusieurs tests pour améliorer la fiabilité de la suite de tests.
- **Améliorations de la documentation :** Mise à jour de la documentation pour refléter les changements récents.
- **Refactoring du code :** Refactoring de certaines parties du code pour améliorer la lisibilité et la maintenabilité.
- **Correction de l'affichage des liens externes :** Correction d'un problème d'affichage des liens externes [#1591](https://github.com/tchapgouv/tchap-web-v4/pull/1591).
- **Modification du texte d'introduction PNC :** Modification du texte d'introduction pour le PNC (Point de Contact National) [#1594](https://github.com/tchapgouv/tchap-web-v4/pull/1594).
