## Changelog : lab-anssi-pala (30 derniers jours, au 21 octobre 2026)

### Résumé
Le projet a franchi une étape majeure en passant d'une collection de scripts disparates à une suite d'outils d'audit industrialisée et robuste. La transition vers une interface de ligne de commande (CLI) basée sur TypeScript permet désormais de piloter des scans complexes sur plusieurs cibles de manière séquentielle, avec un contrôle précis du périmètre (via l'historique Git) et une gestion rigoureuse des coûts liés aux modèles d'IA.

### Évolutions fonctionnelles
- **Industrialisation des scans** : Possibilité d'enchaîner l'analyse de plusieurs cibles lors d'une seule exécution.
- **Contrôle du périmètre** : Définition dynamique de la zone d'analyse basée sur les fichiers modifiés dans une fenêtre de temps ajustable (option `--jours`).
- **Maîtrise des coûts** : 
    - Estimation du coût des scans (Codex et Shannon) en fin d'exécution.
    - Mise en place de plafonds de budget configurables pour le proxy LiteLLM.
- **Nouvelle interface CLI** : Introduction de commandes structurées (`pnpm scan`, `pnpm validate`, `pnpm shannon`, `pnpm bootstrap`, `pnpm estimer-cout`, etc.).
- **Reporting amélioré** : 
    - Envoi automatique des résultats et des constats de sécurité vers Mattermost.
    - Sorties console colorées pour une meilleure lisibilité des étapes de scan et de validation.
- **Outils de diagnostic** : Ajout de la commande `check-tool-calls` pour vérifier la compatibilité des modèles avec l'appel d'outils.

### Évolutions techniques
- **Migration technologique** : Refonte majeure du socle de l'outillage vers TypeScript (Node 24) pour remplacer progressivement les scripts Bash et Python.
- **Architecture événementielle** : Implémentation d'un bus d'événements interne pour la communication entre les composants (ex: événement `SCAN_TERMINÉ`).
- **Gestion des configurations** : Automatisation de la génération de fichiers de configuration YAML spécifiques à chaque cible.
- **Optimisation du Proxy LLM** : 
    - Amélioration de la gestion du proxy LiteLLM (support des déploiements distants/PaaS via `LITELLM_BASE_URL`).
    - Découplage de la gestion des variables d'environnement pour une meilleure sécurité et flexibilité.
- **CI/CD et Déploiement** : 
    - Mise en place de la chaîne de CI.
    - Ajout du support Docker et d'une étape de déploiement vers un environnement de démonstration (Clever Cloud).
- **Refactoring structurel** : Réorganisation complète de l'arborescence (regroupement des outils dans `outillage/`, création de `passerelles/` pour l'échange de données comme le format SARIF).

### Autres changements
- **Documentation** : Mise à jour massive du README, ajout de documents de décision d'architecture (ADR) et documentation de la nouvelle approche TypeScript.
- **Nettoyage** : Suppression des scripts Bash obsolètes, des fichiers d'environnement inutilisés et harmonisation des noms de variables (standardisation vers `FOURNISSEUR_*`).
