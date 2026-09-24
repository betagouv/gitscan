## Changelog : tchap-web-v4 (30 derniers jours, au 23 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur via une interface plus claire et des messages d'erreur plus explicites, tout en renforçant la confidentialité et la fiabilité de l'application grâce à de nouveaux mécanismes de récupération de données.

### Évolutions fonctionnelles
- **Amélioration de l'interface et de la navigation** :
    - Ajout d'un badge "recommandé" lors de la création de nouveaux salons ([#1675](https://github.com/tchapgouv/tchap-web-v4/pull/1675)).
    - Clarification de l'interface avec le renommage du menu en "Support" ([#1664](https://github.com/tchapgouv/tchap-web-v4/pull/1664)) et mise à jour des titres des réglages rapides.
- **Confidentialité et sécurité** :
    - Masquage du numéro de téléphone dans les paramètres utilisateur pour renforcer la protection des données ([#1666](https://github.com/tchapgouv/tchap-web-v4/pull/1666)).
    - Ajout de messages d'erreur explicites lors des échecs d'authentification OIDC ([#1671](https://github.com/tchapgouv/tchap-web-v4/pull/1671)).
- **Corrections d'utilisation** :
    - Résolution d'un problème empêchant l'ouverture correcte des liens de service Gaufre sur la version desktop ([#1674](https://github.com/tchapgouv/tchap-web-v4/pull/1674)).

### Évolutions techniques
- **Fiabilité du système** :
    - Ajout d'un mécanisme de tentatives automatiques (retry) lors de la récupération de l'adresse du serveur (homeserver) via l'e-mail, améliorant la résilience de la connexion ([#1668](https://github.com/tchapgouv/tchap-web-v4/pull/1668)).
- **Optimisation** :
    - Nettoyage des journaux (logs) de l'application Tauri.

### Autres changements
- Mise à jour de la documentation (README).
- Maintenance du code via l'application des règles de formatage Prettier.
