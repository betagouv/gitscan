## Changelog : recommandations-collaboratives (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la sécurité avec l'implémentation de l'authentification à deux facteurs (2FA) pour les administrateurs, ainsi que par des corrections de bugs et des optimisations de l'interface utilisateur, notamment au niveau du CRM et de la gestion des projets. Des améliorations de la documentation et de l'infrastructure ont également été apportées.

### Évolutions fonctionnelles
- Ajout de l'authentification à deux facteurs (2FA) pour les comptes staff/admin [#2220](https://github.com/betagouv/recommandations-collaboratives/pull/2220).
- Possibilité de cliquer sur le nom de l'organisation dans la vue CRM pour accéder à sa page [#2296](https://github.com/betagouv/recommandations-collaboratives/pull/2296).
- Ajout d'un bouton "Annuler" lors de la suppression d'une ressource [#2275](https://github.com/betagouv/recommandations-collaboratives/pull/2275).
- Ajout d'un indicateur visuel pour les projets à faible portée [#2229](https://github.com/betagouv/recommandations-collaboratives/pull/2229).
- Amélioration de l'affichage des informations de projet sur la page d'accueil.
- Ajout d'un indicateur pour les projets en pause dans la vue CRM [#2125](https://github.com/betagouv/recommandations-collaboratives/pull/2109).

### Évolutions techniques
- Refactorisation du code pour améliorer la gestion des plugins, notamment pour l'intégration de hooks et l'utilisation dans les commandes de gestion [#2246](https://github.com/betagouv/recommandations-collaboratives/pull/2246).
- Amélioration de la gestion des schémas de base de données pour les plugins [#2298](https://github.com/betagouv/recommandations-collaboratives/pull/2298).
- Correction de problèmes liés à l'utilisation des plugins dans les contextes multi-tenant [#2299](https://github.com/betagouv/recommandations-collaboratives/pull/2299).
- Mise à jour des dépendances npm et yarn (postcss, fast-uri, dompurify, immutable, shell-quote, systeminformation, ws)
- Amélioration de la performance des requêtes dans le CRM pour éviter les problèmes de N+1 [#2259](https://github.com/betagouv/recommandations-collaboratives/pull/2259).
- Refactorisation du code pour simplifier et améliorer la lisibilité.
- Suppression de dépendances inutilisées.
- Amélioration de la gestion des erreurs et des exceptions.
- Mise à jour de la documentation README avec une section sur le déploiement [#1e1bd7da1](https://github.com/betagouv/recommandations-collaboratives/commit/1e1bd7da1).

### Autres changements
- Correction de bugs mineurs liés à l'interface utilisateur et à la gestion des notifications [#2249](https://github.com/betagouv/recommandations-collaboratives/pull/2249), [#2304](https://github.com/betagouv/recommandations-collaboratives/pull/2304), [#2301](https://github.com/betagouv/recommandations-collaboratives/pull/2301).
- Amélioration de la gestion des erreurs de validation d'email.
- Correction de problèmes d'affichage sur les écrans responsives.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- Mise à jour de la configuration de l'environnement de développement.
- Correction de problèmes liés à la visibilité des notifications.
- Suppression de code inutile.
- Amélioration de la documentation interne.
