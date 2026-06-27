## Changelog : seves (30 derniers jours, au 26 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Sèves se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans les modules d'investigation (TIAC et SSA) avec l'introduction d'un nouveau sélecteur d'arborescence pour faciliter la recherche et la sélection d'informations. Des corrections de bugs et des optimisations de performance ont également été apportées pour une meilleure stabilité et réactivité de l'application. L'intégration avec Mastro a été finalisée.

### Évolutions fonctionnelles
- Amélioration de la gestion des notifications DI envoyées aux agents.
- Ajout d'un organisme nuisible dans le module SV.
- Possibilité de choisir une date lors de l'envoi d'un message de note.
- Amélioration de l'affichage des sauts de ligne dans les commentaires des fiches zone délimitée et de détection (SV).
- Nouveau sélecteur d'arborescence pour l'investigation des cas humains (SSA) [#2038](https://github.com/betagouv/seves/issues/2038).
- Nouveau sélecteur d'arborescence sur l'investigation TIAC.
- Ajout d'un champ pour le numéro RASFF sans limite de caractères (SV).
- Amélioration de l'affichage et de l'édition des établissements dans TIAC.
- Ajout d'un indicateur visuel pour les enregistrements simples avec 10 personnes ou plus malades.
- Possibilité de voir les sous-objets ajoutés dans la même révision.
- Amélioration de l'importation Agricoll pour les utilisateurs.
- Ajout d'un placeholder dans l'éditeur de texte enrichi.
- Ajout d'un tooltip sur la description dans la vue liste SSA.
- Correction de la gestion des valeurs lors de la fermeture de la modale "repas".
- Correction d'un bug empêchant la sauvegarde d'un événement produit SSA avec le nouveau sélecteur d'arborescence.
- Correction d'un bug d'alignement des filtres avec liens libres sur SSA et TIAC.
- Correction d'un bug d'affichage de certaines cases à cocher après la mise à jour de django-dsfr.
- Correction d'un problème d'ordre des messages pour les notes avec date sélectionnée.
- Correction d'un bug dans le formulaire d'événement produit (SSA).
- Amélioration des tests pour les cartes d'établissement dans TIAC et SSA.
- Amélioration de la sécurité des vues sur TIAC.
- Suppression des membres de l'équipe SEVES de la désactivation de compte.
- Correction du nom de l'en-tête pour TIAC dans le CSV.
- Correction d'une erreur de console JavaScript mineure dans AlertController.
- Utilisation de l'API de rendu de formulaire pour le formulaire Lieu.
- Amélioration de la précision des tests dans TIAC.
- Finalisation de l'intégration avec Mastro.

### Évolutions techniques
- Refactorisation du code pour permettre l'utilisation de querysets avec le sélecteur d'arborescence.
- Suppression de code mort.
- Mise à jour de la bibliothèque `cryptography`.
- Mise à jour de `django-environ` (0.13.0 -> 0.14.0).
- Mise à jour de `django-debug-toolbar` (6.3.0 -> 7.0.0).
- Mise à jour de `sentry-sdk` (2.61.1 -> 2.63.0).
- Mise à jour de `ruff` (0.15.17 -> 0.15.18).
- Mise à jour de `django-reversion` (6.2.0 -> 6.3.0).
- Mise à jour de `beautifulsoup4` (4.14.3 -> 4.15.0).
- Mise à jour de `django` (6.0.5 -> 6.0.6).
- Mise à jour de `redis` (7.4.0 -> 8.0.0).
- Refactorisation du formulaire `lieux` dans SV.
- Réduction de la taille des instances Scalingo.

### Autres changements
- Ajout d'un avertissement dans le README.md concernant l'utilisation d'un merge-commit pour la MEP.
- Ajout d'un avertissement dans README.md sur l'utilisation d'un merge-commit pour la MEP.
- Amélioration des performances du bloc commun.
- Correction d'un test pour éviter des chargements de page trop longs (SV).
- Amélioration de la fiabilité des tests pour l'application de compte.
- Correction d'un bug lié au type MIME des EML.
- Amélioration de l'affichage de l'étiquette complète avec les catégories dans le bouton du sélecteur d'arborescence lorsqu'un élément est sélectionné.
- Force d'une mise à jour de la détection lors de la modification d'une ZoneInfestee.
