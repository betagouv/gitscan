## Changelog : rapportnav2 (30 derniers jours, au 6 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la modernisation des outils de développement et la correction de bugs. Une nouvelle fonctionnalité permettant la gestion des criées a été ajoutée, et des améliorations ont été apportées à l'API et à l'interface utilisateur. Des mises à jour de dépendances et des optimisations de l'infrastructure CI/CD ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de la gestion des criées avec l'ajout d'une liste, d'endpoints et d'un panneau d'administration dédié. [#1325](https://github.com/MTES-MCT/rapportnav2/pull/1325)
- Amélioration de l'API pour corriger un problème lié à l'utilisation de l'adresse pour l'établissement.
- Correction d'un bug dans le calcul de la durée des opérations de surveillance analytique.
- Correction d'un bug dans l'interface utilisateur concernant le ciblage lors de l'ajout d'une nouvelle infraction.

### Évolutions techniques
- Mise à jour de Vite vers la version 8.
- Mise à jour de Spring Boot.
- Mise à jour de Flyway.
- Refonte de la configuration `release-please-config.json`.
- Mise à jour de l'action CI pour utiliser GitLab Forge.
- Amélioration de la configuration de l'analyse de sécurité (Trivy, dependency-check).
- Suppression de fichiers `.env` inutilisés.
- Suppression temporaire de SonarQube et de l'analyse SonarQube dans le pipeline CI.
- Mise à jour de plusieurs dépendances (Monitor-UI, Gradle, Jackson Core).

### Autres changements
- Suppression de fausses positives dans la configuration de la suppression des CVE.
- Mise à jour des snapshots de tests.
- Correction de problèmes de vulnérabilités identifiés par Snyk dans les dépendances frontend.
- Correction de problèmes d'audit npm dans le frontend.
- Mise à jour de la version de l'action Trivy dans le workflow CI.
- Mise à jour de la version de l'action dependency-check dans le workflow CI.
- Correction de l'artefact de SonarQube dans le workflow CI.
- Correction de l'artefact de dependency-check dans le workflow CI.
- Mise à jour du conteneur PostgreSQL vers la version 15.17.
- Mise à jour de la suppression XML SVE.
