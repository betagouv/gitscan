## Changelog : idp-status-monitoring (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la réactivité du producteur, l'ajout de points de terminaison de santé Kubernetes pour le consommateur et le producteur, et une refonte du consommateur pour une meilleure découplage et une gestion plus robuste de la connexion RabbitMQ. Des améliorations de logging et de traçabilité ont également été apportées.

### Évolutions fonctionnelles
- Le producteur diffuse désormais les résultats `/idp/internet` au fur et à mesure qu'ils sont disponibles, améliorant ainsi la réactivité. [#99](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/99)
- Ajout d'un point de terminaison `/health/idps` au consommateur pour faciliter la surveillance de son état de santé. [#85](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/85)
- Ajout de points de terminaison de santé Kubernetes standard au producteur et au consommateur pour une meilleure intégration avec les orchestrateurs de conteneurs. [#88](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/88) [#87](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/87)

### Évolutions techniques
- Refonte du consommateur pour découpler le serveur du démarrage d'AMQP via l'introduction de `ServerContext`. [#86](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/86)
- Mise à jour de la bibliothèque `amqplib` vers la version 1.0.3. [#83](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/83)
- Amélioration du logging avec l'intégration de `consola` et l'utilisation de la variable d'environnement `LOG_LEVEL`. Ajout du traçage. [#80](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/80)

### Autres changements
- Rétrogradation d'une modification précédente autorisant la liaison au port 80 en tant que non-root. [#81](https://github.com/proconnect-gouv/idp-status-monitoring/pulls/81)
- Mises à jour mineures des dépendances (Hono, TypeScript, Prettier, Bun, actions GitHub, etc.). Ces mises à jour sont gérées par Dependabot et ne nécessitent pas d'attention particulière.
