## Changelog : acceslibre (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la performance de la plateforme, notamment au niveau de la gestion des statistiques et de la génération de documents. Des corrections ont été apportées à l'interface utilisateur pour améliorer l'expérience de recherche et la gestion des erreurs. Des mises à jour de sécurité et de dépendances ont également été effectuées.

### Évolutions fonctionnelles
- Amélioration de la recherche avec correction d'une erreur Sentry et support des combobox RGAAs. [#2609](https://github.com/MTES-MCT/acceslibre/issues/2609)
- Possibilité de contourner les vérifications de doublons. [#2626](https://github.com/MTES-MCT/acceslibre/issues/2626)
- Utilisation de POST pour la génération des PDF RPA. [#2623](https://github.com/MTES-MCT/acceslibre/issues/2623)
- Correction d'un problème lié à la question Pente. [#2600](https://github.com/MTES-MCT/acceslibre/issues/2600)
- Correction d'un problème lié aux détails ERP. [#2599](https://github.com/MTES-MCT/acceslibre/issues/2599)

### Évolutions techniques
- Mise à jour de Django. [#2625](https://github.com/MTES-MCT/acceslibre/issues/2625)
- Mise en cache du comptage pour la pagination afin d'améliorer les performances. [#2621](https://github.com/MTES-MCT/acceslibre/issues/2621)
- Utilisation de Redis pour stocker les événements des widgets et les vider dans la base de données toutes les heures. [#2624](https://github.com/MTES-MCT/acceslibre/issues/2624)
- Optimisation des performances des statistiques. [#2610](https://github.com/MTES-MCT/acceslibre/issues/2610)
- Application stricte des versions des paquets pour assurer la stabilité. [#2635](https://github.com/MTES-MCT/acceslibre/issues/2635)

### Autres changements
- Suppression temporaire de la génération de PDF RPA. [#2622](https://github.com/MTES-MCT/acceslibre/issues/2622)
- Désindexation du PDF RPA. [#2611](https://github.com/MTES-MCT/acceslibre/issues/2611)
