## Changelog : kevent-ai (30 derniers jours, au 05 juin 2026)

### Résumé
Ce mois-ci, le projet kevent-ai a connu une refonte majeure de son architecture, passant d'une dépendance à Kafka pour la gestion des files d'attente à une solution basée sur Redis. Cette transition simplifie l'infrastructure, améliore la résilience et permet une gestion plus fine des priorités des tâches. Des améliorations ont également été apportées à la surveillance et à la gestion du cycle de vie des tâches.

### Évolutions fonctionnelles
- **Gestion de la priorité des tâches :** Introduction d'une file d'attente prioritaire via Redis (`LPUSH`) pour les requêtes disposant d'un en-tête spécifique (`server.priority_header`). [#82](https://github.com/IA-Generative/kevent-ai/pull/82)
- **Indication de la position dans la file d'attente :** L'API expose désormais la position d'une tâche dans la file d'attente Redis. [#62](https://github.com/IA-Generative/kevent-ai/pull/62)
- **Gestion améliorée des tâches annulées :** Les tâches annulées sont conservées en Redis pour une suppression ultérieure par le garbage collector, améliorant la robustesse.
- **Nouvelles métriques :** Ajout de métriques Prometheus pour suivre les tâches asynchrones soumises, y compris la distinction entre les tâches prioritaires et non prioritaires.
- **Endpoints d'informations et de purge :** Ajout d'endpoints pour obtenir des informations sur le système et pour purger les tâches.
- **Amélioration de la gestion des erreurs :** Propagation correcte des erreurs de contexte lors des appels d'inférence.

### Évolutions techniques
- **Suppression de Kafka :** Suppression complète de la dépendance à Kafka, simplifiant l'architecture et réduisant la complexité opérationnelle.
- **Utilisation de Redis pour la gestion des files d'attente :**  Le gateway utilise désormais Redis pour la gestion des files d'attente de tâches, remplaçant l'ancien système basé sur Kafka.
- **Refonte du relay :** Le relay a été réécrit pour utiliser un modèle de consommation pull basé sur Redis (`BLMOVE`).
- **Amélioration de la résilience du relay :** Ajout de mécanismes de retry, de timeouts configurables et de vérifications de l'état de santé pour le relay.
- **Gestion du cycle de vie des tâches :** Implémentation d'un garbage collector unifié pour les tâches en attente et les objets S3 orphelins.
- **Utilisation de KEDA pour le scaling :** Intégration de KEDA pour le scaling automatique du relay en fonction du lag de la file d'attente Kafka (avant suppression de Kafka).
- **Amélioration des tests :** Ajout de tests unitaires et d'intégration pour la gestion des erreurs, la gestion des taux limites et les fonctionnalités de PII.
- **Refactoring de la configuration :** Simplification et unification de la configuration, notamment pour la gestion du cycle de vie des tâches.
- **Mise à jour des dashboards Grafana :** Adaptation des dashboards Grafana pour refléter les nouvelles métriques et l'architecture sans Kafka.

### Autres changements
- **Documentation mise à jour :** Mise à jour de la documentation pour refléter les changements architecturaux et les nouvelles fonctionnalités.
- **Correction de bugs :** Correction de plusieurs bugs, notamment liés à la gestion des timeouts, à la propagation des erreurs et à la gestion des ressources.
- **Ajout d'une licence :** Ajout d'une licence au projet.
- **Nettoyage du code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Mise à jour des dépendances :** Mise à jour des dépendances du projet.
- **Amélioration du processus de release :** Mise en place d'un processus de release basé sur les pull requests.
