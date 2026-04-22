## Changelog : rapportnav2 (30 derniers jours, au 2026-04-21)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'ajout de nouvelles fonctionnalités liées à la gestion des contrôles (types de contrôle, permis d'armement), l'amélioration de la validation des données et l'intégration de services externes pour la recherche d'adresses et de ports. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. Un travail significatif a été réalisé sur la gestion des données Sati, avec la création de la structure de base de données et l'implémentation des cas d'utilisation associés.

### Évolutions fonctionnelles
- Ajout du champ "permis d'armement confirmé" pour les contrôles administratifs. [#1099](https://github.com/MTES-MCT/rapportnav2/issues/1099)
- Ajout de la possibilité de sélectionner le type de contrôle "coquillages" pour les missions ULAM. [#1272](https://github.com/MTES-MCT/rapportnav2/issues/1272)
- Intégration d'un service d'autocomplétion d'adresses via l'API data.gouv.fr.
- Intégration d'un service de recherche de ports via l'API MonitorFish.
- Amélioration de la validation des données pour les missions ULAM, notamment en rendant obligatoire le nombre d'heures en mer pour les missions de type "MER". [#1250](https://github.com/MTES-MCT/rapportnav2/issues/1250)
- Amélioration des messages d'erreur de validation pour les ressources ULAM.
- Ajout de la gestion des pays et codes pays pour les adresses.
- Implémentation des cas d'utilisation (GET/PUT) pour la gestion des données Sati.
- Création de la structure de base de données Sati.

### Évolutions techniques
- Mise à jour de Spring Boot.
- Refactoring de l'architecture pour respecter les principes hexagonaux pour les Vessels.
- Archivage des anciennes tables SQL dans un nouveau schéma "archived".
- Correction de la configuration de l'action Trivy pour utiliser un hash fixe.
- Mise à jour de la version de Java à Java 25.
- Suppression de code obsolète (control-utils.ts).
- Amélioration de la performance en ajoutant un cache Caffeine pour les ports.
- Utilisation de HTTP 1.1 pour MonitorEnv.

### Autres changements
- Correction de problèmes d'audit npm.
- Ajout de listeners sur les modèles de données.
- Suppression de valeurs codées en dur (fishActionType, hardcoded fishActionType).
- Amélioration de la validation du secteur de contrôle.
- Amélioration de la validation du type de contrôle nautique et de loisirs.
- Correction d'un problème de validation sur les actions ULAM.
- Ajout de tests unitaires.
- Mise à jour de la documentation.
