## Changelog : domifa (30 derniers jours, au 12 juin 2026)

### Résumé
Cette période a été marquée par de nombreuses corrections de bugs et améliorations de la sécurité, notamment autour de l'authentification (ajout de l'OTP) et de la gestion des utilisateurs. Des améliorations ont également été apportées à la journalisation et à la gestion des erreurs pour faciliter le diagnostic et la résolution des problèmes. Enfin, une mise à jour majeure des dépendances Angular a été effectuée.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer des utilisateurs dans l'interface d'administration.
- Implémentation de l'authentification à deux facteurs (OTP) pour une sécurité renforcée.
- Ajout de la possibilité de renvoyer un OTP.
- Ajout de statistiques sur les sessions utilisateurs.
- Ajout de la possibilité de débloquer des utilisateurs.
- Amélioration de la recherche et des filtres dans l'interface d'administration.
- Ajout de la possibilité de délier un compte Brevo.

### Évolutions techniques
- Mise à jour de la version d'Angular à la v19 sur l'ensemble des frontends.
- Amélioration de la journalisation (logs) pour faciliter le débogage et le suivi des événements.
- Ajout de filtres d'exceptions pour une meilleure gestion des erreurs.
- Refactorisation de la gestion des logs pour la sécurité et l'ajout d'un délai de 30 minutes pour l'OTP.
- Amélioration de la gestion des tests unitaires.
- Suppression de la "fabrique social" du backend.
- Ajout de tests unitaires pour l'OTP.
- Suppression de code obsolète et nettoyage général du code.

### Autres changements
- Correction de problèmes liés à l'affichage de l'agent utilisateur.
- Correction de problèmes liés aux alertes par email.
- Correction de problèmes liés à la gestion des utilisateurs bloqués.
- Correction de problèmes de construction de l'application frontend.
- Correction de problèmes d'affichage des caractères spéciaux (@) dans le frontend.
- Correction de problèmes liés au bouton de validation OTP.
- Correction de problèmes de typage dans le backend.
- Correction de problèmes liés aux logs pour les connexions inconnues.
- Mise à jour des dépendances et des configurations de sécurité.
- Ajout de titres et de pages pour améliorer l'expérience utilisateur.
- Amélioration de la gestion des erreurs 401.
- Ajout de labels d'action pour une meilleure identification des événements.
- Ajout d'une structure de logs plus claire.
- Correction de problèmes liés aux tests de bout en bout.
- Ajout de la possibilité de réinitialiser l'OTP.
- Correction de problèmes liés au chargement des utilisateurs.
- Correction de problèmes de linting et de composants autonomes dans l'administration.
- Amélioration de la gestion des limites de throttling.
- Ajout de la possibilité de consulter les statistiques des sessions.
- Correction de problèmes liés à la suppression d'utilisateurs.
- Ajout de la possibilité de consulter les alertes de sécurité.
- Correction de problèmes liés à l'affichage des titres et des pages.
- Correction de problèmes liés au fonctionnement des dropdowns et des listes dans l'interface d'administration.
- Ajout d'un identifiant unique (UUID) aux endpoints de la structure.
- Correction d'une potentielle vulnérabilité de type "Type confusion through parameter tampering" identifiée par CodeQL.
