## Changelog : idp-status-monitoring (30 derniers jours)

### Résumé
Ce changelog fait état de mises à jour régulières des dépendances du projet, ainsi que de quelques corrections mineures concernant la version de Bun utilisée dans le Dockerfile. L'application continue de fonctionner sans interruption de service et ces changements visent à maintenir la sécurité et la stabilité du projet.

### Évolutions techniques
- Mise à jour de la version de Bun utilisée dans le Dockerfile pour corriger un problème. (#31cba7e)
- Mise à jour de l'écosystème de dépendances vers Bun. (#600ba4a)
- Mises à jour de plusieurs actions utilisées dans les workflows CI/CD (actions/checkout, docker/metadata-action, docker/setup-buildx-action, actions/download-artifact, actions/upload-artifact). (#36, #35, #39, #38, #37)
- Mises à jour de plusieurs dépendances : hono, @hono/zod-validator, zod, prettier, @types/bun, @types/amqplib, @tsconfig/bun. (#55, #42, #45, #46, #44, #51, #49, #50)

### Autres changements
- Mises à jour mineures des dépendances de développement (@types/bun, @tsconfig/bun). (#56, #43)
- Mise à jour de l'action docker/build-push-action. (#54)
- Mise à jour de l'action docker/login-action. (#47)
- Mise à jour de l'action oven/bun. (#53, #48)
- Mise à jour de l'action oven-sh/setup-bun. (#40)
