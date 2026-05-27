## Changelog : lba-github-mcp (30 derniers jours, au 25 mai 2026)

### Résumé
Ce mois-ci, le projet a connu une avancée significative avec l'implémentation de nouvelles fonctionnalités pour enrichir les données exposées via l'API, notamment l'ajout de champs comme la priorité, l'épopée, l'approbateur et le sprint. Des outils pour interagir avec les projets GitHub ont également été ajoutés, ainsi qu'une restriction d'accès à l'endpoint MCP.

### Évolutions fonctionnelles
- Ajout du champ de priorité (Urgent/High/Medium/Low) aux issues.
- Exposition des champs épopée, approbateur et sprint pour les projets GitHub.
- Implémentation des outils `add_to_project` et `set_project_field` pour manipuler les projets GitHub.
- Restriction de l'accès à l'endpoint MCP via un token URL optionnel.

### Évolutions techniques
- Initialisation du serveur MCP GitHub pour labonnealternance.
- Mise à jour de la configuration Vercel (`vercel.json`).
- Ajout d'un fichier `.gitignore`.
- Correction de la configuration des variables d'environnement (`env`).

### Autres changements
- Correction de dépendances.
