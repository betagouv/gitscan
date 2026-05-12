## Changelog : ami-notifications-api (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur de l'interface agent, notamment avec l'ajout de fonctionnalités pour la gestion des notifications et l'agenda. Des corrections ont également été apportées pour améliorer la stabilité et la robustesse de l'API, ainsi que des optimisations techniques pour la réplication de données et la gestion des logs.

### Évolutions fonctionnelles
- **Interface Agent :** Ajout de la possibilité d'envoyer des notifications directement depuis l'interface d'administration ([#773](https://github.com/numerique-gouv/ami-notifications-api/issues/773)).
- **Gestion des agendas :** Implémentation de la gestion des agendas et des congés scolaires, avec la possibilité de définir des préférences de zones pour l'affichage des notifications ([#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)).
- **Confirmation de déconnexion :** Ajout d'une modal de confirmation lors de la déconnexion de l'interface agent ([#753](https://github.com/numerique-gouv/ami-notifications-api/issues/753)).
- **Amélioration de l'adresse :** Correction du défilement de la page d'adresse et ajout d'en-têtes fixes pour une meilleure expérience utilisateur ([#568](https://github.com/numerique-gouv/ami-notifications-api/issues/568)).
- **Bouton FranceConnect :** Centrage vertical du bouton FranceConnect sur la page de connexion ([#515](https://github.com/numerique-gouv/ami-notifications-api/issues/515)).
- **Validation des notifications :**  Le `partner_id` est désormais obligatoire lors de la création d'une notification ([#798](https://github.com/numerique-gouv/ami-notifications-api/issues/798)).

### Évolutions techniques
- **Réplication de la base de données :** Ajout d'une commande pour répliquer les données de la base de données, avec des tests associés ([#791](https://github.com/numerique-gouv/ami-notifications-api/issues/791)).
- **Mise à jour Django :** Mise à jour de Django vers la version 6.0.5.
- **Refactoring des logs :** Refactorisation de la méthode de logging pour supprimer le nom du champ ([#626](https://github.com/numerique-gouv/ami-notifications-api/issues/626)).
- **Gestion des erreurs API :** Ajout des headers dans le log des erreurs d'API Part.
- **API endpoints :** Déplacement des endpoints agenda et follow-p derrière `/api/v1` ([#762](https://github.com/numerique-gouv/ami-notifications-api/issues/762)).
- **Scheduled Notifications :** Simplification des commandes et des tests pour les notifications planifiées ([#786](https://github.com/numerique-gouv/ami-notifications-api/issues/786)).
- **Cache HTTP :** Ajout d'un cache pour les requêtes GET HTTP afin d'améliorer les performances ([#508](https://github.com/numerique-gouv/ami-notifications-api/issues/508)).

### Autres changements
- **Documentation :** Mise à jour de la documentation CONTRIBUTING et suppression de la commande `django-admin` ([#795](https://github.com/numerique-gouv/ami-notifications-api/issues/795)).
- **Linting :** Correction de plusieurs avertissements de linting dans le code frontend ([#792](https://github.com/numerique-gouv/ami-notifications-api/issues/792)).
- **Correction de bugs :** Diverses corrections de bugs et améliorations de la stabilité.
- **Suppression de proxy FC en production :** Suppression du proxy FranceConnect en production ([#826](https://github.com/numerique-gouv/ami-notifications-api/issues/826)).
- **Correction lien préférences :** Correction du lien vers les préférences de notification depuis la page de notification ([#833](https://github.com/numerique-gouv/ami-notifications-api/issues/833)).
