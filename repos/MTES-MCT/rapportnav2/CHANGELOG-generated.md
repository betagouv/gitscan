## Changelog : rapportnav2 (30 derniers jours, au 13 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'infrastructure CI/CD, notamment en optimisant les temps de construction et en intégrant des analyses de sécurité plus robustes. De nouvelles fonctionnalités ont été ajoutées pour faciliter la saisie d'informations géographiques et pour la gestion des criées. Des corrections ont également été apportées pour améliorer la précision des données et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'un service d'adresse provenant de data.gouv.fr avec auto-complétion dans l'interface utilisateur.
- Ajout de la gestion des criées avec une interface d'administration dédiée.
- Amélioration de la recherche d'établissements.
- Ajout du type de localisation pour les contrôles de navigation.
- Correction de l'affichage des actions SEA et LAND pour les AEM 4.3.3.
- Correction du comptage des cibles pour les AEM 7.4.
- Correction de la gestion des résumés d'environnement dans les rapports de patrouille.

### Évolutions techniques
- Optimisation de l'utilisation du cache lors de la construction du backend.
- Refonte du pipeline CI/CD pour inclure des tests frontend plus complets et une intégration avec SonarQube.
- Mise à jour de l'image Docker utilisée pour les builds CI/CD (utilisation de bellsoft/liberica-openjdk-alpine:25).
- Amélioration de la configuration de SonarQube.
- Mise à jour de plusieurs dépendances : Vite (version 8), Monitor-UI, Gradle, Spring Boot.
- Utilisation du hash de commit pour renforcer la sécurité.
- Suppression d'assets frontend inutilisés pour SonarQube.

### Autres changements
- Mise à jour des suppressions de CVE pour corriger des faux positifs.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour de la documentation et de la configuration du projet.
- Suppression d'imports inutilisés.
- Correction de problèmes liés à la validation du schéma de création de mission.
- Correction d'un problème d'infinite loop dans l'authentification frontend.
- Mise à jour des conteneurs PostgreSQL.
- Suppression d'un ancien fichier .env inutilisé.
- Amélioration de la configuration de release-please.
- Correction de problèmes liés à la gestion des durées dans les analyses.
- Correction de problèmes liés à l'analyse de sécurité Trivy.
- Correction de problèmes liés à l'intégration de Snyk.
- Mise à jour des snapshots de tests.
