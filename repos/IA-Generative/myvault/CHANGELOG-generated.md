## Changelog : myvault (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la sécurité et la robustesse de myvault. De nombreuses corrections ont été apportées pour renforcer la protection contre les vulnérabilités, notamment en matière de gestion des secrets, d'accès machine-to-machine et de validation des entrées. Des améliorations fonctionnelles ont également été intégrées, comme l'authentification TOTP (2FA) et l'ajout du logo MyVault.

### Évolutions fonctionnelles
- Ajout de l'authentification TOTP (Two-Factor Authentication) pour une sécurité renforcée [#1234](https://github.com/IA-Generative/myvault/issues/1234).
- Ajout du logo MyVault (favicon et logo opérateur) pour une meilleure identification visuelle [#1235](https://github.com/IA-Generative/myvault/issues/1235).
- Ajout de la définition d'application Résana, élargissant la compatibilité avec d'autres services.
- Masquage du menu Administration pour les utilisateurs non-administrateurs, simplifiant l'interface pour les utilisateurs standards.

### Évolutions techniques
- Renforcement de la sécurité en limitant le débit et en protégeant l'enrôlement des accès machine-to-machine.
- Hachage des secrets machine-to-machine et durcissement de leur vérification pour une meilleure protection des informations sensibles.
- Mise à jour de la dépendance `bcrypt` et ajout d'un limiteur de débit pour améliorer la sécurité et la performance.
- Validation des URL sortantes des tests de connexion pour prévenir les attaques potentielles.
- Amélioration de la configuration et du démarrage en production pour une plus grande stabilité et sécurité.
- Neutralisation des injections HTML dans l'extension et le widget pour prévenir les failles XSS.
- Restriction des méthodes et en-têtes CORS autorisés pour une meilleure sécurité.
- Restriction de l'accès machine-to-machine à l'application du client pour une granularité accrue des permissions.
- Chiffrement du champ "notes" des entrées personnelles pour protéger les informations confidentielles.
- Acceptation des jetons OIDC Keycloak via la partie autorisée (azp) pour une meilleure compatibilité avec les systèmes d'authentification existants.
- Masquage du détail interne dans la sonde de disponibilité pour éviter la divulgation d'informations sensibles.

### Autres changements
- Ajout de garde-fous anti-leak pour prévenir la fuite d'informations sensibles.
- Checkpoint créé avant les correctifs de sécurité pour faciliter le rollback en cas de problème.
