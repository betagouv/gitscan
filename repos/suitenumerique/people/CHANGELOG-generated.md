## Changelog : people (30 derniers jours)

### Résumé
Les dernières mises à jour de l'application people se concentrent sur l'amélioration de la gestion des invitations, des alias et des domaines, ainsi que sur la correction de vulnérabilités de sécurité et l'optimisation des performances. Des améliorations de l'interface utilisateur ont également été apportées, notamment l'ajout d'icônes et la correction de problèmes de pagination.

### Évolutions fonctionnelles
- Possibilité de supprimer les invitations par un administrateur (#1052).
- Ajout d'une icône au bouton de configuration d'un domaine (#1054).
- Affichage des invitations liées aux domaines dans l'interface (#1040).
- Comptabilisation des alias dans l'endpoint de statistiques.
- Ajout des alias à la démo.
- Possibilité de supprimer les invitations expirées.
- Gestion des alias : création, suppression et affichage.
- Importation des alias existants depuis Dimail.
- Synchronisation du mot de passe des nouvelles boîtes aux lettres avec Dimail.

### Évolutions techniques
- Mise à jour de Python à la version 3.14.2.
- Migration de l'outil de gestion des dépendances de pip à uv.
- Mise à jour des dépendances Python pour corriger des vulnérabilités de sécurité (pillow, cryptography, django, next).
- Déplacement des exceptions liées aux invitations vers le cœur de l'application.
- Simplification des tests liés aux invitations par email.
- Correction d'une tentative d'envoi d'invitations à des utilisateurs existants.

### Autres changements
- Correction de warnings linter.
- Mise à jour des chaînes de traduction.
- Correction d'un job d'upload Crowdin.
- Ignorer la casse lors de la recherche d'emails existants (#1056).
- Correction d'un bug lié à la pagination des domaines dans l'interface (#950, #946).
