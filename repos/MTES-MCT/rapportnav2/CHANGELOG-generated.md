## Changelog : rapportnav2 (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les évolutions de rapportnav2 se concentrent sur l'amélioration des fonctionnalités existantes, notamment la gestion des ressources des agents, l'intégration de Metabase pour des rapports plus visuels, et des corrections pour une meilleure expérience utilisateur. Des améliorations techniques ont également été apportées, notamment concernant la validation des données et la gestion des dépendances.

### Évolutions fonctionnelles
- Ajout de la gestion des ressources des agents, permettant de gérer les moyens alloués aux agents. [#1381](https://github.com/MTES-MCT/rapportnav2/issues/1381)
- Intégration d'un iframe Metabase pour afficher des rapports directement dans l'application. [#1390](https://github.com/MTES-MCT/rapportnav2/issues/1390)
- Ajout de la fonctionnalité "diving" pour les contrôles environnementaux.
- Amélioration de l'interface utilisateur pour la création de missions (dimensions du dialogue).
- Remplacement des champs texte par des zones de texte pour les observations des contrôles environnementaux.
- Correction de l'affichage des dropdown dans les dialogues d'administration.
- Restauration de la fonctionnalité "diving" pour les contrôles environnementaux.

### Évolutions techniques
- Mise à jour des règles de validation des données, avec ajout d'un générateur de documentation pour ces règles.
- Correction d'un bug concernant le type de localisation GPS des contrôles.
- Amélioration de la validation des données côté backend.
- Mise à jour des dépendances frontend (Monitor-UI).
- Corrections de bugs et améliorations diverses de l'interface utilisateur frontend.

### Autres changements
- Mise à jour de la documentation et des snapshots de tests.
- Correction de problèmes liés aux audits npm.
- Mise à jour du playbook de déploiement.
- Corrections mineures et refactoring du code.
