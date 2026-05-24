## Changelog : rapportnav2 (30 derniers jours, au 21 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des ressources et des agents, ainsi que des corrections de bugs et des optimisations de performance, notamment au niveau du pipeline CI/CD. L'intégration d'un service d'adresse via data.gouv.fr améliore l'expérience utilisateur en offrant une fonctionnalité d'autocomplétion. Des efforts ont été faits pour renforcer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'un service d'adresse provenant de data.gouv.fr avec autocomplétion dans l'interface utilisateur.
- Amélioration de la gestion des ressources et des agents (ajout, suppression, modification).
- Correction de l'affichage des erreurs 400 dans l'interface utilisateur.
- Amélioration de la gestion des données d'environnement pour les contrôles.
- Corrections et améliorations des règles AEM (Actions Environnementales Marines) pour différents types de missions.
- Ajout de la gestion des opérations de plongée pour les contrôles environnementaux.

### Évolutions techniques
- Mise à jour de plusieurs dépendances (Spring Boot, Flyway, Gradle, Monitor-UI, etc.).
- Refonte du pipeline CI/CD pour améliorer la performance et la fiabilité des builds et des tests.
- Utilisation d'une image Docker plus légère (bellsoft/liberica-openjdk-alpine:25) pour les builds.
- Amélioration de la configuration SonarQube et intégration de l'analyse du frontend.
- Optimisation de la gestion du cache pour les ressources d'environnement.
- Correction de problèmes liés à la configuration de Tomcat pour renforcer la sécurité.
- Mise à jour de la version de Vite à la version 8.

### Autres changements
- Suppression d'imports inutilisés.
- Mise à jour des suppressions de CVE (Common Vulnerabilities and Exposures).
- Suppression de fichiers `.env` inutilisés.
- Amélioration de la documentation et des commentaires dans le code.
- Correction de divers problèmes de configuration et de build.
- Suppression de l'analyse temporaire de SonarQube.
- Mise à jour des snapshots de tests.
- Ajout de fichiers `.trivyignore.yml` pour ignorer certains problèmes de sécurité dans Trivy.
- Correction de problèmes liés à la gestion des promesses rejetées dans SonarQube.
- Suppression de l'artefact frontend dans SonarQube.
- Correction de l'analyse des durées dans les rapports analytiques.
