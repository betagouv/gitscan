## Changelog : rapportnav2 (30 derniers jours, au 01 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des ressources et des agents, notamment l'ajout de fonctionnalités pour gérer l'affectation des ressources aux missions. Des corrections ont également été apportées pour améliorer la stabilité et la fiabilité de l'application, ainsi que des optimisations de l'infrastructure CI/CD.

### Évolutions fonctionnelles
- Ajout de la gestion des ressources et des agents : possibilité de gérer l'affectation des ressources (matériel, personnel) aux missions. [#1364](https://github.com/MTES-MCT/rapportnav2/pull/1364)
- Restauration de la fonctionnalité de "diving" (exploration détaillée) pour les contrôles environnementaux.
- Amélioration de l'affichage des erreurs 400 sur le frontend.
- Ajout d'un service d'adresse via data.gouv.fr avec auto-complétion sur le frontend.
- Ajout du type de localisation pour les contrôles de navigation.
- Correction de l'affichage des dropdown dans les dialogues d'administration.
- Correction du type de ressource ControlUnitResource manquant dans l'environnement.
- Correction de l'affichage des actions SEA et LAND pour AEM 4.3.3.
- Correction du comptage des cibles pour AEM 7.4.
- Correction du typage de `operationalSummary.envSummary` pour une meilleure compatibilité avec `otherActionsSummary.envSurveillances`.

### Évolutions techniques
- Mise à jour de l'infrastructure CI/CD :
    - Utilisation de `bellsoft/liberica-openjdk-alpine:25` pour les builds.
    - Amélioration de la mise en cache des builds backend.
    - Refonte de l'exclusion de fichiers dans le CI.
    - Ajout de rapports frontend à SonarQube.
    - Mise à jour des versions de Gradle et Vite.
- Mise à jour de la version de Flyway.
- Mise à jour de Kotlin.
- Amélioration de la configuration backend et exclusion des fichiers de configuration de la couverture de test.
- Correction de problèmes liés à SonarQube (analyse, artefacts, couverture).
- Mise à jour des dépendances npm et yarn.
- Suppression de l'analyse OSS Index.
- Correction de problèmes de sécurité liés à Tomcat (forcer la version `tomcat-embed-core`).
- Suppression de fichiers `.env` inutilisés.
- Mise à jour de la version de PostgreSQL.

### Autres changements
- Mise à jour de la documentation et des suppressions de CVE.
- Correction de divers problèmes de fiabilité détectés par SonarQube.
- Ajout de snapshots pour les tests.
- Suppression d'imports inutilisés.
- Mise à jour des suppressions de vulnérabilités (SVE suppression.xml).
- Correction de problèmes liés à la gestion des promesses rejetées dans SonarQube.
