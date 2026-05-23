## Changelog : ami-notifications-api (30 derniers jours, au 21 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'interface utilisateur, notamment concernant la gestion des zones géographiques et des préférences utilisateur dans l'agenda. Des corrections et des optimisations ont également été apportées à la gestion des notifications, à l'authentification FranceConnect et à l'infrastructure de réplication des données.

### Évolutions fonctionnelles
- **Agenda :** Amélioration de l'affichage et de la gestion des zones géographiques (A, B, C) et des jours fériés en fonction des préférences de l'utilisateur. Possibilité de définir des préférences de zone et d'adresses pour filtrer les informations affichées. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- **Notifications :** Désactivation des notifications lors de la déconnexion de l'utilisateur. [#721](https://github.com/numerique-gouv/ami-notifications-api/issues/721)
- **Gestion des utilisateurs (Agent Admin) :** Implémentation de nouvelles fonctionnalités pour la gestion des utilisateurs dans l'interface d'administration : recherche, détails, suppression, et audit des actions. [#774](https://github.com/numerique-gouv/ami-notifications-api/issues/774)
- **Notifications :** Ajout d'un champ `content_private_body` aux modèles de notification pour stocker du contenu privé. [#875](https://github.com/numerique-gouv/ami-notifications-api/issues/875)
- **Interface utilisateur :** Amélioration de la disposition du bouton "gérer" dans l'écran des notifications. [#874](https://github.com/numerique-gouv/ami-notifications-api/issues/874)
- **Interface utilisateur :** Ajout d'un composant `PageWrapper` pour améliorer la structure et le style des pages. [#801](https://github.com/numerique-gouv/ami-notifications-api/issues/801)
- **FranceConnect :** Authentification des requêtes vers l'API Github. [#417](https://github.com/numerique-gouv/ami-notifications-api/issues/417)

### Évolutions techniques
- **Réplication :** Refonte de la commande de réplication des données avec ajout de tests et de logs.  Amélioration de la gestion des erreurs et de la configuration. [#791](https://github.com/numerique-gouv/ami-notifications-api/issues/791)
- **Infrastructure :** Utilisation de `mkcert` pour la gestion des certificats SSL en local. [#828](https://github.com/numerique-gouv/ami-notifications-api/issues/828)
- **Dépendances :** Mise à jour de Django en version 6.0.5.
- **Cache :** Ajout de cache pour les requêtes des jours fériés.
- **HTTP Client :** Ajout d'un gestionnaire de contexte pour fermer les connexions HTTP.
- **Suppression de code obsolète :** Suppression du "feature flag" "requests enabled" qui n'est plus utilisé. [#823](https://github.com/numerique-gouv/ami-notifications-api/issues/823)

### Autres changements
- **Documentation :** Amélioration de la documentation et des commentaires.
- **Tests :** Ajout et mise à jour de tests unitaires.
- **Matomo :** Ajout du suivi des zones de jours fériés sur Matomo. [#750](https://github.com/numerique-gouv/ami-notifications-api/issues/750)
- **Interface utilisateur :** Suppression de `target="_self"` dans le code Svelte. [#877](https://github.com/numerique-gouv/ami-notifications-api/issues/877)
- **Interface utilisateur :** Refactorisation de code et simplification de méthodes dans le code front-end.
- **Interface utilisateur :** Amélioration de l'affichage des toasts et des bannières. [#723](https://github.com/numerique-gouv/ami-notifications-api/issues/723)
