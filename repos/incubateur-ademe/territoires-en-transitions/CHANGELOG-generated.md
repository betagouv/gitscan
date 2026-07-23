## Changelog : territoires-en-transitions (30 derniers jours, au 21 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la sécurité, notamment la correction de failles potentielles d'injection IDOR et de création de membres non autorisés.  De plus, des fonctionnalités importantes ont été ajoutées pour la gestion des référentiels, en particulier pour la migration vers le nouveau référentiel TE (Territoires en Transition), avec des outils de fusion de données et de gestion des statuts. L'interface utilisateur a également été améliorée, notamment avec l'introduction d'une nouvelle grille d'indicateurs et des améliorations de l'expérience utilisateur pour les audits et labellisations.

### Évolutions fonctionnelles
- Amélioration de la sécurité : blocage de l'injection IDOR dans les relations cross-collectivité pour les plans et les discussions [#7358](https://github.com/incubateur-ademe/territoires-en-transitions/issues/7358).
- Amélioration de la sécurité : blocage de la création de membres fantômes dans les collectivités [#7360](https://github.com/incubateur-ademe/territoires-en-transitions/issues/7360).
- Ajout de dates de début/fin pour les plans [#7490](https://github.com/incubateur-ademe/territoires-en-transitions/issues/7490).
- Possibilité d'importer des données via l'IA pour un plan.
- Nouvelle grille d'indicateurs avec édition en ligne, réordonnancement, et possibilité de collage de données.
- Amélioration de l'interface pour les audits et labellisations, avec une nouvelle checklist et une gestion améliorée des documents.
- Ajout de la possibilité d'archiver les preuves d'audit.
- Ajout d'un bandeau d'information pour les référentiels archivés ou en lecture seule.
- Ajout de la fusion des services, pilotes et explications CAE/ECI vers les mesures TE.
- Ajout de la fusion des liens fiches CAE/ECI vers TE.
- Ajout de la fusion des statuts d'origine vers les actions du référentiel CR.

### Évolutions techniques
- Refactor de l'authentification et migration vers une application Next.js unique.
- Mise à jour de Nx et des dépendances.
- Migration de certains composants vers TypeScript 6/7.
- Amélioration du pipeline CI/CD avec parallélisation des tests et optimisation des temps d'exécution.
- Suppression de code obsolète et simplification de certaines structures de données.
- Utilisation de `date-fns` au lieu de `luxon` pour les manipulations de dates.
- Mise en place d'un système de gestion des variables d'environnement plus robuste avec `dotenvx`.
- Refonte de l'architecture des tests E2E pour une meilleure fiabilité et parallélisation.
- Migration vers le pattern Result pour la gestion des erreurs dans certains modules.
- Amélioration de la gestion des erreurs et des transactions.
- Suppression de dépendances inutiles.

### Autres changements
- Amélioration de la documentation pour les agents IA.
- Mise à jour des labels et des textes de l'interface utilisateur.
- Correction de bugs mineurs et améliorations de la performance.
- Ajout de tests unitaires et E2E pour couvrir les nouvelles fonctionnalités et les corrections de bugs.
- Amélioration de la configuration de Storybook.
- Ajout de scripts pour faciliter le développement et le déploiement.
- Mise à jour du schéma des préférences de la collectivité.
- Ajout d'un script d'import des statuts EMT.
- Suppression de configurations npm obsolètes.
- Nettoyage du code et amélioration de la lisibilité.
