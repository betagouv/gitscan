## Changelog : people (30 derniers jours)

### Résumé
Les dernières mises à jour de l'application "people" se concentrent sur l'amélioration de la gestion des invitations, des domaines et des alias, ainsi que sur la correction de vulnérabilités de sécurité et l'amélioration de la stabilité générale. Des améliorations de l'interface utilisateur ont également été apportées, notamment l'ajout d'icônes et la gestion des invitations.

### Évolutions fonctionnelles
- Possibilité de supprimer les invitations par un administrateur (#1052).
- Ajout d'une icône au bouton de configuration d'un domaine (#1054).
- Possibilité de supprimer les invitations de domaine.
- Ajout de l'affichage des invitations liées aux domaines dans l'interface utilisateur (#1040).
- Comptabilisation des alias dans l'endpoint de statistiques.
- Ajout des alias à la démo.
- Possibilité de supprimer les invitations de domaine.
- Amélioration de la gestion des erreurs lors de la synchronisation des boîtes aux lettres avec Dimail.

### Évolutions techniques
- Migration de l'outil de gestion des dépendances de `pip` à `uv`.
- Mise à jour de la version de Python à 3.14.2.
- Mise à jour de Django à la version 5.2.11 (correction de vulnérabilités).
- Mise à jour de la librairie `lodash` à la version 4.17.23 (correction de vulnérabilités).
- Mise à jour de la librairie `pillow` et `cryptography` pour corriger des CVEs.
- Mise à jour de `next` à la version 15.5.10 (correction de vulnérabilités).
- Déplacement des exceptions liées aux invitations vers le cœur de l'application.
- Simplification des tests liés aux invitations de domaine par email.

### Autres changements
- Mise à jour des chaînes de traduction (i18n).
- Correction de warnings linter.
- Publication des versions 1.23.1, 1.23.0 et 1.22.2.
