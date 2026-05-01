## Changelog : acces-cible (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'importation et l'exportation de données, la correction de bugs liés à la gestion des URLs et des fichiers CSV, ainsi que sur la sécurité et la maintenance technique de l'application. Une nouvelle fonctionnalité permet le téléchargement de CSV filtrés.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger un CSV filtré. [#513](https://github.com/betagouv/acces-cible/issues/513)
- Amélioration de la détection des liens externes. [#497](https://github.com/betagouv/acces-cible/issues/497)
- Ajout du BOM UTF-8 aux exports CSV pour une meilleure compatibilité avec les tableurs. [#520](https://github.com/betagouv/acces-cible/issues/520)
- Correction de la recherche du taux d'accessibilité. [#509](https://github.com/betagouv/acces-cible/issues/509)

### Évolutions techniques
- Sécurisation du rendu des URLs externes pour prévenir les failles XSS. [#508](https://github.com/betagouv/acces-cible/issues/508)
- Mise à jour de la gem `dsfr-view-components`. [#518](https://github.com/betagouv/acces-cible/issues/518)
- Correction d'un problème lié à la gestion des URLs invalides lors de l'importation de sites via CSV. [#504](https://github.com/betagouv/acces-cible/issues/504)
- Correction d'un problème lié à l'ignorance des lignes vides dans les fichiers CSV importés. [#503](https://github.com/betagouv/acces-cible/issues/503)
- Mise à jour de la gem `pagy` pour utiliser `max_limit` au lieu de `client_max_limit` (déprécié). [#533](https://github.com/betagouv/acces-cible/issues/533)
- Ajout de la gem `i18-tasks` pour la gestion des traductions.
- Suppression des traductions inutilisées.
- Correction d'une traduction invalide pour les années. [#521](https://github.com/betagouv/acces-cible/issues/521)
- Ajout des champs `url` et `normalized_url` aux données des sites. [#529](https://github.com/betagouv/acces-cible/issues/529)
- Ajout d'une commande `make test` pour faciliter l'exécution des tests. [#499](https://github.com/betagouv/acces-cible/issues/499)
- Persistance de l'historique de la console Rails et du shell dans les conteneurs Docker.

### Autres changements
- Rétrogradation d'un commit expérimental ("upside down").
- Mise à jour des dépendances via Dependabot. [#523](https://github.com/betagouv/acces-cible/issues/523)
