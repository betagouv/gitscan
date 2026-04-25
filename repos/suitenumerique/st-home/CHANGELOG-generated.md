## Changelog : st-home (30 derniers jours, au 24 avril 2026)

### Résumé
Les dernières mises à jour de st-home se concentrent sur l'amélioration de la carte de déploiement avec de nouvelles données et fonctionnalités, l'ajout d'une page dédiée aux partenaires OPSN, et des corrections de bugs concernant l'affichage des données et l'export CSV. L'infrastructure a également été modernisée avec le remplacement de Nginx par Caddy.

### Évolutions fonctionnelles
- Ajout d'une nouvelle page listant les partenaires OPSN. [#58](https://github.com/suitenumerique/st-home/issues/58)
- Nouvelle version de la carte de déploiement (v2) incluant des informations sur les services et les EPCI. [#56](https://github.com/suitenumerique/st-home/issues/56)
- Amélioration de la gestion des différents niveaux d'affichage sur la carte de déploiement.
- Ajout d'une nouvelle entrée de menu pour le déploiement.
- Mise à jour des textes dans les pages RPNT et OPSN pour une meilleure clarté.
- Correction de l'affichage des données OPSN, qui n'était pas visible avant l'étape d'intention.
- Correction de l'export CSV pour les statistiques groupées par niveau.

### Évolutions techniques
- Remplacement de Nginx par Caddy comme reverse proxy pour améliorer la performance et la simplicité de configuration. [#58](https://github.com/suitenumerique/st-home/issues/58)
- Désactivation des logs d'accès Caddy et utilisation des logs du routeur Scalingo. [#59](https://github.com/suitenumerique/st-home/issues/59)
- Mise à jour de la fréquence de mise à jour de la base de données à toutes les 4 heures.
- Ajout d'une commande pour restaurer la base de données à distance.

### Autres changements
- Suppression des logs de débogage (console.log) dans le code.
- Utilisation des données du centre de déploiement pour la carte des partenaires.
