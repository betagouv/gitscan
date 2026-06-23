## Changelog : portail-rse (30 derniers jours, au 17 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur lors de la saisie et de la gestion des indicateurs RSE. Des corrections ont été apportées pour éviter les suppressions accidentelles de données et assurer un fonctionnement correct des notifications et des redirections. La documentation a également été enrichie avec un diagramme d'architecture plus complet.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage correct de la page de connexion après expiration de la session lors du remplissage d'un indicateur.
- Amélioration de la gestion des erreurs lors de la saisie des indicateurs, notamment en évitant la suppression involontaire de lignes dans les tableaux.
- Notification de l'utilisateur lors de l'enregistrement d'un indicateur.
- Redirection vers l'exigence de publication si la requête vers la vue "fragment indicateur" n'est pas effectuée via Htmx.
- Ajout de la gestion de l'identifiant externe (EXT_ID) de Brevo pour une meilleure intégration.

### Évolutions techniques
- Mise à jour de la documentation avec un diagramme d'architecture plus complet [#46d3b7e](https://github.com/betagouv/portail-rse/commit/46d3b7e).
- Correction d'un problème d'import conditionnel lié à l'ID de liste Brevo [#f726705](https://github.com/betagouv/portail-rse/commit/f726705).

### Autres changements
- Correction de typos dans les labels VSME [#de88114](https://github.com/betagouv/portail-rse/commit/de88114).
