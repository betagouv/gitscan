## Changelog : csplab (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'ingestion des offres d'emploi, l'ajout de nouvelles fonctionnalités pour la gestion des sources d'offres, et l'amélioration de l'expérience utilisateur, notamment avec l'ajout de tests end-to-end pour le parcours CV. Des travaux importants ont également été réalisés sur l'infrastructure et les outils de développement.

### Évolutions fonctionnelles
- Ajout d'une colonne de référence aux offres d'emploi dans l'interface web. [#657](https://github.com/betagouv/csplab/issues/657)
- Mise en place de l'authentification par email et mot de passe pour les utilisateurs. [#639](https://github.com/betagouv/csplab/issues/639)
- Possibilité de mettre à jour certains champs des utilisateurs dans l'interface d'administration. [#653](https://github.com/betagouv/csplab/issues/653)
- Ajout de pages statiques pour les mentions légales, la politique de confidentialité et l'accessibilité. [#224](https://github.com/betagouv/csplab/issues/224), [#225](https://github.com/betagouv/csplab/issues/225), [#226](https://github.com/betagouv/csplab/issues/226), [#227](https://github.com/betagouv/csplab/issues/227)
- Intégration de tests end-to-end (E2E) pour le parcours de candidature (CV). [#460](https://github.com/betagouv/csplab/issues/460), [#461](https://github.com/betagouv/csplab/issues/461), [#462](https://github.com/betagouv/csplab/issues/462), [#463](https://github.com/betagouv/csplab/issues/463)
- Ajout de la possibilité de filtrer les offres par catégorie A+. [#482](https://github.com/betagouv/csplab/issues/482)
- Publication du notebook sur GitHub Pages. [#641](https://github.com/betagouv/csplab/issues/641)
- Ajout de métiers dans le cas d'utilisation de mise en relation CV/opportunités. [#637](https://github.com/betagouv/csplab/issues/637)
- Ajout d'un endpoint pour lister les offres. [#440](https://github.com/betagouv/csplab/issues/440)

### Évolutions techniques
- Refactorisation de l'architecture de l'ingestion pour une meilleure gestion des webhooks TalentSoft.
- Amélioration de la gestion des erreurs et de la journalisation dans l'ingestion.
- Mise en place d'un nouveau système de gestion des sources d'offres (Source entity et API).
- Migration vers un modèle utilisateur personnalisé pour une plus grande flexibilité.
- Refactorisation des tests de présentation et ajout de tests E2E avec Playwright.
- Mise à jour des dépendances (vitest, node24, etc.).
- Amélioration de la configuration et des workflows CI/CD.
- Utilisation de couleurs DSFR exactes dans l'interface ATS. [#679](https://github.com/betagouv/csplab/issues/679)
- Refactorisation du code pour utiliser npm sass pour le MVP CV. [#646](https://github.com/betagouv/csplab/issues/646)
- Isolation des vues d'ingestion. [#662](https://github.com/betagouv/csplab/issues/662)
- Amélioration de la gestion des variables d'environnement pour l'ingestion.
- Ajout de la gestion des erreurs frontend. [#629](https://github.com/betagouv/csplab/issues/629)
- Refactorisation de l'API pour utiliser v1 scope. [#588](https://github.com/betagouv/csplab/issues/588)

### Autres changements
- Documentation de l'API TalentSoft webhooks. [#503](https://github.com/betagouv/csplab/issues/503)
- Traduction du template de pull request en français. [#619](https://github.com/betagouv/csplab/issues/619)
- Ajout de règles de linting pour le schéma. [#608](https://github.com/betagouv/csplab/issues/608)
- Mise à jour de la documentation.
- Nettoyage de code et corrections de bugs mineurs.
- Ajout de tests unitaires et d'intégration.
- Amélioration de la configuration du projet.
- Ajout de la possibilité de récupérer tous les commits du dépôt. [#661](https://github.com/betagouv/csplab/issues/661)
