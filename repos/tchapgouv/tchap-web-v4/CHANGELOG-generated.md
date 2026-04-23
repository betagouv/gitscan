## Changelog : tchap-web-v4 (30 derniers jours, au 2026-04-22)

### Résumé
Ce mois-ci, les évolutions de tchap-web-v4 se concentrent sur l'amélioration de la sécurité et de la flexibilité de la plateforme. Des options de création de salons privés non chiffrés ont été ajoutées, ainsi que des ajustements pour l'ouverture des appels groupés en fonction des différents environnements d'utilisation. Des corrections et optimisations techniques ont également été apportées pour améliorer la stabilité et la performance.

### Évolutions fonctionnelles
- Ajout de la possibilité de créer des salons privés non chiffrés. Un badge indique clairement le statut non chiffré de ces salons. [#1536](https://github.com/tchapgouv/tchap-web-v4/pull/1536)
- Ouverture des appels groupés pour les environnements "interieur" et "collectivite". [#1570](https://github.com/tchapgouv/tchap-web-v4/pull/1570), [#1569](https://github.com/tchapgouv/tchap-web-v4/pull/1569)
- Amélioration de l'affichage des badges dans l'interface. [#1555](https://github.com/tchapgouv/tchap-web-v4/pull/1555)
- Modification du flux de réinitialisation d'identité pour une meilleure expérience utilisateur. [#1558](https://github.com/tchapgouv/tchap-web-v4/pull/1558)
- Ajout d'une option via un *feature flag* pour utiliser le chiffement de bout en bout (EC) dans les discussions privées. [#1563](https://github.com/tchapgouv/tchap-web-v4/pull/1563)
- Amélioration de l'affichage des notifications sur la version desktop, avec un indicateur visuel et une gestion du nombre de notifications. [#1544](https://github.com/tchapgouv/tchap-web-v4/pull/1544)
- Modification de la formulation de la vérification des emojis. [#1546](https://github.com/tchapgouv/tchap-web-v4/pull/1546)

### Évolutions techniques
- Mise à jour de la bibliothèque Compound-web vers la version 5.0.5. [#1564](https://github.com/tchapgouv/tchap-web-v4/pull/1564)
- Mise à jour vers la version 4.19.5 de la plateforme. [#1568](https://github.com/tchapgouv/tchap-web-v4/pull/1568)
- Refonte du routage pour différencier les pages de connexion et d'enregistrement.
- Suppression du code lié à l'ancienne fonctionnalité MAS (par défaut, MAS est activé).
- Ajout d'un schéma de lien profond personnalisé pour la version desktop. [#1571](https://github.com/tchapgouv/tchap-web-v4/pull/1571)
- Nettoyage du code et suppression de code obsolète.

### Autres changements
- Correction de problèmes de linting et ajout de tests unitaires.
- Mise à jour de la configuration pour l'ouverture des appels groupés en finance. [#1549](https://github.com/tchapgouv/tchap-web-v4/pull/1549)
- Correction d'un bug lié à l'affichage des labels. [#1567](https://github.com/tchapgouv/tchap-web-v4/pull/1567)
- Ajout de tests pour le hook `tchaproomtype`.
- Ajout de tests pour `roomaccess`.
- Ajout de tests pour tchaputils.
