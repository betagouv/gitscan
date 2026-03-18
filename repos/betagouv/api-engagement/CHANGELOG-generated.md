## Changelog : api-engagement (30 derniers jours, au 16 mars 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la gestion des missions et des organisations, ainsi que par des corrections de bugs et des optimisations de l'infrastructure. L'ajout de nouvelles fonctionnalités, comme les endpoints CRUD pour les missions, et les améliorations apportées à l'interface de modération, facilitent la gestion et l'analyse de l'engagement. Des efforts ont également été déployés pour améliorer la robustesse et la performance de l'API.

### Évolutions fonctionnelles
- Ajout d'endpoints CRUD pour la gestion des missions via l'API v2. [#847](https://github.com/betagouv/api-engagement/issues/847)
- Amélioration du job `letudiant` avec l'ajout de quotas pour une meilleure gestion des données importées. [#855](https://github.com/betagouv/api-engagement/issues/855)
- Ajout d'un bouton "événements en direct" sur les listes de campagnes et de widgets pour faciliter l'accès aux événements. [#809](https://github.com/betagouv/api-engagement/issues/809)
- Amélioration de la recherche d'organisations avec l'ajout d'un champ `search_text`. [#817](https://github.com/betagouv/api-engagement/issues/817)
- Ajout de métriques de taux de conversion dans les analytics. [#811](https://github.com/betagouv/api-engagement/issues/811)
- Correction du bug empêchant la suppression de l'adresse d'une mission lors de l'importation. [#819](https://github.com/betagouv/api-engagement/issues/819)
- Correction d'un bug empêchant le retour de l'adresse de la mission lors de la modération.
- Amélioration de l'interface de modération avec des corrections de l'affichage et de la navigation.
- Correction d'un problème de déconnexion pour les utilisateurs accédant à la section "mes missions".

### Évolutions techniques
- Mise à jour de l'AWS SDK vers la version 3. [#865](https://github.com/betagouv/api-engagement/issues/865)
- Refactorisation de l'exclusion de diffusion des publishers pour lier à l'organisation publisher. [#848](https://github.com/betagouv/api-engagement/issues/848)
- Mise à jour de la version de Prisma à la version 7. [#812](https://github.com/betagouv/api-engagement/issues/812)
- Ajout d'un index partiel sur la table `mission` pour optimiser les requêtes de comptage de recherche géographique. [#806](https://github.com/betagouv/api-engagement/issues/806)
- Mise à jour de la configuration de scaleway pour l'API.
- Mise à jour de la version de Node.js à la version 24. [#802](https://github.com/betagouv/api-engagement/issues/802)
- Amélioration de la gestion des erreurs non gérées et non capturées avec Sentry. [#797](https://github.com/betagouv/api-engagement/issues/797)
- Ajout d'un proxy WAF pour le widget. [#795](https://github.com/betagouv/api-engagement/issues/795)
- Refactorisation de l'utilisation du service dans les fixtures. [#858](https://github.com/betagouv/api-engagement/issues/858)
- Ajout de tests non-régression pour la fonctionnalité de modération. [#818](https://github.com/betagouv/api-engagement/issues/818)
- Ajout de tests pour valider l'utilisation du dashboard avec un rôle utilisateur. [#857](https://github.com/betagouv/api-engagement/issues/857)

### Autres changements
- Correction de la gestion des adresses inconnues lors de l'importation des jobs. [#872](https://github.com/betagouv/api-engagement/issues/872)
- Amélioration du workflow de release avec un lien vers le tag. [#860](https://github.com/betagouv/api-engagement/issues/860)
- Nettoyage et mise à jour du fichier `CHANGELOG.md`.
- Ajout d'un environnement sandbox pour les tests et le développement. [#850](https://github.com/betagouv/api-engagement/issues/850)
- Correction de plusieurs problèmes d'environnement dans les workflows CI.
- Suppression du workflow de synchronisation sandbox.
- Ajout de vérifications de l'organisation publisher.
- Amélioration de la documentation du `publisher_organization`. [#840](https://github.com/betagouv/api-engagement/issues/840)
- Correction de problèmes d'accessibilité dans l'application (éléments manquants, focus, etc.).
- Mise à jour des dépendances et des actions CI.
- Correction de problèmes liés à l'affichage et au comportement de l'interface utilisateur de l'application.
