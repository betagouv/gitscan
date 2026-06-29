## Changelog : proconnect-identite (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, les évolutions de ProConnect Identité se sont concentrées sur l'amélioration de la sécurité et de l'expérience utilisateur, notamment en renforçant la gestion des niveaux d'authentification (ACR), en optimisant le processus d'inscription et en améliorant la surveillance et l'analyse des données via Metabase. Des corrections de bugs et des mises à jour de dépendances ont également été effectuées pour assurer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Authentification :** Ajout de nouveaux niveaux d'ACR (Authentification Context Reference) pour une gestion plus fine des exigences d'authentification. [#1965](https://github.com/proconnect-gouv/proconnect-identite/pull/1965)
- **Inscription :** Amélioration de la validation automatique des utilisateurs lors de l'inscription avec un domaine de contact officiel. [#1934](https://github.com/proconnect-gouv/proconnect-identite/pull/1934)
- **Annuaire Service Public :** Correction d'un bug empêchant l'exclusion des adresses email non valides lors de la recherche. [#1996](https://github.com/proconnect-gouv/proconnect-identite/pull/1996)
- **Certification Dirigeant :** Correction d'un bug lié à la compatibilité des nouvelles valeurs ACR avec le processus de certification des dirigeants. [#2004](https://github.com/proconnect-gouv/proconnect-identite/pull/2004)
- **Catégorie Juridique :** Ajout du "Pôle d'équilibre territorial et rural" à la liste des catégories juridiques. [#1982](https://github.com/proconnect-gouv/proconnect-identite/pull/1982)
- **Raison d'utilisation :** Ajout d'un nouveau champ "raison d'utilisation" dans la base de données pour une meilleure traçabilité. [#1931](https://github.com/proconnect-gouv/proconnect-identite/pull/1931)
- **Whitelist Administration Etat :** Ajout de la gestion de la whitelist pour l'administration de l'état. [#1969](https://github.com/proconnect-gouv/proconnect-identite/pull/1969)

### Évolutions techniques
- **Performance :** Ajout d'un index sur la table `users_oidc_clients` pour améliorer les performances des requêtes. [#1989](https://github.com/proconnect-gouv/proconnect-identite/pull/1989)
- **Base de données :** Mise à jour du schéma de la base de données pour assurer la compatibilité avec PostgreSQL 17. [#1983](https://github.com/proconnect-gouv/proconnect-identite/pull/1983)
- **Metabase :** Intégration des authenticators aux statistiques Metabase pour un meilleur suivi. [#1967](https://github.com/proconnect-gouv/proconnect-identite/pull/1967)
- **Dépendances :** Mise à jour de plusieurs dépendances (Hono, undici, sentry, proconnect-test-client, etc.) pour bénéficier des dernières corrections et améliorations.
- **CI/CD :** Amélioration du pipeline CI/CD pour la publication des packages.

### Autres changements
- **Documentation :** Amélioration de la documentation interne.
- **Configuration :** Ajustements de la configuration pour améliorer la stabilité.
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Sécurité :** Correction d'un problème permettant de spammer les codes de vérification par email. [#2004](https://github.com/proconnect-gouv/proconnect-identite/pull/2004)
