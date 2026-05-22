## Changelog : rapportnav2 (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les évolutions de rapportnav2 se concentrent sur l'amélioration de la gestion des ressources des agents, l'ajout de nouvelles fonctionnalités comme la recherche d'adresses via un service externe, et des optimisations significatives du processus d'intégration continue (CI) pour accélérer les tests et l'analyse du code. Des corrections de sécurité et des améliorations de la robustesse de l'application ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la gestion des ressources et de l'équipe associée aux agents.  Cela inclut la gestion des rôles et des types de ressources. ([#1364](https://github.com/MTES-MCT/rapportnav2/pull/1364))
- Implémentation d'une recherche d'adresses avec autocomplétion, s'appuyant sur le service data.gouv.fr. ([ea7d759](https://github.com/MTES-MCT/rapportnav2/commit/ea7d75913664b3966a4c52b971d37cf38301fc6c))
- Amélioration de la gestion des opérations de plongée dans le module EnvControl.
- Correction de l'affichage des erreurs 400 sur le frontend.
- Amélioration du calcul de la durée des surveillances environnementales dans l'API Analytics.
- Mise à jour des règles AEM (Actions Environnementales Marines) pour une meilleure précision.

### Évolutions techniques
- Refonte du pipeline CI pour utiliser des images Docker plus légères et optimiser la mise en cache des builds.
- Intégration de l'analyse statique du code frontend avec SonarQube.
- Amélioration de la configuration du pipeline CI pour une meilleure gestion des artefacts et des dépendances.
- Mise à jour de plusieurs dépendances : Spring Boot, Flyway, Gradle, Monitor-UI, et des plugins Babel.
- Mise à jour de l'image PostgreSQL utilisée dans les conteneurs.
- Suppression d'éléments inutilisés dans la configuration du backend pour améliorer la couverture des tests.
- Correction de problèmes de configuration liés à l'analyse de sécurité avec Trivy.
- Utilisation du hash de commit au lieu du tag pour renforcer la sécurité.

### Autres changements
- Suppression d'imports inutilisés.
- Mise à jour des suppressions de vulnérabilités (CVE).
- Correction de problèmes de configuration SonarQube.
- Diverses corrections de bugs et améliorations de la robustesse du code.
- Mise à jour des snapshots de tests.
- Suppression d'un ancien fichier .env.
- Correction de problèmes de validation du schéma lors de la création de missions.
- Correction d'un problème d'infini loop dans le code.
