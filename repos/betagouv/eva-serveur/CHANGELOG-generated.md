## Changelog : eva-serveur (30 derniers jours, au 30 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la gestion des évaluations Evapro, avec une refonte de l'interface et de l'accès aux données. Des améliorations ont également été apportées à l'administration des structures et des comptes utilisateurs, ainsi que des corrections de bugs et des optimisations de code.

### Évolutions fonctionnelles
- Ajout d'un menu "Evaluation" avec des sections distinctes pour les évaluations EVA et Evapro pour les superadmins.
- Création d'une page dédiée à la gestion des évaluations Evapro, incluant l'export en PDF.
- Affichage de l'email et du numéro de téléphone de l'accueil dans la page de détails des structures locales.
- Amélioration de l'affichage des événements et réduction de la largeur des tableaux de campagnes.
- Affichage du nom du bénéficiaire des évaluations.
- Correction de la traduction du message d'erreur lors de la génération de PDF.
- Correction du message d'accueil pour les comptes en attente.
- Ajout de la colonne "structure" à l'index des évaluations Evapro pour les superadmins.
- Simplification du nom généré pour les campagnes Evapro.

### Évolutions techniques
- Refactorisation importante du code lié aux évaluations Evapro, avec déplacement des partials et des traductions dans des fichiers dédiés.
- Création du modèle `EvaluationEva` et migration des spécificités Evapro.
- Suppression de code mort et d'indirection dans le modèle `Evaluation`.
- Factorisation de constantes et de méthodes pour améliorer la lisibilité et la maintenabilité du code.
- Suppression de routes et de fonctionnalités obsolètes (connexion espace jeu, formatage des numéros de téléphone).
- Suppression d'autorisations inutiles sur le modèle `Evaluation`.
- Utilisation d'un composant `NavigationComponent` pour gérer la position des éléments dans le menu.
- Correction de nombreux `rubocop_todo`.
- Ajout d'une inflexion pour le modèle `evaluation_evapro`.

### Autres changements
- Mise à jour des typologies de structures.
- Correction de deux typologies de structures.
- Suppression d'une helper method non utilisée.
- Ajout de redirections pour l'ancienne route `admin_evaluations_path`.
- Correction de la redirection après suppression ou erreur de PDF.
- Correction de bugs liés à l'accès aux campagnes Evapro pour les utilisateurs Evapro.
- Mise à jour de certaines dépendances (fast-uri, rails-html-sanitizer, loofah, tarteaucitronjs).
