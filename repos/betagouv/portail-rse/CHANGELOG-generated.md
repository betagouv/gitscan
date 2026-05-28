## Changelog : portail-rse (30 derniers jours, au 22 mai 2026)

### Résumé
Cette mise à jour apporte des améliorations à la gestion des données VSME, notamment en permettant de choisir le module de rapport directement dans les données synchronisées avec Metabase. Des corrections ont également été apportées pour gérer les cas où l'API Sirene ne fournit pas le code postal du siège social d'une entreprise. Enfin, quelques corrections de coquilles et améliorations de la documentation ont été effectuées.

### Évolutions fonctionnelles
- Permet de choisir le module d'un rapport VSME dans les données synchronisées sur Metabase. [#0ce4a67](https://github.com/betagouv/portail-rse/commit/0ce4a67)
- Corrige un bug où la propriété `choix_module` renvoyait le choix par défaut au lieu de `None` si l'utilisateur n'avait pas fait de choix. [#631e78e](https://github.com/betagouv/portail-rse/commit/631e78e)
- Gère le cas où l'API Sirene ne fournit pas le code postal du siège lors de la création d'une nouvelle entreprise. [#e6b9159](https://github.com/betagouv/portail-rse/commit/e6b9159)

### Évolutions techniques
- Extrait des constantes pour améliorer la lisibilité et la maintenabilité du code. [#385951e](https://github.com/betagouv/portail-rse/commit/385951e)

### Autres changements
- Correction de coquilles sur la VSME. [#628de24](https://github.com/betagouv/portail-rse/commit/628de24)
- Ajout d'une indication temporaire concernant la directive Omnibus dans la section CSRD. [#4c82506](https://github.com/betagouv/portail-rse/commit/4c82506)
- Amélioration de la coloration syntaxique du SQL dans la documentation. [#ed9d129](https://github.com/betagouv/portail-rse/commit/ed9d129)
