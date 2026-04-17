## Changelog : apistration (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse de l'application, la gestion des configurations et des secrets, l'ajout d'une nouvelle fonctionnalité d'annonces sur le site, et la préparation à une publication open source de la partie SIADE. Des corrections de bugs et des mises à jour de documentation ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'une bannière d'annonce pour communiquer des maintenances ou des informations importantes sur le site. [#33](https://github.com/datagouv/apistration/pull/33)
- Intégration du régime de pensionnat dans l'API d'inscription des élèves (V5). [#13](https://github.com/datagouv/apistration/pull/13)
- Mise à jour des données CNAV pour l'année 2026.
- Ajout de nouveaux endpoints pour l'API AEEH. [#2139](https://github.com/datagouv/apistration/pull/2139)
- Amélioration de la documentation pour l'API AEEH.

### Évolutions techniques
- Refactorisation de la gestion de la configuration pour une meilleure performance et éviter les erreurs liées aux descripteurs de fichiers ouverts. [#27](https://github.com/datagouv/apistration/pull/27)
- Centralisation des fichiers de configuration et des mocks dans un dépôt "commons" pour faciliter la réutilisation et la maintenance. [#19](https://github.com/datagouv/apistration/pull/19)
- Utilisation locale des fichiers OpenAPI pour les mocks en CI.
- Amélioration de la robustesse des tests en gelant le temps autour des actions et en liant le wizard au token résolu.
- Mise en place d'un système d'expansion pour les configurations communes.
- Refonte de la gestion des identifiants sensibles (credentials) avec un passage à des fichiers YAML en clair et une gestion spécifique pour l'environnement de staging. [#4](https://github.com/datagouv/apistration/pull/4), [#6](https://github.com/datagouv/apistration/pull/6)
- Introduction d'un script `bin/test` pour simplifier l'exécution des tests. [#16](https://github.com/datagouv/apistration/pull/16)
- Préparation du code pour une publication open source de la partie SIADE.
- Suppression de la collection de garbage pour améliorer la performance des suites de tests.
- Utilisation de stubs pour l'encryptor de données dans les tests.
- Mise à jour des dépendances (Rubocop, Rack, Activestorage, bcrypt, etc.).
- Amélioration de la configuration CI/CD.

### Autres changements
- Mise à jour du README avec des informations plus précises.
- Ajout d'un cooldown de 7 jours pour les mises à jour de dépendances via Dependabot. [#28](https://github.com/datagouv/apistration/pull/28)
- Correction de bugs mineurs liés à l'affichage de jetons et à la gestion des anciens endpoints MEN.
- Mise à jour des URLs de référence vers le dépôt `datagouv/apistration`.
- Correction de bugs dans le sitemap.
- Ajout de cassettes VCR pour la suite de tests.
- Suppression de fichiers de configuration inutiles.
- Amélioration de la documentation et des messages d'erreur.
- Correction de problèmes liés à Brakeman et Simplecov.
- Mise à jour des informations de contact pour les pings CNETP.
