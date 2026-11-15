## Changelog : ami-notifications-api (30 derniers jours, au 13 novembre 2026)

### Résumé
Ce mois-ci, l'API a franchi des étapes importantes en matière de conformité et de fonctionnalités. L'accent a été mis sur la gestion du consentement aux données personnelles, l'intégration de l'annuaire des communes et une amélioration globale de l'interface utilisateur ainsi que de la sécurité des connexions.

### Évolutions fonctionnelles
- **Gestion du consentement** : Mise en place d'un système complet pour gérer le consentement aux données personnelles (nouveau modèle, nouveaux points de terminaison et intégration de l'interface dans le profil, les préférences et l'édition d'adresse) [#1214](https://github.com/numerique-gouv/ami-notifications-api/issues/1214).
- **Annuaire des communes** : Intégration de la gestion des mairies dans le profil utilisateur et l'annuaire [#1078](https://github.com/numerique-gouv/ami-notifications-api/issues/1078).
- **Améliorations de l'interface (UI/UX)** :
    - Affichage des titres au lieu du corps de texte pour les éléments de suivi [#1661](https://github.com/numerique-gouv/ami-notifications-api/issues/1661).
    - Ajout de titres pour les notices et masquage d'informations inutiles pour respecter les standards RGAA [#1664](https://github.com/numerique-gouv/ami-notifications-api/issues/1664), [#1665](https://github.com/numerique-gouv/ami-notifications-api/issues/1665).
    - Corrections de liens de navigation (auto-promo, JCC) et de styles visuels [#1673](https://github.com/numerique-gouv/ami-notifications-api/issues/1673), [#1281](https://github.com/numerique-gouv/ami-notifications-api/issues/1281).
    - Possibilité d'ajouter des liens externes aux sous-éléments [#1611](https://github.com/numerique-gouv/ami-notifications-api/issues/1611).
    - Clarification des messages d'erreur lors de l'authentification [#1594](https://github.com/numerique-gouv/ami-notifications-api/issues/1594).

### Évolutions techniques
- **Sécurité et Authentification** :
    - Renforcement de la sécurité des redirections après connexion et validation des URIs autorisés [#1617](https://github.com/numerique-gouv/ami-notifications-api/issues/1617).
    - Sécurisation du flux d'authentification par passkey pour empêcher le retour arrière du navigateur [#1593](https://github.com/numerique-gouv/ami-notifications-api/issues/1593).
- **Infrastructure et Backend** :
    - Mise à jour de l'environnement vers Python 3.14 [#1642](https://github.com/numerique-gouv/ami-notifications-api/issues/1642).
    - Optimisation de la synchronisation des données des mairies via un processus quotidien (cron) [#1614](https://github.com/numerique-gouv/ami-notifications-api/issues/1614).
    - Amélioration de la logique de statut des éléments de suivi [#1663](https://github.com/numerique-gouv/ami-notifications-api/issues/1663).
    - Modification de la gestion des utilisateurs : archivage des inscriptions au lieu de leur suppression [#1602](https://github.com/numerique-gouv/ami-notifications-api/issues/1602).
- **Refactoring et Architecture** :
    - Refonte majeure des composants de fenêtres modales (modals) pour améliorer la structure et la maintenance du front-end [#1430](https://github.com/numerique-gouv/ami-notifications-api/issues/1430).
    - Modularisation de certains blocs d'interface (ex: bloc situation) [#1656](https://github.com/numerique-gouv/ami-notifications-api/issues/1656).
    - Optimisation de la navigation interne pour éviter les boucles de redirection [#1452](https://github.com/numerique-gouv/ami-notifications-api/issues/1452).

### Autres changements
- **Maintenance** : Mise à jour de l'outil de pré-commit [#1679](https://github.com/numerique-gouv/ami-notifications-api/issues/1679) et nettoyage de la suite de tests CI (suppression des tests E2E d'exemple) [#1639](https://github.com/numerique-gouv/ami-notifications-api/issues/1639).
