## Changelog : acces-cible (30 derniers jours, au 11 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des URLs des sites web, l'export de données au format CSV, la sécurité et la maintenance technique de l'application. Des correctifs de traduction et la suppression de traductions inutilisées ont également été effectués.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger un CSV filtré. [#513](https://github.com/betagouv/acces-cible/issues/513)
- Ajout du BOM UTF-8 aux exports CSV pour une meilleure compatibilité avec les logiciels de tableur. [#520](https://github.com/betagouv/acces-cible/issues/520)
- Ajout des colonnes `url` et `normalized_url` à la table `sites` pour une gestion plus précise des URLs. [#529](https://github.com/betagouv/acces-cible/issues/529)

### Évolutions techniques
- Mise à jour de la gem `dsfr-view-components`. [#518](https://github.com/betagouv/acces-cible/issues/518) et [#2d48278](https://github.com/betagouv/acces-cible/commit/2d48278)
- Mise à jour de Puma de la version 7.2.0 à la version 8.0.1. [#540](https://github.com/betagouv/acces-cible/issues/540)
- Sécurisation du rendu des URLs externes et suppression d'une alerte Brakeman concernant une potentielle vulnérabilité XSS. [#508](https://github.com/betagouv/acces-cible/issues/508)
- Mise à jour de la gem `pagy` pour corriger une dépréciation. [#533](https://github.com/betagouv/acces-cible/issues/533)
- Ajout de la gem `i18-tasks` pour la gestion des traductions et suppression des traductions inutilisées.
- Plusieurs mises à jour de dépendances mineures ont été appliquées. [#549](https://github.com/betagouv/acces-cible/issues/549), [#546](https://github.com/betagouv/acces-cible/issues/546), [#523](https://github.com/betagouv/acces-cible/issues/523)

### Autres changements
- Correction d'une traduction invalide pour les années. [#521](https://github.com/betagouv/acces-cible/issues/521)
- Tentatives de migration pour backfiller les URLs des sites, avec plusieurs reverts dus à des problèmes. [#557](https://github.com/betagouv/acces-cible/issues/557), [#556](https://github.com/betagouv/acces-cible/issues/556), [#555](https://github.com/betagouv/acces-cible/issues/555), [#554](https://github.com/betagouv/acces-cible/issues/554), [#553](https://github.com/betagouv/acces-cible/issues/553), [#551](https://github.com/betagouv/acces-cible/issues/551), [#530](https://github.com/betagouv/acces-cible/issues/530)
