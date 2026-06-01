## Changelog : claw-code-go (30 derniers jours, au 30 mai 2026)

### Résumé
Les dernières mises à jour de claw-code-go se concentrent sur l'amélioration de l'intégration avec les modèles d'IA, notamment Claude Opus 4.8, et l'ajout de nouvelles fonctionnalités comme l'automatisation de tâches sur l'ordinateur de l'utilisateur (prise de captures d'écran, clics de souris, saisie de texte). Des améliorations ont également été apportées à la gestion des outils et à la robustesse de l'API.

### Évolutions fonctionnelles
- Ajout du support pour le modèle Claude Opus 4.8 avec la possibilité de configurer l'effort de raisonnement (low, medium, high, xhigh, max).
- Intégration d'un nouveau tool `computer_use` permettant d'automatiser des actions sur l'ordinateur (clics, saisie de texte, captures d'écran) via `xdotool` et `ImageMagick` (sous Linux).
- Possibilité d'installer des skills (plugins) via un marketplace distant.
- Ajout d'un nouveau tool `todo_write` avec une définition de schéma pour assurer la compatibilité avec l'API OpenAI.
- Ajout de la variable d'environnement `ZAI_API_KEY` pour l'authentification auprès de fournisseurs tiers.
- Amélioration de la présentation de la documentation (README) avec une mise en avant des fonctionnalités clés.
- Ajout d'un mode d'authentification ChatGPT-OAuth pour l'API OpenAI.

### Évolutions techniques
- Refactor de la gestion des erreurs dans l'API pour une meilleure gestion des erreurs de transport avec un système de retry exponentiel.
- Amélioration de la gestion du cache du registre d'API avec un rafraîchissement automatique et la fusion du registre par défaut.
- Correction de bugs liés à la gestion des paramètres et des réponses de l'API Anthropic, notamment la préservation des données et la gestion des erreurs SSE.
- Amélioration de la gestion des processus avec la suppression des processus groupés lors d'un timeout pour éviter les blocages.
- Suppression des propriétés vides dans les requêtes OpenAI pour une meilleure compatibilité.
- Correction de problèmes liés à la gestion des tokens et des budgets sur les modèles Anthropic.
- Ajout de la licence MIT au projet.
- Exposition de la capacité de raisonnement par modèle dans l'API.
- Suppression de commentaires inutiles dans le code.

### Autres changements
- Ajout de frontmatter YAML aux skills pour faciliter leur gestion et leur installation.
- Correction de la gestion des espaces dans les préfixes SSE.
- Amélioration de la gestion des erreurs et des logs.
- Mise à jour de la documentation interne.
