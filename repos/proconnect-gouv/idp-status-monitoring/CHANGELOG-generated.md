## Changelog : idp-status-monitoring (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse et l'observabilité de l'application. Des points de terminaison de santé Kubernetes ont été ajoutés pour le producteur et le consommateur, permettant une meilleure intégration dans les environnements orchestrés. Des améliorations de la journalisation et du tracing ont également été implémentées pour faciliter le diagnostic des problèmes.

### Évolutions fonctionnelles
- Ajout d'un point de terminaison `/health/idps` pour le consommateur, permettant de vérifier son état de santé et sa capacité à interroger les IDP. [#85](https://github.com/proconnect-gouv/idp-status-monitoring/issues/85)
- Le producteur dispose maintenant d'un point de terminaison de santé Kubernetes standard. [#88](https://github.com/proconnect-gouv/idp-status-monitoring/issues/88)
- Le consommateur adopte également les chemins de points de terminaison de santé Kubernetes standard. [#87](https://github.com/proconnect-gouv/idp-status-monitoring/issues/87)
- Amélioration des messages d'erreur renvoyés par le producteur en cas d'échec de récupération des données. [#76](https://github.com/proconnect-gouv/idp-status-monitoring/issues/76)

### Évolutions techniques
- Refactorisation du consommateur pour découpler le serveur du démarrage d'AMQP via l'introduction d'un `ServerContext`. [#86](https://github.com/proconnect-gouv/idp-status-monitoring/issues/86)
- Ajout de la journalisation avec `consola` et intégration du tracing et de `Hono`. [#80](https://github.com/proconnect-gouv/idp-status-monitoring/issues/80)
- Mise à jour de `amqplib` vers la version 1.0.3. [#83](https://github.com/proconnect-gouv/idp-status-monitoring/issues/83)
- Tentative de permettre au consommateur de se lier au port 80 en tant que non-root, puis annulation de cette modification. [#81](https://github.com/proconnect-gouv/idp-status-monitoring/issues/81)

### Autres changements
- Documentation mise à jour.
- Diverses mises à jour de dépendances (Bun, Hono, Prettier, TypeScript, actions GitHub, etc.).
