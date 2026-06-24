## Changelog : apistration (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, l'ajout de nouvelles fonctionnalités pour les éditeurs d'API, et l'amélioration de la documentation et de l'expérience utilisateur. Des corrections de bugs et des optimisations ont également été apportées, notamment concernant les endpoints FranceConnect et DGFIP.

### Évolutions fonctionnelles
- Ajout d'un filtre sur le statut des habilitations des fournisseurs dans le tableau de bord des fournisseurs [#216](https://github.com/datagouv/apistration/issues/216).
- Affichage de l'ID interne de l'utilisateur sur la page de son compte. [#217](https://github.com/datagouv/apistration/issues/217)
- Ajout de jeux de données de test CNous v4 avec des scénarios INE pour les boursiers [#218](https://github.com/datagouv/apistration/issues/218).
- Ajout d'une nouvelle fonctionnalité permettant de gérer les éditeurs (ajout, suppression, recherche, filtrage) dans l'interface d'administration [#139](https://github.com/datagouv/apistration/issues/139).
- Ajout d'une nouvelle API pour récupérer les délégations des éditeurs [#144](https://github.com/datagouv/apistration/issues/144).
- Amélioration de la documentation pour l'intégration des éditeurs, incluant des exemples et des instructions claires.
- Ajout d'une page de site satisfaisant l'exigence RGAA 12.1 (sitemap). [#206](https://github.com/datagouv/apistration/issues/206)
- Ajout d'un endpoint DGFIP pour la vérification du numéro de TVA. [#125](https://github.com/datagouv/apistration/issues/125)
- Ajout d'une nouvelle fonctionnalité pour l'expiration des sessions utilisateur après une période d'inactivité. [#182](https://github.com/datagouv/apistration/issues/182)
- Ajout d'une nouvelle fonctionnalité pour l'enregistrement des activités d'administration pour un audit fiable. [#171](https://github.com/datagouv/apistration/issues/171)

### Évolutions techniques
- Suppression du workflow de régénération manuelle du swagger, désormais automatisé. [#206](https://github.com/datagouv/apistration/issues/206)
- Correction d'un test flaky dans les spécifications d'autorisation. [#215](https://github.com/datagouv/apistration/issues/215)
- Mise à jour des dépendances (Rubocop, Ruby, actions GitHub).
- Amélioration de la structure du code pour une meilleure lisibilité et maintenabilité.
- Refactorisation du code pour améliorer la gestion des paramètres de civilité.
- Correction d'une fuite de mémoire dans les tests liés à la date d'ouverture du bureau. [#181](https://github.com/datagouv/apistration/issues/181)
- Amélioration de la gestion des erreurs et de la sécurité, notamment en renforçant la validation des données et en protégeant les endpoints sensibles.
- Ajout de documentation pour les SDK Node.js et Ruby.
- Correction de bugs liés à la gestion des scopes d'API et à la documentation Swagger.

### Autres changements
- Ajout d'un lien vers le Bureau Ouvert sur la page de contact.
- Correction de fautes de frappe et amélioration de la qualité de la documentation.
- Mise à jour de la documentation pour refléter les changements apportés aux endpoints et aux paramètres d'API.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Amélioration des tests unitaires et d'intégration.
- Suppression de code obsolète.
- Ajout d'un changelog pour les API Entreprise.
- Ajout d'un changelog pour les API Particulier.
- Suppression du bouton "Récupérer mes données via FranceConnect".
- Correction d'un bug sur les yaml de région PACA.
- Ajout de payloads France Connect citizen pour les endpoints de civilité.
