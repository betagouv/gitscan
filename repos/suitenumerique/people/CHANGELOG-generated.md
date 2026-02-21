## Changelog : people (30 derniers jours)

### Résumé
Les dernières mises à jour de l'application "people" se concentrent sur l'amélioration de la gestion des invitations, des alias et de la sécurité. Des corrections de bugs ont été apportées pour améliorer la stabilité et l'expérience utilisateur, notamment en lien avec l'importation de données depuis Dimail et la gestion des erreurs. Des mises à jour de dépendances ont également été effectuées pour corriger des vulnérabilités de sécurité.

### Évolutions fonctionnelles
- Possibilité de supprimer les invitations par un administrateur (#1052).
- Ajout d'une icône au bouton de configuration de domaine (#1054).
- Affichage des invitations liées aux domaines dans l'interface (#1040).
- Possibilité de supprimer les invitations de domaine.
- Les alias peuvent maintenant avoir une destination "devnull@devnull" (#1029).
- Le premier utilisateur créé n'est plus automatiquement administrateur (#776).
- Ajout de l'affichage des alias dans la démo.
- Comptabilisation des alias dans l'endpoint des statistiques.

### Évolutions techniques
- Migration de l'outil de gestion des dépendances de `pip` à `uv`.
- Mise à jour de la version de Python à 3.14.2.
- Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité : Django (v5.2.11), Pillow, Cryptography, lodash et next (v15.5.10).
- Déplacement de l'exception liée aux invitations vers le core.
- Simplification des tests liés aux invitations par email.

### Autres changements
- Mise à jour des chaînes de traduction.
- Publication des versions 1.23.1, 1.23.0 et 1.22.1.
- Correction de warnings linter.
- Suppression d'un commentaire inutile dans le fichier des permissions.
- Correction d'un job d'upload Crowdin.
