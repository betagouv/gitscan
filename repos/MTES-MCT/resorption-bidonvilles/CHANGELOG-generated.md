## Changelog : resorption-bidonvilles (30 derniers jours, au 03/09/2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration des capacités d'exportation de données et la stabilisation de l'interface utilisateur. Les utilisateurs bénéficient désormais d'une meilleure continuité de navigation lors des changements de périodes et de fonctionnalités d'export enrichies pour les recherches par commune ou EPCI.

### Évolutions fonctionnelles
- Ajout de l'option d'export des phases de résorption lors des recherches par commune ou EPCI [#1527](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1527).
- Correction de l'affichage des dates (valeurs "NaN") dans les exports des phases de résorption [#1526](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1526).
- Mémorisation de l'onglet actif lors du changement de période de temps pour une navigation plus fluide [#1525](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1525).
- Amélioration de la stabilité des composants de la carte et du sélecteur de dates (datepicker) [#1525](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1525).

### Évolutions techniques
- **API** :
  - Amélioration de la gestion des indicateurs d'action (autorisation du zéro et normalisation des valeurs nulles avant insertion) [#1527](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1527).
  - Nettoyage de la base de données via la suppression de contraintes SQL obsolètes [#1527](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1527).
  - Refactorisation du code pour réduire la duplication et corriger les alertes de qualité (linting) [#1527](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1527).
- **Frontend** :
  - Optimisation de l'affichage pour éviter le clignotement du bandeau lors du chargement initial de la page [#1525](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1525).
  - Renforcement du typage TypeScript et sécurisation de l'initialisation des composants (carte, spinner, datepicker) [#1525](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1525).
  - Simplification et optimisation des tests unitaires [#1525](https://github.com/MTES-MCT/resorption-bidonvilles/pull/1525).

### Autres changements
- Suppression du paquetage `node/matermost`.
