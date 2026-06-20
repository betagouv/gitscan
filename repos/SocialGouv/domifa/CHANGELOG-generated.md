## Changelog : domifa (30 derniers jours, au 12 juin 2026)

### Résumé
Cette période a été marquée par de nombreuses corrections de bugs et améliorations de la sécurité, notamment l'ajout de l'authentification à deux facteurs (OTP) et des améliorations de la gestion des logs et de la sécurité. Des corrections ont également été apportées à l'import de données, à l'interface utilisateur et à la gestion des utilisateurs.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (OTP) pour la connexion des utilisateurs.
- Possibilité de renvoyer un code OTP.
- Ajout de la suppression de comptes utilisateurs (via [#4152](https://github.com/SocialGouv/domifa/issues/4152)).
- Ajout de statistiques sur les sessions utilisateurs.
- Ajout de la possibilité de débloquer les utilisateurs bloqués.
- Ajout de filtres à l'interface d'administration pour faciliter la recherche et la gestion des données.

### Évolutions techniques
- Amélioration de la gestion des logs pour une meilleure traçabilité et détection des problèmes.
- Refonte de la gestion des sessions et ajout de vues de sécurité.
- Mise en place d'un testeur de mails génériques.
- Correction de problèmes de typage dans le code.
- Suppression de la fabrique sociale.
- Ajout de tests unitaires et corrections des tests existants.
- Amélioration de la sécurité avec la correction d'une potentielle vulnérabilité CodeQL.
- Ajout de la gestion de Brevo (anciennement Sendinblue) pour l'envoi d'emails et la possibilité de se désinscrire.

### Autres changements
- Mise à jour de la documentation et des titres/pages.
- Correction de problèmes de build de l'application frontend.
- Correction de l'affichage de l'agent utilisateur.
- Nettoyage du code et correction de problèmes de linting.
- Ajout de filtres pour les éléments supprimés.
- Amélioration de la gestion des erreurs et des exceptions.
- Correction de problèmes liés aux caractères spéciaux (@) dans l'interface utilisateur.
- Désactivation du bouton pendant l'envoi du code OTP.
- Ajout de l'UUID.
- Ajout de la structure des logs.
- Correction de tests end-to-end.
