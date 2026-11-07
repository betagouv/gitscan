## Changelog : lab-anssi-pala (30 derniers jours, au 05/11/2026)

### Résumé
Le projet a franchi une étape majeure en passant d'un ensemble de scripts expérimentaux à une plateforme structurée et industrialisée. Il propose désormais deux outils complémentaires pilotés par IA : **Codex Security** (analyse statique de code) et **Shannon** (tests d'intrusion dynamiques). Une nouvelle interface en ligne de commande (CLI) permet d'automatiser des scans complets sur plusieurs cibles, tout en intégrant une gestion fine des coûts et une persistance des résultats.

### Évolutions fonctionnelles
- **Nouveaux outils d'audit** : Introduction de Codex Security pour l'analyse statique et de Shannon pour la validation dynamique (pentest).
- **Nouvelle interface de commande (CLI)** : Mise à disposition d'une suite de commandes TypeScript pour piloter le cycle de vie du projet (`scan`, `validate`, `bootstrap`, `estimer-cout`, etc.).
- **Automatisation des scans** : Capacité d'enchaîner des scans sur plusieurs cibles de manière séquentielle et programmation de scans périodiques (tous les 3 jours).
- **Maîtrise des coûts LLM** : Intégration d'un système d'estimation des coûts par scan et mise en place de plafonds budgétaires configurables pour l'utilisation des modèles d'IA.
- **Reporting et notifications** : Publication automatique des résultats et des constats de sécurité via Mattermost.
- **Amélioration de l'expérience utilisateur** : Sorties console enrichies (couleurs), aide contextuelle améliorée et gestion de la configuration par fichiers YAML.

### Évolutions techniques
- **Refonte de l'architecture** : Passage à une structure de monorepo utilisant les **pnpm workspaces** (séparation back, front et outillage) et adoption d'une architecture hexagonale plus robuste.
- **Gestion des modèles d'IA** : Implémentation d'un proxy **LiteLLM** pour centraliser l'accès aux différents fournisseurs (Albert, Scaleway/DeepSeek) et normaliser les appels.
- **Persistance des données** : Intégration de **PostgreSQL** pour stocker les rapports de scan et les métadonnées Git (historique des commits analysés).
- **Conteneurisation et déploiement** : Dockerisation complète de l'application et de sa base de données ; mise en place de pipelines CI/CD pour le déploiement sur Clever Cloud.
- **Fiabilisation du code** : Mise en place de tests unitaires (Vitest), de l'analyse statique (ESLint) et de hooks de pré-commit.
- **Gestion de l'environnement** : Centralisation de la configuration via des variables d'environnement et un système de génération de fichiers `.env` sécurisé.

### Autres changements
- **Documentation** : Ajout de schémas d'architecture C4, de documents de décision d'architecture (ADR) et mise à jour complète des guides de déploiement et d'utilisation.
- **Nettoyage** : Suppression des anciens scripts Bash et Python obsolètes au profit de l'outillage TypeScript.
