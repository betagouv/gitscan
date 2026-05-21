## Changelog : federation (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la flexibilité de la plateforme. Des ajustements ont été apportés à la gestion des rôles et des autorisations, notamment pour l'accès aux services publics. Des améliorations ont également été apportées à la validation des emails et à la configuration de l'authentification, ainsi qu'à la gestion des environnements de test.

### Évolutions fonctionnelles
- Ajout d'un label "organisation" aux scopes retournés par l'API. [#1181](https://github.com/proconnect-gouv/federation/issues/1181)
- Amélioration de l'accès aux services publics (SP) en utilisant les rôles de l'utilisateur. [#1158](https://github.com/proconnect-gouv/federation/issues/1158)
- Ajout de rôles par défaut dans l'interface d'administration. [#1161](https://github.com/proconnect-gouv/federation/pulls/1161)
- Mise en place d'un indicateur pour activer/désactiver la validation des adresses email. [#1144](https://github.com/proconnect-gouv/federation/pulls/1144)
- Ajout d'une bannière d'avertissement pour l'environnement de test. [#1141](https://github.com/proconnect-gouv/federation/pulls/1141)
- Amélioration de l'accessibilité : ajout d'un lien vers la déclaration d'accessibilité et amélioration du balisage HTML. [#1142](https://github.com/proconnect-gouv/federation/pulls/1142)

### Évolutions techniques
- Utilisation de DNS-over-HTTPS pour la résolution MX des adresses email, améliorant ainsi la confidentialité et la sécurité. [#1159](https://github.com/proconnect-gouv/federation/pulls/1159)
- Correction d'un bug empêchant l'assignation correcte du champ `acr` lorsque les valeurs ACR ne sont pas reconnues. [#1122](https://github.com/proconnect-gouv/federation/pulls/1122)
- Possibilité de configurer plusieurs exclusions pour le point de terminaison `readyz` dans le contexte `core-fca-low`. [#1154](https://github.com/proconnect-gouv/federation/pulls/1154)
- Amélioration de la configuration du client OIDC pour permettre l'utilisation d'une fonction `fetch` personnalisée dans les configurations sans découverte. [#1143](https://github.com/proconnect-gouv/federation/pulls/1143)
- Ajout de logs pour les valeurs `acr` afin de faciliter le débogage. [#1139](https://github.com/proconnect-gouv/federation/pulls/1139)
- Suppression temporaire du test de l'API health, puis restauration. [#1120](https://github.com/proconnect-gouv/federation/pulls/1120)

### Autres changements
- Correction de linting dans l'application d'administration.
- Refactorisation du code pour utiliser `HAS_RED_BORDER` au lieu de `isProduction`.
- Ajout de logs pour faciliter le débogage.
- Mises à jour de diverses dépendances (FastAPI, Mongoose, Uvicorn, etc.).
