## Changelog : st-home (30 derniers jours, au 2026-05-18)

### Résumé
Les dernières mises à jour de st-home se concentrent sur l'amélioration de l'expérience utilisateur, notamment en affinant la présentation des services et des partenaires, et en corrigeant des bugs liés à l'affichage des données et au CMS. Des optimisations techniques ont également été apportées pour améliorer la gestion de la base de données et la configuration du serveur.

### Évolutions fonctionnelles
- Ajout d'une nouvelle page listant les partenaires OPSN. [#59](https://github.com/suitenumerique/st-home/issues/59)
- Amélioration de l'affichage des services au niveau communal, en ne montrant que les services visibles. [#62](https://github.com/suitenumerique/st-home/issues/62)
- Réorganisation des services à partir des données OPSNs. [#64](https://github.com/suitenumerique/st-home/issues/64)
- Séparation des services en deux catégories : socle et écosystème.
- Ajout d'une nouvelle entrée de menu pour la fonctionnalité de déploiement.
- Restauration de l'affichage par défaut du bloc de service ANCT en cas de problème.
- Amélioration de la gestion des différents niveaux d'affichage sur la carte de déploiement.

### Évolutions techniques
- Mise à jour vers la dernière version du CMS et correction des styles pour les blocs de citation et les résumés.
- Modification du format d'import des données pour utiliser le nouveau format d'export de DILA.
- Ajout d'une commande pour restaurer la base de données à partir d'une sauvegarde distante.
- Mise à jour de la fréquence de mise à jour de la base de données à toutes les 4 heures.
- Désactivation des logs d'accès Caddy et utilisation des logs du routeur Scalingo.
- Suppression des logs de console inutiles.
- Simplification de la détection du frontmatter dans le CMS.
- Fusion des blocs de services en un seul bloc pour une meilleure organisation.

### Autres changements
- Suppression de l'affichage des OPSN avant l'étape d'intention.
- Relaxation de la détection du frontmatter dans le CMS pour plus de flexibilité.
