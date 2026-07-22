## Changelog : n8n-nodes-async-api (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce changelog présente les premiers développements du paquet de nœuds n8n pour les services IA BRIO (async-api). Les fonctionnalités de base pour la soumission de tâches, le suivi de leur progression et la récupération des résultats sont maintenant implémentées, ainsi que la gestion des fichiers (upload, téléchargement). L'infrastructure de CI/CD a été mise en place pour automatiser les tests et la publication.

### Évolutions fonctionnelles
- Ajout de la possibilité de soumettre des tâches, de les récupérer et d'attendre leur complétion. [#478](https://github.com/IA-Generative/n8n-nodes-async-api/issues/478) et [#479](https://github.com/IA-Generative/n8n-nodes-async-api/issues/479)
- Implémentation des opérations de fichiers : upload, upload via URL présignée et téléchargement. [#480](https://github.com/IA-Generative/n8n-nodes-async-api/issues/480)
- Sélection automatique du mode d'upload en fonction de la taille du fichier. [#480](https://github.com/IA-Generative/n8n-nodes-async-api/issues/480)
- Fallback automatique vers l'upload via URL présignée si la taille du fichier est trop importante. [#480](https://github.com/IA-Generative/n8n-nodes-async-api/issues/480)
- Création du squelette du paquet de nœuds n8n avec un menu déroulant dynamique pour la sélection du service. [#477](https://github.com/IA-Generative/n8n-nodes-async-api/issues/477)

### Évolutions techniques
- Mise en place d'un workflow GitHub Actions pour la construction, le linting et les tests unitaires.
- Renforcement de la sécurité du nœud suite à une revue de code. [#477](https://github.com/IA-Generative/n8n-nodes-async-api/issues/477)
- Configuration de l'authentification pour la publication sur npm via le secret `NPM_TOKEN`.
- Passage à la distribution publique npm pour `playwright-core`.

### Autres changements
- Aucun changement significatif à signaler.
