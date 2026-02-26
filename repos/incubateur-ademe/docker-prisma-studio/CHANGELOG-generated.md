## Changelog : docker-prisma-studio (30 derniers jours)

### Résumé
Cette mise à jour améliore la compatibilité et l'optimisation du conteneur Docker pour Prisma Studio. Elle corrige des problèmes liés à l'utilisation de Prisma 7 et à la configuration de l'URL du schéma, tout en réduisant la taille de l'image Docker pour une meilleure performance. Une nouvelle fonctionnalité permet de configurer l'accès à Prisma Studio via une URL de schéma.

### Évolutions fonctionnelles
- Ajout de la possibilité de configurer l'accès à Prisma Studio via la variable d'environnement `SCHEMA_URL` (#fecc294).
- Correction d'un problème de compatibilité avec Prisma 7 lors de l'utilisation du mode `SCHEMA_URL` (#ac814e0).

### Évolutions techniques
- Optimisation de l'image Docker pour réduire sa taille (#6b4916c).
- Suppression des générateurs Prisma pour éviter des problèmes potentiels (#229eb70).
