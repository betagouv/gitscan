## Changelog : api-relay-cnav (30 derniers jours, au 06/08/2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes clés dans la mise en place de ses fonctionnalités fondamentales, notamment l'authentification et les capacités d'intégration. Parallèlement, l'environnement de développement et les processus de déploiement automatique ont été stabilisés et optimisés.

### Évolutions fonctionnelles
- Mise en place de l'authentification par jeton (token authentication) pour sécuriser les accès.
- Ajout d'un client InterOps pour faciliter les échanges avec les services tiers.

### Évolutions techniques
- **API & Développement :**
  - Intégration des bibliothèques Django REST Framework (DRF) pour la gestion de l'API.
  - Ajout d'un "API stub" pour faciliter les tests et les simulations d'appels.
- **CI/CD & Automatisation :**
  - Optimisation de la gestion du cache pour l'action `setup-uv`.
  - Ajout de la commande `grant_app_privileges` dans les processus d'intégration continue.
- **Infrastructure :**
  - Alignement de la version de PostgreSQL sur la version 17 dans les environnements Docker et CI.
