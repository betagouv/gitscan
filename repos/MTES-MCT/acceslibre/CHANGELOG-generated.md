## Changelog : acceslibre (30 derniers jours, au 09 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des établissements RPA (Référent Public Unique), avec notamment la possibilité de les marquer comme tels et d'adapter l'interface en conséquence. Des corrections et améliorations ont également été apportées à l'interface utilisateur, notamment au niveau des modals et des pages de succès. Enfin, plusieurs mises à jour de dépendances ont été effectuées pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Possibilité de marquer un ERP comme RPA, empêchant ainsi sa modification. [#2698](https://github.com/MTES-MCT/acceslibre/issues/2698)
- Ajout d'une indication visuelle pour les ERP RPA sur la page d'accessibilité. [#2691](https://github.com/MTES-MCT/acceslibre/issues/2691)
- Modification du libellé et du placement du registre d'accessibilité pour les ERP RPA. [#2711](https://github.com/MTES-MCT/acceslibre/issues/2711)
- Amélioration des règles de déclenchement de la modal RPA. [#2701](https://github.com/MTES-MCT/acceslibre/issues/2701)
- Mise à jour de la page de succès et de la page de réclamation. [#2700](https://github.com/MTES-MCT/acceslibre/issues/2700)
- Ajout d'outils sur la page d'accessibilité. [#2682](https://github.com/MTES-MCT/acceslibre/issues/2682)
- Correction d'un bug empêchant la modification des ERP RPA. [#2692](https://github.com/MTES-MCT/acceslibre/issues/2692)
- Amélioration du calcul du taux de complétion. [#2681](https://github.com/MTES-MCT/acceslibre/issues/2681)
- Correction de problèmes d'accessibilité suite aux retours RGAA. [#2670](https://github.com/MTES-MCT/acceslibre/issues/2670)

### Évolutions techniques
- Mise à jour de Django. [#2716](https://github.com/MTES-MCT/acceslibre/issues/2716)
- Traduction du champ d'accessibilité à la demande pour optimiser les performances. [#2692](https://github.com/MTES-MCT/acceslibre/issues/2692)
- Utilisation d'une locale `fr_FR` pour le générateur de données fictives (faker). [#2680](https://github.com/MTES-MCT/acceslibre/issues/2680)

### Autres changements
- Suppression d'instructions `print` inutiles.
- Export du flag RPA pour une utilisation plus large.
- Correction de l'affichage du badge RPA si l'ERP n'est pas un RPA. [#2715](https://github.com/MTES-MCT/acceslibre/issues/2715)
- Correction de la condition d'affichage de la page de succès. [#2714](https://github.com/MTES-MCT/acceslibre/issues/2714)
- Amélioration de la modal de réclamation et des mises à jour de la page de succès. [#2713](https://github.com/MTES-MCT/acceslibre/issues/2713)
