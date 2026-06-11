## Changelog : rapportnav2 (30 derniers jours, au 09 juin 2026)

### Résumé
Ce mois-ci, les évolutions de rapportnav2 se concentrent sur l'amélioration des fonctionnalités existantes, notamment l'intégration de Metabase pour la visualisation de données, l'ajout de nouvelles fonctionnalités pour la gestion des ressources des agents, et des corrections pour l'outil d'entretien des moyens. Des améliorations techniques ont également été apportées pour optimiser le processus de construction et de déploiement.

### Évolutions fonctionnelles
- Intégration d'un iframe Metabase pour l'affichage de tableaux de bord et de rapports ([335da44](https://github.com/MTES-MCT/rapportnav2/commit/335da44f3a3fde0e0af055f8d1d97eb584458155)).
- Ajout de la gestion des ressources des agents, permettant de gérer les équipes et les équipements associés aux missions [#1381](https://github.com/MTES-MCT/rapportnav2/pull/1381) et [#1390](https://github.com/MTES-MCT/rapportnav2/issues/1390).
- Ajout de la possibilité de plonger (diving) pour les contrôles environnementaux.
- Amélioration de l'interface utilisateur pour la création de missions (dimensions du dialogue).
- Ajout d'un service d'adresse via data.gouv.fr avec auto-complétion dans l'interface.
- Amélioration de la gestion des types de ressources pour les unités de contrôle environnemental.

### Évolutions techniques
- Mise à jour de l'image Docker pour la construction avec Bellsoft Liberica JDK Alpine 25.
- Optimisation du processus de construction backend avec une meilleure utilisation du cache.
- Amélioration de la configuration du pipeline CI/CD.
- Corrections de vulnérabilités identifiées par l'analyse de sécurité (npm audit).
- Mise à jour des dépendances frontend (Monitor-UI).
- Amélioration de la couverture de test.

### Autres changements
- Correction de bugs divers liés à la validation des données.
- Amélioration de la gestion des types de données dans les rapports de patrouille.
- Correction de problèmes d'affichage et de comportement de l'interface utilisateur.
- Suppression d'imports inutilisés.
- Documentation mise à jour.
