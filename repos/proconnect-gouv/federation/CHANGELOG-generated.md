## Changelog : federation (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la flexibilité de la plateforme. Des ajustements ont été apportés à la gestion des rôles et des permissions, notamment dans l'interface d'administration, ainsi que des améliorations de la validation des emails et de la configuration OIDC. Des mises à jour de dépendances ont également été effectuées pour maintenir la sécurité et la performance du système.

### Évolutions fonctionnelles
- Ajout d'un bandeau d'avertissement pour l'environnement de test [#1141](https://github.com/proconnect-gouv/federation/pull/1141).
- Amélioration de l'accessibilité : ajout d'un lien vers la déclaration d'accessibilité et amélioration du balisage HTML [#1142](https://github.com/proconnect-gouv/federation/pull/1142).
- Ajout de l'étiquette `organization_label` par défaut lors de la création d'un fournisseur de services [#1159](https://github.com/proconnect-gouv/federation/pull/1159).
- L'acr (autorisation claim) n'est plus assigné si les valeurs ne sont pas reconnues [#1122](https://github.com/proconnect-gouv/federation/pull/1122).
- Ajout d'un indicateur pour afficher une bordure rouge en environnement de production dans l'admin [#1157](https://github.com/proconnect-gouv/federation/pull/1157).

### Évolutions techniques
- Suppression des rôles de base de données dans l'administration [#1184](https://github.com/proconnect-gouv/federation/pull/1184).
- Mise à jour de Node.js vers la version 24.16 [#1186](https://github.com/proconnect-gouv/federation/pull/1186).
- Refonte de la validation d'email avec l'ajout d'un flag `FEATURE_VALIDATE_EMAIL` [#1144](https://github.com/proconnect-gouv/federation/pull/1144).
- Amélioration de la configuration OIDC pour permettre l'utilisation d'une fonction `customFetch` [#1143](https://github.com/proconnect-gouv/federation/pull/1143).
- Utilisation de DNS-over-HTTPS pour la résolution MX dans la validation d'email [#1159](https://github.com/proconnect-gouv/federation/pull/1159).
- Support de multiples exclusions dans la configuration `readyz` pour le core-fca-low [#1154](https://github.com/proconnect-gouv/federation/pull/1154).
- Ajout de rôles par défaut dans l'interface d'administration [#1161](https://github.com/proconnect-gouv/federation/pull/1161).

### Autres changements
- Ajout de logs pour les valeurs `acr` [#1139](https://github.com/proconnect-gouv/federation/pull/1139).
- Plusieurs mises à jour de dépendances ont été effectuées pour améliorer la sécurité et la stabilité du système (cryptography, pydantic, systeminformation, uvicorn, fastapi, mongoose, axe-core, fast-uri, dotenv, cypress, globals, amqplib, postcss, uuid, @nestjs/testing, @proconnect-gouv/proconnect.api_entreprise, ejs).
