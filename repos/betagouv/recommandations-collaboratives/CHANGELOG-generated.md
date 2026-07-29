## Changelog : recommandations-collaboratives (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment au niveau de la gestion des organisations et des projets, ainsi que par l'ajout de fonctionnalités de gestion de plugins. Des corrections de bugs et des optimisations de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de l'interface pour la fusion d'organisations [#2249](https://github.com/betagouv/recommandations-collaboratives/pull/2249).
- Ajout d'un bouton d'annulation lors de la suppression d'une ressource [#2275](https://github.com/betagouv/recommandations-collaboratives/pull/2275).
- Possibilité de cliquer sur le nom d'une organisation dans la fiche d'un utilisateur pour accéder à sa page [#2293](https://github.com/betagouv/recommandations-collaboratives/pull/2293).
- Ajout d'un indicateur visuel pour les projets avec peu de retours [#2220](https://github.com/betagouv/recommandations-collaboratives/pull/2220).
- Refonte de la page d'accueil du CRM et de la page des organisations [#2182](https://github.com/betagouv/recommandations-collaboratives/pull/2182), [#2205](https://github.com/betagouv/recommandations-collaboratives/pull/2205).
- Ajout de la possibilité de masquer le bouton de création de nouveau projet [#2170](https://github.com/betagouv/recommandations-collaboratives/pull/2205).
- Amélioration de la gestion des notifications, notamment pour les notifications privées [#2292](https://github.com/betagouv/recommandations-collaboratives/pull/2292).
- Ajout de la possibilité de filtrer les projets par statut de lecture des recommandations [#2274](https://github.com/betagouv/recommandations-collaboratives/pull/2274).
- Ajout d'un système de plugins pour étendre les fonctionnalités de l'application [#2246](https://github.com/betagouv/recommandations-collaboratives/pull/2246).

### Évolutions techniques
- Mise à jour de plusieurs dépendances frontend (postcss, fast-uri, dompurify, immutable, axios, shell-quote, systeminformation, ws) pour corriger des failles de sécurité et améliorer les performances.
- Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment au niveau des filtres et des composants d'interface utilisateur.
- Amélioration de la gestion des erreurs et des validations.
- Optimisation des requêtes SQL pour réduire les temps de chargement.
- Mise en place d'un système de gestion des migrations pour les plugins.
- Amélioration de la gestion des tests.
- Mise à jour de JupyterLab à la version 4.6.2 [#2284](https://github.com/betagouv/recommandations-collaboratives/pull/2284).
- Suppression de dépendances inutilisées.
- Ajout de la possibilité de configurer l'authentification à deux facteurs (2FA) pour les utilisateurs staff [#2220](https://github.com/betagouv/recommandations-collaboratives/pull/2220).

### Autres changements
- Amélioration de la documentation README [#2293](https://github.com/betagouv/recommandations-collaboratives/pull/2293).
- Corrections de bugs mineurs liés à l'affichage et au comportement de l'interface utilisateur.
- Ajout de tests unitaires pour garantir la qualité du code.
- Mise à jour des messages d'erreur pour une meilleure clarté.
- Nettoyage du code et suppression de code obsolète.
- Ajout d'un mécanisme pour gérer les plugins et leurs migrations.
- Correction d'un problème lié à l'affichage des notifications.
- Amélioration de la gestion des cookies Sesame.
- Ajout d'un champ "paused_by" pour indiquer qui a mis un projet en pause.
- Ajout de la possibilité de trier la liste des utilisateurs dans le CRM par date d'inscription.
- Suppression de l'entrée 'plugins' du fichier .gitignore.
