## Changelog : domifa (30 derniers jours, au 12 juin 2026)

### Résumé
Cette période a été marquée par de nombreuses corrections et améliorations, notamment concernant la gestion des utilisateurs, la sécurité, et la robustesse de l'application. Des améliorations ont également été apportées à la gestion des logs et des tests. L'authentification a été revue et corrigée.

### Évolutions fonctionnelles
- Ajout de la possibilité de supprimer des utilisateurs dans le backend.
- Amélioration de la gestion des utilisateurs bloqués.
- Ajout de statistiques sur les sessions utilisateurs.
- Intégration de Brevo pour l'envoi d'emails et la gestion des liens de déconnexion.
- Ajout d'un testeur de mails générique.
- Correction de l'affichage de l'agent utilisateur.
- Correction du fonctionnement du mot de passe.
- Correction de la gestion des filtres pour les éléments supprimés.
- Suppression de la fabrique sociale.

### Évolutions techniques
- Amélioration des logs pour la sécurité et le débogage.
- Ajout de tests unitaires et correction de tests existants.
- Refactorisation des logs pour améliorer la lisibilité et la maintenance.
- Mise à jour de la gestion des erreurs avec l'ajout de filtres d'exception.
- Correction de problèmes de typage.
- Amélioration de la gestion des sessions.
- Correction de problèmes liés à l'importation de données.
- Correction de problèmes de construction de l'application frontend.

### Autres changements
- Correction de problèmes de linting.
- Ajout de titres et de pages.
- Correction d'un problème potentiel de sécurité lié à la confusion de type via la manipulation de paramètres (CodeQL).
- Correction de l'affichage de l'arobase dans le frontend.
- Désactivation du bouton dans le processus d'authentification à deux facteurs (OTP).
- Ajout de 30 minutes au délai d'expiration de l'OTP.
- Correction de problèmes liés à l'UUID.
- Ajout de filtres dans l'interface d'administration.
- Correction d'un bug lié à l'affichage de l'agent utilisateur.
- Correction de problèmes de compatibilité avec la production.
- Ajout de statistiques sur les sessions.
