## Changelog : st-home (30 derniers jours, au 30 avril 2026)

### Résumé
Les dernières mises à jour de st-home se concentrent sur l'amélioration de la carte de déploiement, l'intégration de nouvelles données (notamment de DILA), et l'optimisation de l'affichage des services et des partenaires. Des améliorations techniques ont également été apportées, notamment le remplacement de Nginx par Caddy et des ajustements de la planification des mises à jour de la base de données.

### Évolutions fonctionnelles

- **Carte de déploiement (Deploymap) v2 :** Nouvelle version de la carte de déploiement avec affichage des services, des EPCI et d'autres informations. [#56](https://github.com/suitenumerique/st-home/issues/56)
- **Affichage des services :**
    - Correction de l'affichage des services visibles dans la liste des services d'une commune. [#62](https://github.com/suitenumerique/st-home/issues/62)
    - Séparation des services en deux catégories : socle et écosystème.
    - Amélioration de la gestion des différents niveaux d'affichage des services.
- **Partenaires :** Ajout d'une nouvelle page dédiée aux partenaires OPSN. [#58](https://github.com/suitenumerique/st-home/issues/58)
- **Données :** Mise à jour pour utiliser le nouveau format d'export de données de DILA. [#64](https://github.com/suitenumerique/st-home/issues/64)
- **Réorganisation des services :** Réorganisation de l'ordre des services provenant d'OPSNs.
- **Textes :** Mise à jour des textes sur les pages RPNT et OPSN.

### Évolutions techniques

- **Infrastructure :** Remplacement de Nginx par Caddy comme reverse proxy. [#58](https://github.com/suitenumerique/st-home/issues/58)
- **Base de données :**
    - Ajout d'une commande de restauration de base de données à distance.
    - Mise à jour de la base de données toutes les 4 heures.
- **Logs :** Désactivation des logs d'accès de Caddy et utilisation des logs du routeur Scalingo. [#59](https://github.com/suitenumerique/st-home/issues/59)
- **Refactoring :** Regroupement des blocs de services en un seul bloc de service.

### Autres changements

- Correction d'un bug dans l'export CSV pour les niveaux groupés dans les statistiques.
- Suppression d'un affichage prématuré des OPSN avant l'étape d'intention.
- Suppression de `console.log` inutiles.
- Utilisation des données du `deploycenter` pour la carte des partenaires.
