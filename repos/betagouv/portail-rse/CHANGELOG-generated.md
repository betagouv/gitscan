## Changelog : portail-rse (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur lors de la saisie des indicateurs VSME, avec des corrections de bugs et des notifications plus claires. Des ajustements ont également été apportés à la synchronisation des données avec Metabase et à la gestion des entreprises.

### Évolutions fonctionnelles
- Correction d'un bug qui empêchait l'affichage correct de la page de connexion après expiration de la session lors du remplissage d'un indicateur.
- Correction d'un bug qui provoquait la suppression involontaire de lignes dans les tableaux lors de l'utilisation de la touche Entrée.
- Ajout de notifications pour informer l'utilisateur lorsqu'un indicateur a été enregistré.
- Amélioration de la gestion des entreprises : le code postal du siège est maintenant correctement géré même si l'API Sirene ne le fournit pas. [#e6b9159](https://github.com/betagouv/portail-rse/commit/e6b9159)
- Ajout du choix du module d'un rapport VSME dans les données synchronisées sur Metabase, permettant un suivi plus précis. [#0ce4a67](https://github.com/betagouv/portail-rse/commit/0ce4a67)
- Amélioration du comportement de la propriété `choix_module` pour renvoyer `None` si aucun choix n'a été fait par l'utilisateur. [#631e78e](https://github.com/betagouv/portail-rse/commit/631e78e)
- Redirection de la vue fragment indicateur vers l'exigence de publication si la requête n'est pas Htmx. [#d33324e](https://github.com/betagouv/portail-rse/commit/d33324e)

### Évolutions techniques
- Refactoring du code pour extraire des constantes, améliorant la lisibilité et la maintenabilité. [#385951e](https://github.com/betagouv/portail-rse/commit/385951e)
- Ajout de l'attribut `EXT_ID` de Brevo pour une meilleure intégration. [#d5119f5](https://github.com/betagouv/portail-rse/commit/d5119f5)
- Annulation de l'import si l'ID de la liste Brevo n'est pas fourni, évitant des erreurs potentielles. [#f726705](https://github.com/betagouv/portail-rse/commit/f726705)

### Autres changements
- Corrections de typos et d'espaces superflus dans les labels VSME. [#de88114](https://github.com/betagouv/portail-rse/commit/de88114) et [#628de24](https://github.com/betagouv/portail-rse/commit/628de24)
- Ajout d'une indication temporaire concernant la directive Omnibus dans le CSDR. [#4c82506](https://github.com/betagouv/portail-rse/commit/4c82506)
