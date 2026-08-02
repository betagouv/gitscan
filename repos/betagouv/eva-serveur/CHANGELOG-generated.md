## Changelog : eva-serveur (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à la gestion des évaluations Evapro, notamment une séparation claire des fonctionnalités et des accès pour les utilisateurs standards et Evapro. L'interface utilisateur a été optimisée pour une meilleure lisibilité et une navigation plus intuitive, avec des corrections de traductions et des ajustements visuels. Des refactorings importants ont été réalisés pour simplifier le code et préparer l'application à de futures évolutions.

### Évolutions fonctionnelles
- Ajout d'un menu "Évaluation" distinct pour les superadmins, avec des sections dédiées à Eva et Evapro.
- Les noms des bénéficiaires des évaluations sont maintenant affichés, permettant une identification plus facile.
- Amélioration de l'affichage des événements et réduction de la largeur des tableaux de campagnes pour une meilleure lisibilité.
- Ajout de l'email et du téléphone de l'accueil dans la page de détails des structures locales.
- Simplification du nom généré pour les campagnes Evapro.
- Correction de la traduction du message d'erreur lors de la génération de PDF.
- Correction du message d'accueil pour les comptes en attente.
- Les utilisateurs Evapro peuvent désormais lancer des campagnes, mais n'y ont pas accès en lecture.
- Restauration de l'accès en lecture aux campagnes Evapro.
- Correction de l'accès aux campagnes Evapro pour les utilisateurs concernés.

### Évolutions techniques
- Refactor important du code lié aux évaluations Evapro, avec création d'un nouveau modèle `EvaluationEva` et de vues dédiées.
- Séparation des traductions Evapro dans un fichier dédié.
- Suppression de code mort et de constantes inutilisées.
- Factorisation de composants réutilisables, notamment pour les barres latérales et les boutons de modales.
- Suppression de routes et de fonctionnalités obsolètes (connexion espace jeu, formatage des numéros de téléphone).
- Amélioration de la gestion des autorisations et des accès pour les différents types d'utilisateurs.
- Préparation de la migration vers le modèle `evaluation_eva` avec ajout d'une inflexion.
- Suppression de la logique `Evaluation.evapro?`.
- Déplacement de méthodes et de constantes vers le modèle `EvaluationEva` pour une meilleure organisation.

### Autres changements
- Mise à jour de plusieurs dépendances (fast-uri, rails-html-sanitizer, loofah, tarteaucitronjs).
- Correction de nombreux `rubocop_todo`.
- Ajout de redirections pour l'ancienne route `admin_evaluations_path`.
- Correction de typologies de structures.
- Correction de bugs mineurs liés à l'affichage et aux redirections.
- Amélioration du style de la modale d'invitation.
