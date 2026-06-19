## Changelog : fondation (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur une refonte architecturale majeure vers une approche "feature-first", améliorant la maintenabilité et l'organisation du code.  Des améliorations significatives ont également été apportées à la gestion des documents, notamment les agendas et les rapports officiels, avec de nouvelles fonctionnalités pour la sélection de fichiers, la gestion des statuts et l'archivage. Des corrections de sécurité et des mises à jour de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Ajout de la possibilité de joindre des fichiers à un dossier de nomination [#407](https://github.com/betagouv/fondation/issues/407).
- Amélioration de la sélection des fichiers d'agenda, avec la possibilité de pré-sélectionner et de verrouiller les fichiers officiellement rapportés [#384](https://github.com/betagouv/fondation/issues/384).
- Ajout de la possibilité de renoncer à une présentation dans les plans de présentation [#378](https://github.com/betagouv/fondation/issues/378).
- Amélioration de l'affichage des plans de présentation, avec la possibilité d'ajouter des membres absents [#358](https://github.com/betagouv/fondation/issues/358).
- Ajout de la possibilité d'ajouter des avis ("Je donne mon avis") [#360](https://github.com/betagouv/fondation/issues/360).
- Amélioration de l'affichage des documents dans la liste des documents, notamment pour les rapports officiels sans agenda [#368](https://github.com/betagouv/fondation/issues/368).
- Ajout de la possibilité de filtrer les agendas pour exclure les fichiers déjà rapportés [#397](https://github.com/betagouv/fondation/issues/397).
- Amélioration de l'affichage des noms d'agenda dans la liste des plans [#391](https://github.com/betagouv/fondation/issues/391) et dans les rapports officiels [#402](https://github.com/betagouv/fondation/issues/402).
- Ajout de l'heure de fin dans les documents du rapport officiel [#379](https://github.com/betagouv/fondation/issues/379).

### Évolutions techniques
- Refonte architecturale majeure vers une approche "feature-first" pour améliorer la maintenabilité et l'organisation du code (PRs [#433](https://github.com/betagouv/fondation/pull/433), [#432](https://github.com/betagouv/fondation/pull/432), [#431](https://github.com/betagouv/fondation/pull/431), [#430](https://github.com/betagouv/fondation/pull/430), [#429](https://github.com/betagouv/fondation/pull/429), [#428](https://github.com/betagouv/fondation/pull/428), [#427](https://github.com/betagouv/fondation/pull/427)).
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (React, Vite, Axios, @nestjs/core, PostCSS) [#423](https://github.com/betagouv/fondation/issues/423), [#422](https://github.com/betagouv/fondation/issues/422), [#346](https://github.com/betagouv/fondation/issues/346), [#347](https://github.com/betagouv/fondation/issues/347), [#344](https://github.com/betagouv/fondation/issues/344).
- Mise en place de Vitest et Storybook pour les tests et le développement de composants [#409](https://github.com/betagouv/fondation/issues/409).
- Utilisation des tokens de couleurs DSFR au lieu des couleurs Tailwind natives [#418](https://github.com/betagouv/fondation/issues/418).
- Configuration d'oxfmt comme formateur de code par langage dans VSCode [#406](https://github.com/betagouv/fondation/issues/406).
- Suppression de composants inutilisés et de packages obsolètes [#426](https://github.com/betagouv/fondation/issues/426).

### Autres changements
- Mise à jour de la documentation README [#392](https://github.com/betagouv/fondation/issues/392) et [#353](https://github.com/betagouv/fondation/issues/353).
- Amélioration de la configuration de Renovate pour éviter les limites de mémoire [#420](https://github.com/betagouv/fondation/issues/420) et limiter le nombre de PRs ouverts [#350](https://github.com/betagouv/fondation/issues/350).
- Ajout de tests d'acceptation pour la documentation [#399](https://github.com/betagouv/fondation/issues/399).
- Correction de divers bugs et améliorations mineures de l'interface utilisateur.
