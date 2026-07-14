## Changelog : acceslibre (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des établissements en RPA (Référencement des Personnes en Situation de Handicap), notamment en ajoutant des fonctionnalités de réclamation et de gestion des exemptions. Des corrections et améliorations ont également été apportées à l'interface utilisateur et à la logique de l'application, ainsi que des mises à jour techniques pour maintenir la sécurité et la performance.

### Évolutions fonctionnelles
- Ajout de la possibilité de réclamer un établissement en tant que RPA. [#2713](https://github.com/MTES-MCT/acceslibre/issues/2713)
- Amélioration de l'interface de réclamation et ajout d'une page de succès après réclamation. [#2700](https://github.com/MTES-MCT/acceslibre/issues/2700) et [#2714](https://github.com/MTES-MCT/acceslibre/issues/2714)
- Modification du libellé et du placement du lien vers le registre d'accessibilité pour les établissements RPA. [#2711](https://github.com/MTES-MCT/acceslibre/issues/2711)
- Les établissements RPA ne peuvent plus être modifiés. [#2698](https://github.com/MTES-MCT/acceslibre/issues/2698) et [#2701](https://github.com/MTES-MCT/acceslibre/issues/2701)
- Ajout d'un indicateur visuel pour les établissements RPA. [#2691](https://github.com/MTES-MCT/acceslibre/issues/2691)
- Correction de l'affichage du bouton de traduction et du rendu du texte. [#2726](https://github.com/MTES-MCT/acceslibre/issues/2726)
- Ajout d'un lien vers les outils d'accessibilité sur la page d'accessibilité. [#2682](https://github.com/MTES-MCT/acceslibre/issues/2682)
- Mise à jour de la logique de calcul du taux de complétion. [#2681](https://github.com/MTES-MCT/acceslibre/issues/2681)
- Modification de la date `checked_up_to_date_at` lors de la création, modification ou importation d'un ERP. [#2712](https://github.com/MTES-MCT/acceslibre/issues/2712)

### Évolutions techniques
- Mise à jour de Django (minor upgrade). [#2716](https://github.com/MTES-MCT/acceslibre/issues/2716)
- Traduction du champ d'accessibilité à la demande pour optimiser les performances. [#2692](https://github.com/MTES-MCT/acceslibre/issues/2692)
- Utilisation d'une locale `fr_FR` pour la librairie `faker` afin de générer des données plus pertinentes. [#2680](https://github.com/MTES-MCT/acceslibre/issues/2680)

### Autres changements
- Correction d'un bug empêchant l'affichage du badge RPA si l'ERP n'était pas concerné. [#2715](https://github.com/MTES-MCT/acceslibre/issues/2715)
- Suppression d'instructions `print` inutiles. [#2702](https://github.com/MTES-MCT/acceslibre/issues/2702)
- Export du flag RPA pour une meilleure gestion. [#2601](https://github.com/MTES-MCT/acceslibre/issues/2601) et [#2691](https://github.com/MTES-MCT/acceslibre/issues/2691)
