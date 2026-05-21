## Changelog : envergo (30 derniers jours, au 20 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations de la performance, notamment au niveau de l'affichage des haies et de la gestion des données, ainsi que par des corrections de bugs et des améliorations de l'expérience utilisateur, notamment concernant la gestion des jetons d'authentification et l'affichage des informations de responsabilité. Des efforts ont également été déployés pour améliorer la documentation et la clarté du code.

### Évolutions fonctionnelles
- Amélioration de l'affichage des haies : optimisation de la requête et simplification de la topologie pour un affichage plus rapide [#1096](https://github.com/MTES-MCT/envergo/pull/1096).
- Correction d'un bug empêchant l'affichage correct des longueurs de haies [#1097](https://github.com/MTES-MCT/envergo/pull/1097).
- Amélioration de la gestion des jetons d'authentification : affichage de messages d'erreur plus clairs en cas de jeton expiré ou invalide, et ajout de tests pour garantir le bon fonctionnement [#1096](https://github.com/MTES-MCT/envergo/pull/1096).
- Ajout d'informations de suivi concernant la responsabilité dans les résultats de simulation et les pages d'évaluation [#1098](https://github.com/MTES-MCT/envergo/pull/1098).
- Correction d'un bug lié à l'affichage des champs de démarches simplifiées [#1105](https://github.com/MTES-MCT/envergo/pull/1105).
- Correction d'un bug lié à la date dans un formulaire [#1105](https://github.com/MTES-MCT/envergo/pull/1105).
- Correction d'un bug lié à la fin du dessin des haies [#1108](https://github.com/MTES-MCT/envergo/pull/1108).
- Correction d'un bug lié à l'affichage des haies [#1109](https://github.com/MTES-MCT/envergo/pull/1109).
- Amélioration de l'affichage des messages d'erreur et des informations contextuelles.
- Ajout d'un lien vers la documentation Gitbook pour les instructeurs [#1098](https://github.com/MTES-MCT/envergo/pull/1098).

### Évolutions techniques
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- Optimisation des requêtes pour améliorer les performances, notamment au niveau de la gestion des zones et des coefficients RU [#1086](https://github.com/MTES-MCT/envergo/pull/1086).
- Simplification de la logique de calcul de la densité des haies.
- Amélioration de la gestion des migrations de base de données.
- Mise à jour des dépendances et correction de problèmes liés aux tests.
- Utilisation d'une méthode plus précise pour les comparaisons de nombres à virgule flottante dans les tests.
- Suppression de code obsolète et nettoyage du code.
- Migration des champs d'identifiants vers des champs JSON pour plus de flexibilité.
- Amélioration de la structure des tables de densité.

### Autres changements
- Amélioration de la documentation et ajout de commentaires pour faciliter la compréhension du code.
- Mise à jour des tests pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- Ajout de tests pour la gestion des cookies.
- Correction de problèmes mineurs d'interface utilisateur.
- Ajout de logs pour faciliter le débogage.
- Amélioration de la gestion des erreurs et des exceptions.
- Modification de l'URL de la FAQ des instructeurs vers Gitbook.
- Ajout d'un bouton pour obtenir un nouveau lien.
- Ajout d'éléments Matomo pour le suivi des pages vues.
- Amélioration de la gestion des permissions d'accès.
- Correction de problèmes de validation des formulaires.
- Ajout de migrations pour les changements de schéma de base de données.
- Amélioration de la gestion des erreurs de validation dans les tests.
- Ajout de tests unitaires et d'intégration.
- Correction de bugs liés à l'upload de fichiers [#1083](https://github.com/MTES-MCT/envergo/pull/1083).
- Correction d'un bug lié à la configuration manquante [#1089](https://github.com/MTES-MCT/envergo/pull/1089).
