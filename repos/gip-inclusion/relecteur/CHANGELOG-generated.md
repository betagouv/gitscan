## Changelog : relecteur (30 derniers jours, au 28 octobre 2026)

### Résumé
Le projet a franchi une étape importante dans l'automatisation et la fiabilité de la revue de code. Les utilisateurs bénéficient désormais d'une meilleure intégration dans les flux de travail (support des dépôts privés, gestion intelligente des nouveaux commits) et de rapports plus clairs, notamment en français. Le système d'évaluation de l'outil a également été considérablement renforcé pour offrir des analyses plus précises et détaillées.

### Évolutions fonctionnelles
- **Support des dépôts privés** : Capacité de réviser des pull requests sur des dépôts privés en utilisant des jetons d'accès sécurisés.
- **Amélioration de l'expérience Pull Request** : Chaque revue est désormais affichée comme un "check" distinct et un résumé par revue est publié pour une meilleure lisibilité.
- **Gestion dynamique des commits** : Lorsqu'un nouveau commit est poussé pendant une revue en cours, l'outil peut reprendre ou relancer la revue sur la nouvelle version.
- **Personnalisation accrue** :
    - Sélection spécifique des fichiers à réviser via le fichier `.relecteur/config.toml`.
    - Possibilité de choisir le modèle d'IA et le "juge" via la configuration du dépôt.
    - Rédaction des conclusions de revue en français (configurable).
- **Système d'évaluation (evals) enrichi** :
    - Génération de rapports incluant le temps moyen et le nombre de tokens consommés.
    - Capacité à créer automatiquement des cas de test à partir de l'historique du dépôt.
    - Scoring des défauts basé sur la probabilité et la confiance du modèle.

### Évolutions techniques
- **Auto-revue via CI/CD** : Mise en place d'un workflow GitHub Actions permettant à l'outil de réviser ses propres Pull Requests pour garantir sa qualité.
- **Résilience et robustesse** :
    - Amélioration de la gestion des limites de taux (rate limits) et des erreurs réseau des fournisseurs d'IA (avec des mécanismes de pause et de reprise).
    - Meilleure gestion des timeouts et des erreurs de service (503).
- **Refactorisation** : Optimisation de la gestion des statuts de l'IA et des classes d'erreurs pour un code plus maintenable.

### Autres changements
- **Refonte de la documentation** : Passage de la documentation en français par défaut, amélioration du guide de démarrage rapide et création de pages dédiées selon le profil de l'utilisateur (développeur, décideur, etc.).
- **Comparatifs** : Ajout de documents comparant l'outil avec des solutions du marché (Claude Code Review, CodeRabbit, Greptile).
- **Maintenance** : Nettoyage des artefacts de build et optimisation des processus de test.
