## Changelog : mon-service-securise (30 derniers jours, au 20 octobre 2026)

### Résumé
Ce mois-ci, le service a franchi une étape majeure avec l'introduction de la gestion par groupes, permettant aux utilisateurs d'organiser leurs services et leurs entités de manière plus structurée. Nous avons également renforcé la visibilité de l'activité via une synchronisation automatique avec nos outils de gestion (CRM) et introduit un nouveau rôle de "superviseur" pour affiner la gestion des accès et des périmètres de sécurité.

### Évolutions fonctionnelles
- **Gestion par groupes** : Introduction de la possibilité de créer, renommer, supprimer et organiser des groupes de services et d'entités pour une meilleure gestion des périmètres.
- **Nouveau rôle de Superviseur** : Mise en place d'un rôle de superviseur permettant une gestion étendue des services et une visibilité accrue dans les tableaux de bord.
- **Améliorations de l'interface utilisateur** :
    - Navigation optimisée grâce à l'utilisation d'onglets et d'accordéons pour les listes de services et d'entités.
    - Amélioration de l'ergonomie avec des barres d'actions fixes (sticky), des indicateurs de chargement (loaders) et des notifications de succès (toasts).
    - Meilleure gestion de la recherche au sein des groupes.
- **Conformité** : Mise à jour des Conditions Générales d'Utilisation (CGU).

### Évolutions techniques
- **Intégration CRM** : Automatisation de la remontée de données vers le CRM (nombre de services, nombre d'homologations, nouveaux utilisateurs et imports de services) et mise en place d'outils de synchronisation des données historiques (rattrapage en mode batch).
- **Optimisation des performances** :
    - Optimisation des requêtes de lecture pour les services et les statistiques.
    - Exécution des requêtes de statistiques en parallèle pour réduire les temps de réponse.
    - Limitation du débit (rate limiting) sur l'API recherche-entreprises pour garantir la stabilité.
- **Observabilité et Sécurité** :
    - Amélioration du suivi des erreurs avec Sentry (extraction de la configuration, ajout d'un "scrubber" pour la protection des données sensibles et intégration de notifications via Mattermost).
    - Renforcement de la protection des autorisations des superviseurs.
- **Architecture** :
    - Refactoring du client HTTP et extraction de composants UI réutilisables.
    - Gestion des nouvelles fonctionnalités via des "feature flags" pour un déploiement sécurisé.

### Autres changements
- **Documentation** : Mise à jour de la documentation de l'API (inclusion de l'URL de base et de la spécification OpenAPI).
- **Maintenance** : Nettoyage du code (suppression de duplications, renommage de composants pour plus de clarté) et mise à jour de l'environnement de build (pnpm).
