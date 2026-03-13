## Changelog : data_pass (30 derniers jours)

### Résumé
Les dernières semaines ont été marquées par des améliorations significatives de l'expérience utilisateur, notamment dans la gestion des habilitations et des demandes d'accès. Des corrections de bugs et des optimisations ont également été apportées, ainsi que des évolutions concernant l'intégration avec FranceConnect et les API partenaires. L'ajout de nouvelles pages (Mentions Légales, Politique de Confidentialité) et l'amélioration de la gestion des types d'habilitation contribuent à une meilleure conformité et une plus grande flexibilité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la page Politique de confidentialité et des Mentions Légales. [#1357](https://github.com/etalab/data_pass/pull/1357), [#1367](https://github.com/etalab/data_pass/pull/1367)
- Possibilité de sélectionner une habilitation FranceConnect existante lors d'une demande APIPFC. [#1407](https://github.com/etalab/data_pass/pull/1407)
- Amélioration de la réouverture d'une habilitation APIPFC compatible APIPFC sans générer une nouvelle habilitation FC. [#1399](https://github.com/etalab/data_pass/pull/1399)
- Ajout de la possibilité de révoquer une habilitation APIP. [#1404](https://github.com/etalab/data_pass/pull/1404)
- Amélioration de l'affichage du motif d'annulation d'une réouverture d'habilitation. [#1381](https://github.com/etalab/data_pass/pull/1381)
- Possibilité de sélectionner du texte dans le champ email lors du transfert d'une habilitation. [#1364](https://github.com/etalab/data_pass/pull/1364)
- Ajout de la gestion des types d'habilitation dans l'interface d'administration (création, modification, suppression). [#1422](https://github.com/etalab/data_pass/pull/1422), [#1436](https://github.com/etalab/data_pass/pull/1436)
- Ajout de scopes aux types d'habilitation dynamiques. [#1425](https://github.com/etalab/data_pass/pull/1425)
- Affichage du nom du type d'habilitation dans les messages de confirmation. [#1428](https://github.com/etalab/data_pass/pull/1428)
- Ajout d'un badge "nouveau message" dans la liste des demandes pour les instructeurs. [#1411](https://github.com/etalab/data_pass/pull/1411)
- Amélioration de la gestion des habilitations liées à la suppression d'un type d'habilitation. [#1438](https://github.com/etalab/data_pass/pull/1438)
- Ajout de la possibilité de choisir une habilitation FC existante pour la lier à une nouvelle demande. [#1396](https://github.com/etalab/data_pass/pull/1396)

### Évolutions techniques
- Refactor de la validation des types dynamiques pour améliorer la lisibilité des tests. [#1435](https://github.com/etalab/data_pass/pull/1435)
- Rotation annuelle du token webhook de l'API E/P. [#1439](https://github.com/etalab/data_pass/pull/1439)
- Mise à jour des dépendances (Rubocop, RSpec, Rails Pulse, etc.). [#1429](https://github.com/etalab/data_pass/pull/1429), [#1408](https://github.com/etalab/data_pass/pull/1408), [#1368](https://github.com/etalab/data_pass/pull/1368), [#1365](https://github.com/etalab/data_pass/pull/1365)
- Amélioration de la configuration du worktree Git pour faciliter le développement parallèle. [#1365](https://github.com/etalab/data_pass/pull/1365)
- Correction de tests flaky. [#1374](https://github.com/etalab/data_pass/pull/1374)
- Suppression de gem dupliquée. [#1424](https://github.com/etalab/data_pass/pull/1424)
- Mise en place de Rails Pulse pour le monitoring. [#1359](https://github.com/etalab/data_pass/pull/1359)
- Correction d'un problème lié à la gestion des habilitations FC lors de la réouverture d'une demande. [#1390](https://github.com/etalab/data_pass/pull/1390)

### Autres changements
- Mise à jour de la documentation pour les nouvelles habilitations. [#1372](https://github.com/etalab/data_pass/pull/1372)
- Corrections de liens et de textes dans l'interface utilisateur. [#1420](https://github.com/etalab/data_pass/pull/1420), [#1341](https://github.com/etalab/data_pass/pull/1341)
- Modifications des API partenaires (APIPFC, API Entreprise). [#1380](https://github.com/etalab/data_pass/pull/1380), [#1340](https://github.com/etalab/data_pass/pull/1340)
- Ajout de commentaires et de documentation pour clarifier le code.
- Suppression de code obsolète.
- Corrections d'accessibilité (RGAA). [#1422](https://github.com/etalab/data_pass/pull/1422)
