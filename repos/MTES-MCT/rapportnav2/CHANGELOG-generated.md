## Changelog : rapportnav2 (30 derniers jours, au 23 avril 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des ports et des criées, avec l'intégration de données externes et de nouvelles fonctionnalités dans l'interface utilisateur. Des corrections et améliorations ont également été apportées à la gestion des missions, des contrôles et de la sécurité. L'ajout de la gestion Sati est également une évolution majeure.

### Évolutions fonctionnelles
- Ajout de la liste des criées avec les endpoints associés et un panneau d'administration.
- Intégration d'un service d'adresse via l'API data.gouv.fr avec une fonction d'autocomplétion dans l'interface utilisateur.
- Ajout de la connexion à l'API des ports de MonitorFish et ajout d'un composant de recherche dans l'interface utilisateur.
- Implémentation de la gestion Sati avec des fonctionnalités de création, lecture et mise à jour.
- Ajout du "permis d'armement confirmé" pour les contrôles administratifs [#1099](https://github.com/MTES-MCT/rapportnav2/issues/1099).
- Ajout de la possibilité de renseigner le nombre d'heures en mer pour les missions de type "SEA" [#1250](https://github.com/MTES-MCT/rapportnav2/issues/1250).
- Amélioration du message d'avertissement pour les contrôles navals [#1259](https://github.com/MTES-MCT/rapportnav2/issues/1259).
- Ajout de la gestion des catégories d'infraction pour les contrôles navals.

### Évolutions techniques
- Mise à jour de Spring Boot.
- Archivage des anciennes tables SQL dans un nouveau schéma "archived".
- Amélioration de l'architecture hexagonale pour les Vessels.
- Utilisation du hash de commit au lieu du tag pour l'action Trivy afin de renforcer la sécurité.
- Ajout de stubs de ports.
- Mise à jour de la version de Trivy.

### Autres changements
- Correction de la validation du schéma pour les secteurs de contrôle.
- Correction de la validation du schéma pour les contrôles nautiques et de loisirs.
- Correction d'un bug empêchant l'affichage du message d'erreur de validation ULAM.
- Correction d'un problème empêchant l'exécution de la complétion de la mission environnementale sur les missions navales.
- Suppression de l'utilitaire de contrôle obsolète.
- Correction de bugs et améliorations de la sécurité grâce à Snyk.
- Correction de problèmes liés à la gestion des ressources ULAM.
- Correction de l'utilisation de l'API d'établissement en cas d'absence d'adresse.
- Correction des tests frontend.
- Mise à jour des dépendances.
- Publication des versions 2.72.0 et 2.73.0.
