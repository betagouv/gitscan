## Changelog : st-home (30 derniers jours)

### Résumé
Les dernières mises à jour de st-home améliorent la sécurité, l'expérience utilisateur et les capacités de gestion de la base de données. Des améliorations ont été apportées à la carte interactive, aux statistiques affichées sur la page d'accueil et à la recherche de communes. Des optimisations ont également été réalisées au niveau de l'infrastructure pour une meilleure performance et une gestion des logs plus efficace.

### Évolutions fonctionnelles
- Amélioration du graphique d'historique pour une meilleure lisibilité et une expérience utilisateur plus agréable. [#50](https://github.com/suitenumerique/st-home/issues/50)
- Les zones voisines sur la carte interactive sont désormais cliquables, offrant une nouvelle interaction pour l'exploration des données. [#51](https://github.com/suitenumerique/st-home/issues/51)
- Mise à jour des statistiques affichées sur la page d'accueil pour refléter des informations plus récentes et pertinentes.
- Ajout d'un bloc de recherche de communes au CMS, permettant une gestion plus facile du contenu.
- Implémentation d'une liste noire de domaines pour renforcer la sécurité et prévenir l'utilisation de liens potentiellement dangereux.
- Prévention de l'utilisation d'URLs potentiellement non sécurisées provenant de DILA.

### Évolutions techniques
- Mise à jour des étapes des workflows GitHub Actions pour bénéficier des dernières améliorations et corrections de bugs. [#54](https://github.com/suitenumerique/st-home/issues/54)
- Ajout d'une commande `make db-restore` pour faciliter la restauration de la base de données à partir d'une sauvegarde de production.
- Désactivation des logs Nginx et utilisation des logs du routeur Scalingo pour une gestion plus centralisée et efficace des logs. [#53](https://github.com/suitenumerique/st-home/issues/53)
- Ajout de Nginx en front-end de Next.js avec une liste noire dynamique pour une sécurité accrue. [#52](https://github.com/suitenumerique/st-home/issues/52)
- Correction de la taille des informations affichées dans les services.

### Autres changements
- Documentation de la commande `make db-restore` dans le fichier README.
