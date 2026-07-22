## Changelog : rapportnav2 (30 derniers jours, au 21 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'administration des missions, notamment avec l'ajout d'actions dans l'interface d'administration et l'intégration de données sur les pays. Des optimisations de performance ont également été apportées, ainsi que des corrections de bugs pour améliorer la stabilité et l'expérience utilisateur.

### Évolutions fonctionnelles
- Ajout d'actions de mission à l'interface d'administration.
- Possibilité de rechercher des missions par ID et ID interne dans l'interface d'administration.
- Pré-remplissage de la table des missions et synchronisation avec les données d'environnement.
- Intégration de données sur les pays via l'API.
- Amélioration de l'interface de gestion de l'équipage des missions PAM.
- Corrections de l'affichage des options dans les radios multiples (Fish).
- Refonte de l'affichage des contrôles d'action dans la navigation (Fish).
- Ajout de deux attributs à ActionFish.
- Harmonisation de l'affichage des infractions.

### Évolutions techniques
- Optimisation des performances lors du calcul du statut des actions en utilisant des données en mémoire.
- Amélioration des performances des requêtes en base de données grâce à l'utilisation de `@BatchSize` pour les requêtes liées aux infractions, aux contrôles, aux agents, aux rôles d'agents.
- Mise à jour de la version de Spring Boot vers la 4.1.0.
- Utilisation de mocks dans les tests.
- Nettoyage de fichiers backend.

### Autres changements
- Correction de bugs liés à la validation des règles.
- Correction d'un bug empêchant la suppression d'une infraction sur les contrôles Fish [#1412](https://github.com/MTES-MCT/rapportnav2/issues/1412).
- Prévention de la duplication des informations générales et des cibles.
- Correction de problèmes de build et de tests.
- Suppression de boutons désactivés.
- Mise à jour des dépendances frontend.
