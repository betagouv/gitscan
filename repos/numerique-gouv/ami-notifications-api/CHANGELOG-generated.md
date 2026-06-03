## Changelog : ami-notifications-api (30 derniers jours, au 02 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur pour l'administration des notifications, notamment avec l'ajout de nouvelles fonctionnalités pour la gestion des utilisateurs et l'envoi de notifications. Des travaux importants ont également été réalisés sur la réplication de la base de données et l'intégration de FranceConnect. Enfin, des corrections et optimisations diverses ont été apportées pour améliorer la stabilité et la performance de l'API.

### Évolutions fonctionnelles
- **Gestion des utilisateurs (Agent Admin):** Ajout de vues pour la recherche, la consultation des détails, la suppression et la création d'utilisateurs. Des audits sont désormais enregistrés pour les actions de consultation et de suppression d'utilisateurs. [#774](https://github.com/numerique-gouv/ami-notifications-api/issues/774)
- **Notifications:** Possibilité de demander l'envoi de notifications en tant que partenaire AMI. Ajout de messages d'erreur plus clairs en cas d'échec. [#773](https://github.com/numerique-gouv/ami-notifications-api/issues/773)
- **OTV (Objectifs de Travail):** Amélioration de la gestion de la date dans les notifications OTV, avec une date par défaut si nécessaire et un paramètre de date correct. [#852](https://github.com/numerique-gouv/ami-notifications-api/issues/852)
- **Préférences de zone:** Navigation vers les préférences de zone lors de la première connexion. [#788](https://github.com/numerique-gouv/ami-notifications-api/issues/788)
- **Déconnexion:** Désactivation des notifications lors de la déconnexion. [#721](https://github.com/numerique-gouv/ami-notifications-api/issues/721)
- **Toasts:** Amélioration de l'affichage des toasts (messages d'information) pour une meilleure expérience utilisateur. [#723](https://github.com/numerique-gouv/ami-notifications-api/issues/723)
- **Autocomplete:** Ajout d'un champ d'autocomplete pour la recherche d'identifiants FranceConnect. [#773](https://github.com/numerique-gouv/ami-notifications-api/issues/773)

### Évolutions techniques
- **Réplication de la base de données:** Travaux importants sur la réplication de la base de données, incluant la gestion des identifiants, l'ajout de commandes de migration et l'amélioration de la journalisation. [#791](https://github.com/numerique-gouv/ami-notifications-api/issues/791)
- **Mise à jour Django:** Mise à jour de Django vers la version 6.0.5.
- **Sécurité:** Utilisation de `mkcert` pour la gestion des certificats SSL locaux.
- **Environnement:** Chargement de la variable d'environnement `DEBUG` à partir du fichier `.env.local`.
- **Optimisation:** Limitation du stockage des enregistrements de registration pour un même appareil mobile. [#893](https://github.com/numerique-gouv/ami-notifications-api/issues/893)
- **Refactoring:** Suppression du code lié à la fonctionnalité "requests enabled" qui n'est plus utilisée. [#823](https://github.com/numerique-gouv/ami-notifications-api/issues/823)
- **Architecture Frontend:** Introduction d'un composant `PageWrapper` pour uniformiser la structure des pages et gérer le header. [#801](https://github.com/numerique-gouv/ami-notifications-api/issues/801)
- **Route replication:** Routage des accès à la base de données de réplication vers le datawarehouse. [#904](https://github.com/numerique-gouv/ami-notifications-api/issues/904)

### Autres changements
- **Documentation:** Renommage des textes d'aide pour les notifications planifiées. [#708](https://github.com/numerique-gouv/ami-notifications-api/issues/708)
- **FranceConnect (FI):** Ajout de la gestion de la session FranceConnect, incluant l'authentification, l'autorisation, la gestion des cookies et la déconnexion. [#708](https://github.com/numerique-gouv/ami-notifications-api/issues/708)
- **Nettoyage de code:** Suppression d'un dossier `.claude` inutile.
- **Configuration:** Mise à jour de la variable d'environnement `PUBLIC_FC_PROXY_BASE_URL`.
- **Matomo:** Ajout du suivi des zones de vacances sur Matomo. [#750](https://github.com/numerique-gouv/ami-notifications-api/issues/750)
- **Suppression d'un revert:** Suppression d'un revert inutile sur le modèle `ScheduledNotification`. [#914](https://github.com/numerique-gouv/ami-notifications-api/issues/914)
