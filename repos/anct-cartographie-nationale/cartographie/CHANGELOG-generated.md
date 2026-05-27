## Changelog : cartographie (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, la cartographie nationale des lieux d’inclusion numérique a bénéficié d'améliorations significatives en termes de performance, notamment concernant l'affichage des horaires d'ouverture. De nouvelles fonctionnalités ont été ajoutées pour faciliter la recherche de lieux ouverts actuellement ou le week-end. Des améliorations ont également été apportées à l'infrastructure et à l'expérience utilisateur, comme l'ajout d'un bouton pour intégrer la carte et la gestion des erreurs dans les paramètres de recherche.

### Évolutions fonctionnelles
- Ajout de filtres pour afficher uniquement les lieux ouverts actuellement ou le week-end. Ces filtres utilisent une nouvelle méthode de calcul des horaires pour une meilleure performance.
- Ajout d'un bouton "Intégrer la carte" dans la barre de navigation, permettant d'intégrer facilement la carte sur d'autres sites web. Le bouton est associé à un suivi Matomo pour mesurer son utilisation.
- Amélioration de l'affichage du lien vers le site internet d'un lieu, qui est maintenant libellé "Site internet" pour plus de clarté.
- Amélioration de la navigation : utilisation de l'historique du navigateur pour revenir à la page précédente depuis la page de détail d'un lieu.

### Évolutions techniques
- Optimisation du chargement et du traitement des horaires d'ouverture pour améliorer les performances, notamment grâce à un parsing paresseux et un filtrage en deux passes.
- Mise à jour de l'infrastructure pour provisionner un domaine Scaleway TEM et injecter la configuration SMTP dans le conteneur.
- Mise à jour de pnpm en version 11 et ajustement de l'ordre d'initialisation de Node et pnpm dans les workflows CI/CD.
- Correction d'un problème lié à la gestion du paramètre `territoire_type` dans l'URL.

### Autres changements
- Correction temporaire d'un problème lié à la mise à jour du domaine TEM, puis annulation de cette correction.
- Correction d'un test qui dépendait de la timezone.
