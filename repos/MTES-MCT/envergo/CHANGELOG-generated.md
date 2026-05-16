## Changelog : envergo (30 derniers jours, au 11 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment dans la gestion des haies Natura 2000 et des contacts. Des corrections de bugs et des optimisations techniques ont également été apportées, améliorant la stabilité et la performance de l'application. L'intégration de nouvelles fonctionnalités, comme le suivi des informations de responsabilité, renforce l'utilité de l'outil pour les agents de l'administration.

### Évolutions fonctionnelles
- Amélioration de la gestion des contacts pour les haies, avec un fallback sur la configuration la plus récente et un avertissement si le portail n'est pas activé. [#1081](https://github.com/MTES-MCT/envergo/pull/1081)
- Ajout d'un suivi des informations de responsabilité dans les pages d'évaluation et de simulation. [#1092](https://github.com/MTES-MCT/envergo/pull/1092)
- Amélioration des notifications d'état des pétitions, avec des informations plus claires pour l'instructeur. [#1092](https://github.com/MTES-MCT/envergo/pull/1092)
- Correction de l'affichage du périmètre dans les haies. [#1088](https://github.com/MTES-MCT/envergo/pull/1088)
- Correction de l'affichage des haies générées avant les dernières modifications. [#1109](https://github.com/MTES-MCT/envergo/pull/1109)
- Correction de l'affichage de la date dans les formulaires. [#1105](https://github.com/MTES-MCT/envergo/pull/1105)
- Amélioration de l'interface utilisateur pour la gestion des actions, notamment l'ajout d'un bouton pour supprimer une pièce jointe. [#1081](https://github.com/MTES-MCT/envergo/pull/1081)
- Ajout d'un message d'information envoyé par la DS (Directions des Services). [#1092](https://github.com/MTES-MCT/envergo/pull/1092)

### Évolutions techniques
- Refactorisation du code pour utiliser des dictionnaires imbriqués au lieu de chaînes concaténées pour la gestion du statut DS. [#1092](https://github.com/MTES-MCT/envergo/pull/1092)
- Optimisation de la récupération des valeurs des champs de la démarche numérique (DN). [#1103](https://github.com/MTES-MCT/envergo/pull/1103)
- Mise à jour de la logique de calcul des coefficients RU (Régime Unique). [#1086](https://github.com/MTES-MCT/envergo/pull/1086)
- Amélioration de la gestion des zones pour optimiser les performances. [#1070](https://github.com/MTES-MCT/envergo/pull/1070)
- Simplification de la logique de calcul des résultats pour les haies. [#1070](https://github.com/MTES-MCT/envergo/pull/1070)
- Suppression de code obsolète et amélioration de la lisibilité du code.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les corrections de bugs.
- Ajout de migrations pour les modifications de la base de données.
- Correction de problèmes de validation dans les tests.
- Amélioration des messages d'erreur et des validations des formulaires.
- Mise à jour de l'URL de la FAQ pour les instructeurs vers Gitbook. [#1101](https://github.com/MTES-MCT/envergo/pull/1101)
- Nettoyage du code et correction de problèmes de style avec pre-commit.
