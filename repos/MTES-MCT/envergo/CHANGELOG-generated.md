## Changelog : envergo (30 derniers jours)

### Résumé
Cette période a été marquée par de nombreuses améliorations et corrections de bugs, touchant à la fois l'interface utilisateur, la gestion des données et l'infrastructure du projet. Les améliorations concernent notamment la gestion des configurations, l'évaluation de l'impact environnemental des haies, et la correction de problèmes liés à l'affichage et à la manipulation des données. Des efforts ont également été faits pour améliorer la robustesse et la performance de l'application.

### Évolutions fonctionnelles
- Amélioration de la gestion des dates de validité des configurations, avec ajout de champs de date de début et de fin de validité et une vérification des chevauchements. [#954](https://github.com/MTES-MCT/envergo/pull/954)
- Ajout de la possibilité de filtrer les configurations par date. [#971](https://github.com/MTES-MCT/envergo/pull/971)
- Amélioration de l'affichage des réglementations Natura 2000. [#1008](https://github.com/MTES-MCT/envergo/pull/1008)
- Correction d'un bug empêchant l'affichage correct des projets. [#1032](https://github.com/MTES-MCT/envergo/pull/1032)
- Correction d'un bug lié à la synchronisation des données avec Pipedrive. [#1031](https://github.com/MTES-MCT/envergo/pull/1031)
- Amélioration de l'affichage des informations relatives aux haies sur la carte. [#1018](https://github.com/MTES-MCT/envergo/pull/1018)
- Ajout de la possibilité d'afficher les sites inscrits. [#997](https://github.com/MTES-MCT/envergo/pull/997)
- Amélioration de l'affichage de la table récapitulative des haies. [#990](https://github.com/MTES-MCT/envergo/pull/990)
- Correction de liens incorrects dans les notifications. [#995](https://github.com/MTES-MCT/envergo/pull/995)
- Ajout de la possibilité d'afficher la carte par département. [#981](https://github.com/MTES-MCT/envergo/pull/981)
- Suppression des tokens d'analytics liés aux consultations. [#986](https://github.com/MTES-MCT/envergo/pull/986)

### Évolutions techniques
- Mise à jour de Django en version 4.2.x. [#1009](https://github.com/MTES-MCT/envergo/pull/1009)
- Refactorisation du code pour améliorer la performance et la maintenabilité.
- Amélioration des tests unitaires et d'intégration, avec ajout de nouvelles couvertures de tests. [#1028](https://github.com/MTES-MCT/envergo/pull/1028)
- Correction de problèmes de linting et de conformité au style de code.
- Amélioration de la gestion des erreurs et des exceptions.
- Optimisation des requêtes à la base de données.
- Suppression de dépendances inutiles (bs4).
- Utilisation de nouveaux widgets pour les champs de surface avec unités.
- Amélioration de la gestion des URL et des liens.
- Mise en place de vérifications de sécurité pour prévenir les attaques XSS.
- Correction de problèmes de syntaxe HTML.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.

### Autres changements
- Mise à jour de la documentation.
- Correction de typos et d'erreurs de texte.
- Amélioration de la précision des définitions relatives à l'assiette du terrain.
- Précision sur les droits d'accès à la page de paramétrage.
- Mise à jour des messages d'erreur pour plus de clarté.
- Correction de problèmes mineurs d'interface utilisateur.
- Ajout de tests pour les nouvelles fonctionnalités.
- Amélioration de la gestion des configurations et des paramètres de l'application.
- Correction de problèmes liés à la gestion des sessions utilisateur.
- Ajout de logs pour faciliter le débogage.
- Amélioration de la gestion des erreurs Sentry.
