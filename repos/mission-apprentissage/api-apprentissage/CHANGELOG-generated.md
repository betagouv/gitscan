## Changelog : api-apprentissage (30 derniers jours, au 31 août 2026)

### Résumé
Ce mois a été marqué par l'introduction d'un environnement "Sandbox" permettant de tester les fonctionnalités de manière isolée et sécurisée. Parallèlement, une montée en version majeure de l'infrastructure technique (Node.js, Next.js, TypeScript) a été réalisée pour garantir la stabilité et la performance de l'API, tout en améliorant l'interface d'administration des organisations.

### Évolutions fonctionnelles
- **Mise en place du mode Sandbox** : Introduction d'un environnement de test avec des clés API dédiées ([#505](https://github.com/mission-apprentissage/api-apprentissage/issues/505)), des habilitations automatiques ([#507](https://github.com/mission-apprentissage/api-apprentissage/issues/507)) et la possibilité de choisir l'environnement du jeton directement dans l'interface ([#508](https://github.com/mission-apprentissage/api-apprentissage/issues/508)).
- **Gestion des environnements** : Routage automatique des requêtes selon l'environnement de la clé API ([#506](https://github.com/mission-apprentissage/api-apprentissage/issues/506)) et possibilité de fermer les inscriptions en environnement de recette ([#511](https://github.com/mission-apprentissage/api-apprentissage/issues/511)).
- **Administration et Permissions** : Résolution de conflits lors de la création, de la recherche et du filtrage des habilitations dans l'administration des organisations ([#504](https://github.com/mission-apprentissage/api-apprentissage/issues/504)).
- **Améliorations de l'interface (UI)** : Ajustements visuels sur la page profil sandbox ([#514](https://github.com/mission-apprentissage/api-apprentissage/issues/514)) et correction du positionnement des blocs de génération de jetons et des notifications (toasts) ([#515](https://github.com/mission-apprentissage/api-apprentissage/issues/515), [#516](https://github.com/mission-apprentissage/api-apprentissage/issues/516)).
- **Précisions métier** : Clarification des conditions d'utilisation de l'API de candidature ([#509](https://github.com/mission-apprentissage/api-apprentissage/issues/509)).

### Évolutions techniques
- **Montée en version technologique** : Migration vers Next.js 16 ([#501](https://github.com/mission-apprentissage/api-apprentissage/issues/501)), TypeScript 7 et passage de l'outillage de linting vers Biome ([#502](https://github.com/mission-apprentissage/api-apprentissage/issues/502)).
- **Infrastructure et CI/CD** : Passage à Node 26 avec mise à jour des GitHub Actions pour stabiliser le déploiement ([#519](https://github.com/mission-apprentissage/api-apprentissage/issues/519), [#520](https://github.com/mission-apprentissage/api-apprentissage/issues/520)) et mise à jour de l'image Docker Metabase ([#500](https://github.com/mission-apprentissage/api-apprentissage/issues/500)).
- **Architecture** : Refactorisation du middleware vers un proxy pour alléger le bundle du SDK ([#503](https://github.com/mission-apprentissage/api-apprentissage/issues/503)) et optimisation de la gestion des arrêts (shutdown) lors des migrations ([#512](https://github.com/mission-apprentissage/api-apprentissage/issues/512)).
- **Fiabilité** : Correction d'erreurs de production via Sentry ([#517](https://github.com/mission-apprentissage/api-apprentissage/issues/517)) et amélioration de la gestion des requêtes (forwards) lors des problèmes de connexion ([#518](https://github.com/mission-apprentissage/api-apprentissage/issues/518)).

### Autres changements
- **Documentation** : Mise à jour de la documentation technique (URL canoniques) et documentation complète du mode Sandbox (OpenAPI et UI) ([#510](https://github.com/mission-apprentissage/api-apprentissage/issues/510), [#514](https://github.com/mission-apprentissage/api-apprentissage/issues/514), [#515](https://github.com/mission-apprentissage/api-apprentissage/issues/515)).
