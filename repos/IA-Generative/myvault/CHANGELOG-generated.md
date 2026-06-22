## Changelog : myvault (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la sécurité et la robustesse de myvault. De nombreuses corrections ont été apportées pour renforcer la protection contre les vulnérabilités, limiter les abus et améliorer la gestion des accès. Des améliorations fonctionnelles ont également été implémentées, notamment l'ajout de l'authentification à deux facteurs (2FA) et l'intégration de la définition d'application Résana.

### Évolutions fonctionnelles
- Ajout de l'authentification TOTP (Time-based One-Time Password) pour une sécurité renforcée avec l'authentification à deux facteurs (2FA).
- Intégration de la définition d'application Résana, permettant une meilleure compatibilité avec cet environnement.
- Ajout du logo MyVault (favicon et logo opérateur) pour une meilleure identification visuelle.

### Évolutions techniques
- Mise en place de garde-fous anti-leak pour prévenir les fuites d'informations sensibles.
- Limitation du débit (rate limiting) et protection de l'enrôlement des accès machine-to-machine (M2M) pour prévenir les attaques par force brute et les abus.
- Hachage des secrets M2M et renforcement de leur vérification pour une sécurité accrue.
- Validation des URL sortantes lors des tests de connexion pour éviter les redirections malveillantes.
- Restriction des méthodes et en-têtes CORS (Cross-Origin Resource Sharing) autorisés pour limiter les risques d'attaques cross-site scripting (XSS).
- Restriction de l'accès machine-to-machine à l'application du client pour une meilleure isolation.
- Durcissement de la configuration et du démarrage en production pour une meilleure stabilité et sécurité.
- Chiffrement du champ "notes" des entrées personnelles pour protéger les informations sensibles.
- Masquage du menu "Administration" pour les utilisateurs non-administrateurs.

### Autres changements
- Correction de vulnérabilités identifiées par Dependabot [#f38a1bf](https://github.com/IA-Generative/myvault/commit/f38a1bf).
- Correction d'une injection HTML potentielle dans l'extension et le widget [#95a10ef](https://github.com/IA-Generative/myvault/commit/95a10ef).
- Acceptation des jetons OIDC Keycloak via la partie autorisée (azp) [#6ac3ead](https://github.com/IA-Generative/myvault/commit/6ac3ead).
- Masquage du détail interne dans la sonde de disponibilité [#6ff422c](https://github.com/IA-Generative/myvault/commit/6ff422c).
- Checkpoint avant les correctifs de sécurité pour faciliter le suivi des modifications [#89ef875](https://github.com/IA-Generative/myvault/commit/89ef875).
- Épinglage de la version de `bcrypt` à une version sécurisée (<4.1) [#7614aeb](https://github.com/IA-Generative/myvault/commit/7614aeb).
