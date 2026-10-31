## Changelog : lab-anssi-pala (30 derniers jours, au 30 octobre 2026)

### Résumé
Le projet a franchi une étape majeure en passant d'un prototype à un outil industrialisable. Les évolutions récentes permettent désormais d'automatiser les audits de sécurité de manière régulière, de gérer plusieurs cibles successivement et de conserver un historique des rapports dans une base de données. L'expérience utilisateur est enrichie par des notifications automatiques et une meilleure visibilité sur les coûts de consommation des modèles d'IA.

### Évolutions fonctionnelles
- **Automatisation des scans** : Mise en place de tâches planifiées pour exécuter des scans complets automatiquement (tous les 3 jours).
- **Gestion multi-cibles** : Possibilité d'enchaîner des scans sur plusieurs projets ou domaines de manière séquentielle.
- **Périmètre intelligent** : Le périmètre de scan est désormais délimité par les modifications Git (diff) sur une fenêtre de temps paramétrable (via l'option `--jours`).
- **Reporting et notifications** : 
    - Publication automatique des résultats et des constats de sécurité sur Mattermost.
    - Persistance des rapports de scan dans une base de données pour consultation ultérieure.
- **Suivi des coûts** : Affichage d'une estimation du coût du scan (basée sur les tokens consommés) à la fin de chaque exécution.
- **Interface de présentation** : Ajout d'une page d'accueil (landing page) pour présenter les capacités de PALA.

### Évolutions techniques
- **Persistance des données** : Implémentation de PostgreSQL pour le stockage des scans et des rapports, incluant la gestion des migrations de base de données.
- **Nouvelle architecture monorepo** : Migration vers une structure de travail avec `pnpm workspaces`, séparant distinctement le backend, le frontend et l'outillage.
- **Conteneurisation** : Dockerisation complète de l'application et de sa base de données pour faciliter le développement local et le déploiement.
- **Portage TypeScript** : Migration de l'outillage vers Node.js/TypeScript pour une exécution native et une meilleure robustesse.
- **Optimisation du Proxy LLM** : Refonte de la gestion du proxy LiteLLM, incluant la possibilité d'utiliser un proxy distant et l'ajout de plafonds de budget configurables.
- **Amélioration de la CI/CD** : Intégration de tests automatisés (Vitest), de vérifications de qualité de code (ESLint) et de processus de déploiement vers Clever Cloud.

### Autres changements
- **Documentation** : Mise à jour approfondie du README et ajout de documents d'architecture (ADR) pour documenter les choix techniques.
- **Expérience CLI** : Amélioration de l'interface en ligne de commande avec des sorties colorées et une aide plus explicite.
- **Nettoyage** : Suppression des scripts obsolètes et réorganisation des dossiers pour une meilleure maintenabilité.
