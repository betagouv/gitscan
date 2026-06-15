## Changelog : fondation (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des agendas, des rapports officiels et des documents, avec un accent particulier sur l'expérience utilisateur. Des corrections de bugs et des optimisations ont été apportées pour fluidifier le workflow des agents et améliorer la fiabilité de l'application. Des efforts ont également été faits pour renforcer la sécurité et moderniser l'infrastructure.

### Évolutions fonctionnelles
- Amélioration de la sélection des fichiers d'agenda et verrouillage des fichiers une fois rapportés officiellement [#384](https://github.com/betagouv/fondation/issues/384), [#385](https://github.com/betagouv/fondation/issues/385).
- Ajout de la possibilité d'indiquer l'heure de fin dans les rapports officiels [#379](https://github.com/betagouv/fondation/issues/379).
- Ajout de la fonctionnalité "Je donne mon avis" pour les rapports [#360](https://github.com/betagouv/fondation/issues/360).
- Possibilité d'ajouter des membres absents dans les plans de présentation [#358](https://github.com/betagouv/fondation/issues/358).
- Amélioration de l'affichage des plans de présentation [#386](https://github.com/betagouv/fondation/issues/386).
- Ajout de la renonciation dans les plans de présentation [#378](https://github.com/betagouv/fondation/issues/378).
- Ajout d'un éditeur WYSIWYG pour les documents [#352](https://github.com/betagouv/fondation/issues/352).
- Amélioration de la gestion des statuts des sessions [#362](https://github.com/betagouv/fondation/issues/362).
- Correction de l'affichage des plans dans la liste [#391](https://github.com/betagouv/fondation/issues/391).
- Correction du design des boutons de sélection de fichiers d'agenda [#390](https://github.com/betagouv/fondation/issues/390).
- Correction de l'affichage du badge de documentation [#389](https://github.com/betagouv/fondation/issues/389).
- Amélioration de la sélection des fichiers d'agenda [#384](https://github.com/betagouv/fondation/issues/384).

### Évolutions techniques
- Mise en place de Vitest et Storybook pour les tests et le développement de composants [#409](https://github.com/betagouv/fondation/issues/409).
- Application de l'outil de formatage de code oxfmt [#406](https://github.com/betagouv/fondation/issues/406).
- Refactorisation pour utiliser lolfi ingest pour les données de test [#398](https://github.com/betagouv/fondation/issues/398).
- Extraction de la génération d'archives lolfi [#396](https://github.com/betagouv/fondation/issues/396).
- Mise à jour de la configuration de Renovate pour des commits sémantiques et un scope FON [#394](https://github.com/betagouv/fondation/issues/394).
- Mise à jour de la version de pnpm à la version 11 [#363](https://github.com/betagouv/fondation/issues/363).
- Configuration du cache de playwright pour accélérer les tests [#357](https://github.com/betagouv/fondation/issues/357).
- Correction de la configuration de Renovate pour limiter à un seul PR ouvert [#350](https://github.com/betagouv/fondation/issues/350).

### Autres changements
- Mise à jour de la documentation README [#392](https://github.com/betagouv/fondation/issues/392), [#353](https://github.com/betagouv/fondation/issues/353).
- Correction de plusieurs bugs mineurs liés à l'affichage et à la gestion des données dans l'interface utilisateur.
- Correction de problèmes liés à l'importation de données [#355](https://github.com/betagouv/fondation/issues/355).
- Correction de la synchronisation des données des rapports officiels [#402](https://github.com/betagouv/fondation/issues/402).
- Correction du nom de l'agenda dans le sélecteur de rapports officiels [#401](https://github.com/betagouv/fondation/issues/401).
- Correction du placeholder de recherche dans le tableau des nominations [#405](https://github.com/betagouv/fondation/issues/405).
- Suppression de la condition de migration inutile [#1071b5d](https://github.com/betagouv/fondation/commit/1071b5d).
- Mise à jour des dépendances (axios, vite, postcss, @nestjs/core) pour corriger des failles de sécurité [#347](https://github.com/betagouv/fondation/issues/347), [#346](https://github.com/betagouv/fondation/issues/346), [#344](https://github.com/betagouv/fondation/issues/344), [#356](https://github.com/betagouv/fondation/issues/356).
