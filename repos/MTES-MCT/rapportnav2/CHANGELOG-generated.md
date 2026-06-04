## Changelog : rapportnav2 (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, les évolutions de rapportnav2 se concentrent sur l'amélioration de la gestion des ressources et des agents, l'ajout de nouvelles fonctionnalités pour les contrôles environnementaux (notamment la plongée), et des optimisations techniques pour la CI/CD et la sécurité. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la gestion des ressources et des agents dans l'interface d'administration ([#1381](https://github.com/MTES-MCT/rapportnav2/issues/1381)).
- Possibilité d'ajouter des informations de plongée aux contrôles environnementaux.
- Mise à jour de l'action "entretien des moyens" avec l'ajout d'une table `mission_action_resource` [#1390](https://github.com/MTES-MCT/rapportnav2/issues/1390).
- Amélioration de la recherche d'établissements.
- Utilisation d'un service d'adresse de data.gouv.fr avec auto-complétion dans l'interface.
- Ajout du type de localisation pour les contrôles environnementaux.
- Remplacement des champs de texte par des zones de texte pour les observations des contrôles environnementaux.
- Correction de l'affichage des codes d'erreur 400.

### Évolutions techniques
- Mise à jour de la version de Vite à la version 8.
- Amélioration du pipeline CI/CD :
    - Utilisation d'une image Docker plus légère pour les builds (bellsoft/liberica-openjdk-alpine:25).
    - Optimisation de la mise en cache des builds backend.
    - Refonte de la configuration du pipeline.
    - Ajout de rapports SonarQube pour le frontend.
    - Intégration de Trivy pour l'analyse de vulnérabilités.
- Mise à jour des dépendances : Flyway, Monitor-ui, Gradle, et divers paquets npm.
- Amélioration de la couverture de tests.
- Suppression d'artefacts inutiles dans SonarQube.
- Correction de problèmes liés à la configuration de SonarQube.
- Renforcement de la sécurité en forçant l'utilisation d'une version spécifique de `tomcat-embed-core`.
- Suppression de suppressions de CVE obsolètes.
- Ajout de validations côté backend.
- Générateur de documentation pour les règles de validation.

### Autres changements
- Correction de divers problèmes de typage et de configuration.
- Suppression d'imports inutilisés.
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour des conteneurs PostgreSQL.
