## Changelog : api-engagement (30 derniers jours)

### Résumé
Cette période a été marquée par une amélioration significative de l'expérience utilisateur du tableau de bord et du widget, avec des corrections de bugs et des améliorations d'accessibilité. Des optimisations ont également été apportées à l'API, notamment en termes de performances et de gestion des erreurs. Enfin, de nouvelles métriques de conversion ont été ajoutées pour l'analyse.

### Évolutions fonctionnelles
- Ajout d'un bouton "événements en direct" sur les listes de campagnes et de widgets. [#809](https://github.com/betagouv/api-engagement/issues/809)
- Amélioration de l'accessibilité avec l'utilisation d'éléments de bouton sémantiques. [#771](https://github.com/betagouv/api-engagement/issues/771)
- Ajout d'un préfixe d'URL avec l'ID du publisher. [#807](https://github.com/betagouv/api-engagement/issues/807)
- Ajout de métriques de taux de conversion pour l'analyse. [#811](https://github.com/betagouv/api-engagement/issues/811)
- Correction de l'affichage des organisations dans la page "Mes missions".
- Correction du problème de déconnexion pour les utilisateurs de la page "Mes missions". [#799](https://github.com/betagouv/api-engagement/issues/799)
- Amélioration de l'interface utilisateur du sélecteur de date.
- Correction de l'affichage du logo gouvernemental.
- Amélioration de l'interface utilisateur des filtres et de la navigation.
- Correction du pointage du curseur sur les liens de navigation et les filtres.
- Correction du focus sur l'interface utilisateur de feedback.

### Évolutions techniques
- Passage à Node 24. [#802](https://github.com/betagouv/api-engagement/issues/802)
- Ajout d'un middleware dédié pour l'analyse des requêtes. [#800](https://github.com/betagouv/api-engagement/issues/800)
- Ajout d'un en-tête `request-id` avec support Sentry. [#780](https://github.com/betagouv/api-engagement/issues/780)
- Refactor de la logique d'agrégation des widgets. [#790](https://github.com/betagouv/api-engagement/issues/790)
- Optimisation de la recherche de widgets. [#782](https://github.com/betagouv/api-engagement/issues/782)
- Ajout d'un index partiel sur la mission pour les requêtes de comptage de recherche géographique. [#806](https://github.com/betagouv/api-engagement/issues/806)
- Migration des activités de mission vers une table de jointure N-N. [#757](https://github.com/betagouv/api-engagement/issues/757)
- Suppression de MongoDB. [#761](https://github.com/betagouv/api-engagement/issues/761)
- Amélioration de la gestion des erreurs et ajout de logs Sentry.
- Correction d'un problème de mismatch du client Prisma.
- Ajout de tests d'intégration pour les endpoints du widget. [#750](https://github.com/betagouv/api-engagement/issues/750)
- Refactor de la gestion des adresses et ajout d'alias. [#810](https://github.com/betagouv/api-engagement/issues/810)
- Correction d'un bug dans le job de modération automatique. [#813](https://github.com/betagouv/api-engagement/issues/813)
- Ajout de logs pour le widget. [#795](https://github.com/betagouv/api-engagement/issues/795)
- Correction de la gestion des exceptions non gérées et non capturées vers Sentry. [#797](https://github.com/betagouv/api-engagement/issues/797)
- Ajout d'un job pour importer les missions réactivées. [#783](https://github.com/betagouv/api-engagement/issues/783)
- Suppression de l'ancien pipeline. [#706](https://github.com/betagouv/api-engagement/issues/706)

### Autres changements
- Mise à jour des dépendances (Express, @types/express, NextJS, @types/node, @sentry/cli, globals, @sentry/nextjs).
- Correction de problèmes liés à Sentry (spaming de messages, configuration DSN).
- Suppression de la pipeline KPI et des modèles d'analyse associés.
- Mise à jour de la documentation.
- Nettoyage du code.
- Correction de problèmes de zoom dans l'application.
- Suppression de la logique obsolète de `stat_event`.
- Correction de l'affichage des missions refusées en modération. [#758](https://github.com/betagouv/api-engagement/issues/758)
- Correction d'un problème lié à Letudiant. [#784](https://github.com/betagouv/api-engagement/issues/784)
- Ajout de la possibilité de désactiver les images optimisées pour le widget. [#793](https://github.com/betagouv/api-engagement/issues/793)
