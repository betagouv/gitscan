## Changelog : envergo (30 derniers jours, au 2026-06-02)

### Résumé
Cette période a été marquée par des améliorations significatives des performances et de la stabilité de l'application, notamment au niveau de la gestion des données et des requêtes en base de données. Des corrections ont également été apportées pour améliorer l'expérience utilisateur, en particulier concernant l'affichage des données et la gestion des conditions d'évaluation. Enfin, des efforts ont été déployés pour renforcer la sécurité et la conformité, notamment en matière de RGPD.

### Évolutions fonctionnelles
- Amélioration de l'affichage des haies et de leur densité sur la carte. [#1124](https://github.com/MTES-MCT/envergo/issues/1124)
- Ajout d'un message d'avertissement lors de la présence d'espèces sensibles. [#1120](https://github.com/MTES-MCT/envergo/issues/1120)
- Modification du libellé "Administration" en "Espace instruction" pour plus de clarté. [#1145](https://github.com/MTES-MCT/envergo/issues/1145)
- Correction de l'affichage des messages et des erreurs dans l'interface utilisateur. [#1096](https://github.com/MTES-MCT/envergo/issues/1096)
- Amélioration de la gestion des conditions d'évaluation des règles urbaines (RU). [#1146](https://github.com/MTES-MCT/envergo/issues/1146)
- Ajout de la possibilité de compléter le contexte après l'évaluation des conditions. [#1119](https://github.com/MTES-MCT/envergo/issues/1119)
- Correction d'un problème d'affichage des données dans les détails des conditions de plantation. [#1141](https://github.com/MTES-MCT/envergo/issues/1141)
- Correction d'un bug lié à la gestion des jetons expirés. [#1097](https://github.com/MTES-MCT/envergo/issues/1097)
- Correction d'un problème de validation des données dans le formulaire Moulinette. [#1139](https://github.com/MTES-MCT/envergo/issues/1139)

### Évolutions techniques
- Optimisations significatives des performances des requêtes en base de données, notamment pour l'affichage des zones et des données Moulinette. [#1123](https://github.com/MTES-MCT/envergo/issues/1123)
- Mise en cache de plusieurs données fréquemment utilisées pour réduire la charge sur la base de données.
- Refactorisation du code pour améliorer la qualité et la maintenabilité.
- Simplification de la topologie des cercles pour accélérer l'affichage des données.
- Amélioration de la gestion des conditions d'évaluation des règles urbaines (RU) avec une meilleure organisation du code et ajout de tests.
- Suppression de code obsolète et de fonctionnalités non utilisées.
- Correction de plusieurs erreurs de style (PEP8).
- Mise à jour des dépendances. [#1096](https://github.com/MTES-MCT/envergo/issues/1096)
- Suppression des événements suivis par Brevo pour améliorer la conformité RGPD. [#1126](https://github.com/MTES-MCT/envergo/issues/1126)

### Autres changements
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Correction de tests unitaires et d'intégration.
- Amélioration de la lisibilité du code.
- Clarification de certains noms de paramètres et de variables.
- Mise à jour de la documentation.
- Correction de problèmes liés à la gestion des erreurs 403 et 405.
- Ajout de commentaires pour expliquer les choix de conception.
- Correction de problèmes de compatibilité avec les évaluations générées précédemment.
- Amélioration de la gestion des erreurs liées aux données départementales.
- Correction d'un problème lié à l'affichage des données dans le tableau des espèces.
- Suppression de messages d'avertissement inutiles.
