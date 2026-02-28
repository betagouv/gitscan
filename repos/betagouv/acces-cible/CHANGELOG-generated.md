## Changelog : acces-cible (30 derniers jours)

### Résumé
Les dernières améliorations apportées à acces-cible se concentrent sur l'amélioration de la gestion des données et de l'expérience utilisateur.  Des corrections ont été apportées pour assurer la fiabilité des calculs de conformité et la gestion des transitions, ainsi qu'une amélioration de la suppression en masse. De plus, la pagination est désormais configurable et l'application a été mise à jour avec les dernières versions de ses outils de sécurité.

### Évolutions fonctionnelles
- Amélioration de la suppression en masse : l'opération est plus performante et fiable (#449).
- Pagination configurable : les limites de pagination sont désormais configurables, permettant d'adapter l'affichage des données aux besoins des utilisateurs (#454).
- Amélioration de l'extraction du taux de conformité : correction d'un bug pour un calcul plus précis (#450).
- Correction d'un problème de logique du crawler (#7b26042).

### Évolutions techniques
- Correction d'une condition de concurrence lors de la création de transitions (#455). Rétractation d'une correction précédente (#801f945).
- Mise à jour de Brakeman vers la version 8.0.2 pour renforcer la sécurité de l'application (#437).
- Mise à jour des expressions régulières du schéma et ajout d'exemples partagés pour améliorer la maintenance et la testabilité (#436).
- Suppression du helper `time_ago` et adaptation des vues pour utiliser des formats de date plus clairs (#452).

### Autres changements
- Mise à jour du fichier README pour améliorer la documentation (#451).
