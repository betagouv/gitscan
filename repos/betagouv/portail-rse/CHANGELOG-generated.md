## Changelog : portail-rse (30 derniers jours, au 2026-06-17)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur lors de la saisie des indicateurs RSE, notamment la gestion des sessions, la navigation et la notification des actions. Des corrections de typographie et des ajustements ont également été apportés pour améliorer la qualité globale du portail.

### Évolutions fonctionnelles
- Correction d'un bug qui empêchait l'affichage correct de la page de connexion après expiration de la session lors du remplissage d'un indicateur.
- Amélioration de la navigation : redirection de la vue fragment indicateur vers l'exigence de publication si la requête n'est pas Htmx.
- Notification à l'utilisateur lors de l'enregistrement d'un indicateur.
- Correction d'un bug qui provoquait la suppression involontaire de lignes dans les tableaux lors de l'utilisation de la touche Entrée.
- Ajout du choix du module d'un rapport VSME dans les données synchronisées sur Metabase.
- La propriété `choix_module` renvoie désormais `None` si l'utilisateur n'a pas fait de choix, au lieu du choix par défaut.

### Évolutions techniques
- Ajout de l'attribut `EXT_ID` de Brevo.
- Refactoring du code pour extraire des constantes.
- Amélioration de la gestion de l'importation si l'ID de la liste Brevo n'est pas fourni.

### Autres changements
- Corrections de coquilles et de typographie sur la VSME [#issue](https://github.com/betagouv/portail-rse/issues/).
- Mise à jour de la documentation avec le diagramme overview.
