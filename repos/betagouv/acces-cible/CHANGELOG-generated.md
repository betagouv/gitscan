## Changelog : acces-cible (30 derniers jours)

### Résumé
Cette mise à jour apporte des améliorations à l'application, notamment concernant la suppression en masse de sites web, l'extraction du taux de conformité, et la logique du crawler. Des ajustements ont également été faits pour moderniser le code et améliorer la lisibilité, ainsi que des mises à jour de sécurité.

### Évolutions fonctionnelles
- Amélioration de la suppression en masse de sites web (#449).
- Amélioration de l'extraction du taux de conformité (#450).
- Correction de la logique du crawler (#452).
- Renommage de la colonne `checked_at` en `completed_at` dans toute l'application (#436).

### Évolutions techniques
- Mise à jour de la gem Brakeman vers la version 8.0.2 (#437) pour renforcer la sécurité de l'application.
- Suppression de l'helper `time_ago` et adaptation des vues pour utiliser des formats de date plus modernes (#452).
- Mise à jour de la documentation README (#451).
- Ajout d'exemples partagés pour améliorer la testabilité et la réutilisabilité du code (#436).
