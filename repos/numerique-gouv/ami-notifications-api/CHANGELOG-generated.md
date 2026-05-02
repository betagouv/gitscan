## Changelog : ami-notifications-api (30 derniers jours, au 30 avril 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur et de la gestion des accès, notamment l'ajout d'une gestion des agents et des rôles, ainsi que l'intégration de l'agenda et des préférences de zones pour les notifications. Des corrections et optimisations ont également été apportées pour améliorer l'expérience utilisateur et la stabilité de l'API.

### Évolutions fonctionnelles
- **Gestion des agents et des accès :** Ajout d'une page de gestion des accès avec la possibilité de créer, modifier et supprimer des agents et de leur attribuer des rôles (administrateur, agent, agent administrateur) [#609].
- **Agenda et préférences de zones :** Implémentation de la gestion des préférences de zones pour l'agenda, permettant aux utilisateurs de filtrer les informations en fonction de leur localisation. Ajout de la possibilité de définir des zones préférées et d'afficher les vacances scolaires correspondantes [#508].
- **Notifications :** Amélioration de la gestion des notifications, notamment l'ajout d'un lien vers l'élément concerné dans les notifications [#726] et la correction de problèmes liés à l'envoi de notifications planifiées [#782].
- **Déconnexion :** Ajout d'une confirmation avant la déconnexion pour éviter les actions accidentelles [#753].
- **Interface utilisateur :** Amélioration de l'interface utilisateur avec des en-têtes fixes, un défilement amélioré et une meilleure gestion de l'espace d'affichage [#568].
- **FranceConnect :** Centrage vertical du bouton FranceConnect [#515] et suppression du proxy FranceConnect en production [#826].

### Évolutions techniques
- **Réplication de la base de données :** Amélioration des tests de réplication de la base de données et ajout d'une commande Django pour répliquer les utilisateurs [#791].
- **Cache :** Ajout de mécanismes de cache pour améliorer les performances, notamment pour les requêtes d'agenda et les vacances scolaires [#508].
- **Configuration :** Migration des variables d'environnement vers le fichier de configuration pour une meilleure gestion et sécurité [#609].
- **Logs :** Ajout d'en-têtes dans les logs des erreurs d'API Part pour faciliter le débogage.
- **Refactoring :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans la gestion des utilisateurs et des notifications.
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances (Django, cryptography, uv, pytest, etc.) pour bénéficier des dernières corrections et améliorations de sécurité.

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements apportés.
- **Linting :** Correction de plusieurs avertissements de linting dans le code front-end [#792].
- **Tests :** Ajout et mise à jour de tests unitaires pour garantir la qualité du code.
- **Suppression de code obsolète :** Suppression de code obsolète et de variables d'environnement inutilisées [#609].
- **Audit :** Ajout de logs d'audit pour les changements de rôle des utilisateurs [#609].
