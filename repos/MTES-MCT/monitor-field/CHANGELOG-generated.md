## Changelog : monitor-field (30 derniers jours, au 05/08/2026)

### Résumé
L'application a franchi une étape majeure avec l'implémentation de la consultation des zones de réglementation de la pêche. L'expérience utilisateur a été enrichie par des fonctions de recherche et de navigation cartographique, tandis que l'infrastructure de développement a été considérablement renforcée pour garantir la qualité du code et automatiser les déploiements.

### Évolutions fonctionnelles
- **Consultation des zones réglementaires** : possibilité de consulter la liste des zones et d'afficher leurs détails en cliquant sur la carte ou sur la liste [#1](https://github.com/MTES-MCT/monitor-field/pull/1).
- **Recherche textuelle** : ajout d'une fonction de recherche par nom pour retrouver rapidement une zone réglementaire [#21](https://github.com/MTES-MCT/monitor-field/pull/21).
- **Navigation cartographique améliorée** : ajout de fonctions de zoom automatique sur une zone et d'un mode d'affichage isolé.
- **Gestion de la localisation** : suivi de l'état du GPS de l'utilisateur pour s'assurer que la localisation est active pendant l'utilisation.
- **Identité visuelle et ergonomie** : intégration d'un écran de démarrage (splash screen), d'icônes d'application adaptatives et ajout de boutons de fermeture sur les fenêtres modales.

### Évolutions techniques
- **Automatisation des déploiements (CI/CD)** : mise en place de workflows pour la génération de builds Android (environnements de développement et de preview) via EAS et GitHub Actions.
- **Qualité et fiabilité du code** : intégration de SonarQube et Codecov pour le suivi de la qualité, et ajout de tests de type automatiques dans le workflow de validation.
- **Optimisation du workflow de développement** : mise en place de `Husky` pour les pré-commit hooks et migration du linting vers `oxlint` pour plus de rapidité.
- **Validation des données** : utilisation de `Zod` pour sécuriser la structure des données relatives aux zones réglementaires.

### Autres changements
- **Documentation** : mise à jour du fichier README et des scripts de commande du projet.
- **Maintenance** : nettoyage et mise à jour des configurations techniques (TypeScript, Jest, et fichiers de configuration de linting).
