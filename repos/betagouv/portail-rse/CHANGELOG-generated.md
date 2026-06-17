## Changelog : portail-rse (30 derniers jours, au 2026-06-16)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur lors de la saisie des indicateurs VSME, avec des corrections de bugs et des améliorations de l'interface. Des ajustements ont également été apportés à la synchronisation des données avec Metabase et à la documentation du projet.

### Évolutions fonctionnelles
- Correction d'un bug qui empêchait l'affichage correct de la page de connexion après expiration de la session lors du remplissage d'un indicateur.
- Correction d'un bug qui provoquait la suppression involontaire de lignes dans les tableaux lors de l'utilisation de la touche Entrée.
- Amélioration de la notification utilisateur après l'enregistrement d'un indicateur.
- Redirection de la vue "fragment indicateur" vers l'exigence de publication si la requête n'est pas Htmx.
- Le choix du module d'un rapport VSME est maintenant correctement synchronisé avec Metabase.
- La propriété `choix_module` renvoie `None` si l'utilisateur n'a pas fait de choix, améliorant la logique de l'application.

### Évolutions techniques
- Ajout de l'attribut `EXT_ID` de Brevo pour une meilleure intégration.
- Refactoring du code pour extraire des constantes, améliorant la lisibilité et la maintenabilité.
- Mise à jour de la documentation avec un diagramme overview plus complet [#46d3b7e](https://github.com/betagouv/portail-rse/commit/46d3b7e).

### Autres changements
- Corrections de coquilles et d'espaces superflus dans les labels VSME [#de88114](https://github.com/betagouv/portail-rse/commit/de88114) et [#628de24](https://github.com/betagouv/portail-rse/commit/628de24).
- Les dépendances `pyjwt`, `aiohttp` et `idna` ont été mises à jour. (Ces mises à jour automatiques ne sont pas détaillées individuellement).
