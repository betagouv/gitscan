## Changelog : ami-notifications-api (30 derniers jours, au 08/09/2026)

### Résumé
Ce mois-ci, l'API a franchi une étape majeure avec l'introduction de l'authentification par Passkey (WebAuthn), offrant une connexion plus simple et sécurisée. L'expérience de notification a été optimisée pour éviter les doublons et améliorer le support sur ordinateur, tandis que de nouveaux éléments visuels, comme le carrousel "AutoPromo", enrichissent l'interface utilisateur.

### Évolutions fonctionnelles
- **Authentification** : Introduction des Passkeys (WebAuthn) pour une connexion simplifiée et sécurisée [#1088](https://github.com/numerique-gouv/ami-notifications-api/issues/1088), gestion améliorée des erreurs de connexion et nouvelle vue de reconnexion [#1179](https://github.com/numerique-gouv/ami-notifications-api/issues/1179).
- **Notifications** : Suppression des doublons pour les notifications programmées [#839](https://github.com/numerique-gouv/ami-notifications-api/issues/839) et amélioration de la gestion des abonnements pour les appareils mobiles et les ordinateurs [#939](https://github.com/numerique-gouv/ami-notifications-api/issues/939).
- **Contenu et affichage** : Intégration d'un carrousel "AutoPromo" sur la page d'accueil [#1142](https://github.com/numerique-gouv/ami-notifications-api/issues/1142) et amélioration de la hiérarchie d'affichage pour le suivi des informations (follow-up) [#825](https://github.com/numerique-gouv/ami-notifications-api/issues/825).
- **Expérience utilisateur** : Amélioration de la navigation avec un nouveau bouton de retour [#1200](https://github.com/numerique-gouv/ami-notifications-api/issues/1200), gestion plus fluide des consentements [#911](https://github.com/numerique-gouv/ami-notifications-api/issues/911) et enrichissement visuel des services via l'ajout d'icônes [#1048](https://github.com/numerique-gouv/ami-notifications-api/issues/1048).

### Évolutions techniques
- **Sécurité** : Renforcement de la validation des jetons FranceConnect, support du format JWT pour les informations utilisateur [#1219](https://github.com/numerique-gouv/ami-notifications-api/issues/1219) et ajout du suivi Matomo pour les événements liés aux Passkeys [#1187](https://github.com/numerique-gouv/ami-notifications-api/issues/1187).
- **Architecture** : Migration de la base de données pour les champs partenaires [#1131](https://github.com/numerique-gouv/ami-notifications-api/issues/1131) et optimisation du routage (WebSockets, fichiers statiques et URLs de clés de notification) via Vite [#1138](https://github.com/numerique-gouv/ami-notifications-api/issues/1138).
- **Observabilité et CI/CD** : Intégration de Sentry pour le suivi des erreurs en production [#1240](https://github.com/numerique-gouv/ami-notifications-api/issues/1240) et automatisation du déclenchement des tests système dans les workflows GitHub Actions [#10](https://github.com/numerique-gouv/ami-notifications-api/issues/10).

### Autres changements
- **Maintenance** : Nettoyage du code (suppression de logs et de tests obsolètes) et corrections typographiques diverses.
