## Changelog : gestion-des-subventions-locales (30 derniers jours, au 29 avril 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de performance, notamment sur les pages projets et simulations, ainsi que par l'ajout de nombreux filtres pour affiner la recherche et la gestion des données. Des corrections de bugs et des refactorings ont également été réalisés pour améliorer la stabilité et la maintenabilité de l'application. L'intégration avec Turgot a été renforcée, notamment en synchronisant les montants et en adaptant l'interface pour refléter ce changement.

### Évolutions fonctionnelles
- Ajout de filtres par catégorie DETR/DSIL sur les listes de projets. [#634](https://github.com/betagouv/gestion-des-subventions-locales/issues/634)
- Ajout de filtres par date sur les listes projets, simulations et programmation. [#625](https://github.com/betagouv/gestion-des-subventions-locales/issues/625)
- Ajout de filtres pour le budget vert, la dotation sollicitée et le dossier complet. [#640](https://github.com/betagouv/gestion-des-subventions-locales/issues/640)
- Ajout d'une colonne "Taux sollicité" dans l'export. [#636](https://github.com/betagouv/gestion-des-subventions-locales/issues/636)
- Affichage de la priorité du dossier si plusieurs ont été déposés par le même demandeur. [#675](https://github.com/betagouv/gestion-des-subventions-locales/issues/675)
- Ajout d'un filtre EPCI sur les pages projet, programmation et simulation. [#673](https://github.com/betagouv/gestion-des-subventions-locales/issues/673)
- Possibilité de changer le statut en masse des dossiers sur la page de simulation. [#661](https://github.com/betagouv/gestion-des-subventions-locales/issues/661)
- Amélioration de l'affichage des cofinancements sur la page projet. [#643](https://github.com/betagouv/gestion-des-subventions-locales/issues/643)
- Ajout de la possibilité de fermer la modale "Vous ne faites pas partie du groupe d'instructeurs". [#690](https://github.com/betagouv/gestion-des-subventions-locales/issues/690)
- Mise à jour de l'enveloppe lorsqu'on modifie les montants des projets acceptés. [#674](https://github.com/betagouv/gestion-des-subventions-locales/issues/674)
- Ajout d'une FAQ. [#672](https://github.com/betagouv/gestion-des-subventions-locales/issues/672)
- Correction de l'affichage de la date de notification. [#695](https://github.com/betagouv/gestion-des-subventions-locales/issues/695)
- Correction de l'affichage des documents. [#694](https://github.com/betagouv/gestion-des-subventions-locales/issues/694)

### Évolutions techniques
- Refactoring pour utiliser `personne_morale` au lieu de `projet demandeur`. [#1234](https://github.com/betagouv/gestion-des-subventions-locales/issues/1234)
- Optimisation de la requête GraphQL pour le GroupeInstructeur afin de limiter les timeouts. [#691](https://github.com/betagouv/gestion-des-subventions-locales/issues/691)
- Amélioration de la performance de la page projet (BO). [#637](https://github.com/betagouv/gestion-des-subventions-locales/issues/637)
- Ajout de la librairie `django-query-counter`. [#671](https://github.com/betagouv/gestion-des-subventions-locales/issues/671)
- Mise en place de tests CI avec SQLite en mémoire pour les PR et PostgreSQL pour la merge queue. [#596](https://github.com/betagouv/gestion-des-subventions-locales/issues/596)
- Ajout de workflows de déploiement en production via GitHub Actions. [#647](https://github.com/betagouv/gestion-des-subventions-locales/issues/647)
- Ajout d'un déploiement pour l'environnement de démo. [#653](https://github.com/betagouv/gestion-des-subventions-locales/issues/653)
- Ajout d'une commande `just release-dry-run` pour prévisualiser un tag et ses notes de version. [#680](https://github.com/betagouv/gestion-des-subventions-locales/issues/680)
- Correction de l'URL du script HeatmapSessionRecording de Matomo. [#687](https://github.com/betagouv/gestion-des-subventions-locales/issues/687)
- Ajout du script HeatmapSessionRecording de Matomo. [#666](https://github.com/betagouv/gestion-des-subventions-locales/issues/666)
- Stream d'un heartbeat pour éviter les timeouts Scalingo du proxy DS. [#676](https://github.com/betagouv/gestion-des-subventions-locales/issues/676)
- Proxy GraphQL DS filtré par instructeurs. [#641](https://github.com/betagouv/gestion-des-subventions-locales/issues/641)
- Amélioration de la synchronisation des montants avec Turgot lors de l'acceptation d'un projet.
- Refactoring du système de mentions de publipostage. [#632](https://github.com/betagouv/gestion-des-subventions-locales/issues/632)

### Autres changements
- Mise à jour de la documentation pour les releases en production.
- Changement des titres des pages pour refléter l'intégration avec Turgot. [#639](https://github.com/betagouv/gestion-des-subventions-locales/issues/639)
- Correction de la réouverture des modales de statut avec contenu obsolète. [#621](https://github.com/betagouv/gestion-des-subventions-locales/issues/621)
- Suppression des logs verbeux de fontTools en production. [#684](https://github.com/betagouv/gestion-des-subventions-locales/issues/684)
- Correction d'un problème de typo CSS. [#667](https://github.com/betagouv/gestion-des-subventions-locales/issues/667)
- Correction de l'affichage des documents de l'autre dotation.
