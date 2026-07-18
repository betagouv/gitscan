## Changelog : agreste (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la recherche avec l'ajout de filtres, des corrections de bugs concernant l'affichage des noms de fichiers longs et des publications récentes, ainsi que des optimisations techniques pour le déploiement et la gestion des médias. Des efforts ont également été faits pour améliorer la testabilité et la maintenabilité du code.

### Évolutions fonctionnelles
- **Recherche :** Ajout de filtres de recherche avancés, incluant la possibilité de filtrer par thèmes et collections [#32](https://github.com/betagouv/agreste/pull/32), [#33](https://github.com/betagouv/agreste/pull/33).
- **Publications récentes :** Correction de l'affichage des publications récentes, notamment le libellé du bouton "Voir toutes les publications" [#21](https://github.com/betagouv/agreste/pull/21).
- **Fichiers :** Correction d'un bug d'affichage des noms de fichiers trop longs dans le bloc "Fichiers à télécharger" [#40](https://github.com/betagouv/agreste/pull/40).
- **Accessibilité :** Améliorations de l'accessibilité pour la recherche avec facettes et les publications [#37](https://github.com/betagouv/agreste/pull/37).
- **Steppers :** Ajout de la possibilité de choisir la balise de titre sur les steppers.
- **Tags :** Ajout d'un titre sur les tags sélectionnés et correction de l'affichage des tags.

### Évolutions techniques
- **Tests :** Amélioration de la couverture de tests avec l'utilisation de factories pour la création d'objets de test [#39](https://github.com/betagouv/agreste/pull/39), [#27](https://github.com/betagouv/agreste/pull/27), [#30](https://github.com/betagouv/agreste/pull/30).
- **CI/CD :** Mise en place d'un workflow GitHub Actions pour la création de releases [#18](https://github.com/betagouv/agreste/pull/18), [#21](https://github.com/betagouv/agreste/pull/21).
- **Refactoring :** Refactorisation du code pour une meilleure réutilisation et simplification, notamment dans les blocs de publications [#24](https://github.com/betagouv/agreste/pull/24).
- **Gestion des médias :** Scripts améliorés pour la sauvegarde et la restauration des médias, avec une meilleure gestion des erreurs et des logs [#32](https://github.com/betagouv/agreste/pull/32).
- **Indépendance i18n :** Suppression de la dépendance aux fichiers i18n de sites-conformes [#35](https://github.com/betagouv/agreste/pull/35).
- **Migrations :** Corrections et améliorations des scripts de migration.

### Autres changements
- Mise à jour de la documentation pour ProConnect [#547](https://github.com/betagouv/agreste/pull/547).
- Mise à jour des traductions.
- Corrections mineures et améliorations de la lisibilité du code.
- Bump de version : 2.4.1-4.0.2 et 3.1.1-4.0.1.
