## Changelog : mon-service-securise (30 derniers jours, au 20 octobre 2026)

### Résumé
Ce mois-ci, le service a franchi des étapes clés avec l'introduction de la gestion par groupes (services et entités), le lancement d'une API publique documentée et une synchronisation automatisée des données avec le CRM pour améliorer le suivi des activités.

### Évolutions fonctionnelles
- **Gestion par groupes** : possibilité de créer, renommer, supprimer et organiser des services et des entités au sein de groupes pour une meilleure structuration.
- **Gestion des clés d'API** : nouvelle interface permettant aux utilisateurs de créer et de révoquer leurs propres clés d'API.
- **Nouveau rôle de "superviseur"** : introduction de permissions spécifiques permettant aux superviseurs de gérer et de visualiser les services de leur périmètre.
- **Améliorations de l'interface utilisateur** :
    - Navigation optimisée via l'utilisation d'accordéons et d'onglets.
    - Ergonomie améliorée avec des barres d'actions fixes (sticky), des indicateurs de chargement (loaders) et des notifications de succès (toasts).
    - Amélioration de la recherche et de l'affichage des statistiques.

### Évolutions techniques
- **Intégration CRM** : automatisation de la remontée d'informations vers le CRM (nouveaux utilisateurs, nombre de services, nombre d'homologations et imports de services) et création d'outils de rattrapage de données en ligne de commande.
- **API Publique** : déploiement de l'API, mise en place de la documentation OpenAPI, intégration du traçage des appels et sécurisation via Helmet.
- **Optimisations de performance** : parallélisation des requêtes de statistiques et optimisation des lectures en base de données pour réduire la charge.
- **Qualité et CI/CD** :
    - Optimisation des pipelines de tests (exécution en parallèle, mise en cache de Chromium).
    - Réorganisation structurelle du code (middlewares, routes, adaptateurs et mappers) pour une meilleure maintenabilité.
    - Amélioration de la gestion des erreurs et du logging via Sentry.
    - Mise à jour des processus de migration de données (notamment pour les hashs).

### Autres changements
- **Documentation** : mise à jour des Conditions Générales d'Utilisation (CGU) et de la documentation de l'API.
- **Configuration** : mise en place de "feature flags" pour permettre le déploiement progressif des nouvelles fonctionnalités (notamment pour les groupes).
