## Changelog : proconnect-test-client (30 derniers jours, au 30 avril 2026)

### Résumé
Cette mise à jour apporte une nouvelle fonctionnalité permettant de forcer l'authentification multi-facteur (MFA) avec des valeurs d'ACR (Authentication Context Class) spécifiques pour les environnements EIDAS 0 et 1. Cela permet de tester plus précisément les scénarios d'authentification avec MFA.

### Évolutions fonctionnelles
- Ajout de la possibilité de forcer l'authentification multi-facteur (MFA) avec les valeurs d'ACR `eidas0-mfa` et `eidas1-mfa` via l'endpoint `/force-2fa` [#180](https://github.com/proconnect-gouv/proconnect-test-client/issues/180).

### Évolutions techniques
- Aucune évolution technique notable.

### Autres changements
- Mise à jour de la dépendance `lodash-es` de la version 4.17.23 à la version 4.18.1 [#179](https://github.com/proconnect-gouv/proconnect-test-client/issues/179).
