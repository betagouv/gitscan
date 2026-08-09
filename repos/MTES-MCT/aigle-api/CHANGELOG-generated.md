## Changelog : aigle-api (30 derniers jours, au 06/08/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration des outils de pilotage (tableau de bord DDT) et la fiabilisation de la gestion des données géospatiales. Des optimisations importantes ont été apportées à la gestion des zones et à la précision des droits d'accès pour garantir une exploitation plus sûre et performante des détections.

### Évolutions fonctionnelles
- **Visualisation et administration :**
    - Amélioration du tableau de bord DDT.
    - Optimisation de la gestion de l'écrasement des groupes dans l'interface d'administration.
- **Sécurité et accès :**
    - Renforcement du contrôle des permissions : l'accès et la modification des détections sont désormais basés sur l'identifiant de la commune (au lieu de la géométrie), offrant une gestion des droits plus robuste.
- **Gestion des zones :**
    - Mise en place de la fonctionnalité de blocage des zones urbaines.

### Évolutions techniques
- **Gestion des données et zones :**
    - Amélioration de la robustesse du processus d'importation des détections.
    - Optimisation de l'assignation des zones/ZAE lors de la création de groupes et du déploiement de données.
    - La commande `update_custom_zones` effectue désormais un nettoyage automatique des détections situées en dehors des zones personnalisées.
- **Optimisation des commandes système :**
    - Amélioration des performances de la commande `update_detectionobject_commune`.
    - Ajout d'un paramètre de forçage (`force`) pour la commande `update_detectionobject_commune`.
