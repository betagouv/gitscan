## Changelog : cdtn-admin (30 derniers jours, au 07 octobre 2026)

### Résumé
Ce mois-ci, l'outil d'administration renforce ses capacités d'analyse de données, notamment pour le suivi des contributions et de l'utilisation des simulateurs. Un nouveau simulateur d'indemnités de retraite a été intégré, tandis que des optimisations techniques ont été apportées pour accélérer les déploiements et sécuriser l'accès à la plateforme.

### Évolutions fonctionnelles
- **Analyses et statistiques**
  - Ajout de nouveaux rapports et outils d'analyse de données.
  - Mise en place d'un entonnoir (funnel) pour le suivi du parcours des contributions [#1711](https://github.com/SocialGouv/cdtn-admin/issues/1711).
  - Migration du mode de calcul du taux de complétion des contributions [#1720](https://github.com/SocialGouv/cdtn-admin/issues/1720).
  - Ajout du suivi du taux de personnalisation des simulateurs [#1716](https://github.com/SocialGouv/cdtn-admin/issues/1716).
- **Outils et interface**
  - Intégration d'un nouveau simulateur d'indemnité de départ à la retraite [#1714](https://github.com/SocialGouv/cdtn-admin/issues/1714).
  - Ajout de descriptions pour les thèmes de l'interface afin d'en faciliter le choix [#1712](https://github.com/SocialGouv/cdtn-admin/issues/1712).

### Évolutions techniques
- **Infrastructure et CI/CD**
  - Optimisation de la vitesse des déploiements via la persistance du cache `pnpm` au travers des releases [#1715](https://github.com/SocialGouv/cdtn-admin/issues/1715).
  - Renforcement de la sécurité de l'accès à l'administration par restriction d'adresse IP.
