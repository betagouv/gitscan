## Changelog : claw-code-go (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois-ci, le projet a considérablement élargi son support pour les nouveaux modèles d'IA, incluant la compatibilité avec les futurs standards comme GPT-6 et Opus 5.5. L'écosystème de fournisseurs s'est enrichi avec l'arrivée native de Moonshot et z.ai. Parallèlement, la fiabilité de l'exécution des commandes (Bash) a été renforcée par une meilleure gestion des délais et de la mémoire, tandis que les workflows d'agents sont devenus plus robustes grâce à une validation accrue des résultats structurés.

### Évolutions fonctionnelles
- **Nouveaux modèles et fournisseurs** : 
    - Support étendu des modèles via les transports Opus 5.5 et GPT-6 [#10](https://github.com/SocialGouv/claw-code-go/pull/10).
    - Intégration native des fournisseurs Moonshot (Kimi) et z.ai (GLM) via des protocoles compatibles Anthropic.
- **Amélioration des commandes** : 
    - Possibilité de résoudre des commandes situées dans un répertoire de workspace spécifique (`.claude/commands/`).
    - Autorisation de l'utilisation de points (`.`) dans les noms de commandes.
- **Gestion des outils et workflows** : 
    - Introduction de délais d'exécution (timeouts) pour les commandes Bash afin de sécuriser les sessions d'agents.
    - Amélioration des workflows : les agents peuvent désormais résoudre des tâches en utilisant les résultats structurés et validés de sous-agents.
- **Génération d'images** : Correction de la génération d'images via l'authentification Codex pour OpenAI.
- **Visibilité API** : Affichage du nombre de tokens de prompt pour les endpoints OpenAI.

### Évolutions techniques
- **CI/CD** : Automatisation complète des builds, des tests, de la détection de "race conditions" et du linting sur chaque Pull Request [#8](https://github.com/SocialGouv/claw-code-go/pull/8).
- **Optimisation de l'exécution Bash** : 
    - Amélioration de la capture de la sortie des commandes pour éviter les saturations de mémoire [#5](https://github.com/SocialGouv/claw-code-go/pull/5) [#7](https://github.com/SocialGouv/claw-code-go/pull/7).
    - Meilleure gestion des limites (bounds) lors de la lecture et de la séparation des arguments.
- **Architecture API et Modèles** : 
    - Mise à jour du registre de modèles pour inclure la famille Claude 5.
    - Amélioration de la gestion des schémas JSON (support des types sous forme de tableaux).
    - Optimisation de la gestion des entrées de modèles en temps réel pour éviter les mutations en place.

### Autres changements
- **Documentation** : Correction de la documentation publique (godoc) concernant les règles de nommage des commandes.
