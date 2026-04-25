## Changelog : ami-notifications-api (30 derniers jours, au 23 avril 2026)

### Résumé
Les dernières mises à jour apportent des améliorations significatives à l'expérience utilisateur, notamment l'ajout de la gestion des zones pour l'agenda des notifications, une meilleure gestion des utilisateurs et de leurs rôles, ainsi que des corrections de bugs et des optimisations de performance. Des améliorations de la sécurité et de la gestion des logs ont également été implémentées.

### Évolutions fonctionnelles
- **Agenda des notifications :** Ajout de la possibilité de définir des préférences de zones pour l'affichage des vacances scolaires dans l'agenda. L'utilisateur peut maintenant sélectionner ses zones géographiques pour une information plus pertinente. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- **Gestion des utilisateurs :** Ajout de la gestion des rôles d'agents (admin, agent) avec une page dédiée pour l'administration des accès. Possibilité de créer des agents lors de la connexion via ProConnection. [#609](https://github.com/numerique-gouv/ami-notifications-api/issues/609)
- **Déconnexion :** Ajout d'une confirmation modale lors de la déconnexion de l'utilisateur. [#753](https://github.com/numerique-gouv/ami-notifications-api/issues/753)
- **Notifications mobiles :** L'URL de l'application mobile est maintenant incluse dans les notifications push. [#648](https://github.com/numerique-gouv/ami-notifications-api/issues/648)
- **Page d'accueil :** Correction de problèmes de padding sur la page d'accueil. [#764](https://github.com/numerique-gouv/ami-notifications-api/issues/764)
- **Affichage des notifications :** Amélioration de l'affichage des notifications, notamment pour les journaux d'audit.
- **Accès refusé :** Amélioration du style de la page d'accès refusé.

### Évolutions techniques
- **Refactoring de l'API :** Les points d'entrée de l'API agenda et follow-p ont été regroupés sous `/api/v1`. [#762](https://github.com/numerique-gouv/ami-notifications-api/issues/762)
- **Cache :** Implémentation d'un cache pour les requêtes des vacances scolaires afin d'améliorer les performances. [#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)
- **Logging :** Amélioration du logging des erreurs d'API, avec ajout des headers dans les logs.
- **Configuration :** Migration des variables de configuration de `.env` vers les fichiers de settings Django.
- **Suppression de code obsolète :** Suppression de l'utilisation de `settings.CONFIG` et du script `django-admin`.
- **Amélioration de la sécurité :** Correction d'une vulnérabilité potentielle concernant l'URL du secteur. [#747](https://github.com/numerique-gouv/ami-notifications-api/issues/747)
- **Linting :** Correction de plusieurs avertissements de linting dans le code frontend. [#792](https://github.com/numerique-gouv/ami-notifications-api/issues/792)
- **Tests :** Mise à jour des fixtures de tests.

### Autres changements
- **Documentation :** Mise à jour de la documentation CONTRIBUTING.
- **Dépendances :** Mise à jour de plusieurs dépendances (uuid, @cucumber/cucumber, python-dotenv, lxml, @sveltejs/kit, uv, pytest, pygments, requests, yaml, picomatch, brace-expansion, cryptography).
- **Interface utilisateur :** Amélioration de l'interface utilisateur, notamment le centrage du bouton FranceConnect et le défilement des champs d'adresse. [#515](https://github.com/numerique-gouv/ami-notifications-api/issues/515), [#568](https://github.com/numerique-gouv/ami-notifications-api/issues/568)
