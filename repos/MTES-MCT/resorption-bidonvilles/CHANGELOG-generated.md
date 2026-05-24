## Changelog : resorption-bidonvilles (30 derniers jours, au 06 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur et de la gestion des adresses des ETI (Établissements Travailleurs Itinérants), notamment dans le formulaire de déclaration d'action. Des corrections de typage et des optimisations de code ont également été apportées pour améliorer la robustesse et la maintenabilité de l'application. Enfin, des ajustements ont été faits pour une meilleure expérience utilisateur, comme l'ajustement automatique du zoom de la carte et l'ajout d'un indicateur d'état "En cours de résorption".

### Évolutions fonctionnelles
- Ajout d'un tag "En cours de résorption" sur la liste des sites existants. [#2676](https://trello.com/c/v3T8gn3K/2676)
- Ajout d'une option "toutes" au filtre de financement DIHAL. [#2672](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2672)
- Synchronisation des coordonnées lors du changement d'adresse ETI.
- Ajustement automatique du zoom de la carte pour afficher tous les marqueurs ETI.
- Le champ adresse est maintenant obligatoire lorsque le type de localisation est "ETI". [#2652](https://trello.com/c/ZvoH4cJE/2652)

### Évolutions techniques
- Refactor important du formulaire de déclaration d'action (FormDeclarationAction) pour améliorer la lisibilité et la maintenabilité du code, incluant :
    - Suppression de props drilling et utilisation de `useFormContext`.
    - Extraction de la logique de parsing des coordonnées dans un helper partagé (`parseCoordinates`).
    - Simplification de la déclaration des propriétés booléennes.
    - Suppression d'imports inutiles.
- Amélioration du typage dans l'API, notamment pour les fonctions `getHistory`, `historizeAddresses` et `resetAddresses`.
- Centralisation des fonctions de conversion de date en timestamp.
- Pré-bundle des librairies nécessaires à Nuxt 4 pour améliorer les performances.
- Correction de plusieurs risques d'injection et de problèmes d'interpolation de chaînes de caractères.
- Correction de typage erroné.

### Autres changements
- Suppression d'un log inutile.
- Ajout d'un HR et renommage d'un filtre dans l'interface utilisateur.
- Correction du formatage de la date dans les dernières activités.
- Ajout d'un garde-fou pour éviter d'itérer inutilement dans une boucle.
- Correction d'un filtrage effectué deux fois.
- Suppression d'un export inutile.
- Corrections de linting (espaces inutiles).
