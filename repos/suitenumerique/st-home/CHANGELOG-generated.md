## Changelog : st-home (30 derniers jours)

### Résumé
Les dernières mises à jour de st-home améliorent la sécurité, l'expérience utilisateur et la gestion de l'infrastructure. Des améliorations ont été apportées à la cartographie interactive, à la présentation des statistiques et à la restauration de la base de données. L'ajout d'un bloc de recherche de communes au CMS permet une plus grande flexibilité dans la configuration de la page d'accueil.

### Évolutions fonctionnelles
- Amélioration du graphique d'historique (#50) pour une meilleure visualisation des données.
- Les zones voisines sur la carte sont désormais cliquables (#51), offrant une nouvelle interaction avec les données géographiques.
- Ajout d'un bloc de recherche de communes au CMS (#50), permettant de personnaliser la page d'accueil avec une recherche de communes.
- Mise à jour des statistiques affichées sur la page d'accueil pour refléter des informations plus récentes et pertinentes.

### Évolutions techniques
- Mise à jour des actions GitHub pour utiliser les dernières versions (#54), améliorant la sécurité et la stabilité du CI/CD.
- Ajout d'une commande `make db-restore` pour faciliter la restauration de la base de données à partir d'une sauvegarde de production.
- Configuration de Nginx en front-end de Next.js avec une blocklist dynamique (#52) pour améliorer la sécurité et les performances.
- Désactivation des logs Nginx et utilisation des logs du routeur Scalingo (#53) pour simplifier la gestion des logs.
- Mise à jour de Next.js vers la dernière version (#90a8029) pour bénéficier des dernières améliorations et corrections de bugs.
- Correction de la taille des informations affichées dans les services (#9a5c922).
- Prévention de l'utilisation d'URLs potentiellement non sécurisées provenant de DILA (#25f3fab).

### Autres changements
- Documentation de la commande `make db-restore` dans le fichier README (#9100e98).
