## Changelog : proconnect-identite (30 derniers jours, au 5 juin 2026)

### Résumé
Ce mois-ci, les évolutions de ProConnect Identité se concentrent sur l'amélioration de l'expérience utilisateur lors de l'inscription et de la gestion des organisations, ainsi que sur la consolidation de la sécurité et de la compatibilité du système. Des améliorations ont également été apportées à la gestion des erreurs et à la configuration de l'environnement de pré-production.

### Évolutions fonctionnelles
- Simplification de l'inscription pour les petites organisations civiles ou agricoles disposant d'une adresse email gratuite [#1972](https://github.com/proconnect-gouv/proconnect-identite/issues/1972).
- Ajout d'une description d'erreur OIDC plus informative pour faciliter le diagnostic des problèmes d'authentification [#1930](https://github.com/proconnect-gouv/proconnect-identite/issues/1930).
- Amélioration de la gestion des motifs de rejet de modération : suppression du motif et ajout d'un message guidant l'utilisateur vers l'email reçu [#1927](https://github.com/proconnect-gouv/proconnect-identite/issues/1927).
- Ajout d'une raison pour les rejets de modération stockée en base de données [#1931](https://github.com/proconnect-gouv/proconnect-identite/issues/1931).
- Mise en place d'un nouveau système de calcul de la qualité d'un service public, avec une compatibilité ascendante pour les algorithmes existants [#1952](https://github.com/proconnect-gouv/proconnect-identite/issues/1952).
- Migration progressive des envois d'emails depuis MonComptePro pour une meilleure gestion et fiabilité [#1932](https://github.com/proconnect-gouv/proconnect-identite/issues/1932).

### Évolutions techniques
- Création d'un client dédié pour l'environnement de pré-production, avec des identifiants spécifiques [#1937](https://github.com/proconnect-gouv/proconnect-identite/issues/1937).
- Refactorisation du code de seed pour les tests E2E, utilisant un hook `before` pour une meilleure gestion de l'initialisation [#1926](https://github.com/proconnect-gouv/proconnect-identite/issues/1926).
- Publication du package `rne` pour une utilisation publique [#1963](https://github.com/proconnect-gouv/proconnect-identite/issues/1963).
- Ajout d'une administration pour la gestion de la liste blanche des états [#1969](https://github.com/proconnect-gouv/proconnect-identite/issues/1969).
- Correction d'un bug lié à l'encodage des URL [#1966](https://github.com/proconnect-gouv/proconnect-identite/issues/1966).
- Correction d'un problème d'importation de types PostgreSQL pour une meilleure compatibilité avec les bundlers de navigateurs [#1947](https://github.com/proconnect-gouv/proconnect-identite/issues/1947).

### Autres changements
- Mise à jour de la documentation et des scripts d'administration pour la gestion des annuaires d'entreprises [#1946](https://github.com/proconnect-gouv/proconnect-identite/issues/1946), [#1943](https://github.com/proconnect-gouv/proconnect-identite/issues/1943), [#1941](https://github.com/proconnect-gouv/proconnect-identite/issues/1941).
- Ajout d'un workflow pour exécuter les scripts d'administration localement [#1945](https://github.com/proconnect-gouv/proconnect-identite/issues/1945).
- Amélioration de la granularité du ratio d'envoi d'emails alternatifs [#1951](https://github.com/proconnect-gouv/proconnect-identite/issues/1951).
- Diverses mises à jour de dépendances (Cypress, Redis, Node.js, Prettier, etc.).
