## Changelog : cartographie (30 derniers jours, au 7 mai 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives en termes de performance, notamment au niveau du chargement des données et de la gestion du cache. Des corrections de bugs ont été implémentées pour améliorer la stabilité et l'expérience utilisateur, et de nouvelles fonctionnalités ont été ajoutées, comme des filtres de disponibilité et un bouton pour intégrer la carte. L'infrastructure a également été renforcée avec l'ajout de mesures de sécurité et d'optimisations.

### Évolutions fonctionnelles
- Ajout de filtres pour afficher les lieux "ouverts maintenant" et "ouverts le week-end" ([5e43199](https://github.com/anct-cartographie-nationale/cartographie/commit/5e43199f3e4939fa0e925077adbd1f2d51f51b79)).
- Ajout d'un bouton pour intégrer la carte sur d'autres sites web, avec suivi via Matomo ([c339f1b](https://github.com/anct-cartographie-nationale/cartographie/commit/c339f1ba7d95b1dcdc9f55946125a8770c348270)).
- Amélioration de l'affichage du label "Site internet" sur la page de détail d'un lieu ([2ae2aff](https://github.com/anct-cartographie-nationale/cartographie/commit/2ae2affe016c37e76fbfc7311987b6f7728e5599)).
- Correction du comportement de la navigation arrière depuis la page de détail d'un lieu, qui utilise maintenant l'historique du navigateur ([91009c8](https://github.com/anct-cartographie-nationale/cartographie/commit/91009c871f278b3256b726334eabf8b895a67d86)).

### Évolutions techniques
- Optimisation des performances en utilisant un chargement paresseux (lazy loading) pour l'analyse des horaires d'ouverture ([4f7f332](https://github.com/anct-cartographie-nationale/cartographie/commit/4f7f332b940c39b0a8479776ddabf64f2d446961)).
- Mise à jour de pnpm en version 11 et configuration de Node.js avant l'exécution de pnpm ([2672b3e](https://github.com/anct-cartographie-nationale/cartographie/commit/2672b3e58476936068613415697340924132431d), [1cc1998](https://github.com/anct-cartographie-nationale/cartographie/commit/1cc199862a4427f63d451f132426359833d9826d)).
- Amélioration de la gestion du cache avec l'utilisation de cache tags et de revalidation à la demande (on-demand revalidation) ([c50fbbc](https://github.com/anct-cartographie-nationale/cartographie/commit/c50fbbc6f533191686211961178449815993399f)).
- Refonte de l'infrastructure avec l'ajout d'un reverse proxy Nginx pour la mise en cache, la limitation du débit, la protection contre les bots et l'amélioration de la sécurité ([a84e9ad](https://github.com/anct-cartographie-nationale/cartographie/commit/a84e9ad8449475f987752914283d23129169649c) et commits suivants).
- Utilisation de streaming pour les exports CSV afin de réduire la consommation de mémoire ([51ade24](https://github.com/anct-cartographie-nationale/cartographie/commit/51ade249726617f623708973241936f4643431f0)).
- Migration vers un BFF (Backend For Frontend) en mémoire pour les appels à l'API PostgREST ([3d5ffab](https://github.com/anct-cartographie-nationale/cartographie/commit/3d5ffab14f44117b1282619a1096467435773f7b)).

### Autres changements
- Correction de la gestion des paramètres de requête `territoire_type` ([d37f489](https://github.com/anct-cartographie-nationale/cartographie/commit/d37f4898c5e396bec73eecccd9b5112e79957a35)).
- Mise à jour des dépendances et des outils de développement.
- Amélioration de la configuration et des tests de l'infrastructure.
- Ajout de logs pour faciliter le débogage et le monitoring.
