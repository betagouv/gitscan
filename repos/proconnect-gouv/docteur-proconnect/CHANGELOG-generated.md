## Changelog : docteur-proconnect (30 derniers jours, au 16 mai 2026)

### Résumé
Cette version apporte des améliorations concernant les valeurs d'ACR (Authentification Context Reference) pour la compatibilité avec eIDAS, ainsi qu'une mise à jour des scopes ProConnect pour inclure les informations sur l'unité organisationnelle et les rôles. Une régression introduite par une redirection vers Tally a été corrigée.

### Évolutions fonctionnelles
- Ajout des valeurs d'ACR `eidas0-mfa` et `eidas1-mfa` pour une meilleure compatibilité avec les solutions d'authentification eIDAS. [#54](https://github.com/proconnect-gouv/docteur-proconnect/issues/54)
- Mise à jour des scopes ProConnect (`PC_SCOPES`) pour inclure les informations sur l'unité organisationnelle et les rôles de l'utilisateur. [#53](https://github.com/proconnect-gouv/docteur-proconnect/issues/53)
- Rétractation de la redirection forcée vers Tally après une connexion réussie, corrigeant ainsi un problème de régression. [#50](https://github.com/proconnect-gouv/docteur-proconnect/issues/50)

### Évolutions techniques
- Aucune évolution technique significative à signaler.

### Autres changements
- Mise à jour de la documentation et des dépendances internes (prettier, lodash-es, path-to-regexp) via Dependabot. Ces mises à jour sont automatiques et ne devraient pas impacter l'utilisation de l'outil. [#51](https://github.com/proconnect-gouv/docteur-proconnect/issues/51) [#52](https://github.com/proconnect-gouv/docteur-proconnect/issues/52) [#55](https://github.com/proconnect-gouv/docteur-proconnect/issues/55) [#56](https://github.com/proconnect-gouv/docteur-proconnect/issues/56)
