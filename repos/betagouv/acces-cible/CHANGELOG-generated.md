## Changelog : acces-cible (30 derniers jours, au 04 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'export de données, la correction de bugs liés à la gestion des URLs et des traductions, ainsi que sur des optimisations techniques pour la sécurité et la maintenance du code. Une nouvelle fonctionnalité permet désormais de télécharger des fichiers CSV filtrés.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger un fichier CSV filtré. [#513](https://github.com/betagouv/acces-cible/issues/513)
- Ajout du BOM UTF-8 aux exports CSV pour une meilleure compatibilité avec les logiciels de tableur. [#520](https://github.com/betagouv/acces-cible/issues/520)
- Correction de la recherche du taux d'accessibilité. [#509](https://github.com/betagouv/acces-cible/issues/509)
- Gestion améliorée des URLs invalides lors de l'import de fichiers CSV. [#504](https://github.com/betagouv/acces-cible/issues/504)

### Évolutions techniques
- Sécurisation du rendu des URLs externes pour prévenir les failles XSS. [#508](https://github.com/betagouv/acces-cible/issues/508)
- Mise à jour de la gem `dsfr-view-components`. [#518](https://github.com/betagouv/acces-cible/issues/518)
- Mise à jour de la gem `pagy` pour utiliser `max_limit` au lieu de `client_max_limit` (déprécié). [#533](https://github.com/betagouv/acces-cible/issues/533)
- Ajout de la gem `i18-tasks` pour la gestion des traductions.
- Suppression des traductions inutilisées.
- Correction d'une traduction invalide pour les années. [#521](https://github.com/betagouv/acces-cible/issues/521)
- Ajout d'une commande `make test` pour faciliter l'exécution des tests. [#499](https://github.com/betagouv/acces-cible/issues/499)
- Ajout des champs `url` et `normalized_url` aux sites. [#529](https://github.com/betagouv/acces-cible/issues/529)
