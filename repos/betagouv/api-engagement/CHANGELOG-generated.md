## Changelog : api-engagement (30 derniers jours, au 12 mai 2026)

### Résumé
Ce mois-ci, l'API Engagement a bénéficié d'améliorations significatives en matière de sécurité, notamment avec l'ajout de journaux d'audit et de limitations de débit pour protéger contre les abus. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité de l'API, ainsi que des optimisations de performance. L'interface utilisateur du back-office a été améliorée avec l'ajout d'une gestion des clés API pour les annonceurs.

### Évolutions fonctionnelles
- Ajout de journaux d'audit pour une meilleure traçabilité des actions sur l'API. [#1019](https://github.com/betagouv/api-engagement/issues/1019)
- Ajout d'un onglet de gestion des clés API pour les annonceurs dans le back-office. [#1015](https://github.com/betagouv/api-engagement/issues/1015)
- Amélioration de l'affichage de l'URL sandbox de l'API dans l'interface du back-office. [#1012](https://github.com/betagouv/api-engagement/issues/1012)
- Activation des missions de service civique dans le job Grimpio. [#977](https://github.com/betagouv/api-engagement/issues/977)
- Correction de l'affichage des filtres de modération et du débordement d'onglets dans le back-office. [#975](https://github.com/betagouv/api-engagement/issues/975)
- Correction de la déconnexion pour l'utilisateur "my-missions" dans le back-office. [#799](https://github.com/betagouv/api-engagement/issues/799)

### Évolutions techniques
- Refactorisation de la validation des adresses IP pour Brevo afin d'améliorer la sécurité. [#1026](https://github.com/betagouv/api-engagement/issues/1026)
- Suppression de la validation des adresses IP Brevo. [#1027](https://github.com/betagouv/api-engagement/issues/1027)
- Refactorisation de la gestion des règles d'accès à l'API avec ajout de tests. [#1013](https://github.com/betagouv/api-engagement/issues/1013)
- Refactorisation du middleware de contrôle d'accès. [#1017](https://github.com/betagouv/api-engagement/issues/1017)
- Ajout de limitations de débit (rate limiting) pour protéger l'API contre les abus. [#932](https://github.com/betagouv/api-engagement/issues/932)
- Optimisation de la recherche d'organisations en utilisant `tsvector` dans PostgreSQL. [#950](https://github.com/betagouv/api-engagement/issues/950)
- Mise en place de jobs de sauvegarde de la base de données RDB. [#955](https://github.com/betagouv/api-engagement/issues/955)
- Amélioration de la gestion des échelles (scaling) de l'API. [#949](https://github.com/betagouv/api-engagement/issues/949)
- Correction d'un problème de build des jobs. [#1018](https://github.com/betagouv/api-engagement/issues/1018)
- Déploiement de la spécification OpenAPI sur le CI. [#1014](https://github.com/betagouv/api-engagement/issues/1014)
- Mise en place d'une configuration Mockoon pour les tests. [#978](https://github.com/betagouv/api-engagement/issues/978)
- Exécution séquentielle des agrégations du widget pour éviter les problèmes de concurrence. [#966](https://github.com/betagouv/api-engagement/issues/966)
- Refactorisation de la gestion des missions avec exclusion de l'organisation publiant. [#965](https://github.com/betagouv/api-engagement/issues/965)
- Suppression de la relation `activity_id` dans les missions. [#787](https://github.com/betagouv/api-engagement/issues/787)

### Autres changements
- Mise à jour de la version de Git Cliff pour la génération du changelog. [#1001](https://github.com/betagouv/api-engagement/issues/1001)
- Mise à jour de l'action Scaleway. [#1000](https://github.com/betagouv/api-engagement/issues/1000) et [#967](https://github.com/betagouv/api-engagement/issues/967)
- Mise à jour de l'action de checkout. [#1022](https://github.com/betagouv/api-engagement/issues/1022)
- Correction de la version de dbt pour les dépendances analytics. [#1023](https://github.com/betagouv/api-engagement/issues/1023)
- Ajout d'une limite de tokens pour le script de génération du changelog. [#1001](https://github.com/betagouv/api-engagement/issues/1001)
- Publication des versions v1.5.1 et v1.5.0.
- Diverses mises à jour de dépendances (React Tooltip, TypeScript, UUID, etc.).
