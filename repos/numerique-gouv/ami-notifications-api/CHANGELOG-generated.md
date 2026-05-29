## Changelog : ami-notifications-api (30 derniers jours, au 27 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations concernant l'intégration avec FranceConnect et l'implémentation d'une nouvelle fonctionnalité "FI" (probablement une intégration spécifique). Des corrections et améliorations ont également été apportées à l'interface utilisateur, notamment au niveau de la gestion des utilisateurs et des notifications, ainsi qu'à la robustesse et la configuration de l'application.

### Évolutions fonctionnelles
- **Gestion des utilisateurs (Agent Admin):** Ajout de fonctionnalités pour la gestion des utilisateurs dans l'interface d'administration, incluant la recherche, la consultation des détails, la suppression et la gestion des droits.  Des messages d'erreur plus clairs ont été ajoutés en cas d'échec de requête. [#773]
- **Notifications:** Amélioration de l'affichage des notifications, notamment l'ajout d'un champ "corps privé" pour les notifications, permettant de stocker des informations sensibles. [#875]
- **Intégration FranceConnect (FC) et "FI":** Implémentation d'une nouvelle intégration "FI" avec gestion de l'authentification, de l'autorisation, de la déconnexion et de la gestion des sessions utilisateurs.  Amélioration de la gestion de la déconnexion de FranceConnect avant la connexion "FI". [#708]
- **Notifications OTV:**  Ajout de la date dans les paramètres des notifications planifiées pour les OTV (Objets de Transmission de Valeurs). [#852]
- **Gestion des zones:** Amélioration de l'affichage et de la gestion des zones géographiques dans l'interface utilisateur, notamment pour les alertes et les notifications. [#802]
- **Suppression des notifications:** Désactivation des notifications lors de la déconnexion de l'utilisateur. [#721]

### Évolutions techniques
- **Réplication:** Amélioration de la gestion de la réplication des données, avec ajout de tests et de logs plus précis. [#791]
- **Configuration:**  Simplification de la configuration de l'application, notamment en supprimant des variables d'environnement inutiles et en améliorant la gestion des certificats SSL locaux avec `mkcert`. [#826, #828]
- **Dépendances:** Mise à jour de plusieurs dépendances, notamment Django (6.0.5), urllib3 et Twisted.
- **Architecture Frontend:** Refonte de l'architecture frontend avec l'introduction de composants réutilisables comme `PageWrapper` pour une meilleure organisation et une mise en page plus cohérente. [#801]
- **Matomo:** Ajout du suivi des zones de vacances (holiday zones) dans Matomo pour une meilleure analyse de l'utilisation. [#750]
- **Suppression de code obsolète:** Suppression du code lié à la fonctionnalité "requests enabled" qui n'est plus utilisée. [#823]

### Autres changements
- **Interface utilisateur:** Amélioration de l'interface utilisateur avec des messages toast standardisés et un positionnement amélioré. [#723]
- **Documentation:**  Amélioration de la documentation et des commentaires dans le code.
- **Nettoyage du code:** Suppression de dossiers et fichiers inutiles.
- **Tests:** Ajout et amélioration des tests unitaires et d'intégration.
- **Audit:** Ajout d'entrées d'audit pour les actions de gestion des utilisateurs dans l'interface d'administration. [#774]
