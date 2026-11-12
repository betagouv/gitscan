## Changelog : lab-anssi-pala (30 derniers jours, au 11 novembre 2026)

### Résumé
Le projet PALA a franchi une étape majeure en passant d'un prototype à un outil d'audit plus structuré et sécurisé. Les évolutions récentes se concentrent sur la protection des données via le chiffrement de bout en bout, l'amélioration de l'expérience utilisateur grâce à une nouvelle interface de commande (CLI) plus complète, et l'automatisation des processus d'audit (Codex et Shannon), incluant désormais le suivi des coûts et des notifications automatiques.

### Évolutions fonctionnelles
- **Sécurisation des données** : Implémentation du chiffrement de bout en bout (protocoles HPKE et AES-GCM) et de l'enrôlement des utilisateurs pour protéger les identités cryptographiques.
- **Authentification** : Ajout du support WebAuthn pour les étapes d'enregistrement et d'authentification.
- **Automatisation des audits** : Nouvelle interface en ligne de commande (CLI) permettant de lancer des scans, de valider des résultats et d'estimer les coûts de consommation LLM.
- **Reporting et suivi** : Envoi de notifications automatiques sur Mattermost après chaque scan, incluant des métriques détaillées (durée, nombre de fichiers analysés, hash de commit).
- **Gestion multi-cibles** : Capacité d'exécuter des scans complets de manière séquentielle sur plusieurs projets ou dépôts.

### Évolutions techniques
- **Refonte de l'architecture** : Transition vers une architecture hexagonale organisée en *workspaces* pnpm (back, front, outillage) et introduction d'un bus d'événements interne.
- **Modernisation du socle** : Portage massif de l'outillage vers TypeScript (Node 24) pour une meilleure robustesse et une exécution native.
- **Infrastructure et Déploiement** : Dockerisation complète de l'application et de sa base de données PostgreSQL ; support du déploiement sur Clever Cloud.
- **Optimisation du Proxy LLM** : Amélioration du proxy LiteLLM avec génération automatique de configuration, support de l'hébergement distant et mise en place de plafonds budgétaires.
- **Persistance des données** : Mise en place de PostgreSQL pour le stockage des rapports de scan et gestion des migrations de base de données.
- **Amélioration de la CI** : Intégration de tests automatisés (Vitest) et de vérifications de qualité de code (Linting) dans le pipeline de déploiement.

### Autres changements
- **Documentation** : Ajout de schémas d'architecture C4, de fiches de décision technique (ADR) et mise à jour des guides de déploiement et d'utilisation.
- **Qualité et maintenance** : Harmonisation des commandes de la CLI en français, application systématique du formatage Prettier/ESLint et nettoyage des scripts obsolètes.
