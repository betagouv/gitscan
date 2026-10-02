## Changelog : st-ansible (30 derniers jours, au 01/10/2026)

### Résumé
Ce mois-ci a été marqué par la sortie de la version 0.4.0, apportant des fonctionnalités clés comme le support de l'application "Projets" et des améliorations significatives de l'outil en ligne de commande (CLI). La sécurité a également été renforcée, notamment par la gestion des accès aux interfaces d'administration, tandis que l'architecture réseau a été optimisée pour une meilleure intégration avec Caddy.

### Évolutions fonctionnelles
- **Nouvelles applications** : Ajout du support pour l'application "Projets".
- **Amélioration de la CLI** : Optimisation du processus de mise à jour et ajout de la commande `rebootstrap`.
- **Sécurité** : Mise en place d'une liste blanche d'adresses IP (allowlist) pour sécuriser l'accès aux interfaces d'administration Django (notamment pour Drive et Meet).
- **Messagerie** : Introduction du nouveau composant `pymta` et dépréciation de l'ancien composant `mta-in`.

### Évolutions techniques
- **Architecture & Réseau** : 
    - Migration de l' "edge" vers Caddy pour le composant Drive.
    - Support de Caddy en tant que proxy frontal pour l'image `messages-keycloak`.
- **Qualité du code** : Refactoring de la CLI pour éliminer le code mort et les doublons, et application de nouvelles règles de qualité via Ruff.
- **CI/CD** : Mise à jour des empreintes (digests) des GitHub Actions pour renforcer la sécurité des pipelines.

### Autres changements
- **Documentation** : Publication de la procédure officielle de publication (release) destinée aux mainteneurs.
