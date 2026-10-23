## Changelog : federation (30 derniers jours, au 22 octobre 2026)

### Résumé
Ce mois-ci, la plateforme a franchi des étapes importantes dans la gestion des accès sécurisés, notamment avec l'introduction de nouvelles fonctionnalités pour les demandes XDA et l'amélioration des processus d'authentification (support multi-appareils et Entra ID). Parallèlement, des travaux de nettoyage et de mise à jour de l'infrastructure ont été menés pour renforcer la stabilité et la sécurité du système.

### Évolutions fonctionnelles
- **Gestion des demandes XDA** :
    - Ajout de la configuration XDA pour les prestataires de services [#1691](https://github.com/proconnect-gouv/federation/issues/1691).
    - Gestion du cycle de vie des demandes (approbation et rejet) [#1727](https://github.com/proconnect-gouv/federation/issues/1727).
    - Amélioration de la revue des demandes via l'affichage d'emojis pour faciliter la lecture [#1725](https://github.com/proconnect-gouv/federation/issues/1725).
- **Authentification et Sécurité** :
    - Implémentation des demandes d'authentification multi-appareils [#1717](https://github.com/proconnect-gouv/federation/issues/1717).
    - Ajout du mapping de contexte d'authentification Entra ID pour le standard eidas1-mfa [#1746](https://github.com/proconnect-gouv/federation/issues/1746).
    - Autorisation des URLs de rappel (callback) en `localhost` et `http` pour les tests et environnements spécifiques [#1753](https://github.com/proconnect-gouv/federation/issues/1753).
    - Affichage conditionnel de l'URL de déconnexion [#1684](https://github.com/proconnect-gouv/federation/issues/1684).
- **Interface Utilisateur** :
    - Affichage de l'ID client sur la page de mise à jour des prestataires de services [#1790](https://github.com/proconnect-gouv/federation/issues/1790).
    - Amélioration de la lisibilité de l'User-Agent et génération d'emojis pour l'interface [#1724](https://github.com/proconnect-gouv/federation/issues/1724).
- **Corrections** :
    - Résolution de problèmes d'affichage du design en production [#1661](https://github.com/proconnect-gouv/federation/issues/1661).
    - Correction de la gestion des assets (JS/CSS) de l'interface d'administration en production.

### Évolutions techniques
- **Infrastructure et Environnement** :
    - Mise à jour de l'environnement d'exécution vers Node.js 24.22.1.
    - Verrouillage de la version de Docker Compose à la v5.5.1 [#1694](https://github.com/proconnect-gouv/federation/issues/1694).
    - Mise en place d'un contrôle via variable d'environnement pour l'activation du script Matomo [#458d23e](https://github.com/proconnect-gouv/federation/issues/458d23e).
- **Refactoring et Nettoyage** :
    - Suppression de champs et paramètres inutilisés dans les fournisseurs d'identité (`trustedIdentity`, `redirect_uris`, `post_logout_redirect_uris`) [#1758](https://github.com/proconnect-gouv/federation/issues/1758), [#1757](https://github.com/proconnect-gouv/federation/issues/1757), [#1756](https://github.com/proconnect-gouv/federation/issues/1756) et du champ `statusUrl` [#c672a68](https://github.com/proconnect-gouv/federation/issues/c672a68).
    - Suppression du scope "roles" pour les prestataires de services afin de simplifier les permissions [#1687](https://github.com/proconnect-gouv/federation/issues/1687).
    - Simplification de l'architecture en supprimant NestJS du composant `csmr-rie` [#1689](https://github.com/proconnect-gouv/federation/issues/1689).
    - Migration des chemins `@fc/*` vers des imports natifs via `package.json` [#1716](https://github.com/proconnect-gouv/federation/issues/1716).
- **Dépendances métier** :
    - Mise à jour du package "ProConnect Identité" pour l'Annuaire des Entreprises.

### Autres changements
- **Documentation** : Mise à jour des guides de contribution et ajout d'un modèle de description pour les Pull Requests afin d'harmoniser les pratiques [#1750](https://github.com/proconnect-gouv/federation/issues/1750).
- **Tests** : Nettoyage de la suite de tests (suppression des tests focalisés) [#1718](https://github.com/proconnect-gouv/federation/issues/1718).
