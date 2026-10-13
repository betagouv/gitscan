## Changelog : people (30 derniers jours, au 12 octobre 2026)

### Résumé
Cette période est marquée par une simplification majeure du système d'authentification et un renforcement de la sécurité, notamment sur la gestion des domaines et la protection des accès. L'accent a également été mis sur la modernisation des outils de développement et de la chaîne de déploiement.

### Évolutions fonctionnelles
- **Sécurité des domaines** : Renforcement de la validation des domaines d'e-mail des organisations pour garantir une correspondance exacte.
- **Gestion des permissions** : Restriction de la visibilité de la configuration des domaines pour les utilisateurs disposant uniquement d'un droit de lecture.

### Évolutions techniques
- **Simplification de l'authentification** : Suppression des fonctionnalités liées à OAuth2 et aux fournisseurs d'identité (IdP), incluant le nettoyage des tables de base de données associées.
- **Qualité du code (Frontend)** : Migration vers ESLint 9 et transformation de la configuration de linting en plugin pour une meilleure gestion des règles de développement.
- **CI/CD** : Mise à jour de l'ensemble des GitHub Actions (checkout, setup-python, setup-node, cache, upload-artifact) pour optimiser les pipelines.
- **Sécurité** : Mise à jour de la bibliothèque `urllib3` pour corriger des vulnérabilités.

### Autres changements
- **Internationalisation** : Mise à jour des chaînes de caractères traduites.
- **Maintenance et configuration** : Mise à jour des configurations des applications (desk, i18n, e2e) et nettoyage de variables pour respecter les standards Sonar.
- **Release** : Publication de la version 1.26.1.
