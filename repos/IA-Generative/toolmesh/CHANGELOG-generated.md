## Changelog : toolmesh (30 derniers jours, au 13 octobre 2026)

### Résumé
Le projet a franchi une étape majeure avec l'intégration de la sécurité et de l'automatisation. Les capacités de gestion de l'identité sont désormais opérationnelles, et la structure technique de base (backend et déploiement) est en place pour permettre des développements futurs rapides et sécurisés.

### Évolutions fonctionnelles
- **Sécurité et accès** : Mise en place de l'authentification via Keycloak, incluant la gestion de l'échange de jetons pour sécuriser les communications entre les différents services.
- **Nouveaux outils** : Ajout d'un serveur MCP dédié à la gestion des dates et des heures (`datetime`).

### Évolutions techniques
- **Architecture Backend** : Initialisation de la structure du serveur backend basée sur FastAPI.
- **Automatisation (CI/CD)** : Implémentation des pipelines de déploiement continu pour automatiser les cycles de mise à jour.
- **Fiabilité des conteneurs** : Amélioration de la robustesse du service `mcp-datetime` par l'ajout d'un mécanisme de contrôle de santé (`HEALTHCHECK`) dans son Dockerfile.
