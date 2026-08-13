## Changelog : test-helm (30 derniers jours, au 12 août 2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la sécurisation et l'optimisation des processus d'automatisation. Les workflows de déploiement (CI/CD) ont été renforcés pour garantir des mises à jour de charts Helm plus fiables, sécurisées et conformes aux meilleures pratiques.

### Évolutions techniques
- **Sécurité & Authentification**
  - Migration de l'authentification vers GitHub App pour une gestion plus sécurisée des accès.
  - Renforcement de la sécurité des workflows via l'application du principe de moindre privilège et la gestion de la concurrence.
- **Automatisation & CI/CD**
  - Optimisation du workflow `update-chart` : introduction d'un mode de mise à jour automatique ('auto') et verrouillage du mode de livraison.
  - Standardisation des releases de charts en fixant la publication sur le canal OCI.
