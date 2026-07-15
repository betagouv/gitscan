## Changelog : resorption-bidonvilles (30 derniers jours, au 08 juillet 2026)

### Résumé
Les dernières mises à jour se concentrent sur l'amélioration de l'interface utilisateur et de la gestion des phases préparatoires à la résorption des bidonvilles. Des corrections de bugs et des optimisations de performance ont également été apportées, notamment au niveau de la validation des données et de l'affichage des informations sur la carte. Plusieurs améliorations concernent la gestion des actions et des indicateurs, avec un focus sur la clarté et la réactivité de l'interface.

### Évolutions fonctionnelles
- Refonte de l'affichage des cartes de phases préparatoires à la résorption.
- Refonte du formulaire des phases préparatoires à la résorption.
- Amélioration de la synchronisation date/statut des phases préparatoires.
- Correction de l'affichage du libellé de date de la phase "official_opening".
- Ajout de l'option "Inconnu" au filtre "Type de propriétaire".
- Affichage des badges d'indicateurs uniquement lorsqu'il existe des actions associées.
- Limitation de l'onglet "actions de ma structure" aux actions en cours.
- Correction de l'affichage de l'item actif dans le menu.
- Correction de la popup.
- Ajout d'un item dans la popup de la version.

### Évolutions techniques
- Optimisation de la recherche de la phase associée dans l'item de phase.
- Simplification de l'affichage de la date sur la carte de phase.
- Refactor de la validation des indicateurs scolaires côté API et Frontend pour plus d'autonomie.
- Utilisation de `structuredClone` au lieu de `cloneDeep` pour améliorer la performance.
- Amélioration des messages d'erreur de validation.
- Suppression des contraintes SQL obsolètes des indicateurs scolaires.
- Utilisation de `includes` au lieu de `indexOf` pour une meilleure lisibilité.
- Amélioration de la gestion des erreurs et des validations côté frontend.
- Refactor du code pour utiliser des computed properties réactives pour le type de badge.
- Correction de l'appel à Submit et désactivation du bouton si déjà à jour.
- Modification des libellés affichés dans les DsfrTags.
- Correction d'un doublon d'ID d'élément.
- Correction de coquilles et amélioration de la lisibilité du code.

### Autres changements
- Mise à jour des conditions d'utilisation.
- Ajout de tests pour l'API.
- Correction de linting et amélioration de la qualité du code.
- Mise à jour de la date de PROD et de la date limite du questionnaire.
- Ajout d'un bandeau canicule.
- Correction de la persistance des phases préparatoires en édition.
- Correction d'une coquille dans le nom du type de badge de la carte de phase.
- Correction de l'affichage de la colonne suivant le lancement officiel de la résorption.
- Correction de la synchronisation date/statut des phases préparatoires.
- Correction de l'affichage des coins vides des boutons de zoom.
- Correction de l'affichage du bouton "Mettre à jour" après correction d'un indicateur.
- Correction de la gestion du pluriel des onglets d'actions.
- Correction de la transparence au survol des boutons de zoom sur la carte.
- Correction de la vérification du type de champ dans sortFn.
- Amélioration de la validation de organizationId.
- Correction d'un chemin dans l'import des migrations.
- Mise à jour de la version et des métadonnées.
- Correction de tests unitaires.
