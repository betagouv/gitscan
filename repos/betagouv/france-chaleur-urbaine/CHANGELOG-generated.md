## Changelog : france-chaleur-urbaine (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des permissions et des accès, la correction de bugs liés à l'affectation des demandes et des réseaux, ainsi que l'ajout de nouvelles fonctionnalités de suivi et d'analyse des données. Des améliorations significatives ont également été apportées à l'expérience utilisateur, notamment au niveau de l'administration et de la cartographie. Enfin, le projet a bénéficié d'un effort important de documentation et de suivi des événements via PostHog.

### Évolutions fonctionnelles
- Ajout d'un nouveau système de permissions avec des rôles et une gestion plus fine des accès.
- Amélioration du workflow d'affectation des demandes aux réseaux.
- Ajout d'un lien pour corriger les permissions d'un gestionnaire directement depuis l'interface.
- Affichage des demandes plutôt que des tests d'adresses dans l'administration des réseaux.
- Ajout d'un bandeau d'information concernant une future indisponibilité du service.
- Ajout d'une FAQ accessible depuis la page d'accueil.
- Ajout de liens entrants vers la FAQ depuis d'autres pages.
- Amélioration de la visibilité des demandes à traiter et affectées dans l'interface d'administration.
- Ajout d'un bouton pour effacer la sélection dans les champs d'auto-complétion.
- Ajout d'un indicateur visuel pour les réseaux en construction.
- Ajout d'une fonctionnalité permettant de réaffecter une demande à un autre réseau.
- Amélioration de la gestion des relances et ajout de notes.
- Ajout d'une fonctionnalité pour afficher les emails dans l'administration.
- Intégration de l'outil Ademe Connect via iframe.

### Évolutions techniques
- Mise en place d'un cache au niveau des tuiles cartographiques pour améliorer les performances.
- Refactor de plusieurs composants et services pour améliorer la maintenabilité du code.
- Ajout d'un système de métriques avec une API Prometheus pour le monitoring.
- Amélioration du typage TypeScript dans plusieurs parties du code.
- Migration des comptes métropoles.
- Ajout de tests unitaires et d'intégration.
- Optimisation des requêtes en base de données pour améliorer les performances.
- Mise en place d'un système de suivi des événements avec PostHog pour l'analyse du comportement utilisateur.
- Suppression de code obsolète et nettoyage du codebase.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de scripts pour faciliter l'analyse et la mise à jour des données.

### Autres changements
- Mise à jour de la documentation.
- Correction de plusieurs erreurs de typographie et de style.
- Amélioration de l'accessibilité du site web.
- Ajout de commentaires dans le code pour faciliter la compréhension.
- Suppression de fichiers inutiles du dépôt.
- Amélioration de la configuration du projet.
- Ajout d'un fichier `.claudeignore`.
- Correction de problèmes de linting.
- Ajout de tests pour les routes territoires.
- Mise à jour des dépendances.
