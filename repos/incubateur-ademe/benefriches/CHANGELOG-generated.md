## Changelog : benefriches (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur la refonte du processus de création de projets, en particulier pour les zones urbaines. De nombreuses améliorations ont été apportées à l'interface utilisateur, à la gestion des données et à l'expérience globale de création de projet. Des corrections de bugs et des optimisations ont également été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout d'une intégration avec Crisp pour l'assistance utilisateur, notamment en cas de problème avec la réception des liens d'authentification.
- Amélioration du processus de création de projets en zone urbaine avec l'ajout de nouvelles étapes : gestion, introduction, espaces vacants, emplois à temps plein, contamination des sols, stockage du carbone dans les sols, et distribution des surfaces.
- Ajout de pictogrammes pour les différents types d'usage dans la création de projets urbains.
- Possibilité de supprimer des projets et leurs impacts directement depuis l'interface.
- Ajout de tests E2E pour la création de sites personnalisés (friches et agricoles).
- Mise à jour de la version de l'API PVGIS.
- Ajout d'un indicateur "projet non modifiable" pour les projets de démonstration.
- Amélioration de la gestion des types de sols et des surfaces dans les formulaires.
- Modification des libellés et de l'ordre des étapes dans le processus de création de projet.
- Ajout d'une option pour sauter certaines étapes de création de projet en fonction du type de site.
- Amélioration de la recherche d'adresse avec une fonction de détection automatique et un délai pour éviter les requêtes excessives.

### Évolutions techniques
- Refactorisation importante du code de création de projet, notamment pour les zones urbaines, avec une meilleure organisation et une séparation des préoccupations.
- Migration de la logique de création de site vers l'API pour une meilleure cohérence.
- Utilisation du pattern ViewData pour une gestion plus centralisée des données affichées dans l'interface utilisateur.
- Amélioration de la gestion des états avec Redux et l'utilisation de sélecteurs typés.
- Mise à jour des dépendances (NestJS, oxlint, prettier, pnpm).
- Amélioration des tests E2E avec l'ajout de nouvelles assertions et la correction de problèmes de concurrence.
- Amélioration de l'infrastructure CI/CD avec la configuration des variables d'environnement et la simplification des scripts.
- Mise en place d'un système de gestion des décisions d'architecture (ADR).
- Refonte de l'organisation des dossiers et des fichiers pour une meilleure maintenabilité.

### Autres changements
- Documentation : Mise à jour de la documentation interne (CLAUDE.md) pour refléter les changements apportés au code et à l'architecture.
- Nettoyage du code et suppression du code mort.
- Amélioration des messages d'erreur et des indications pour l'utilisateur.
- Correction de problèmes de configuration et de dépendances.
- Ajout d'un script pour faciliter la création d'environnements de travail locaux.
- Correction de problèmes de performance et de stabilité.
- Mise à jour des scripts de déploiement.
- Ajout d'un skill pour la planification de features.
- Correction de la configuration du Content Security Policy (CSP) pour autoriser les domaines de Crisp.
