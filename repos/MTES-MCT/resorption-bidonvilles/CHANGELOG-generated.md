## Changelog : resorption-bidonvilles (30 derniers jours, au 08 juillet 2026)

### Résumé
Cette période a été marquée par une refonte significative du formulaire et de l'affichage des phases préparatoires à la résorption, ainsi que par des améliorations de la validation et de la gestion des indicateurs scolaires. Plusieurs corrections de bugs et optimisations de performance ont également été apportées pour améliorer l'expérience utilisateur et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Refonte complète du formulaire et de l'affichage des cartes des phases préparatoires à la résorption.
- Amélioration de l'affichage des badges de phases sur la carte.
- Ajout de l'option "Inconnu" au filtre "Type de propriétaire".
- Affichage plus clair des actions en cours pour chaque structure.
- Correction de l'affichage de la date de la phase "official_opening".
- Correction de la synchronisation date/statut des phases préparatoires.
- Correction de la persistance des phases préparatoires en édition.
- Correction d'une coquille dans le nom du type de badge de la carte de phase.
- Correction de l'affichage de la colonne suivant le lancement officiel de la résorption.

### Évolutions techniques
- Refactorings importants du code frontend et backend pour améliorer la maintenabilité et la performance.
- Optimisation de la recherche de la phase associée dans l'item de phase.
- Utilisation de `structuredClone` au lieu de `cloneDeep` pour améliorer la performance et la compatibilité.
- Amélioration de la validation des indicateurs scolaires côté frontend et backend.
- Suppression de contraintes SQL obsolètes pour les indicateurs scolaires.
- Utilisation de `includes` au lieu de `indexOf` pour une meilleure lisibilité du code.
- Amélioration des messages d'erreur de validation.
- Mise en place d'un service centralisé pour la gestion des notifications Mattermost.
- Correction de linting et amélioration de la qualité du code.
- Mise à jour des conditions d'utilisation.

### Autres changements
- Ajout d'un item dans la popup de la version.
- Correction de doublons d'ID d'élément.
- Mise à jour de la date de PROD et de la date limite du questionnaire.
- Ajout d'un bandeau canicule.
- Correction de la popup.
- Correction de l'appel à Submit et désactivation du bouton si déjà à jour.
- Correction de tests unitaires.
- Amélioration de la documentation.
- Publication des versions v2.54.0 et v2.55.1.
