## Changelog : acces-cible (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à acces-cible au cours des 30 derniers jours. Les modifications incluent des corrections de bugs pour améliorer la précision des taux de conformité, des améliorations de la suppression en masse, ainsi que des refactorisations internes pour une meilleure maintenance et une détection plus précise des liens internes et des schémas d'accessibilité. La documentation et l'interface utilisateur ont également été mises à jour.

### Évolutions fonctionnelles
- Amélioration de l'extraction du taux de conformité (#450).
- Amélioration de la suppression en masse de sites web (#449).
- Correction de la logique du crawler pour une analyse plus fiable (#449).
- Amélioration de la détection des liens internes (#449).
- Amélioration de l'extraction de l'année et de la validation de la logique des schémas d'accessibilité (#436, #449).

### Évolutions techniques
- Refactorisation du `Crawler` et du `FindAccessibilityPageService` pour une meilleure organisation et maintenabilité (#449).
- Renommage de la colonne `checked_at` en `completed_at` dans toute l'application pour une meilleure clarté (#436).
- Mise à jour de Brakeman vers la version 8.0.2 pour améliorer la sécurité (#437).
- Suppression de l'helper `time_ago` et adaptation des vues pour utiliser des formats de date plus appropriés (#452).

### Autres changements
- Mise à jour du fichier README (#451).
- Ajout d'exemples partagés pour faciliter les tests (#436).
