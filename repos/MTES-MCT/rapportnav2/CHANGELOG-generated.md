## Changelog : rapportnav2 (30 derniers jours, au 13 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'infrastructure CI/CD, notamment en optimisant les temps de build et en intégrant des outils d'analyse de code plus performants. De nouvelles fonctionnalités ont été ajoutées, comme l'intégration d'un service d'adresse et l'ajout de la gestion des criées. Des corrections ont également été apportées, notamment concernant la gestion des règles AEM et la typage des données.

### Évolutions fonctionnelles
- Ajout d'un service d'adresse provenant de data.gouv.fr avec auto-complétion dans l'interface utilisateur.
- Intégration de la gestion des criées avec l'ajout d'une liste, d'endpoints et d'un panneau d'administration.
- Ajout du type de localisation pour les contrôles de navigation.
- Amélioration de la recherche d'établissement.
- Ajout d'opérations de plongée pour les contrôles environnementaux.

### Évolutions techniques
- Optimisation de l'utilisation du cache lors des builds backend.
- Refonte du processus de build et de test frontend pour une meilleure performance.
- Intégration de SonarQube pour l'analyse du code frontend.
- Mise à jour de l'image Gradle utilisée dans le CI.
- Utilisation de bellsoft/liberica-openjdk-alpine:25 pour le CI.
- Mise à jour de Vite vers la version 8.
- Amélioration de la configuration de Release Please.
- Mise à jour de plusieurs dépendances (Spring Boot, Flyway, Monitor-UI, Jackson Core).
- Utilisation du hash de commit au lieu du tag pour renforcer la sécurité.

### Autres changements
- Correction de plusieurs problèmes identifiés par SonarQube.
- Suppression d'assets frontend inutilisés.
- Suppression de fichiers .env inutilisés.
- Mise à jour des suppressions CVE.
- Correction de problèmes mineurs et améliorations diverses.
- Mise à jour des conteneurs PostgreSQL.
- Correction d'une boucle infinie dans le code frontend.
- Correction de problèmes de typage dans l'API.
- Amélioration de la validation de la création de missions.
- Suppression temporaire de Trivy.
- Ajout de fichiers `.trivyignore.yml`.
- Correction de problèmes liés à la gestion du cache HTML.
- Correction de bugs dans les règles AEM 4.1.3, 4.1.4, 7.4.
- Correction de la gestion de la durée des surveillances analytiques.
- Correction d'un problème d'importation non utilisée.
- Suppression de la dépendance à des versions spécifiques de certaines librairies.
- Ajout de snapshots mis à jour.
- Correction de problèmes liés à l'analyse Trivy.
- Correction de problèmes liés à l'analyse de sécurité Snyk.
