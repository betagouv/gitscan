## Changelog : domifa (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions de DomiFa se concentrent sur la correction de bugs et l'amélioration de la sécurité. Des corrections ont été apportées concernant l'authentification, la gestion des téléchargements, la gestion des utilisateurs bloqués et des vulnérabilités potentielles. Des améliorations de la journalisation et de la surveillance ont également été implémentées.

### Évolutions fonctionnelles
- Correction d'un bug concernant la réponse "autre" dans le backend.
- Suppression de la possibilité d'éditer les utilisateurs bloqués dans l'interface.
- Amélioration de la gestion des téléchargements avec l'ajout d'un blocage.
- Ajout de statistiques de session pour une meilleure surveillance.
- Ajout de la possibilité de supprimer des utilisateurs.

### Évolutions techniques
- Correction de vulnérabilités potentielles liées à la confusion de type via la manipulation de paramètres.
- Ajout de filtres pour les utilisateurs supprimés.
- Suppression de la fabrique sociale.
- Amélioration de la gestion des erreurs avec l'ajout de filtres d'exception.
- Ajout de logs pour les téléchargements et les tentatives de connexion inconnues.
- Mise à jour de la gestion des agents utilisateurs.
- Refactorisation des logs pour la sécurité et ajout d'un délai de 30 minutes pour les OTP.
- Intégration de Brevo pour la gestion des emails et la possibilité de se désinscrire.
- Amélioration de la gestion des sessions.

### Autres changements
- Correction de divers problèmes de linting.
- Mise à jour des tests unitaires.
- Amélioration de la page de titre et des titres.
- Ajout d'un testeur d'emails génériques.
- Correction de problèmes de typage.
- Correction de bugs dans la construction de l'application frontend.
- Correction d'un problème d'affichage de l'arobase dans le frontend.
- Désactivation du bouton dans le processus OTP.
- Correction d'un bug lié à l'importation.
- Ajout de filtres dans l'interface d'administration.
- Correction d'un problème de filtre HTTP.
- Ajout d'un test pour la gestion des mots de passe.
