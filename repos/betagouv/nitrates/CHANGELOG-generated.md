## Changelog : nitrates (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, le projet nitrates a connu une évolution majeure avec l'implémentation d'un éditeur YAML pour la configuration des règles, permettant une gestion plus flexible et intuitive.  Des améliorations significatives ont également été apportées à l'importation de données (zones vulnérables et RPG), à l'interface utilisateur (validation, cartographie) et à l'intégration avec ProConnect pour l'authentification.  Enfin, des corrections de bugs et des optimisations ont été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Éditeur YAML :** Implémentation d'un éditeur YAML en ligne pour la configuration des règles, incluant l'édition, la suppression, l'annulation et le verrouillage pour la gestion de la concurrence. [#28](https://github.com/betagouv/nitrates/issues/28)
- **Authentification ProConnect :** Intégration de l'authentification via ProConnect, avec une page de connexion dédiée et une gestion des erreurs améliorée.
- **Importation de données :** Amélioration de l'importation des zones vulnérables (ZV) et des référentiels parcellaire (RPG) depuis des sources externes.
- **Interface de validation :** Refonte de l'interface de validation manuelle des règles, avec une présentation plus claire des informations et des fonctionnalités de recherche améliorées.
- **Cartographie :** Amélioration de l'affichage des données cartographiques, avec la possibilité d'afficher les zones vulnérables et les RPG en superposition.
- **Simulation :** Ajout d'une vue simulateur avec un formulaire HTML brut et un affichage des résultats.
- **Gestion des brouillons :**  Possibilité de créer, renommer et archiver des brouillons de configurations.
- **Aide contextuelle :** Ajout d'une aide contextuelle pour les champs de formulaire.

### Évolutions techniques
- **Refactorisation du code :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
- **Mise à jour des dépendances :** Mise à jour de plusieurs dépendances, notamment `ruamel.yaml` et `Pygments`.
- **Docker :** Correction d'un problème de build Docker pour les architectures ARM64.
- **Tests :** Ajout de tests fonctionnels (Playwright) et de tests d'intégration.
- **CI/CD :** Amélioration des workflows CI/CD pour automatiser les tests et le déploiement.
- **Configuration :**  Amélioration de la gestion de la configuration, notamment avec l'ajout de variables d'environnement.
- **Sécurité :** Ajout d'une politique de sécurité de contenu (CSP) plus restrictive.
- **Base de données :** Optimisation des requêtes à la base de données.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements récents.
- **Nettoyage du code :** Suppression de code obsolète et amélioration de la qualité du code.
- **Amélioration des messages d'erreur :** Amélioration des messages d'erreur pour faciliter le débogage.
- **Correction de bugs :** Correction de plusieurs bugs mineurs.
- **Ajout de commentaires :** Ajout de commentaires pour améliorer la compréhension du code.
- **Suppression de code redondant :** Suppression de code redondant pour simplifier le code.
