## Changelog : st-ansible (30 derniers jours, au 14 octobre 2026)

### Résumé
Cette période est marquée par l'intégration de nouveaux services clés comme les **Conversations** et les outils de **Transfert/Scan de fichiers**, ainsi que par un renforcement significatif de la sécurité (antivirus et filtrage d'accès). L'outil de gestion en ligne de commande (CLI) a également été rendu plus robuste pour faciliter les mises à jour et les redémarrages d'environnement.

### Évolutions fonctionnelles
- **Nouveaux services** :
    - Ajout du module **Conversations** (incluant le bootstrapping et la documentation dédiée).
    - Ajout des applications **Transfers** et **File-scanner**, avec intégration native de l'antivirus pour le scan des fichiers.
- **Messagerie** : Introduction du composant `pymta` pour la gestion des messages (remplace progressivement `mta-in`).
- **Amélioration du CLI** : 
    - Ajout de la commande `rebootstrap` pour faciliter la réinitialisation des environnements.
    - Optimisation du processus de mise à jour pour une meilleure fiabilité.

### Évolutions techniques
- **Sécurité et filtrage** :
    - Renforcement de la protection de la messagerie via l'intégration de l'antivirus Exav et du classificateur Bayes (apprentissage automatique) pour Rspamd.
    - Mise en place d'une liste blanche d'adresses IP (allowlist) pour l'administration Django sur les services Docs, Drive et Meet via Caddy.
- **Infrastructure et Conteneurs** :
    - Migration de l'accès au service Drive vers Caddy.
    - Mise en place de Caddy en amont de l'image `messages-keycloak`.
    - Optimisation de l'usage de Podman : installation de `podman-compose 1.6.0` et amélioration des tests de santé (*healthchecks*) des workers.
- **CLI et automatisation** :
    - Amélioration de la gestion des groupes d'hôtes hérités (*legacy*) et réparation automatique du proxy SOCKS lors des montées de version.
    - Découplage des tests de réparation du proxy SOCKS des drapeaux de mise à jour.

### Autres changements
- **Qualité du code** : Nettoyage global du code (suppression du code mort et des doublons) et application des règles de linting Ruff.
