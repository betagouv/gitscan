## Changelog : lab-anssi-pala (30 derniers jours, au 28 octobre 2026)

### Résumé
Le projet a franchi une étape majeure en passant d'une suite de scripts disparates à une interface de ligne de commande (CLI) robuste et structurée en TypeScript. Cette évolution permet une automatisation accrue des audits de sécurité, une meilleure maîtrise des coûts liés aux modèles d'IA et un reporting plus détaillé via Mattermost.

### Évolutions fonctionnelles
- **Automatisation des audits** : Mise en place d'une tâche planifiée pour effectuer un scan complet tous les 3 jours.
- **Reporting enrichi** : Les notifications Mattermost incluent désormais des métriques clés (durée d'exécution, nombre de fichiers analysés, fenêtre de jours et informations sur les derniers commits).
- **Scans ciblés et intelligents** : 
    - Possibilité de limiter le périmètre d'analyse aux seuls fichiers modifiés via un historique Git paramétrable (option `--jours`).
    - Support du scan multi-cibles pour traiter plusieurs projets successivement.
- **Maîtrise des coûts** : Intégration d'une estimation du coût des analyses (basée sur les tokens consommés) affichée en fin de scan.
- **Nouvelles commandes CLI** : Introduction de commandes structurées pour le bootstrap, l'estimation des coûts, le scan, la validation et la gestion du proxy.

### Évolutions techniques
- **Migration TypeScript** : Refonte massive de l'outillage vers TypeScript (Node 24) pour améliorer la fiabilité et la maintenabilité.
- **Gestion des environnements** : Centralisation de la configuration dans un fichier `.env` unique, servant de source de vérité et supprimant la dépendance aux fichiers d'environnement spécifiques par outil.
- **Architecture et communication** : 
    - Implémentation d'un bus d'événements interne pour la gestion des fins de scan.
    - Adoption de principes d'architecture hexagonale pour découpler les adaptateurs (Git, Docker, API).
- **Optimisation du Proxy LLM** : Amélioration de la gestion du proxy LiteLLM, supportant désormais des déploiements locaux ou distants (PaaS) et l'intégration de modèles comme DeepSeek (via Scaleway).
- **Infrastructure et CI/CD** : 
    - Initialisation de la CI/CD.
    - Mise en place de scripts de build et de déploiement Docker pour Clever Cloud.
- **Refactoring de la CLI** : Harmonisation des commandes (renommage en français pour plus de cohérence) et amélioration de l'expérience utilisateur (sorties console colorées, aide détaillée).

### Autres changements
- **Documentation** : Mise à jour complète du README, ajout de documents de décision d'architecture (ADR) et documentation de l'outillage TypeScript.
- **Nettoyage** : Suppression des scripts Bash et des variables d'environnement obsolètes, et réorganisation de la structure des répertoires (`outillage/`, `passerelles/`, etc.).
