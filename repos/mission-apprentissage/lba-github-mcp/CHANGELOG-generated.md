## Changelog : lba-github-mcp (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution significative avec l'ajout de nombreuses fonctionnalités pour améliorer l'exposition des informations et la manipulation des issues GitHub via l'API. Les améliorations concernent notamment la gestion des priorités, des sprints, des champs personnalisés et l'intégration avec les projets GitHub. Des outils ont été ajoutés pour faciliter l'ajout d'issues à des projets et la modification de leurs champs.

### Évolutions fonctionnelles
- Ajout de la possibilité de définir et de lire la priorité d'une issue (Urgent/High/Medium/Low) [#11968d2](https://github.com/mission-apprentissage/lba-github-mcp/commit/11968d2).
- Exposition des dates de début et de fin de sprint, ainsi que de sa durée, dans la liste des éléments de projet [#1505a39](https://github.com/mission-apprentissage/lba-github-mcp/commit/1505a39).
- Ajout de la possibilité de spécifier une issue parente et des issues bloquantes lors de la création d'une nouvelle issue [#e28a79a](https://github.com/mission-apprentissage/lba-github-mcp/commit/e28a79a).
- Exposition des champs "epic", "approver" et "sprint" sur les projets GitHub [#070c4df](https://github.com/mission-apprentissage/lba-github-mcp/commit/070c4df).
- Ajout des outils `list_project_items` et `list_status_history` pour récupérer des informations sur les projets et l'historique de statut des issues [#15b2bdb](https://github.com/mission-apprentissage/lba-github-mcp/commit/15b2bdb).
- L'outil `update_issue` accepte désormais tous les champs et permet de définir le type de champ lors de la modification d'un champ de projet [#8eb6651](https://github.com/mission-apprentissage/lba-github-mcp/commit/8eb6651).
- Ajout des outils `add_to_project` et `set_project_field` pour manipuler les projets GitHub [#7f8b9ac](https://github.com/mission-apprentissage/lba-github-mcp/commit/7f8b9ac).

### Évolutions techniques
- Correction de la lecture de la priorité depuis le bon champ (IssueFieldSingleSelectValue par ID) [#ef01710](https://github.com/mission-apprentissage/lba-github-mcp/commit/ef01710).
- Correction du placement de la valeur de priorité au niveau de ProjectV2Item et non de Issue [#375bc1d](https://github.com/mission-apprentissage/lba-github-mcp/commit/375bc1d).
- Renommage de `Issue.fieldValues` en `Issue.issueFieldValues` pour plus de clarté [#a2ea440](https://github.com/mission-apprentissage/lba-github-mcp/commit/a2ea440).
- Suppression d'une variable `$pid` non utilisée dans la requête `getIssueContext` [#06ac3df](https://github.com/mission-apprentissage/lba-github-mcp/commit/06ac3df).
- Restriction de l'accès à l'endpoint MCP via un token URL optionnel [#6f073ab](https://github.com/mission-apprentissage/lba-github-mcp/commit/6f073ab).

### Autres changements
- Initialisation du serveur MCP GitHub pour labonnealternance [#82bd574](https://github.com/mission-apprentissage/lba-github-mcp/commit/82bd574).
- Ajout d'un fichier `.gitignore` [#2ad3164](https://github.com/mission-apprentissage/lba-github-mcp/commit/2ad3164).
- Mise à jour de la configuration Vercel (`vercel.json`) [#820a931](https://github.com/mission-apprentissage/lba-github-mcp/commit/820a931).
- Mise à jour des variables d'environnement (`env`) [#fbf2177](https://github.com/mission-apprentissage/lba-github-mcp/commit/fbf2177).
- Corrections de dépendances [#07d856a](https://github.com/mission-apprentissage/lba-github-mcp/commit/07d856a).
