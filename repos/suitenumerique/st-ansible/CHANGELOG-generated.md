## Changelog : st-ansible (30 derniers jours, au 01/10/2026)

### Résumé
Cette période a été marquée par la sortie de la version 0.4.0, apportant des améliorations de sécurité pour les interfaces d'administration, de nouveaux composants de messagerie et une optimisation de l'outil de commande (CLI) pour faciliter les mises à jour et les réinstallations du système.

### Évolutions fonctionnelles
- **Interface de commande (CLI) :** Amélioration du processus de mise à jour et ajout de la commande `rebootstrap` pour faciliter les réinstallations.
- **Sécurité :** Mise en place d'une liste blanche d'adresses IP (allowlist) pour sécuriser l'accès aux interfaces d'administration Django (concernant les services Docs, Drive et Meet).
- **Messagerie :** Introduction du nouveau composant `pymta` et dépréciation de l'ancien composant `mta-in`.

### Évolutions techniques
- **Architecture :** Migration de l'edge du service `drive` vers `caddy`.
- **Architecture :** Support de l'utilisation de Caddy en frontal de l'image `messages-keycloak`.
- **CI/CD :** Mise à jour des digests des GitHub Actions.

### Autres changements
- **Qualité du code :** Nettoyage de l'interface CLI (suppression du code mort et des doublons) et application des règles de linting Ruff.
