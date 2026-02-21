## Changelog : st-home (30 derniers jours)

### Résumé
Les dernières mises à jour de st-home améliorent l'expérience utilisateur avec de nouvelles fonctionnalités de cartographie et de visualisation de données, notamment la possibilité de cliquer sur les zones voisines sur la carte et un graphique d'historique amélioré. Des améliorations techniques ont également été apportées pour optimiser les performances et la gestion de l'infrastructure.

### Évolutions fonctionnelles
- Amélioration du graphique d'historique (#50)
- Possibilité de cliquer sur les zones voisines sur la carte (#51)
- Ajout d'un bloc de recherche de communes dans le CMS (#50)
- Mise à jour des statistiques affichées sur la page d'accueil.
- Correction de la taille des informations affichées dans les services (#50)

### Évolutions techniques
- Mise à jour de Next.js vers la dernière version (#50)
- Ajout d'une commande `make db-restore` pour restaurer la base de données à partir d'une sauvegarde de production.
- Configuration de Nginx en front-end de Next.js avec une blocklist dynamique (#52)
- Désactivation des logs Nginx et utilisation des logs du routeur Scalingo (#53)

### Autres changements
- Documentation de la commande `make db-restore` dans le README (#50)
- Mise à jour des actions GitHub pour utiliser les dernières versions (#54)
