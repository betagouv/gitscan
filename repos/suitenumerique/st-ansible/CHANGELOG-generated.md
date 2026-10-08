## Changelog : st-ansible (30 derniers jours, au 01/10/2026)

### Résumé
La version 0.4.0 a été publiée. Cette mise à jour apporte des améliorations à l'outil de commande (CLI), renforce la sécurité des accès aux interfaces d'administration et optimise l'architecture réseau de certains services grâce à l'utilisation de Caddy.

### Évolutions fonctionnelles
- Amélioration de l'outil de commande (CLI) : ajout de la commande `rebootstrap` et optimisation du processus de mise à jour.
- Messagerie : introduction du composant `pymta` et dépréciation de `mta-in`.
- Sécurité : ajout de la possibilité de restreindre l'accès aux interfaces d'administration Django (`docs`, `drive` et `meet`) via une liste blanche d'adresses IP.

### Évolutions techniques
- Architecture réseau : migration de l'accès "edge" vers Caddy pour le service `drive` et support de Caddy en amont de l'image `messages-keycloak`.
- CI/CD : mise à jour des empreintes (digests) des GitHub Actions.

### Autres changements
- Qualité du code : nettoyage de l'outil CLI (suppression de code mort et de doublons) et application des règles de linting Ruff.
