## Changelog : st-home (30 derniers jours, au 26 avril 2026)

### Résumé
Ce mois-ci, l'application st-home a bénéficié d'améliorations significatives, notamment le déploiement d'une nouvelle version de la carte de déploiement avec plus d'informations (services, EPCI, etc.), l'ajout d'une page dédiée aux partenaires OPSN et des corrections de données et d'affichage. Des optimisations techniques ont également été apportées, comme le remplacement de Nginx par Caddy et la configuration des logs.

### Évolutions fonctionnelles
- Ajout d'une page listant les partenaires OPSN. [#58](https://github.com/suitenumerique/st-home/issues/58)
- Nouvelle version de la carte de déploiement (v2) affichant les services, les EPCI et d'autres informations. [#56](https://github.com/suitenumerique/st-home/issues/56)
- Amélioration de l'affichage des niveaux sur la carte de déploiement. [#62](https://github.com/suitenumerique/st-home/issues/62)
- Ajout d'une nouvelle entrée de menu pour la carte de déploiement.
- Mise à jour des textes dans les pages RPNT et OPSN pour une meilleure clarté.
- Correction de l'affichage des données OPSN, qui n'étaient pas visibles avant l'étape d'intention.
- Correction de l'export CSV pour les statistiques groupées par niveau.

### Évolutions techniques
- Remplacement de Nginx par Caddy comme reverse proxy pour améliorer les performances et la configuration. [#58](https://github.com/suitenumerique/st-home/issues/58)
- Désactivation des logs d'accès de Caddy et utilisation des logs du routeur Scalingo. [#59](https://github.com/suitenumerique/st-home/issues/59)
- Mise à jour de la base de données toutes les 4 heures.
- Ajout d'une commande de restauration de base de données distante.
- Utilisation des données du centre de déploiement pour la carte des partenaires.
- Passage au nouveau format d'export de données de DILA.

### Autres changements
- Suppression des logs de console inutiles.
- Correction d'un bug dans le code.
