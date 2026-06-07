## Changelog : api-engagement (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur de la plateforme et de l'API, notamment en matière d'accessibilité, de gestion des formulaires et de robustesse. Des améliorations techniques ont également été apportées pour optimiser la gestion des règles de diffusion, la gestion des erreurs et la sécurité.

### Évolutions fonctionnelles
- **Plateforme :** Refonte des sections d'accueil et des témoignages pour une meilleure présentation. Amélioration de l'interface utilisateur du quiz et des missions sur la plateforme.
- **Formulaires :** Amélioration de la gestion des champs obligatoires et des erreurs dans les formulaires d'authentification et de compte. Regroupement des champs de formulaire associés pour une meilleure lisibilité. Ajout d'attributs d'autocomplétion aux formulaires d'authentification et de compte.
- **Accessibilité :** Amélioration de l'accessibilité de la carte des missions, de la barre de progression du quiz, des champs de formulaire et des dialogues pour les utilisateurs ayant des besoins spécifiques.
- **API :** Ajout d'une file d'attente de lettres mortes pour améliorer la robustesse de l'API. Amélioration de la gestion des erreurs lors de la mise en file d'attente des missions.
- **Plateforme :** Amélioration de la page de détails des missions.

### Évolutions techniques
- **API :** Remplacement du système d'exclusion de diffusion par un moteur basé sur des règles, offrant une plus grande flexibilité.
- **Infrastructure :** Configuration de Typesense pour l'environnement de production.
- **CI/CD :** Ajout de tests et de workflows de linting pour la plateforme.
- **API :** Implémentation d'une limitation du taux d'accès (rate limiting) basé sur l'adresse IP pour protéger les routes de l'API de la plateforme.
- **API :** Ajout d'index uniques pour optimiser les performances des requêtes.
- **API :** Amélioration de la gestion des journaux d'audit.
- **API :** Amélioration de la gestion des erreurs et de la résilience de l'enrichissement des missions.
- **API :** Suppression d'un ancien modèle de taxonomie.

### Autres changements
- Mise à jour de la documentation.
- Ajout d'un fichier `AGENTS.md` pour documenter les agents.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour des dépendances.
- Ajout de tests pour la plateforme.
- Publication de la spécification OpenAPI.
