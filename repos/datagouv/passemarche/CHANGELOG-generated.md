## Changelog : passemarche (30 derniers jours, au 9 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience d'authentification et de gestion des lots pour les marchés publics. Des corrections de bugs et des améliorations de la sécurité ont également été apportées, notamment concernant la génération de PDF et la gestion des environnements. L'ajout de catégories et sous-catégories permet une meilleure organisation des données.

### Évolutions fonctionnelles
- **Authentification :** Amélioration du flux d'authentification avec la prise en charge de la reconnexion via magic link, et la pré-remplissage automatique de l'email lors de la connexion.
- **Gestion des lots :** Possibilité de gérer plusieurs lots lors de la création d'un marché public. L'interface a été mise à jour pour refléter cette nouvelle fonctionnalité.
- **Catégories et sous-catégories :** Ajout de la possibilité de créer des catégories et sous-catégories depuis l'interface d'administration.
- **Motifs d'exclusion :** Amélioration de la formulation des motifs d'exclusion et ajout de liens vers des articles explicatifs.
- **Sécurité PDF :** Ajout d'un filigrane et d'une bannière d'environnement sur les PDF générés en dehors de la production.
- **Environnements :** Affichage clair de l'environnement (développement, staging, production) dans l'interface utilisateur.

### Évolutions techniques
- **Refactoring de la validation SIRET :** La validation du SIRET a été transformée en interactor pour une meilleure organisation du code.
- **Migration vers ActionMailer :** Remplacement de l'API Brevo par ActionMailer pour l'envoi d'emails, facilitant les tests et le développement.
- **Amélioration de la gestion des erreurs :** Normalisation de la structure des erreurs pour une meilleure gestion et affichage.
- **Correction de problèmes de concurrence :** Résolution d'un problème de concurrence lors de la mise à jour des réponses.
- **Mise à jour des dépendances :** Mises à jour de plusieurs dépendances, notamment Rails, Pagy, RSpec et Cucumber.
- **Refactoring du code d'authentification :** Introduction d'un `Candidate::Authentication` concern et d'un `Candidate::SessionsController` pour une meilleure organisation du code d'authentification.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et modifications.
- **Tests :** Ajout et mise à jour de tests unitaires et fonctionnels pour garantir la qualité du code.
- **Configuration :** Mise à jour des informations d'identification pour les environnements de test (sandbox et staging).
- **Nettoyage du code :** Suppression de code obsolète et amélioration de la lisibilité du code.
