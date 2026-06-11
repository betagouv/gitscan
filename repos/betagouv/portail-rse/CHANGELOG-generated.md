## Changelog : portail-rse (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur lors du remplissage des indicateurs RSE, notamment en corrigeant des bugs liés à la session, à la suppression de lignes dans les tableaux et à l'affichage des pages. Des améliorations ont également été apportées à la gestion des données VSME et à la synchronisation avec Metabase. Enfin, quelques corrections typographiques et une gestion améliorée des données SIRENE ont été implémentées.

### Évolutions fonctionnelles
- Correction d'un bug qui empêchait l'affichage correct de la page de connexion après expiration de la session lors du remplissage d'un indicateur.
- Correction d'un problème de suppression involontaire de lignes dans les tableaux lors de l'utilisation de la touche Entrée.
- Amélioration de la gestion des indicateurs : notification de l'utilisateur lors de l'enregistrement d'un indicateur.
- Redirection de la vue "fragment indicateur" vers l'exigence de publication si la requête n'est pas Htmx.
- Ajout du choix du module d'un rapport VSME dans les données synchronisées sur Metabase.
- Gestion du cas où l'API SIRENE ne fournit pas le code postal du siège lors de la création d'une entreprise.
- La propriété `choix_module` ne renvoie plus le choix par défaut mais `None` si l'utilisateur n'a pas fait de choix.

### Évolutions techniques
- Extraction de constantes pour améliorer la lisibilité et la maintenabilité du code.

### Autres changements
- Corrections typographiques sur la VSME [#de88114](https://github.com/betagouv/portail-rse/commit/de88114).
- Ajout de l'attribut `EXT_ID` de Brevo [#d5119f5](https://github.com/betagouv/portail-rse/commit/d5119f5).
- Annulation de l'import si l'ID de la liste Brevo n'est pas fourni [#f726705](https://github.com/betagouv/portail-rse/commit/f726705).
- Indication temporaire concernant la directive Omnibus dans le CSDR [#4c82506](https://github.com/betagouv/portail-rse/commit/4c82506).
