## Changelog : rapportnav2 (30 derniers jours, au 21 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des ressources et des agents, notamment l'ajout de la gestion des équipes et des ressources associées. Des corrections de bugs et des améliorations de la sécurité ont également été implémentées, ainsi que des optimisations de l'infrastructure CI/CD pour des builds et des tests plus rapides et plus fiables. L'intégration d'un service d'adresse via data.gouv.fr améliore l'expérience utilisateur en offrant une fonctionnalité d'autocomplétion.

### Évolutions fonctionnelles
- Ajout de la gestion des équipes et des ressources associées aux agents. [#1364](https://github.com/MTES-MCT/rapportnav2/pull/1364)
- Intégration d'un service d'adresse via data.gouv.fr avec autocomplétion dans l'interface utilisateur.
- Amélioration de la gestion des opérations de plongée dans le module EnvControl.
- Correction de l'affichage des erreurs 400 sur le frontend.
- Amélioration de la gestion des durées de surveillance environnementale dans l'API Analytics.
- Mise à jour des règles AEM (Actions Environnementales Marines) pour une meilleure précision.

### Évolutions techniques
- Mise à jour de la version de Spring Boot.
- Amélioration de l'infrastructure CI/CD :
    - Utilisation d'une image Docker plus légère (bellsoft/liberica-openjdk-alpine:25).
    - Optimisation de la mise en cache des builds backend.
    - Intégration de rapports frontend à SonarQube.
    - Refonte de la configuration de l'analyse statique (SonarQube, Trivy, Dependency-Check).
- Mise à jour de plusieurs dépendances : Gradle, Monitor-UI, Flyway, Babel.
- Correction de problèmes de sécurité liés à la configuration de Tomcat.
- Suppression d'imports inutilisés.
- Amélioration de la couverture de tests.
- Suppression de fichiers .env inutilisés.

### Autres changements
- Mise à jour des suppressions de CVE (Common Vulnerabilities and Exposures) pour éviter les faux positifs.
- Suppression de l'analyse SonarQube temporaire puis restauration.
- Diverses corrections de bugs et améliorations de la qualité du code.
- Mise à jour de la documentation et de la configuration.
- Correction de problèmes de typage dans le module RapportDePatrouille.
- Amélioration de la gestion des champs nuls dans les requêtes PATCH.
- Ajout de fichiers de configuration pour Trivy et Dependency-Check.
- Correction de problèmes de boucle infinie dans le code frontend.
- Mise à jour de la version de l'image PostgreSQL utilisée dans les tests.
- Correction de problèmes liés à la gestion des promesses rejetées dans les tests SonarQube.
