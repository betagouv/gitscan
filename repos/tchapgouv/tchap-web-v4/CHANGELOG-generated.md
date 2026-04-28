## Changelog : tchap-web-v4 (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, les évolutions de tchap-web-v4 se concentrent sur l'amélioration de la sécurité et de la conformité, notamment avec l'introduction de salons privés non chiffrés et la gestion des appels en visioconférence avec des accès spécifiques pour différents types d'organisations (interieur, collectivités, finance). Des corrections et améliorations concernant l'authentification et l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- **Authentification :** Refonte complète de l'écran de connexion et d'enregistrement, avec une vérification préalable de l'adresse email. [#1583](https://github.com/tchapgouv/tchap-web-v4/pull/1583)
- **Salons privés :** Ajout de la possibilité de créer des salons privés non chiffrés, avec un badge d'indication clair. [#1536](https://github.com/tchapgouv/tchap-web-v4/pull/1536)
- **Appels en visioconférence :**
    - Ouverture des appels en visioconférence pour les organisations "interieur". [#1570](https://github.com/tchapgouv/tchap-web-v4/pull/1570)
    - Ouverture des appels en visioconférence pour les organisations "collectivités". [#1569](https://github.com/tchapgouv/tchap-web-v4/pull/1569)
    - Ouverture des appels en visioconférence pour les organisations "finance". [#1549](https://github.com/tchapgouv/tchap-web-v4/pull/1549)
- **Notifications (Desktop) :** Correction du problème d'affichage des notifications sur la version desktop, avec ajout d'une icône d'overlay. [#1544](https://github.com/tchapgouv/tchap-web-v4/pull/1544)
- **Emoji :** Modification du libellé concernant la vérification des emojis. [#1546](https://github.com/tchapgouv/tchap-web-v4/pull/1546)
- **Deep Links :** Ajout d'un schéma de deep link personnalisé dans la configuration. [#1571](https://github.com/tchapgouv/tchap-web-v4/pull/1571)

### Évolutions techniques
- **Mise à jour de Compound-web :** Passage à la version 5.0.5 de la librairie Compound-web. [#1564](https://github.com/tchapgouv/tchap-web-v4/pull/1564)
- **Refactoring :** Suppression du code lié à l'ancienne fonctionnalité MAS (Messaging and Security).
- **Configuration :** Utilisation de feature flags pour la création de salons privés non chiffrés.
- **Rework :** Refonte du flux de confirmation de réinitialisation d'identité. [#1558](https://github.com/tchapgouv/tchap-web-v4/pull/1558)
- **Routing :** Mise à jour du routing pour différencier les écrans de connexion et d'enregistrement.
- **Tests :** Ajout de tests pour le hook `tchaproomtype`.

### Autres changements
- **Design :** Modification du style des badges.
- **Documentation :** Mise à jour de la documentation (non précisée dans les commits).
- **Linting :** Correction de problèmes de linting.
- **Nettoyage de code :** Suppression de code obsolète.
