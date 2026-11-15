## Changelog : api-subventions-asso (30 derniers jours, au 12 novembre 2026)

### Résumé
Cette période a été marquée par une amélioration significative de l'expérience de recherche pour les utilisateurs, notamment via l'ajout de filtres géographiques et de nouvelles options de tri. Le projet a également entamé une phase de simplification technique avec la suppression de certains outils de visualisation et de suivi, tout en renforçant la robustesse du code par une migration vers TypeScript sur le front-end et des mises à jour de sécurité.

### Évolutions fonctionnelles
- **Amélioration de la recherche d'associations** : ajout de filtres par code postal ou département [#4099](https://github.com/betagouv/api-subventions-asso/issues/4099), intégration du nom SIRENE dans les résultats [#4065](https://github.com/betagouv/api-subventions-asso/issues/4065), et finalisation des options de tri, de pagination et de recherche par nom uniquement [#4087](https://github.com/betagouv/api-subventions-asso/issues/4087).
- **Optimisation de l'expérience utilisateur (UX)** : ajout de la correction orthographique personnalisée dans les champs de recherche [#4074](https://github.com/betagouv/api-subventions-asso/issues/4074) et implémentation de l'autocomplétion dans les formulaires.
- **Corrections de bugs** : résolution des problèmes liés à l'accès direct via URL [#4079](https://github.com/betagouv/api-subventions-asso/issues/4079) et correction de l'historique de recherche [#4107](https://github.com/betagouv/api-subventions-asso/issues/4107).
- **Administration** : création d'un nouvel accès (endpoint) pour consulter les statistiques d'inscription des utilisateurs administrateurs [#4077](https://github.com/betagouv/api-subventions-asso/issues/4077).

### Évolutions techniques
- **Connectivité et données** : mise en place de la connexion avec Chorus Omogen [#4094](https://github.com/betagouv/api-subventions-asso/issues/4094).
- **Refactoring et architecture** : migration du front-end vers TypeScript [#4082](https://github.com/betagouv/api-subventions-asso/issues/4082), restructuration des dossiers d'intégration [#4086](https://github.com/betagouv/api-subventions-asso/issues/4086) et optimisation de la logique interne de recherche d'associations [#4100](https://github.com/betagouv/api-subventions-asso/issues/4100) [#4091](https://github.com/betagouv/api-subventions-asso/issues/4091).
- **Simplification et nettoyage** : suppression de l'intégration Matomo [#4108](https://github.com/betagouv/api-subventions-asso/issues/4108) et retrait de la bibliothèque Chart.js pour les graphiques de données [#4083](https://github.com/betagouv/api-subventions-asso/issues/4083).
- **Sécurité et infrastructure** : mise à jour de la version Node.js pour répondre à une recommandation de sécurité (CERTFR) et intégration de PostHog pour l'analyse [#4075](https://github.com/betagouv/api-subventions-asso/issues/4075).

### Autres changements
- **Documentation** : mise à jour du README incluant le dictionnaire de prénoms INSEE et les spécifications des points de rupture (breakpoints) DSFR.
- **Maintenance** : ajustements des scripts de release et optimisation de la gestion du package manager (pnpm).
