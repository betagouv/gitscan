## Changelog : Docurba (30 derniers jours, au 28 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des collectivités et des événements, notamment en migrant des fonctionnalités vers l'API Django pour une meilleure performance et une plus grande cohérence. L'interface utilisateur a également été améliorée avec la possibilité d'utiliser le markdown dans les descriptions et la correction de plusieurs bugs d'affichage. Des optimisations de sécurité et de performance ont été apportées, ainsi qu'un nettoyage important du code.

### Évolutions fonctionnelles
- Ajout de la possibilité d'utiliser le markdown dans les descriptions des procédures et des événements, permettant une mise en forme plus riche et l'ajout de liens externes. [#4452c5a](https://github.com/MTES-MCT/Docurba/commit/4452c5a)
- Migration des endpoints `/api/communes`, `/api/geo/intercommunalites` et `/api/geo/collectivites` vers l'API Django pour une meilleure performance et une maintenance simplifiée. [#fb08e75](https://github.com/MTES-MCT/Docurba/commit/fb08e75), [#f982096](https://github.com/MTES-MCT/Docurba/commit/f982096), [#f2dea1b](https://github.com/MTES-MCT/Docurba/commit/f2dea1b), [#e72f34e](https://github.com/MTES-MCT/Docurba/commit/e72f34e), [#3c3c42d](https://github.com/MTES-MCT/Docurba/commit/3c3c42d)
- Correction de l'affichage des collaborateurs (insensibilité à la casse). [#e68e8a7](https://github.com/MTES-MCT/Docurba/commit/e68e8a7)
- Correction de l'affichage des listes de codes SIREN longues. [#da3cdde](https://github.com/MTES-MCT/Docurba/commit/da3cdde)
- Correction du chargement des types d'événements avant la sélection. [#e9fb6a7](https://github.com/MTES-MCT/Docurba/commit/e9fb6a7)
- Ajout des types d'événements PPLH et PPILH. [#5917f55](https://github.com/MTES-MCT/Docurba/commit/5917f55)
- Ajout d'une relation ForeignKey pour le type d'événement. [#33e86ac](https://github.com/MTES-MCT/Docurba/commit/33e86ac)
- Correction de la gestion des emails non null dans le partage de procédures. [#385056d](https://github.com/MTES-MCT/Docurba/commit/385056d)

### Évolutions techniques
- Migration de l'API des collectivités vers un plugin dédié dans Nuxt. [#a0b94e9](https://github.com/MTES-MCT/Docurba/commit/a0b94e9), [#d687eba](https://github.com/MTES-MCT/Docurba/commit/d687eba), [#d4eee06](https://github.com/MTES-MCT/Docurba/commit/d4eee06), [#8acb12f](https://github.com/MTES-MCT/Docurba/commit/8acb12f)
- Refactoring pour utiliser l'API Django avec une URL racine unique. [#8e0d6a2](https://github.com/MTES-MCT/Docurba/commit/8e0d6a2)
- Ajout d'un modèle `SupabaseUser` pour remplacer `User`. [#6e69dc3](https://github.com/MTES-MCT/Docurba/commit/6e69dc3)
- Ajout d'une variable d'environnement `$ENABLE_MIGRATIONS` pour contrôler l'exécution des migrations. [#ae15917](https://github.com/MTES-MCT/Docurba/commit/ae15917)
- Mise en place d'un script `post_deploy` corrigé. [#365d806](https://github.com/MTES-MCT/Docurba/commit/365d806)
- Exécution de `link_events_with_event_types` en CRON. [#b9d4c3e](https://github.com/MTES-MCT/Docurba/commit/b9d4c3e)
- Ajout de RLS (Row Level Security) sur plusieurs tables (eventtype, eventsnapshot, history context). [#0d549a8](https://github.com/MTES-MCT/Docurba/commit/0d549a8)
- Amélioration des performances de l'API Django et correction de N+1 queries. [#952a9e5](https://github.com/MTES-MCT/Docurba/commit/952a9e5), [#b8962ee](https://github.com/MTES-MCT/Docurba/commit/b8962ee)
- Ajout de tests et correction de tests existants (pytest, syrupy). [#f8c91f3](https://github.com/MTES-MCT/Docurba/commit/f8c91f3), [#c2d7d5e](https://github.com/MTES-MCT/Docurba/commit/c2d7d5e), [#f2dea1b](https://github.com/MTES-MCT/Docurba/commit/f2dea1b), [#8ae80ad](https://github.com/MTES-MCT/Docurba/commit/8ae80ad), [#20df824](https://github.com/MTES-MCT/Docurba/commit/20df824)

### Autres changements
- Suppression de composants et d'assets inutilisés dans l'interface utilisateur. [#ea814f5](https://github.com/MTES-MCT/Docurba/commit/ea814f5) et commits suivants.
- Mise à jour de la documentation des types d'événements. [#50c58d5](https://github.com/MTES-MCT/Docurba/commit/50c58d5), [#1a5c06a](https://github.com/MTES-MCT/Docurba/commit/1a5c06a)
- Mises à jour de dépendances (ruff, django, pytest, syrupy, etc.). (Ignorées car de routine)
- Ajout de `Collectivite.siren` et `Collectivite.code_insee`. [#d947e06](https://github.com/MTES-MCT/Docurba/commit/d947e06)
- Suppression de code commenté et de fichiers inutiles.
- Amélioration de la sécurité en restreignant l'accès aux tables de versements. [#8eef40c](https://github.com/MTES-MCT/Docurba/commit/8eef40c)
