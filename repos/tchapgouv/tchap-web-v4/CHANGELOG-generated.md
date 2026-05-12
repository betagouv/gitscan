## Changelog : tchap-web-v4 (30 derniers jours, au 11 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à tchap-web-v4 au cours des 30 derniers jours. Les principales évolutions concernent l'amélioration de la sécurité, notamment avec la gestion des liens externes et l'ouverture des appels groupés, ainsi que des ajustements d'interface utilisateur et de configuration pour répondre aux besoins spécifiques de l'administration.

### Évolutions fonctionnelles
- Amélioration de la sécurité : correction d'un problème lié au comportement des liens externes, qui étaient désactivés de manière incorrecte [#1591](https://github.com/tchapgouv/tchap-web-v4/pull/1591).
- Sécurité : Mise en place d'un correctif pour un problème de sécurité lié à l'ouverture de fichiers sur la version desktop [#1574](https://github.com/tchapgouv/tchap-web-v4/pull/1574).
- Ouverture des appels groupés : Activation progressive des appels groupés pour différents types d'utilisateurs (collectivités, intérieur) via des flags de configuration [#1569](https://github.com/tchapgouv/tchap-web-v4/pull/1569), [#1570](https://github.com/tchapgouv/tchap-web-v4/pull/1570), [#1579](https://github.com/tchapgouv/tchap-web-v4/pull/1579).
- Amélioration de l'authentification : Simplification du processus de connexion et d'inscription en utilisant un pré-contrôle de l'adresse email [#1583](https://github.com/tchapgouv/tchap-web-v4/pull/1583).
- Gestion des salons privés : Ajout d'un badge pour indiquer les salons privés non chiffrés [#1536](https://github.com/tchapgouv/tchap-web-v4/pull/1536).
- Amélioration de l'interface : Utilisation de la liste des salons Tchap pour les nouveaux salons [#1567](https://github.com/tchapgouv/tchap-web-v4/pull/1567).
- Ajout d'un schéma de lien profond personnalisé pour la version desktop [#1571](https://github.com/tchapgouv/tchap-web-v4/pull/1571).
- Possibilité d'utiliser le chiffage de bout en bout (EC) dans les conversations directes via un flag de fonctionnalité [#1563](https://github.com/tchapgouv/tchap-web-v4/pull/1563).

### Évolutions techniques
- Mise à jour de la librairie Compound-web en version 5.0.5 et 5.0.6 [#1564](https://github.com/tchapgouv/tchap-web-v4/pull/1564), [#1585](https://github.com/tchapgouv/tchap-web-v4/pull/1585).
- Refactorisation du code pour supprimer la fonctionnalité MAS (Message Archive System) qui est désormais activée par défaut [#1575](https://github.com/tchapgouv/tchap-web-v4/pull/1575).
- Ajout de la configuration de la visibilité dans les règles d'accès Tchap [#1585](https://github.com/tchapgouv/tchap-web-v4/pull/1585).
- Mise à jour vers la version 4.19.6 et 4.19.7 [#1580](https://github.com/tchapgouv/tchap-web-v4/pull/1580), [#1592](https://github.com/tchapgouv/tchap-web-v4/pull/1592).
- Suppression d'un test flaky [#1591](https://github.com/tchapgouv/tchap-web-v4/pull/1591).

### Autres changements
- Modification du texte d'introduction pour le PNC (Prestataire Numérique de Confiance) [#1594](https://github.com/tchapgouv/tchap-web-v4/pull/1594).
- Amélioration de la couleur du texte en mode contraste élevé (HC) pour le spotlight [#1568](https://github.com/tchapgouv/tchap-web-v4/pull/1568).
- Correction de problèmes de linting et de tests après la refactorisation du code [#1575](https://github.com/tchapgouv/tchap-web-v4/pull/1575).
