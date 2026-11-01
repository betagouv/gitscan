## Changelog : federation (30 derniers jours, au 30/10/2026)

### Résumé
Ce mois-ci, le projet a franchi des étapes importantes avec le lancement de l'outil de statistiques "Statisticat" et l'amélioration du flux de gestion des demandes XDA. Les capacités d'authentification ont été renforcées (support multi-appareils, mapping Entra ID) et l'infrastructure a été modernisée pour gagner en stabilité et en sécurité.

### Évolutions fonctionnelles
- Lancement de **Statisticat**, un nouvel outil permettant la gestion des données statistiques via l'import de fichiers CSV [#1752](https://github.com/proconnect-gouv/federation/pull/1752).
- Amélioration du workflow **XDA** : ajout de la configuration pour les Service Providers [#1691](https://github.com/proconnect-gouv/federation/pull/1691) et gestion complète des approbations et rejets de demandes [#1727](https://github.com/proconnect-gouv/federation/pull/1727).
- Optimisation de l'interface utilisateur : affichage de l'ID client sur la page de mise à jour des Service Providers [#8f3a89a](https://github.com/proconnect-gouv/federation/commit/8f3a89a) et ajout d'emojis pour faciliter la revue des demandes.
- Évolutions de l'authentification : implémentation des requêtes d'authentification sur plusieurs appareils [#1717](https://github.com/proconnect-gouv/federation/pull/1717) et ajout du mapping de contexte d'authentification Entra ID pour le MFA eidas1 [#7cb2a57](https://github.com/proconnect-gouv/federation/commit/7cb2a57).
- Correction de la gestion des accès RIE en cas de désaccord (mismatch) [#1690](https://github.com/proconnect-gouv/federation/pull/1690).

### Évolutions techniques
- Infrastructure & Environnement : passage à **Node.js 24.22.1** [#188ec72](https://github.com/proconnect-gouv/federation/commit/188ec72), fixation de la version de **Docker Compose à v5.5.1** [#9393f3f](https://github.com/proconnect-gouv/federation/commit/9393f3f) et gestion de l'activation de Matomo via variable d'environnement [#458d23e](https://github.com/proconnect-gouv/federation/commit/458d23e).
- Refactoring & Optimisation : suppression de NestJS du composant `csmr-rie` [#1689](https://github.com/proconnect-gouv/federation/pull/1689), transition vers des imports natifs `package.json` [#1716](https://github.com/proconnect-gouv/federation/pull/1716), ajout de timeouts sur les appels proxy HTTP [#1715](https://github.com/proconnect-gouv/federation/pull/1715) et optimisation du transfert CSV pour Statisticat via l'utilisation de deux proxys distincts [#4e0e96a](https://github.com/proconnect-gouv/federation/commit/4e0e96a).
- Sécurité : nettoyage des Identity Providers (suppression des champs inutilisés `trustedIdentity`, `redirect_uris`, etc.) [#1758](https://github.com/proconnect-gouv/federation/pull/1758), [#1757](https://github.com/proconnect-gouv/federation/pull/1757), [#1756](https://github.com/proconnect-gouv/federation/pull/1756), retrait du scope `roles` pour les Service Providers [#1687](https://github.com/proconnect-gouv/federation/pull/1687) et autorisation des URLs de callback en `localhost` ou `http` [#1753](https://github.com/proconnect-gouv/federation/pull/1753).
- Qualité : montée de version de Cypress et du préprocesseur Cucumber [#ea950e7](https://github.com/proconnect-gouv/federation/pull/ea950e7).

### Autres changements
- Documentation : mise à jour des directives de contribution et ajout de modèles de description pour les Pull Requests [#1750](https://github.com/proconnect-gouv/federation/pull/1750).
