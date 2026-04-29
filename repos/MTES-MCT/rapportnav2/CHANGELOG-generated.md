## Changelog : rapportnav2 (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions de rapportnav2 se concentrent sur l'ajout de nouvelles fonctionnalités, notamment la gestion des criées, l'intégration d'un service d'adresse et des améliorations de la gestion des infractions. Des corrections de bugs et des mises à jour de sécurité ont également été apportées pour améliorer la stabilité et la sécurité de l'application.

### Évolutions fonctionnelles
- Ajout de la gestion des criées avec une liste, des endpoints associés et un panneau d'administration.
- Intégration d'un service d'adresse provenant de data.gouv.fr avec une fonctionnalité d'autocomplétion dans l'interface utilisateur.
- Amélioration de la gestion des infractions lors de la création de nouveaux contrôles.
- Mise à jour de la règle AEM 4.1.3.
- Ajout de la possibilité de récupérer les SATI avec un retour possible de null.
- Implémentation de cas d'utilisation pour la gestion des SATI (GET/PUT).
- Ajout d'attributs avec code pays pour les SATI.
- Ajout d'un listener sur les modèles de données.

### Évolutions techniques
- Refonte de la configuration de release-please pour optimiser le processus de publication.
- Mise à jour de Spring Boot.
- Amélioration de la validation des schémas pour les contrôles nautiques et de loisirs.
- Mise à jour de la dépendance `tools.jackson.core:jackson-core`.
- Correction d'une boucle infinie causée par `isLoggedIn` dans `use-auth.ts`.
- Correction d'un problème de cache HTML avec CSP.
- Mise à jour de la dépendance `monitor-ui`.
- Correction de l'utilisation de l'API d'établissement en cas d'absence d'adresse.
- Amélioration de l'architecture hexagonale pour les Vessels.
- Ajout de stubs de ports.
- Ajout de cache pour la configuration de Caffeine.
- Utilisation du hash de commit au lieu du tag pour une meilleure sécurité.
- Correction de problèmes de validation de schéma.

### Autres changements
- Ajout d'un fichier `.trivyignore.yml` pour ignorer certains résultats de l'analyse de vulnérabilités Trivy.
- Correction de problèmes de sécurité identifiés par Snyk dans les dépendances frontend.
- Mise à jour des snapshots de tests.
- Désactivation temporaire de Trivy.
- Mise à jour de la documentation.
- Correction de problèmes liés à l'environnement InfractionEnvEntity.
- Suppression de valeurs codées en dur pour le type d'action de pêche (FishActionType).
- Ajout de `compliantSafeManningPermit` au type Control.
