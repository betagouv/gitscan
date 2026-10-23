## Changelog : grist-docker-image (30 derniers jours, au 21 octobre 2026)

### Résumé
Les récentes mises à jour se sont concentrées sur l'amélioration de l'identité visuelle de l'interface et sur la stabilisation de l'image Docker, notamment par l'optimisation de l'environnement de construction et la gestion rigoureuse des versions de l'application.

### Évolutions fonctionnelles
- Intégration de la police de caractères Marianne [#81](https://github.com/gristgouv/grist-docker-image/pull/81).
- Intégration de nouveaux éléments via la pull request [#84](https://github.com/gristgouv/grist-docker-image/pull/84).

### Évolutions techniques
- **Optimisation de l'image** : Mise à jour de la base Alpine pour utiliser la dernière version du builder Node.js.
- **Gestion des versions** : Mise à jour de l'application Grist via la PR [#83](https://github.com/gristgouv/grist-docker-image/pull/83), suivie d'un retour à la version précédente (revert de la v1.7.21) pour garantir la stabilité de l'image.
