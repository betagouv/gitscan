## Changelog : st-home (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, l'application st-home a bénéficié d'améliorations significatives, notamment une refonte de la carte de déploiement avec l'ajout de nouvelles données (services, EPCI), une mise à jour des données des collectivités et des corrections de bugs pour une meilleure expérience utilisateur. L'infrastructure a également été modernisée avec le remplacement de Nginx par Caddy.

### Évolutions fonctionnelles
- **Carte de déploiement (Deploymap) v2 :** Nouvelle version de la carte de déploiement avec affichage des services, des EPCI et d'autres informations pertinentes. [#56](https://github.com/suitenumerique/st-home/issues/56)
- **Affichage des services :** Amélioration de l'affichage des services dans la liste des services d'une commune, ne montrant que les services visibles. [#62](https://github.com/suitenumerique/st-home/issues/62)
- **Niveaux d'affichage :** Gestion des différents niveaux d'affichage sur la carte de déploiement. [#56](https://github.com/suitenumerique/st-home/issues/56)
- **Page partenaires OPSN :** Ajout d'une nouvelle page dédiée aux partenaires OPSN.
- **Ordre des services :** Réorganisation des services provenant des OPSN.
- **Séparation des services :** Distinction entre les services de base et l'écosystème.
- **Données DILA :** Mise à jour pour utiliser le nouveau format d'export de données de DILA.
- **Export CSV des statistiques :** Correction de l'export CSV pour les niveaux groupés. [#59](https://github.com/suitenumerique/st-home/issues/59)

### Évolutions techniques
- **Remplacement de Nginx par Caddy :** Nginx a été remplacé par Caddy comme reverse proxy pour améliorer les performances et la configuration. [#58](https://github.com/suitenumerique/st-home/issues/58)
- **Refonte des services :** Regroupement des blocs de services en un seul bloc pour une meilleure organisation. [#64](https://github.com/suitenumerique/st-home/issues/64)
- **Commande de restauration de la base de données :** Ajout d'une nouvelle commande pour restaurer la base de données à partir d'une sauvegarde distante.
- **Mise à jour de la base de données :** La base de données est maintenant mise à jour toutes les 4 heures.
- **Désactivation des logs d'accès Caddy :** Désactivation des logs d'accès de Caddy et utilisation des logs du routeur Scalingo.

### Autres changements
- **CMS :** Mise à jour vers la dernière version de Docs et correction des styles pour les blocs de citation et les résumés.
- **CMS :** Assouplissement de la détection du frontmatter.
- **Suppression de logs de débogage :** Suppression des `console.log` inutiles.
- **Correction de l'affichage des OPSN :** Suppression de l'affichage des OPSN avant l'étape d'intention.
- **Utilisation des données du Deploycenter :** Utilisation des données du Deploycenter pour la carte des partenaires.
