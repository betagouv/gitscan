## Changelog : portail-rse (30 derniers jours, au 2026-06-17)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur lors de la saisie et de la gestion des indicateurs RSE. Des corrections de bugs ont été apportées pour améliorer la stabilité et la fluidité de l'application, notamment concernant la gestion des sessions, la sélection de champs et les notifications. La documentation a également été enrichie avec la complétion du diagramme d'architecture.

### Évolutions fonctionnelles
- Correction d'un bug qui empêchait l'affichage correct de la page de connexion après expiration de la session lors du remplissage d'un indicateur.
- Amélioration de la gestion des événements clavier dans les tableaux pour éviter la suppression involontaire de lignes.
- Notification de l'utilisateur lors de l'enregistrement d'un indicateur.
- Redirection vers l'exigence de publication si la requête vers la vue fragment indicateur n'est pas Htmx.
- Correction de coquilles sur la VSME [#628de24](https://github.com/betagouv/portail-rse/commit/628de24).
- Suppression d'espaces inutiles dans les labels de la VSME [#de88114](https://github.com/betagouv/portail-rse/commit/de88114).

### Évolutions techniques
- Ajout de l'attribut `EXT_ID` de Brevo pour une meilleure intégration.
- Annulation de l'import si l'ID de la liste Brevo n'est pas fourni.
- Complétion du diagramme d'architecture global [#46d3b7e](https://github.com/betagouv/portail-rse/commit/46d3b7e).

### Autres changements
- Aucune information supplémentaire.
