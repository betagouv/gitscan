## Changelog : acceslibre (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des données, notamment avec l'ajout d'un indicateur d'exemption RPA et la mise à jour du schéma de données à la version 0.0.20. Des corrections liées aux retours d'audit RGAA ont également été implémentées, ainsi que des ajustements de sécurité pour Google Analytics. De nombreuses mises à jour de dépendances ont été effectuées pour maintenir la sécurité et la stabilité du projet.

### Évolutions fonctionnelles
- Ajout d'un indicateur d'exemption RPA (Référentiel des Gestes Alternatifs) sur la page d'accessibilité. [#2691](https://github.com/MTES-MCT/acceslibre/issues/2691)
- Ajout d'une propriété RPA pour les établissements. [#2601](https://github.com/MTES-MCT/acceslibre/issues/2601)
- Correction des retours d'audit RGAA pour améliorer l'accessibilité de l'application. [#2670](https://github.com/MTES-MCT/acceslibre/issues/2670)
- Amélioration du calcul du taux de complétion. [#2681](https://github.com/MTES-MCT/acceslibre/issues/2681)
- Ajustement de la sécurité de Google Analytics suite aux recommandations de zizmor. [#2663](https://github.com/MTES-MCT/acceslibre/issues/2663)
- Mise à jour du schéma de données à la version 0.0.20. [#2590](https://github.com/MTES-MCT/acceslibre/issues/2590)

### Évolutions techniques
- Corrections de la base du schéma de données. [#2671](https://github.com/MTES-MCT/acceslibre/issues/2671)
- Utilisation d'une locale `fr_FR` pour la génération de données factices avec Faker. [#2680](https://github.com/MTES-MCT/acceslibre/issues/2680)
- Ajout d'outils sur la page d'accessibilité. [#2682](https://github.com/MTES-MCT/acceslibre/issues/2682)

### Autres changements
- Documentation mise à jour.
- Nettoyage et amélioration du code.
- Mises à jour de nombreuses dépendances (dompurify, prettier, pnpm, ruff, weasyprint, djangorestframework-gis, djlint, faker, gunicorn, eslint, scrapfly-sdk, deepl, django-import-export, django-reversion). Ces mises à jour sont principalement liées à la sécurité et à la maintenance du projet.
