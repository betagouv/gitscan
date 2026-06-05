## Changelog : portail-rse (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur lors de la saisie d'indicateurs et de rapports VSME, avec des corrections de bugs et des ajustements pour une meilleure gestion des données et des notifications. Des corrections ont également été apportées pour gérer les cas où l'API Sirene ne fournit pas toutes les informations nécessaires.

### Évolutions fonctionnelles
- Amélioration de la gestion des indicateurs : notification de l'utilisateur lors de l'enregistrement d'un indicateur. [#7b56b54](https://github.com/betagouv/portail-rse/commit/7b56b54)
- Correction : la page de connexion s'affiche correctement même si la session expire pendant le remplissage d'un indicateur. [#7b56b54](https://github.com/betagouv/portail-rse/commit/7b56b54)
- Correction : empêche la suppression involontaire de lignes dans les tableaux lors de l'utilisation de la touche Entrée. [#0225a11](https://github.com/betagouv/portail-rse/commit/0225a11)
- Amélioration : la propriété `choix_module` renvoie `None` si l'utilisateur n'a pas fait de choix, permettant une meilleure gestion des données. [#631e78e](https://github.com/betagouv/portail-rse/commit/631e78e)
- Ajout : possibilité de choisir le module d'un rapport VSME, synchronisé avec Metabase. [#0ce4a67](https://github.com/betagouv/portail-rse/commit/0ce4a67)
- Correction : gestion du cas où l'API Sirene ne fournit pas le code postal du siège lors de la création d'une entreprise. [#e6b9159](https://github.com/betagouv/portail-rse/commit/e6b9159)
- Correction : redirection de la vue fragment indicateur vers l'exigence de publication si la requête n'est pas Htmx. [#d33324e](https://github.com/betagouv/portail-rse/commit/d33324e)

### Évolutions techniques
- Refactoring : extraction de constantes pour améliorer la lisibilité et la maintenabilité du code. [#385951e](https://github.com/betagouv/portail-rse/commit/385951e)
- Amélioration : annule l'import si l'ID de la liste Brevo n'est pas fourni. [#f726705](https://github.com/betagouv/portail-rse/commit/f726705)
- Ajout : ajout de l'attribut `EXT_ID` de Brevo. [#d5119f5](https://github.com/betagouv/portail-rse/commit/d5119f5)

### Autres changements
- Correction de typos dans la VSME. [#628de24](https://github.com/betagouv/portail-rse/commit/628de24) et [#de88114](https://github.com/betagouv/portail-rse/commit/de88114)
- Indication temporaire concernant la directive Omnibus dans le CSDR. [#4c82506](https://github.com/betagouv/portail-rse/commit/4c82506)
- Mise à jour de la dépendance `idna` de la version 3.11 à la version 3.15. [#8241fe9](https://github.com/betagouv/portail-rse/commit/8241fe9)
- Mise à jour de la dépendance `urllib3` de la version 2.6.3 à la version 2.7.0. [#41a6ac9](https://github.com/betagouv/portail-rse/commit/41a6ac9)
