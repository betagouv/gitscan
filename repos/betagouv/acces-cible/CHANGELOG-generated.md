## Changelog : acces-cible (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des URLs des sites web, l'ajout de fonctionnalités d'export CSV plus flexibles, et la maintenance générale de la base de code. Des corrections de traductions et des améliorations de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger un CSV filtré. [#513](https://github.com/betagouv/acces-cible/issues/513)
- Ajout des colonnes `url` et `normalized_url` à la table `sites` pour une meilleure gestion des adresses web. [#529](https://github.com/betagouv/acces-cible/issues/529)
- Ajout du BOM UTF-8 aux exports CSV pour une meilleure compatibilité avec les logiciels de tableur. [#520](https://github.com/betagouv/acces-cible/issues/520)

### Évolutions techniques
- Sécurisation du rendu des URLs externes et suppression d'un ignore Brakeman lié à une potentielle vulnérabilité XSS. [#508](https://github.com/betagouv/acces-cible/issues/508)
- Mise à jour de la gem `dsfr-view-components`. [#518](https://github.com/betagouv/acces-cible/issues/518) et [#2d48278](https://github.com/betagouv/acces-cible/commit/2d48278)
- Mise à jour de Puma vers la version 8.0.1. [#540](https://github.com/betagouv/acces-cible/issues/540)
- Remplacement de `client_max_limit` par `max_limit` dans la gem `pagy` pour corriger une dépréciation. [#533](https://github.com/betagouv/acces-cible/issues/533)
- Ajout de la gem `i18-tasks` pour la gestion des traductions et suppression des traductions inutilisées.
- Nettoyage du code mort et des dépendances inutilisées. [#542](https://github.com/betagouv/acces-cible/issues/542)

### Autres changements
- Correction d'une traduction invalide pour les années. [#521](https://github.com/betagouv/acces-cible/issues/521)
- Plusieurs tentatives de migration pour backfiller les URLs des sites, avec des reverts et ajustements. [#530](https://github.com/betagouv/acces-cible/issues/530), [#553](https://github.com/betagouv/acces-cible/issues/553), [#554](https://github.com/betagouv/acces-cible/issues/554), [#555](https://github.com/betagouv/acces-cible/issues/555), [#556](https://github.com/betagouv/acces-cible/issues/556), [#557](https://github.com/betagouv/acces-cible/issues/557), [#558](https://github.com/betagouv/acces-cible/issues/558)
- Mises à jour de plusieurs dépendances mineures. [#549](https://github.com/betagouv/acces-cible/issues/549), [#523](https://github.com/betagouv/acces-cible/issues/523), [#546](https://github.com/betagouv/acces-cible/issues/546)
