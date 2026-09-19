## Changelog : st-ansible (30 derniers jours, au 18 septembre 2026)

### Résumé
Cette période a été marquée par l'élargissement des capacités de déploiement avec l'ajout du support pour les applications Projets et Documentation. L'outil de gestion en ligne de commande (CLI) a été amélioré pour rendre les mises à jour et les réinstallations plus fluides, tandis que l'infrastructure de l'application Drive a été modernisée.

### Évolutions fonctionnelles
- **Nouvelles applications** : Ajout du support complet pour l'application **Projects** et du rôle **Docs** (incluant le support du bootstrap via `st-cli`).
- **Amélioration du CLI** : Optimisation du processus de mise à jour et ajout de la commande `rebootstrap` pour faciliter la réinitialisation des environnements.

### Évolutions techniques
- **Architecture Drive** : Migration de la couche "edge" vers Caddy pour une gestion plus robuste du trafic.
- **Mises à jour de composants** : Montée de version des applications et services clés :
    - Drive (0.22.0) et Collabora (26.04.3.2.1).
    - Meet (1.29.0) et LiveKit (1.13.6).

### Autres changements
- **Documentation** : Ajout de la documentation relative à la procédure de release pour les mainteneurs.
- **Maintenance** : Mise à jour de la dépendance pour la documentation (v5.5.0).
