## Changelog : matomo-next (30 derniers jours)

### Résumé
Les dernières mises à jour de matomo-next apportent des améliorations significatives, notamment un proxy côté serveur pour contourner les bloqueurs de publicités, une prise en charge des tests A/B via des hooks React, et une migration vers pnpm pour une meilleure gestion des dépendances. Plusieurs corrections de bugs et améliorations de typage ont également été intégrées.

### Évolutions fonctionnelles
- Ajout d'un proxy de suivi côté serveur pour contourner les bloqueurs de publicités, améliorant ainsi la précision des données analytiques. ([#157](https://github.com/SocialGouv/matomo-next/issues/157))
- Implémentation de la prise en charge des tests A/B avec des hooks React, permettant aux développeurs de facilement intégrer des expériences A/B dans leurs applications. ([#155](https://github.com/SocialGouv/matomo-next/issues/155))
- Correction d'un problème de typage dans la fonction `trackEvent` pour accepter correctement les paramètres de type chaîne de caractères et ajout de typages supplémentaires. ([#148](https://github.com/SocialGouv/matomo-next/issues/148))

### Évolutions techniques
- Migration de Yarn vers pnpm 10 et mise à jour de toutes les dépendances pour améliorer la performance et la sécurité du projet. ([#154](https://github.com/SocialGouv/matomo-next/issues/154))
- Ajout de Prettier comme formateur de code dans la CI pour assurer une cohérence du style de code. ([#158](https://github.com/SocialGouv/matomo-next/issues/158))
- Ajout d'un trigger `workflow_dispatch` au workflow CI pour permettre le lancement manuel des builds. ([#147](https://github.com/SocialGouv/matomo-next/issues/147))
- Amélioration des options de configuration pour Heatmap et Session Recording. ([#146](https://github.com/SocialGouv/matomo-next/issues/146))
- Prise en charge du nouveau dossier `app` de Next.js. ([#143](https://github.com/SocialGouv/matomo-next/issues/143))
