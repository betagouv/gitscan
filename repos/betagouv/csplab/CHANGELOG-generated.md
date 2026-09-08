## Changelog : csplab (30 derniers jours, au 2026-09-07)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans la gestion des organismes et de leurs membres. Les capacités d'importation de données ont été enrichies et fiabilisées grâce à de nouvelles sources, tandis que l'architecture technique a été simplifiée pour gagner en efficacité et en maintenabilité. L'expérience utilisateur a également été améliorée par de nouveaux outils de recherche et une gestion plus fine des processus de recrutement.

### Évolutions fonctionnelles
- **Gestion des organismes** : Création, modification, consultation détaillée et gestion de la liste des organismes via l'interface d'administration [#1207](https://github.com/betagouv/csplab/issues/1207).
- **Gestion des membres** : Possibilité d'ajouter, modifier ou révoquer les rôles des agents au sein d'un organisme [#1219](https://github.com/betagouv/csplab/issues/1219), [#1264](https://github.com/betagouv/csplab/issues/1264), [#1273](https://github.com/betagouv/csplab/issues/1273).
- **Recherche et filtrage** : Amélioration de la recherche d'offres par mots-clés [#1125](https://github.com/betagouv/csplab/issues/1125) et par zone géographique [#1134](https://github.com/betagouv/csplab/issues/1134), ainsi que l'ajout de la recherche d'agents par email [#1322](https://github.com/betagouv/csplab/issues/1322).
- **Processus de recrutement** : Mise à jour des étapes de candidature et du suivi des processus [#1154](https://github.com/betagouv/csplab/issues/1154), [#1197](https://github.com/betagouv/csplab/issues/1197).

### Évolutions techniques
- **Architecture & Refactoring** : Transition vers une approche plus idiomatique Django (ADR-009) pour simplifier le code [#1305](https://github.com/betagouv/csplab/issues/1305) et refactorisation du routage pour qu'il soit lié au contexte de l'organisme [#1338](https://github.com/betagouv/csplab/issues/1338).
- **Ingestion de données** : Intégration de nouveaux référentiels (DILA, GIPCDG) pour l'import des organismes [#1224](https://github.com/betagouv/csplab/issues/1224), [#1262](https://github.com/betagouv/csplab/issues/1262) et optimisation de la consommation mémoire des pipelines d'ingestion [#1369](https://github.com/betagouv/csplab/issues/1369).
- **Infrastructure & Sécurité** : Migration vers la gestion des secrets via Scaleway Secret Manager [#1302](https://github.com/betagouv/csplab/issues/1302) et amélioration de la CI/CD avec l'intégration de l'outil `mise` [#1284](https://github.com/betagouv/csplab/issues/1284).
- **Développement (Tooling)** : Centralisation de la gestion des outils et des versions (Node.js, pnpm, etc.) avec `mise` [#1244](https://github.com/betagouv/csplab/issues/1244).

### Autres changements
- **Documentation** : Mise à jour de la documentation de l'API (OpenAPI/Redoc) incluant le rate limiting [#1345](https://github.com/betagouv/csplab/issues/1345) et les détails des filtres de recherche [#1137](https://github.com/betagouv/csplab/issues/1137).
- **Organisation du code** : Restructuration du projet avec le déplacement et la fusion du package frontend dans la structure web principale [#1344](https://github.com/betagouv/csplab/issues/1344), [#1346](https://github.com/betagouv/csplab/issues/1346).
