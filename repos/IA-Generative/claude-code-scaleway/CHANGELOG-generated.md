## Changelog : claude-code-scaleway (30 derniers jours, au 16 août 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec l'intégration opérationnelle des modèles GLM-5.2 de Scaleway. Les développements se sont concentrés sur la stabilisation de la passerelle API, la gestion rigoureuse des limites de tokens pour éviter les erreurs de réponse, et une refonte complète de la documentation pour offrir un guide d'utilisation plus clair et structuré.

### Évolutions fonctionnelles
- **Support des modèles Scaleway** : Intégration réussie de la passerelle pour utiliser les modèles GLM-5.2.
- **Amélioration de l'expérience Shell** : Correction de la compatibilité avec Zsh pour garantir que l'environnement proxy est correctement transmis lors de l'exécution.

### Évolutions techniques
- **Stabilité de l'API** : 
    - Résolution des erreurs 422 sur les endpoints `/v1/messages` via un pont forcé entre les modes chat et completions.
    - Correction des erreurs 404 et 400 sur certains modèles grâce à l'implémentation d'alias versionnés.
- **Gestion des limites de tokens** : 
    - Mise en place d'un plafond de sortie à 16 384 tokens au niveau du proxy pour s'aligner sur les contraintes de Scaleway.
    - Centralisation de la configuration des limites de tokens pour éviter les duplications de code.
    - Ajustement des tests de diagnostic (`check.sh`) pour permettre aux modèles de "réfléchir" plus longuement avant de répondre.
- **Infrastructure et Sécurité** :
    - Fixation de l'image Docker sur une version stable de LiteLLM (v1.96.2).
    - Renforcement de la sécurité avec l'ajout de `gitleaks` en pré-commit et un durcissement du `.gitignore`.
- **Outils de diagnostic** : Ajout de la commande `make cache-probe` pour mesurer le support du cache de préfixe par Scaleway.

### Autres changements
- **Refonte de la documentation** : 
    - Mise en forme complète du README (sommaire, tableaux, sections repliables).
    - Ajout de sections techniques cruciales : fonctionnement du cache de tokens, intégration avec Ollama, et gestion des tentatives de reconnexion (retry) en cas de saturation (erreur 429).
    - Clarification importante : l'outil est exclusivement destiné à un usage en ligne de commande (CLI) et n'est pas compatible avec VS Code.
    - Ajout d'une section pour les retours utilisateurs et les contributions.
