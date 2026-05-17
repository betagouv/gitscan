## Changelog : acces-cible (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des URLs des sites web, la correction de traductions et la maintenance technique de l'application. Des efforts ont été faits pour améliorer la sécurité et la qualité du code, notamment en supprimant du code mort et en corrigeant des vulnérabilités potentielles. L'export CSV a également été amélioré pour une meilleure compatibilité.

### Évolutions fonctionnelles
- Ajout des colonnes `url` et `normalized_url` à la table `sites` pour une meilleure gestion des adresses web. [#529](https://github.com/betagouv/acces-cible/issues/529)
- Ajout du BOM UTF-8 aux exports CSV pour une meilleure compatibilité avec les logiciels de tableur. [#520](https://github.com/betagouv/acces-cible/issues/520)
- Correction d'une erreur de traduction concernant les années. [#521](https://github.com/betagouv/acces-cible/issues/521)

### Évolutions techniques
- Sécurisation du rendu des URLs externes et suppression d'un ignore Brakeman lié à une potentielle vulnérabilité XSS. [#508](https://github.com/betagouv/acces-cible/issues/508)
- Mise à jour de la gem `pagy` pour utiliser `max_limit` au lieu de `client_max_limit` (déprécié). [#533](https://github.com/betagouv/acces-cible/issues/533)
- Nettoyage du code mort et des dépendances inutilisées. [#542](https://github.com/betagouv/acces-cible/issues/542)
- Ajout de la gem `i18-tasks` pour la gestion des traductions et suppression des traductions inutilisées.
- Plusieurs tentatives de migration pour backfiller les URLs des sites, avec des reverts et ajustements. [#530](https://github.com/betagouv/acces-cible/issues/530), [#553](https://github.com/betagouv/acces-cible/issues/553), [#557](https://github.com/betagouv/acces-cible/issues/557), [#558](https://github.com/betagouv/acces-cible/issues/558)

### Autres changements
- Mises à jour de dépendances : Puma (7.2.0 -> 8.0.1), et plusieurs autres gems. (via dependabot)
