## Changelog : lab-anssi-pala (30 derniers jours, au 13 novembre 2026)

### Résumé
Ce mois a été marqué par un saut qualitatif majeur en matière de sécurité et d'automatisation. PALA intègre désormais un système de chiffrement de bout en bout pour protéger les rapports de scan et propose une authentification moderne via Passkeys. L'outil est devenu plus autonome grâce à la planification automatique des audits et une meilleure gestion des infrastructures de déploiement (Docker, Clever Cloud).

### Évolutions fonctionnelles
- **Sécurité et Confidentialité**
  - Implémentation du chiffrement de bout en bout des rapports de scan via le protocole HPKE (AES-256-GCM et X25519), garantissant que les données sensibles ne sont jamais stockées en clair.
  - Introduction de l'authentification par Passkeys (WebAuthn) pour un enrôlement utilisateur sécurisé.
- **Reporting et Notifications**
  - Enrichissement des notifications Mattermost : les messages incluent désormais la durée de l'audit, le nombre de fichiers analysés, ainsi que les informations de version (hashes de commits).
  - Ajout de liens directs vers les rapports de scan dans les notifications.
  - Amélioration de la clarté des rapports : les sections sans constat ne sont plus affichées.
- **Interface utilisateur**
  - Mise en place d'une page d'accueil (landing page) présentant les objectifs et le fonctionnement de l'expérimentation PALA.

### Évolutions techniques
- **Architecture et Données**
  - Passage à une architecture en workspaces (pnpm) pour séparer distinctement le backend, le frontend et les outils.
  - Mise en place de la persistance des données et des utilisateurs via PostgreSQL avec un système de migrations de base de données.
  - Refactorisation vers un pattern "Repository" et réorganisation des adaptateurs d'infrastructure.
- **Automatisation et Scanning**
  - Automatisation des audits via une tâche planifiée (exécution tous les 3 jours).
  - Capacité de réaliser des scans en série sur plusieurs cibles simultanément.
  - Automatisation de la génération de la configuration du proxy LiteLLM pour une gestion optimisée des modèles d'IA.
- **Infrastructure et Déploiement**
  - Dockerisation complète de l'application pour uniformiser les environnements de développement et de production.
  - Optimisation du déploiement sur Clever Cloud (ajout de routes de santé, gestion des variables d'environnement et scripts de build dédiés).
  - Amélioration de la gestion du proxy LiteLLM avec l'introduction d'un système de fichiers sécurisé (Cellar).
- **Qualité logicielle et CI/CD**
  - Intégration de l'analyse de code (ESLint) et du formatage (Prettier) dans le cycle de développement avec des hooks de pré-commit.
  - Mise en place de tests de base de données dans la chaîne de CI.

### Autres changements
- **Documentation**
  - Ajout d'un schéma d'architecture C4 pour une meilleure compréhension du système.
  - Rédaction de nouveaux ADR (Architecture Decision Records) concernant le déploiement et la gestion des erreurs.
  - Mise à jour globale du README et de la documentation interne.
- **Maintenance**
  - Nettoyage et réorganisation des scripts Node.js.
