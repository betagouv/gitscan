## Changelog : monstagedeseconde (30 derniers jours, au 24 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur pour les entreprises et les étudiants, avec des mises à jour des pages partenaires, des offres et des formulaires. Des corrections et des optimisations techniques ont également été apportées, notamment pour la gestion des tâches d'archivage et la maintenance estivale.

### Évolutions fonctionnelles
- Mise à jour de la page étudiant [#941](https://github.com/betagouv/monstagedeseconde/pull/941).
- Ajout d'un carrousel de logos de partenaires sur les pages pros et partenaires [#944](https://github.com/betagouv/monstagedeseconde/pull/944) et [#942](https://github.com/betagouv/monstagedeseconde/pull/942).
- Amélioration du formulaire de publication d'offres [#937](https://github.com/betagouv/monstagedeseconde/pull/937).
- Adaptation de la plateforme pour la maintenance estivale et les jours fériés [#943](https://github.com/betagouv/monstagedeseconde/pull/943).
- Limitation de la longueur de la description des offres via l'API [#922](https://github.com/betagouv/monstagedeseconde/pull/922).

### Évolutions techniques
- Refactorisation du code pour mutualiser des éléments techniques [#938](https://github.com/betagouv/monstagedeseconde/pull/938).
- Mise à jour des tâches d'archivage des étudiants pour une meilleure gestion.
- Correction de tests unitaires et système pour garantir la stabilité de la plateforme.
- Correction d'une erreur dans la vérification des horaires.

### Autres changements
- Maintien de l'accès administrateur pendant la maintenance.
- Suppression de l'outil Tally.
- Suppression d'un bloc "nl".
- Mise à jour des dépendances : `websocket-driver` (0.8.0 -> 0.8.1) et `view_component` (4.9.0 -> 4.12.0) et `js-yaml` (3.14.2 -> 3.15.0).
