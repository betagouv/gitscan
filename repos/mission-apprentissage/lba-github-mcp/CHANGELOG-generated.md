## Changelog : lba-github-mcp (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des sprints et des issues dans les projets GitHub.  De nouvelles fonctionnalités permettent de générer dynamiquement les sprints à partir des projets GitHub, d'exposer des informations plus détaillées sur les issues (dates de sprint, priorité) et d'améliorer l'API pour la création et la mise à jour des issues.

### Évolutions fonctionnelles
- Ajout de la génération dynamique des sprints à partir des projets GitHub. [#1](https://github.com/mission-apprentissage/lba-github-mcp/pull/1)
- L'API `list_project_items` permet désormais de lister les éléments d'un projet, incluant l'historique de statut.
- L'API `update_issue` accepte désormais tous les champs et permet de définir le type de champ lors de la mise à jour des champs de projet.
- L'API `create_issue` accepte maintenant les paramètres `parent_issue_number` et `blocked_by`.
- Exposition des dates de début, de fin et de durée des sprints via l'API `list_project_items`.
- La priorité d'une issue est désormais correctement lue à partir de l'ID du champ.

### Évolutions techniques
- Renommage de `Issue.fieldValues` en `Issue.issueFieldValues` pour plus de clarté.
- Correction d'une variable `$pid` non utilisée dans la requête `getIssueContext`.
- Correction de l'emplacement de la priorité des champs, déplacée au niveau `ProjectV2Item` au lieu de `Issue`.

### Autres changements
- Aucun changement significatif à signaler.
