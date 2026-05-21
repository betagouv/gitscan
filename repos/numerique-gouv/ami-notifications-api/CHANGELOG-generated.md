## Changelog : ami-notifications-api (30 derniers jours, au 20 mai 2026)

### Résumé
Ce changelog couvre les dernières améliorations apportées à l'API ami-notifications-api, avec un focus sur l'interface utilisateur web (agent-admin et front) et l'ajout de nouvelles fonctionnalités pour la gestion des utilisateurs et des notifications. Des améliorations de performance et de maintenance ont également été réalisées, notamment concernant la réplication des données et la gestion des erreurs.

### Évolutions fonctionnelles
- **Gestion des utilisateurs (agent-admin):** Ajout de vues pour la recherche, la consultation, la suppression et la gestion des rôles des utilisateurs. Une interface de recherche avec autocomplétion a été implémentée.
- **Notifications:** Amélioration de l'affichage des notifications et ajout d'une confirmation de déconnexion via une modale.
- **Agenda et Vacances Scolaires:**  L'application affiche désormais les vacances scolaires en fonction des préférences de l'utilisateur (zones géographiques).  La configuration des zones de préférences utilisateur a été revue et améliorée.
- **Interface utilisateur:** Amélioration de la mise en page du bouton "gérer" dans l'écran des notifications et ajout d'un composant de wrapper de page pour une meilleure cohérence visuelle.
- **Suivi Matomo:** Ajout du suivi des zones de vacances scolaires dans Matomo pour l'analyse des données.

### Évolutions techniques
- **Réplication des données:**  Refonte de la logique de réplication des données avec ajout de commandes et de tests pour assurer la cohérence des données entre les instances.
- **Suppression de code obsolète:** Suppression de la fonctionnalité "requests enabled" qui n'était plus utilisée.
- **Mises à jour de dépendances:**  Mise à jour de plusieurs dépendances, notamment Django (6.0.5), pytest, lxml, uv, postcss, et uuid.
- **Amélioration de la gestion des erreurs:** Ajout de gestion des erreurs pour la réplication des données.
- **Cache HTTP:** Implémentation d'un cache HTTP pour les requêtes concernant les vacances scolaires.
- **Sécurité:** Utilisation de `mkcert` pour la gestion des certificats SSL en local.
- **Linting:** Correction de plusieurs avertissements de linting dans le code frontend.

### Autres changements
- **Documentation:** Mise à jour de la documentation CONTRIBUTING.md.
- **Tests:** Amélioration des tests et ajout de fixtures pour les tests de réplication.
- **Configuration:** Suppression de la variable d'environnement `PUBLIC_FC_PROXY` en production.
- **Nettoyage de code:** Suppression de `django-admin` et simplification des commandes de notifications planifiées.
- **Amélioration de l'UX:** Centrage vertical du bouton FranceConnect et défilement automatique du champ d'adresse lors de la focalisation.
