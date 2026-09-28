## Changelog : st-ansible (30 derniers jours, au 19 septembre 2026)

### Résumé
Le projet a franchi une étape importante avec la publication de la version 0.4.0. Les évolutions récentes apportent le support d'une nouvelle application (projects), améliorent l'expérience de gestion via l'outil en ligne de commande (CLI) et renforcent la sécurité des accès aux interfaces d'administration.

### Évolutions fonctionnelles
- Ajout de la prise en charge de l'application "projects".
- Amélioration de l'outil en ligne de commande (CLI) : optimisation du processus de mise à jour et ajout de la commande `rebootstrap`.
- Renforcement de la sécurité : mise en place d'une liste blanche d'adresses IP (allowlist) pour l'accès aux interfaces d'administration Django via Caddy (concernant les services Drive et Meet).

### Évolutions techniques
- Migration de l'edge du service Drive vers Caddy.
- Amélioration de la qualité du code de la CLI : nettoyage du code mort, suppression des doublons et application de nouvelles règles de linting (Ruff).

### Autres changements
- Documentation de la procédure de publication (release) destinée aux mainteneurs.
