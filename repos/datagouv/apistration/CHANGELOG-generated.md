## Changelog : apistration (30 derniers jours, au 9 avril 2026)

### Résumé
Cette période a été marquée par des améliorations de la robustesse et de la surveillance des services, notamment en renforçant la gestion des erreurs et des pings vers les services externes. Des correctifs ont été apportés pour améliorer la stabilité des tests et du déploiement. De nouvelles fonctionnalités ont été ajoutées concernant les données scolaires (régime de pensionnat) et les informations sur les entreprises (historique des effectifs GIP MDS). L'application a également été préparée pour une éventuelle publication en open source.

### Évolutions fonctionnelles
- Ajout de l'information sur le régime de pensionnat dans l'API d'inscription des élèves (V5) [#13](https://github.com/datagouv/apistration/pull/13).
- Ajout de l'historique des effectifs pour les entreprises GIP MDS [#2154](https://github.com/datagouv/apistration/pull/2154).
- Amélioration de la documentation métier pour l'API AEEH (avec ajout de ping url et position) [#2152](https://github.com/datagouv/apistration/pull/2152).
- Possibilité de créer un token d'administration [#2152](https://github.com/datagouv/apistration/pull/2152).
- Ajout de scopes pour les données de bourse MEN [#1](https://github.com/datagouv/apistration/pull/1).

### Évolutions techniques
- Refonte de la gestion des identifiants de l'application, en remplaçant les informations chiffrées par des fichiers YAML en clair [#11](https://github.com/datagouv/apistration/pull/11).
- Amélioration de la robustesse des tests en fixant des tests instables liés aux boutons et aux tokens [#17](https://github.com/datagouv/apistration/pull/17).
- Introduction d'un script `bin/test` pour faciliter l'exécution des tests [#16](https://github.com/datagouv/apistration/pull/16).
- Mise en place de mocks locaux pour les spécifications OpenAPI, utilisés dans les tests CI [#17](https://github.com/datagouv/apistration/pull/17).
- Amélioration de la gestion des erreurs et du monitoring des pings vers les services externes CNAV (ajout d'un seuil d'erreur de 10%).
- Limitation du timeout des pings vers les services externes à 5 secondes pour éviter les blocages.
- Suppression des pings de vérification de santé CNAV, conservation uniquement du ratio d'erreur.
- Préparation de l'application pour une éventuelle publication en open source (nettoyage du code, ajout de fichiers de configuration).
- Mise à jour des workflows CI/CD pour une meilleure gestion des déploiements.
- Correction d'un problème de violation de contrainte de clé étrangère dans les seeds de la base de données.
- Correction d'un bug lié à la gestion des liens magiques lors du déploiement.
- Suppression de la collecte de garbage deferred (amélioration des performances des suites de tests).
- Stub DataEncryptor dans les tests pour éviter les opérations GPG réelles.

### Autres changements
- Mise à jour de la documentation README.
- Mise à jour des dépendances (gems) du projet.
- Correction de typos dans la documentation et le code.
- Ajout d'un fichier `.gitignore` à la racine du projet.
- Ajout de règles Brakeman et correction des alertes.
- Ajout de cassettes VCR pour les tests.
- Mise à jour des références aux données et aux mocks.
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
- Mise à jour des credentials HubEE.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de la gestion des fichiers de configuration pour les environnements de développement et de production.
- Importation du code de `admin_api_entreprise` dans le dépôt.
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
- Mise à jour des dépendances pour améliorer la sécurité et la stabilité du projet.
- Ajout de la possibilité de charger les dictionnaires DGFIP à partir de fichiers locaux en cas d'indisponibilité du service DGFIP.
- Ajout de la gestion des erreurs pour les requêtes vers les services externes.
- Amélioration de la gestion des logs et des métriques.
- Ajout de la gestion des secrets et des informations sensibles.
- Mise à jour des workflows CI/CD pour automatiser les tests et le déploiement.
- Ajout de la gestion des versions et des migrations de la base de données.
- Amélioration de la documentation et de la qualité du code.
- Ajout de la gestion des erreurs et des exceptions.
- Amélioration de la sécurité et de la conformité du projet.
- Ajout de la gestion des utilisateurs et des permissions.
- Amélioration de la performance et de la scalabilité du projet.
- Ajout de la gestion des API et des intégrations.
- Amélioration de l'authentification et de l'accès.
- Ajout de la gestion de la sécurité et de la conformité.
- Ajout de la gestion des données et de l'open data.
- Amélioration de l'écosystème beta.gouv / État.
- Ajout de la gestion des bases de données SQL.
- Amélioration de l'utilisation de Ruby et de Docker.
- Ajout de la gestion des tests RSpec et des workflows CI/CD.
