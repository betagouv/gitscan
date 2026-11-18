## Changelog : euphrosyne-digilab (30 derniers jours, au 17 novembre 2026)

### Résumé
Les récentes évolutions se sont concentrées sur la stabilisation de la plateforme, notamment par la correction de la transmission des données et l'optimisation de la gestion de l'interface utilisateur pour garantir une meilleure fiabilité.

### Évolutions fonctionnelles
- Correction du format des identifiants de session ("run ids") envoyés lors des requêtes de données pour assurer la bonne récupération des informations [#457](https://github.com/betagouv/euphrosyne-digilab/pull/457).

### Évolutions techniques
- Adaptation de la configuration Sentry pour assurer la compatibilité avec la mise à jour de la bibliothèque `@sentry/nextjs`.
- Optimisation de la gestion de l'état React en évitant les mises à jour synchrones dans les effets, afin d'améliorer la stabilité de l'interface.
