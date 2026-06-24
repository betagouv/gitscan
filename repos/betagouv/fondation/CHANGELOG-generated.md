## Changelog : fondation (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des documents, notamment des agendas et des rapports, avec des fonctionnalités d'archivage, de sélection de fichiers et d'amélioration de l'expérience utilisateur. Des refactorings importants ont été effectués pour adopter une architecture plus moderne et maintenable, basée sur des fonctionnalités. Des corrections de sécurité et des mises à jour de dépendances ont également été intégrées.

### Évolutions fonctionnelles
- Amélioration de la sélection des fichiers d'agenda : ajout de la possibilité de pré-sélectionner des fichiers et de verrouiller les fichiers officiellement rapportés. [#381](https://github.com/betagouv/fondation/issues/381)
- Ajout de la possibilité de donner un avis (fonction "Je donne mon avis"). [#360](https://github.com/betagouv/fondation/issues/360)
- Ajout de la gestion des membres absents dans les plans de présentation. [#334](https://github.com/betagouv/fondation/issues/334)
- Amélioration de l'éditeur de documents avec un éditeur WYSIWYG. [#352](https://github.com/betagouv/fondation/issues/352)
- Ajout de la possibilité d'ajouter des pièces jointes aux dossiers de nomination. [#407](https://github.com/betagouv/fondation/issues/407)
- Amélioration de l'affichage des données dans les rapports officiels, notamment l'heure de fin et la gestion des agendas. [#378](https://github.com/betagouv/fondation/issues/378), [#380](https://github.com/betagouv/fondation/issues/380), [#368](https://github.com/betagouv/fondation/issues/368)
- Amélioration de la gestion de l'archivage des sessions. [#361](https://github.com/betagouv/fondation/issues/361), [#364](https://github.com/betagouv/fondation/issues/364)
- Ajout de la possibilité de renoncer à un plan de présentation. [#376](https://github.com/betagouv/fondation/issues/376)
- Amélioration de la gestion des statuts des sessions. [#362](https://github.com/betagouv/fondation/issues/362)

### Évolutions techniques
- Refactoring important de l'architecture frontend vers une approche "feature-first" pour une meilleure organisation et maintenabilité du code. [#434](https://github.com/betagouv/fondation/issues/434), [#433](https://github.com/betagouv/fondation/issues/433), [#432](https://github.com/betagouv/fondation/issues/432), [#431](https://github.com/betagouv/fondation/issues/431), [#430](https://github.com/betagouv/fondation/issues/430), [#429](https://github.com/betagouv/fondation/issues/429), [#428](https://github.com/betagouv/fondation/issues/428), [#427](https://github.com/betagouv/fondation/issues/427)
- Mise en place de Vitest et Storybook pour les tests et le développement des composants. [#409](https://github.com/betagouv/fondation/issues/409)
- Utilisation des tokens de couleurs DSFR au lieu des couleurs Tailwind natives. [#418](https://github.com/betagouv/fondation/issues/418)
- Migration vers SheetJS pour la gestion des fichiers Excel.
- Amélioration de la configuration du workflow de publication.
- Utilisation de lolfi pour la génération des données de test. [#398](https://github.com/betagouv/fondation/issues/398)

### Autres changements
- Ajout d'une documentation ADR pour l'architecture "feature-first" du frontend. [#434](https://github.com/betagouv/fondation/issues/434)
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité et améliorer la stabilité.
- Suppression de composants et de modèles inutilisés. [#426](https://github.com/betagouv/fondation/issues/426)
- Amélioration de la configuration de Renovate pour éviter les problèmes de mémoire. [#420](https://github.com/betagouv/fondation/issues/420)
- Ajout de tests d'acceptation avec Playwright.
- Mise à jour de la documentation README. [#392](https://github.com/betagouv/fondation/issues/392)
- Correction de divers bugs et améliorations de l'expérience utilisateur mineures.
