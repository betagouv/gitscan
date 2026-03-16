## Changelog : vizeau (30 derniers jours)

### Résumé
Les dernières mises à jour de vizeau se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des exploitations et des parcelles. De nouvelles fonctionnalités ont été ajoutées, comme la gestion des notes sur les parcelles, l'affichage des informations des parcelles dans la barre latérale, et la possibilité de centrer la carte sur une parcelle spécifique. Des améliorations ont également été apportées à l'interface utilisateur, notamment au niveau des couleurs, des icônes et de la navigation. Enfin, des corrections de bugs et des optimisations techniques ont été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- Ajout de la possibilité d'ajouter des notes aux parcelles avec validation et stockage en base de données. [#300](https://github.com/MTES-MCT/vizeau/pulls/300)
- Affichage des informations de la parcelle sélectionnée dans la barre latérale gauche. [#273](https://github.com/MTES-MCT/vizeau/pulls/273)
- Possibilité de centrer la carte sur une parcelle spécifique, avec repli sur l'exploitation si la parcelle n'est pas trouvée.
- Ajout d'un bouton pour se concentrer sur une parcelle.
- Amélioration de la visibilité des liens dans la barre latérale de l'exploitation. [#316](https://github.com/MTES-MCT/vizeau/pulls/316)
- Ajout de contacts multiples pour une exploitation. [#312](https://github.com/MTES-MCT/vizeau/pulls/312)
- Ajout d'un composant de graphique évolutif (EvolutiveChartLine) avec personnalisation des tooltips et support d'axes doubles. [#320](https://github.com/MTES-MCT/vizeau/pulls/320)
- Ajout d'une carte de résumé (ResumeCard). [#319](https://github.com/MTES-MCT/vizeau/pulls/319)
- Amélioration de l'affichage des informations de l'exploitation. [#303](https://github.com/MTES-MCT/vizeau/pulls/303)
- Ajout d'un placeholder pour l'exploitation. [#294](https://github.com/MTES-MCT/vizeau/pulls/294)
- Ajout de la suppression de documents. [#287](https://github.com/MTES-MCT/vizeau/pulls/287)
- Ajout de l'affichage des métadonnées des documents. [#310](https://github.com/MTES-MCT/vizeau/pulls/310)
- Amélioration de la gestion des tags. [#280](https://github.com/MTES-MCT/vizeau/pulls/280)

### Évolutions techniques
- Stockage du centroïde de la parcelle lors de l'attribution. [#277](https://github.com/MTES-MCT/vizeau/pulls/277)
- Refactorisation du code pour une meilleure cohérence, notamment le renommage de `code_group` en `group_code`. [#77a482a](https://github.com/MTES-MCT/vizeau/commit/77a482a)
- Simplification de la requête pour récupérer les entrées de journal de la page d'accueil.
- Suppression des données de démonstration du MVP et de l'exploitation de démonstration.
- Mise en place de seeders idempotents. [#299](https://github.com/MTES-MCT/vizeau/pulls/299)
- Correction de plusieurs erreurs de typage TypeScript.
- Amélioration de la gestion des paramètres d'URL pour les composants de visualisation.
- Utilisation de `map.once('load')` au lieu de `setTimeout` pour une meilleure gestion du chargement de la carte.
- Correction de problèmes liés à l'utilisation des composants Tabs.
- Refactorisation de la gestion des couleurs des cultures. [#318](https://github.com/MTES-MCT/vizeau/pulls/318)

### Autres changements
- Amélioration des contrastes pour une meilleure accessibilité.
- Mise à jour des dépendances.
- Corrections de copilot review.
- Amélioration de la documentation.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de tests fonctionnels pour la gestion des notes sur les parcelles.
- Mise à jour des labels et des textes pour une meilleure clarté.
- Amélioration de la gestion des placeholders vides.
- Suppression des pictos des groupes de cultures.
- Mise à jour du composant FileItem. [#279](https://github.com/MTES-MCT/vizeau/pulls/279)
- Correction de l'affichage des noms de contact.
- Mise à jour du composant TagSelector.
- Correction de bugs et amélioration de la robustesse du code.
