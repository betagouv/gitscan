## Changelog : territoires-en-transitions (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans le module d'audit et de labellisation, avec une refonte de l'interface et l'ajout de nouvelles fonctionnalités comme l'archivage des preuves et la gestion des rôles. Des efforts importants ont également été faits pour améliorer la performance et la sécurité de la plateforme, ainsi que pour faciliter l'import de plans d'action via un nouveau module dédié.

### Évolutions fonctionnelles
- Ajout d'un bandeau permettant de basculer vers la nouvelle vue de labellisation [#6b4b226](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6b4b226).
- Possibilité de dupliquer un plan d'action depuis son identifiant, avec copie des budgets et des preuves associées [#2bb4132](https://github.com/incubateur-ademe/territoires-en-transitions/commit/2bb4132), [#32a9d25](https://github.com/incubateur-ademe/territoires-en-transitions/commit/32a9d25), [#50fcabd](https://github.com/incubateur-ademe/territoires-en-transitions/commit/50fcabd).
- Intégration des informations d'audit dans la vue tableau du référentiel, avec suppression de l'onglet "Suivi" [#6b5adc0](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6b5adc0).
- Affichage du conseiller référent dans l'en-tête de la checklist d'audit [#6f3515a](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6f3515a).
- Possibilité de télécharger une archive des preuves d'un audit [#e59576d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/e59576d).
- Amélioration de l'affichage des scores indicatifs dans les sous-mesures [#390be3d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/390be3d).
- Ajout d'une action "Dupliquer l'action" dans les menus de fiche [#a428150](https://github.com/incubateur-ademe/territoires-en-transitions/commit/a428150).
- Possibilité de filtrer les mesures désactivées par la personnalisation [#ecec29f](https://github.com/incubateur-ademe/territoires-en-transitions/commit/ecec29f).

### Évolutions techniques
- Application d'une Content Security Policy (CSP) globale à toutes les routes pour renforcer la sécurité [#e538a37](https://github.com/incubateur-ademe/territoires-en-transitions/commit/e538a37).
- Refactor du code pour supprimer l'utilisation de row-level security (RLS) dans le service de base de données [#7217fd4](https://github.com/incubateur-ademe/territoires-en-transitions/commit/7217fd4).
- Mise à jour de Next.js et eslint-config-next en version 16.2.7 [#b54924a](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b54924a).
- Amélioration des performances en différant le chargement des dépendances lourdes [#b45496d](https://github.com/incubateur-ademe/territoires-en-transitions/commit/b45496d).
- Mise à jour de Node.js en version 24.18.0 pour corriger une régression avec node-fetch [#75dcfff](https://github.com/incubateur-ademe/territoires-en-transitions/commit/75dcfff).
- Passage des tests Storybook à Vitest addon [#6d2ad2e](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6d2ad2e).
- Parallelisation des tests e2e en CI avec une voie série dédiée [#49d89ed](https://github.com/incubateur-ademe/territoires-en-transitions/commit/49d89ed), [#00fc5c3](https://github.com/incubateur-ademe/territoires-en-transitions/commit/00fc5c3).
- Refactor du module d'import de plans d'action pour une meilleure structuration et performance [#f9348bb](https://github.com/incubateur-ademe/territoires-en-transitions/commit/f9348bb), [#2c6eaa3](https://github.com/incubateur-ademe/territoires-en-transitions/commit/2c6eaa3), [#6a2fdb2](https://github.com/incubateur-ademe/territoires-en-transitions/commit/6a2fdb2).

### Autres changements
- Amélioration de la documentation du dépôt pour les agents IA [#cb735b0](https://github.com/incubateur-ademe/territoires-en-transitions/commit/cb735b0).
- Mise à jour du schéma des préférences de la collectivité [#a6420d1](https://github.com/incubateur-ademe/territoires-en-transitions/commit/a6420d1).
- Ajout d'un plan pour la bascule des référentiels CAE/ECI vers TE [#387f6dc](https://github.com/incubateur-ademe/territoires-en-transitions/commit/387f6dc).
- Nettoyage du code et suppression de dépendances inutilisées.
- Correction de bugs mineurs et améliorations de la stabilité.
