## Changelog : idp-status-monitoring (30 derniers jours)

### Résumé
Ce changelog résume les récentes mises à jour de l'application de surveillance de l'état des services IDP. Les changements se concentrent principalement sur la mise à jour des dépendances du projet, notamment les librairies TypeScript, les outils de CI/CD et l'environnement d'exécution Bun. Une correction de la version de Bun utilisée dans le Dockerfile a également été apportée.

### Évolutions techniques
- Mise à jour de l'écosystème de gestion des paquets vers Bun (#40).
- Correction de la version de Bun utilisée dans le Dockerfile (#31cba7e).
- Mise à jour de Hono de 4.10.2 à 4.11.8 (#42).
- Mise à jour de Zod de 4.1.12 à 4.3.6 (#46).
- Mise à jour de `@hono/zod-validator` (#45).
- Mise à jour de `@types/bun` (#43, #51).
- Mise à jour de `@tsconfig/bun` (#50).
- Mise à jour de `@types/amqplib` (#49).
- Mise à jour de `oven/bun` (#48).
- Mise à jour de `prettier` de 3.6.2 à 3.8.1 (#44).
- Mise à jour des actions GitHub : `checkout` (#36, #41), `docker/metadata-action` (#35), `docker/setup-buildx-action` (#39), `actions/download-artifact` (#38), `actions/upload-artifact` (#37).

### Autres changements
- Mise à jour des dépendances générales du projet via Dependabot. Ces mises à jour concernent principalement des correctifs et des améliorations de sécurité. (#52)
