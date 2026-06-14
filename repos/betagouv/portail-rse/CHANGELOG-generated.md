## Changelog : portail-rse (30 derniers jours, au 05 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur lors du remplissage des indicateurs VSME, avec des corrections de bugs et des améliorations de la gestion des sessions et des interactions avec le formulaire. Des ajustements ont également été apportés à la synchronisation des données avec Metabase et à la gestion des choix de modules pour les rapports VSME.

### Évolutions fonctionnelles
- Correction d'un bug qui empêchait l'affichage correct de la page de connexion après expiration de la session lors du remplissage d'un indicateur.
- Correction d'un problème de suppression involontaire de lignes dans les tableaux lors de l'utilisation de la touche Entrée.
- Amélioration de la notification utilisateur lors de l'enregistrement d'un indicateur.
- Redirection de la vue "fragment indicateur" vers l'exigence de publication si la requête n'est pas Htmx.
- La propriété `choix_module` ne renvoie plus le choix par défaut, mais `None` si l'utilisateur n'a pas fait de choix.
- Ajout du choix du module d'un rapport VSME dans les données synchronisées sur Metabase.

### Évolutions techniques
- Extraction de constantes pour améliorer la lisibilité et la maintenabilité du code.
- Ajout de l'attribut `EXT_ID` de Brevo pour une meilleure intégration.
- Annulation de l'import si l'ID de la liste Brevo n'est pas fourni.

### Autres changements
- Corrections de coquilles sur la VSME. [#628de24](https://github.com/betagouv/portail-rse/commit/628de24)
- Suppression d'espaces en fin de ligne dans les labels VSME. [#de88114](https://github.com/betagouv/portail-rse/commit/de88114)
