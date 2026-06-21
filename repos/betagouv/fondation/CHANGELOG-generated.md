## Changelog : fondation (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur une refonte architecturale majeure vers une approche "feature-first", améliorant la maintenabilité et l'évolutivité du code.  Des améliorations significatives ont également été apportées à la gestion des fichiers, des rapports et des sessions, notamment en termes de sélection, d'archivage et de synchronisation des données. Des corrections de sécurité et des mises à jour de dépendances ont également été intégrées.

### Évolutions fonctionnelles
- Possibilité de joindre des fichiers à un dossier de nomination. [#407](https://github.com/betagouv/fondation/issues/407)
- Amélioration de la sélection des fichiers pour l'agenda, avec la possibilité de pré-sélectionner et de verrouiller les fichiers officiellement rapportés. [#384](https://github.com/betagouv/fondation/issues/384)
- Ajout de la possibilité de renoncer à une présentation planifiée. [#378](https://github.com/betagouv/fondation/issues/378)
- Ajout de la possibilité d'indiquer les membres absents dans un plan de présentation. [#358](https://github.com/betagouv/fondation/issues/358)
- Amélioration de l'affichage des rapports officiels, notamment avec l'ajout de l'heure de fin. [#379](https://github.com/betagouv/fondation/issues/379)
- Ajout de la gestion du statut des sessions. [#362](https://github.com/betagouv/fondation/issues/362)
- Amélioration de l'interface pour l'édition de documents avec un éditeur WYSIWYG. [#352](https://github.com/betagouv/fondation/issues/352)
- Correction de l'affichage des fichiers non archivés dans les rapports officiels. [#381](https://github.com/betagouv/fondation/issues/381)
- Correction de l'affichage des fichiers sans résultat dans les rapports officiels. [#429](https://github.com/betagouv/fondation/issues/429)

### Évolutions techniques
- Refonte de l'architecture vers une approche "feature-first" pour plusieurs modules : auth, admin, reports, summary, hooks, layout, shared et secretariat-general. [#433](https://github.com/betagouv/fondation/issues/433), [#432](https://github.com/betagouv/fondation/issues/432), [#431](https://github.com/betagouv/fondation/issues/431), [#430](https://github.com/betagouv/fondation/issues/430), [#428](https://github.com/betagouv/fondation/issues/428), [#427](https://github.com/betagouv/fondation/issues/427)
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité : `react-router`, `vite`, `postcss`, `axios`, `@nestjs/core`.
- Mise à jour de `pnpm` vers la version 11.
- Ajout de Vitest et Storybook pour les tests et le développement de composants. [#409](https://github.com/betagouv/fondation/issues/409)
- Utilisation des tokens de couleurs DSFR au lieu des couleurs Tailwind natives. [#418](https://github.com/betagouv/fondation/issues/418)
- Utilisation d'oxfmt comme formateur de code par langage dans VSCode. [#406](https://github.com/betagouv/fondation/issues/406)

### Autres changements
- Suppression de packages `shared-models` inutilisés. [#426](https://github.com/betagouv/fondation/issues/426)
- Correction de la configuration de Renovate pour éviter les erreurs de limite de mémoire. [#420](https://github.com/betagouv/fondation/issues/420)
- Amélioration de la documentation et des tests.
- Correction de divers bugs et améliorations mineures de l'interface utilisateur.
- Mise à jour de la documentation README. [#392](https://github.com/betagouv/fondation/issues/392)
- Ajout de tests pour l'ingestion de données Lolfi. [#398](https://github.com/betagouv/fondation/issues/398)
- Suppression de la dépendance `@tailwindcss/postcss`. [#345](https://github.com/betagouv/fondation/issues/345)
