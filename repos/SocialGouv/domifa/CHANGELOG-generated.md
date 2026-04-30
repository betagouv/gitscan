## Changelog : domifa (30 derniers jours, au 2026-04-30)

### Résumé
Ce mois-ci, les évolutions de DomiFa se sont concentrées sur l'amélioration de l'interface utilisateur avec l'intégration du Design System Framework (DSFR), la correction de plusieurs bugs notamment sur les formulaires et l'assignation des référents, et l'ajout de mesures de sécurité pour limiter les requêtes abusives. Des améliorations techniques ont également été apportées pour optimiser les tests et le processus de publication.

### Évolutions fonctionnelles
- Intégration du Design System Framework (DSFR) pour une interface utilisateur plus moderne et accessible.
- Correction de problèmes d'affichage et de fonctionnement des formulaires, notamment sur la page RGAA.
- Amélioration de l'assignation des référents.
- Ajout d'une bannière DSFR à l'interface.
- Correction de l'affichage des fiches pratiques.
- Correction des labels de boutons pour une meilleure clarté.

### Évolutions techniques
- Ajout d'un système de limitation de requêtes (throttling) pour protéger le backend contre les abus, avec ajout de logs pour le suivi.
- Amélioration des tests unitaires backend.
- Optimisation du processus de publication avec l'ajout de `[skip ci]` aux messages de commit de semantic-release.
- Refonte de la gestion des DTO (Data Transfer Objects) pour une meilleure sécurité et validation des données.
- Correction de problèmes liés à l'exécution des tests.

### Autres changements
- Ajout du fichier `claude.md`.
- Mise à jour de la documentation du changelog.
- Ajout d'une branche `fix-enforce-safety` au workflow de publication.
