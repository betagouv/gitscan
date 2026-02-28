## Changelog : rag-facile (30 derniers jours)

### Résumé
Les 30 derniers jours ont été marqués par une refonte importante de l'architecture du projet, avec un passage à une structure modulaire et l'introduction d'un système de configuration plus flexible. De nouvelles fonctionnalités ont été ajoutées, notamment un système de compétences (skills) pour l'agent conversationnel, une gestion de la mémoire de session basée sur Git, et des outils pour l'intégration de documents PDF. L'expérience utilisateur a également été améliorée avec l'ajout d'une interface plus conviviale et des messages d'erreur plus clairs.

### Évolutions fonctionnelles
- Ajout d'un système de compétences (skills) pour l'agent conversationnel, avec 5 compétences intégrées et une intégration avec `npx skills`.
- Implémentation d'une mémoire de session basée sur Git, permettant de conserver l'historique des conversations et de les synchroniser avec un dépôt Git.
- Ajout d'un système de configuration flexible avec la possibilité de définir des presets et de gérer la configuration via un fichier `ragfacile.toml`.
- Intégration de documents PDF avec la possibilité de les uploader et de les utiliser comme source de connaissances pour l'agent conversationnel.
- Ajout d'un nouveau flux d'installation guidé pour simplifier la configuration initiale.
- Ajout d'un outil pour générer des ensembles de données synthétiques pour l'évaluation du système.
- Ajout d'un thème DSFR (Design Système des Administrations Françaises) pour l'interface utilisateur.
- Possibilité d'utiliser des modèles Albert via l'API Albert.
- Ajout d'un outil pour afficher la configuration actuelle du système.
- Ajout d'un système de gestion des collections de documents.
- Ajout d'une fonctionnalité de recherche de documents avec des filtres avancés.
- Ajout d'un outil pour générer des projets avec une structure de base préconfigurée.

### Évolutions techniques
- Refonte de l'architecture du projet pour une meilleure modularité et maintenabilité.
- Passage à une structure de projet basée sur des packages distincts pour chaque fonctionnalité.
- Utilisation de `just` pour la gestion des tâches et des commandes.
- Amélioration de la gestion des dépendances avec `uv`.
- Ajout de tests unitaires pour valider le bon fonctionnement des différentes fonctionnalités.
- Amélioration de la documentation avec des guides d'utilisation et des exemples de code.
- Intégration de `release-please` pour automatiser le processus de publication.
- Utilisation de `moon` pour la gestion des templates et la génération de projets.
- Ajout de workflows CI/CD pour automatiser les tests et le déploiement.
- Mise à jour des dépendances vers les dernières versions stables.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de logs plus détaillés pour faciliter le débogage.

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés au projet.
- Ajout d'un fichier `CONTRIBUTING.md` pour encourager la contribution de la communauté.
- Correction de bugs et amélioration de la stabilité du système.
- Ajout d'un fichier `CHANGELOG.md` pour suivre l'évolution du projet.
- Amélioration de la lisibilité du code et respect des conventions de style.
- Ajout de commentaires pour expliquer le fonctionnement du code.
- Suppression de code obsolète et simplification de la structure du projet.
- Ajout de badges pour indiquer l'état du projet (version, couverture de test, etc.).
- Ajout de support pour l'utilisation de variables d'environnement.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de tests unitaires pour valider le bon fonctionnement des différentes fonctionnalités.
