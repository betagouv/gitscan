## Changelog : idp-status-monitoring (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la réactivité du producteur, l'ajout de points de terminaison de santé Kubernetes pour le consommateur et le producteur, et une refonte du consommateur pour une meilleure découplage et maintenabilité. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Le producteur diffuse désormais les résultats de `/idp/internet` dès qu'ils sont disponibles, améliorant ainsi la réactivité du monitoring. [#99](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/99)
- Ajout de points de terminaison `/health/idps` pour le consommateur, permettant une meilleure intégration avec les outils de monitoring Kubernetes. [#85](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/85)
- Ajout de points de terminaison de santé Kubernetes standards pour le producteur. [#88](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/88)

### Évolutions techniques
- Refactorisation du consommateur pour introduire un `ServletContext` afin de découpler le serveur du démarrage AMQP, améliorant ainsi la modularité et la testabilité. [#86](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/86)
- Mise à jour de plusieurs dépendances, incluant `uuid`, `oven/bun`, `hono`, `@types/bun`, `prettier`, `typescript`, `docker/build-push-action`, `docker/login-action`, `amqplib` et `actions/upload-artifact` pour bénéficier des dernières corrections et améliorations.
- Mises à jour des dépendances de développement (`@types/bun`, `prettier`, `typescript`).

### Autres changements
- Aucune information supplémentaire.
