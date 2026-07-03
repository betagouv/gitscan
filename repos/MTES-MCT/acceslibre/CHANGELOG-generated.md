## Changelog : acceslibre (30 derniers jours, au 02 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des ERP en Référencement Public d'Accès (RPA), avec l'ajout de fonctionnalités spécifiques et des corrections pour une meilleure expérience utilisateur. Des ajustements ont également été apportés à la collecte de données et à la sécurité, ainsi que des mises à jour techniques pour maintenir la performance et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout d'un indicateur d'exemption RPA accessible uniquement aux gestionnaires. [#2691](https://github.com/MTES-MCT/acceslibre/issues/2691)
- Les ERP en RPA ne peuvent plus être modifiés.
- Amélioration de la page d'accessibilité avec l'ajout d'outils pertinents. [#2682](https://github.com/MTES-MCT/acceslibre/issues/2682)
- Correction de l'affichage du bouton de confirmation pour les ERP en RPA. [#2698](https://github.com/MTES-MCT/acceslibre/issues/2698)
- Export de l'indicateur RPA pour une meilleure identification. [#2601](https://github.com/MTES-MCT/acceslibre/issues/2601)
- Ajustement du calcul du taux de complétion. [#2681](https://github.com/MTES-MCT/acceslibre/issues/2681)
- Correction de problèmes liés aux retours d'expérience RGAA. [#2670](https://github.com/MTES-MCT/acceslibre/issues/2670)
- Mise à jour du schéma de données à la version 0.0.20. [#2590](https://github.com/MTES-MCT/acceslibre/issues/2590)
- Amélioration de la sécurité de Google Analytics (GA) suite aux recommandations de zizmor. [#2663](https://github.com/MTES-MCT/acceslibre/issues/2663)
- Corrections de règles de déclenchement de la modale RPA. [#2701](https://github.com/MTES-MCT/acceslibre/issues/2701)
- Modifications sur la page de succès et la page de réclamation. [#2700](https://github.com/MTES-MCT/acceslibre/issues/2700) et [#2699](https://github.com/MTES-MCT/acceslibre/issues/2699)

### Évolutions techniques
- Mise à jour de plusieurs dépendances : `sentry-sdk`, `djlint`, `scrapfly-sdk`, `actions/checkout`, `dompurify`, `prettier`, `pnpm`, `ruff`, `weasyprint`, `djangorestframework-gis`, `deepl`, `django-import-export`, `eslint`, `outscraper`, `django-reversion`, `gunicorn`, `faker`.
- Correction de la base schema. [#2671](https://github.com/MTES-MCT/acceslibre/issues/2671)
- Utilisation d'une locale `fr_FR` pour la librairie `faker`. [#2680](https://github.com/MTES-MCT/acceslibre/issues/2680)
- Suppression d'instructions `print` inutiles.

### Autres changements
- Documentation mise à jour.
- Nettoyage du code.
