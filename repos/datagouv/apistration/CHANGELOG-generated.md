## Changelog : apistration (30 derniers jours, au 6 novembre 2026)

### Résumé
Cette période est marquée par un renforcement majeur de la traçabilité de sécurité, l'introduction de nouveaux mécanismes de monitoring (pings) pour garantir la disponibilité des services, et une optimisation de l'expérience utilisateur, notamment sur mobile et pour la consultation des statistiques publiques.

### Évolutions fonctionnelles
- **Sécurité et traçabilité :** Mise en place d'un système complet d'événements de sécurité permettant de tracer la création, la révocation, le partage ou l'utilisation des jetons, ainsi que les changements de rôles et d'accès [#638](https://github.com/datagouv/apistration/pull/638). Ces événements sont désormais intégrés à SIADE.
- **Gestion des quotas (Rate Limiting) :** Introduction de limites de consommation pour l'API Particulier (60 requêtes/min par jeton et 250 requêtes/min pour les habilitations) [#416](https://github.com/datagouv/apistration/pull/416).
- **Monitoring de disponibilité (Pings) :** Déploiement d'un système de "pings" pour surveiller l'état de santé des fournisseurs et la disponibilité des documents, avec une page de statut dédiée pour les utilisateurs [#585](https://github.com/datagouv/apistration/pull/585).
- **Amélioration de l'interface utilisateur :** 
    - Rendu natif des statistiques publiques (remplaçant l'intégration Metabase).
    - Optimisations de l'affichage sur mobile pour les listes d'habilitations, le catalogue et les fiches d'endpoints.
    - Amélioration de la clarté des messages d'erreur (notamment pour les liens magiques de l'API Particulier).
- **Données et attestations :** Amélioration de la gestion des attestations vérifiables EAJE et affinement de la validation des données pour les services CNAV et DGFIP.

### Évolutions techniques
- **Mises à jour majeures :** Montée de version vers Ruby 4.0.9 [#548](https://github.com/datagouv/apistration/pull/548) et Rails 8.1.4.1 [#642](https://github.com/datagouv/apistration/pull/642).
- **Sécurité et CI/CD :** 
    - Automatisation de l'audit de sécurité quotidien des fichiers de dépendances avec `bundler-audit` [#632](https://github.com/datagouv/apistration/pull/632).
    - Intégration de la construction des SDK Node.js directement dans la CI.
- **Architecture et performance :** 
    - Refactoring de la logique métier vers des composants spécialisés ("organizers" et "fetchers") pour une meilleure maintenabilité.
    - Mise en place de mécanismes de mise en cache pour les statistiques publiques et les données Simplifions.
- **Système de messagerie :** Standardisation des modèles d'emails entre les API Entreprise et Particulier et ajout systématique de versions en texte brut pour améliorer la délivrabilité [#574](https://github.com/datagouv/apistration/pull/574).

### Autres changements
- **Documentation :** Mise à jour de la documentation technique concernant les limites de débit, les conventions des événements de sécurité et les détails sur les numéros de TVA (DGFIP).
- **Nettoyage :** Suppression de modèles d'emails obsolètes et de routes inutilisées.
