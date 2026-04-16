## Changelog : people (30 derniers jours, au 15 avril 2026)

### Résumé
Les dernières mises à jour de People se concentrent sur l'amélioration de l'expérience utilisateur, notamment en clarifiant les messages d'erreur et en ajustant le comportement de redirection. Des corrections de bugs ont également été apportées pour assurer la stabilité et la fiabilité de l'application, ainsi que des améliorations de sécurité avec la mise à jour de plusieurs dépendances.

### Évolutions fonctionnelles
- Amélioration du message d'erreur affiché lorsqu'il n'y a pas d'adresse email secondaire associée à une boîte aux lettres. [#1108](https://github.com/suitenumerique/people/issues/1108)
- Amélioration du message affiché lorsqu'il n'y a pas d'alias sur la page de domaine.
- Priorisation des domaines de messagerie comme page d'atterrissage par défaut après la redirection.
- Export des informations de contact du domaine pour l'administration.
- Les tests d'accès via invitation vérifient maintenant que le rôle attendu est bien attribué lors de la création à partir d'une adresse email.
- Mise à jour du logo dans le modèle d'email d'invitation. [#1085](https://github.com/suitenumerique/people/issues/1085)

### Évolutions techniques
- Mise à jour de Pillow à la version 12.2.0 pour des raisons de sécurité.
- Refactorisation de l'interface utilisateur avec la nouvelle version du UI Kit (regie v2). [#1083](https://github.com/suitenumerique/people/issues/1083)
- Mise à jour de la configuration de l'interface utilisateur pour la modale de domaine. [#1089](https://github.com/suitenumerique/people/issues/1089)
- Ajout d'une étape de build du frontend lors du bootstrap.
- Correction d'un problème d'importation pour les boîtes aux lettres fonctionnelles.
- Correction du chemin de redirection par défaut pour revenir à `/mail-domains/`.
- Suppression d'une bordure inutile dans l'interface utilisateur. [#1107](https://github.com/suitenumerique/people/issues/1107)

### Autres changements
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité : Django, Next.js, pytest, lodash, requests.
- Mise à jour des chaînes de traduction.
- Publication de la version 1.24.0.
