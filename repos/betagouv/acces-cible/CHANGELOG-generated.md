## Changelog : acces-cible (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la robustesse de l'application, notamment lors de l'importation de données via des fichiers CSV, ainsi que sur la correction de bugs et l'amélioration de l'expérience utilisateur. Des améliorations de sécurité et de la gestion des traductions ont également été apportées.

### Évolutions fonctionnelles
- Possibilité de télécharger un fichier CSV filtré. [#513](https://github.com/betagouv/acces-cible/issues/513)
- Ajout du BOM UTF-8 aux exports CSV pour une meilleure compatibilité avec les tableurs. [#520](https://github.com/betagouv/acces-cible/issues/520)
- Amélioration de la détection des liens externes. [#497](https://github.com/betagouv/acces-cible/issues/497)
- Correction de la recherche du taux d'accessibilité. [#509](https://github.com/betagouv/acces-cible/issues/509)
- Correction de la gestion des années invalides dans les traductions. [#521](https://github.com/betagouv/acces-cible/issues/521)

### Évolutions techniques
- Mise à jour de la gem `dsfr-view-components`. [#518](https://github.com/betagouv/acces-cible/issues/518) et [#518](https://github.com/betagouv/acces-cible/issues/518)
- Mise à jour de plusieurs dépendances via Dependabot : `pagy` (9.4.0 -> 43.4.2) [#494](https://github.com/betagouv/acces-cible/issues/494) et `http` (5.3.1 -> 6.0.2) [#495](https://github.com/betagouv/acces-cible/issues/495)
- Sécurisation du rendu des URLs externes pour prévenir les attaques XSS. [#508](https://github.com/betagouv/acces-cible/issues/508)
- Ajout de la gem `i18-tasks` pour la gestion des traductions et suppression des traductions inutilisées.
- Ajout des champs `url` et `normalized_url` aux sites. [#529](https://github.com/betagouv/acces-cible/issues/529)
- Amélioration de la gestion des erreurs lors de l'importation de fichiers CSV malformés ou contenant des URLs invalides. [#503](https://github.com/betagouv/acces-cible/issues/503), [#504](https://github.com/betagouv/acces-cible/issues/504), [#507](https://github.com/betagouv/acces-cible/issues/507)
- Ajout d'une commande `make test` pour faciliter l'exécution des tests. [#499](https://github.com/betagouv/acces-cible/issues/499)

### Autres changements
- Configuration de Sentry ajustée et ajout de logs pour une meilleure surveillance de l'application. [#498](https://github.com/betagouv/acces-cible/issues/498)
- Persistance de l'historique de la console Rails et du shell dans les conteneurs Docker.
- Suppression d'une fonctionnalité expérimentale ("upside down") qui n'était pas pertinente.
