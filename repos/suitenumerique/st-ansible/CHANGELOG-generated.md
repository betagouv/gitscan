## Changelog : st-ansible (30 derniers jours, au 2026-06-18)

### Résumé
Les dernières mises à jour de st-ansible se concentrent sur l'amélioration de la configuration et de la stabilité des applications de La Suite Territoriale, notamment Collabora, Meet et Keycloak. Des corrections ont été apportées pour permettre une personnalisation accrue et résoudre des problèmes liés à l'utilisateur Docker et aux ports non privilégiés.

### Évolutions fonctionnelles
- **Collabora:** Possibilité de personnaliser la police utilisée.
- **Meet:** Ajout d'une configuration Nginx personnalisée pour une meilleure gestion du trafic.
- **Keycloak:** Correction de la configuration de Compose pour les installations en cluster, améliorant la scalabilité et la fiabilité.
- **Drive:** Ajout de nouvelles routes Nginx upstream pour une meilleure intégration et performance.

### Évolutions techniques
- **Meet:** Correction d'un problème d'utilisateur dans le Dockerfile, assurant un fonctionnement correct du conteneur.
- **Meet:** Correction du problème `unprivileged_port_start` pour le challenge ACME de Caddy, permettant une configuration HTTPS plus simple et sécurisée.
- **Messages:** Correction de la commande Compose pour les workers, améliorant la gestion des processus en arrière-plan.

### Autres changements
- **Meet:** Clarification de la documentation concernant les procédures de rollback.
