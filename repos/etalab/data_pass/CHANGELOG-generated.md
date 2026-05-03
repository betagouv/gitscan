## Changelog : data_pass (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de fonctionnalités pour les demandes DGFIP, la gestion des droits utilisateurs et la simplification de l'interface. Des corrections de bugs et des optimisations de performance ont également été apportées. L'API s'enrichit de nouvelles fonctionnalités pour la création et la mise à jour de demandes.

### Évolutions fonctionnelles
- Ajout d'une bannière de maintenance ProConnect visible sur toutes les pages.
- Amélioration de l'affichage du statut des demandes ("revendiqué" ou "non revendiqué").
- Suppression du compteur de longlet "Demandes" pour les instructeurs.
- Simplification de l'affichage des scopes sans groupes dans le formulaire.
- Ajout d'un lien vers la création d'une demande dans la liste des demandes.
- Amélioration de la gestion des CGU pour les types d'habilitation dynamiques.
- Ajout d'un lien vers le formulaire de création d'habilitation dynamique.
- Mise à jour des libellés liés à la tarification Eaje.
- Possibilité de retirer complètement les droits d'un utilisateur.
- Ajout d'informations sur les services CISIRH et mise à jour des scopes associés.
- Amélioration de l'affichage des erreurs de vérification d'email lors de la soumission.
- Ajout d'emails spécifiques pour les approbations DGFIP.
- Amélioration de l'affichage des identifiants d'habilitation dans les routes.
- Ajout de la possibilité de bannir un utilisateur via l'interface d'administration.
- Ajout d'une raison au bannissement d'un utilisateur.
- Amélioration de la gestion des erreurs lors de la soumission de demandes.
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API.

### Évolutions techniques
- Refactorisation du code pour simplifier la gestion des événements et des diffs.
- Introduction d'un service singleton `AnnouncementBanner` pour gérer la bannière de maintenance.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout d'une page de documentation pour les webhooks.
- Ajout d'un service `MarkdownRenderer` pour le rendu du Markdown.
- Mise à jour des dépendances (Rubocop, Yard, Zlib, Rack-Session, Openapi_first).
- Optimisation des tests CI/CD (parallélisation, suppression de dépendances Docker).
- Amélioration de la gestion des requêtes N+1 sur le dashboard demandeur.
- Ajout d'interacteurs et d'organizers pour l'API write.
- Documentation des scopes OAuth2 par endpoint dans l'OpenAPI.
- Ajout d'événements `create_by_api` et `update_by_api`.
- Amélioration de la gestion des slugs.
- Ajout de tests contractuels.
- Migration des tables rails_pulse et lazy_load faker.

### Autres changements
- Mise à jour de la documentation des rôles.
- Correction de typos dans les sujets des emails.
- Ajout de guidelines pour l'utilisation de CLAUDE pour la co-authoring des commits.
- Clarification du message d'erreur de `SkipLinksImplementedChecker`.
- Ajout d'instructions pour arrêter le remplacement des apostrophes par des guillemets simples dans les tests.
- Suppression de code inutile et nettoyage général du code.
- Correction de bugs mineurs et améliorations de la stabilité.
- Mise à jour de la documentation.
- Ajout de commentaires et de documentation au code.
