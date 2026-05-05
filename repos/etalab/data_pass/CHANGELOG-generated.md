## Changelog : data_pass (30 derniers jours, au 4 mai 2026)

### Résumé
Ce mois-ci, les évolutions de DataPass se concentrent sur l'amélioration de l'expérience utilisateur, notamment via des corrections de bugs et des ajustements d'interface. Des améliorations techniques ont également été apportées, incluant la gestion des droits utilisateurs, la robustesse du système et l'ajout de fonctionnalités pour l'API.

### Évolutions fonctionnelles
- Ajout d'une bannière de maintenance ProConnect visible sur toutes les pages.
- Amélioration de l'affichage du statut "revendiqué" dans le processus de demande.
- Suppression du compteur de longlet "demandes" pour les instructeurs, simplifiant l'interface.
- Ajout d'un lien vers la création d'une demande dans la liste des demandes.
- Correction de l'affichage du message legacy lors de soumissions modernes.
- Correction d'un bug empêchant l'affichage du bouton "Précédent" sur certaines étapes du wizard.
- Amélioration de la gestion des erreurs lors de la soumission de demandes sans modifications.
- Ajout d'informations sur les services CISIRH et mise à jour des scopes associés.
- Amélioration de l'affichage des scopes pour les habilitations CNAF.
- Correction d'un problème de N+1 queries sur le dashboard demandeur, améliorant les performances.
- Ajout de la possibilité de retirer complètement les droits d'un utilisateur.
- Ajout d'un message d'erreur plus clair en cas d'échec de connexion.
- Amélioration des textes de l'accusé de réception de dépôt de demande.
- Ajout de la possibilité d'exposer le numéro de téléphone de l'applicant via l'API.
- Correction d'un bug empêchant l'affichage correct des scopes boursier MEN sur les formulaires éditeurs CNAF.

### Évolutions techniques
- Refactorisation de la gestion des événements et des changelogs.
- Amélioration de la gestion des rôles et des droits utilisateurs, notamment avec l'introduction de rôles de niveau FD.
- Ajout d'une API pour la création et la mise à jour de demandes.
- Amélioration de la documentation de l'API et ajout d'une section tutoriels.
- Optimisation des tests CI/CD pour réduire le temps d'exécution.
- Mise à jour de plusieurs dépendances (Rubocop, Yard, Rack-Session, etc.).
- Ajout de tests contractuels pour garantir la cohérence des définitions.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de webhooks pour les événements d'organisation.
- Simplification de l'affichage des erreurs dans les emails.
- Utilisation de l'ID formaté au lieu de l'ID brut dans les URLs.

### Autres changements
- Ajout d'un guide de contribution (CLAUDE) pour encourager la collaboration.
- Mise à jour de la documentation des rôles.
- Correction de fautes de frappe et amélioration de la qualité du code.
- Ajout de checks pour forcer la définition du titre de chaque vue.
- Suppression de code inutile et nettoyage général du code.
