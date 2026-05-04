## Changelog : docteur-proconnect (30 derniers jours, au 30 avril 2026)

### Résumé
Cette mise à jour apporte des améliorations à la reconnaissance des différents niveaux d'authentification eIDAS et met à jour les scopes demandés pour inclure les informations sur l'unité organisationnelle et les rôles de l'utilisateur. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout de la prise en charge des valeurs ACR `eidas0-mfa` et `eidas1-mfa` pour une meilleure reconnaissance des niveaux d'authentification eIDAS. [#54](https://github.com/proconnect-gouv/docteur-proconnect/issues/54)
- Mise à jour des scopes ProConnect (`PC_SCOPES`) pour inclure les informations sur l'unité organisationnelle et les rôles de l'utilisateur. [#53](https://github.com/proconnect-gouv/docteur-proconnect/issues/53)

### Évolutions techniques
- Mise à jour de la dépendance `zod` de la version 4.1.12 à la version 4.4.1. [#58](https://github.com/proconnect-gouv/docteur-proconnect/issues/58)
- Mise à jour de la dépendance `openid-client` de la version 6.8.3 à la version 6.8.4. [#57](https://github.com/proconnect-gouv/docteur-proconnect/issues/57)
- Mise à jour de la dépendance de développement `prettier` de la version 3.6.2 à la version 3.8.3. [#56](https://github.com/proconnect-gouv/docteur-proconnect/issues/56)
- Mise à jour de plusieurs dépendances via Dependabot. [#55](https://github.com/proconnect-gouv/docteur-proconnect/issues/55)
