## Changelog : vizeau (30 derniers jours)

### Résumé
Les dernières mises à jour de Vizeau se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la gestion des exploitations et des parcelles. Des corrections de bugs et des optimisations ont également été apportées pour une meilleure stabilité et performance de l'application. L'interface a été enrichie avec de nouvelles fonctionnalités comme la gestion des documents et des notes sur les parcelles.

### Évolutions fonctionnelles
- Ajout de la possibilité de gérer les notes sur les parcelles avec validation et stockage en base de données. [#298](https://github.com/MTES-MCT/vizeau/pull/298)
- Amélioration de la visibilité des liens dans la barre latérale de l'exploitation. [#306](https://github.com/MTES-MCT/vizeau/pull/306)
- Ajout d'un placeholder pour l'exploitation lorsqu'aucune n'est sélectionnée.
- Amélioration de l'affichage des informations de la parcelle dans la barre latérale. [#273](https://github.com/MTES-MCT/vizeau/pull/273)
- Ajout de la possibilité de supprimer un document. [#287](https://github.com/MTES-MCT/vizeau/pull/287)
- Ajout de la gestion des dates pour les entrées de journal. [#237](https://github.com/MTES-MCT/vizeau/pull/237)
- Amélioration de la gestion des tags, notamment pour la création. [#280](https://github.com/MTES-MCT/vizeau/pull/280)
- Ajout de la possibilité de centrer la carte sur une parcelle et de gérer le cas où la parcelle n'est pas trouvée.
- Ajout d'une fonctionnalité pour afficher les informations de l'exploitation dans des onglets. [#289](https://github.com/MTES-MCT/vizeau/pull/289)
- Ajout d'un indicateur visuel pour les actions de la carte (AAC, PPE, PPR).
- Amélioration de l'UX pour l'attribution des parcelles. [#246](https://github.com/MTES-MCT/vizeau/pull/246)
- Ajout d'un système d'onglets pour l'interface utilisateur. [#252](https://github.com/MTES-MCT/vizeau/pull/252)

### Évolutions techniques
- Mise à jour d'AdonisJS pour corriger des failles de sécurité.
- Simplification de la requête pour récupérer les entrées de journal de la page d'accueil.
- Suppression des données de démo du MVP et de l'exploitation de démonstration.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.
- Ajout de seeders idempotents pour la base de données. [#299](https://github.com/MTES-MCT/vizeau/pull/299)
- Correction de problèmes de typage TypeScript.
- Amélioration de la gestion des erreurs et des exceptions.
- Suppression de dépendances inutiles.
- Mise à jour des dépendances pour réduire les alertes de sécurité. [#247](https://github.com/MTES-MCT/vizeau/pull/247)

### Autres changements
- Amélioration de la documentation.
- Corrections de style et de formatage du code.
- Ajout de tests unitaires et d'intégration.
- Correction de bugs mineurs et amélioration de la stabilité de l'application.
- Ajout d'un composant `TruncatedText` pour gérer l'affichage de textes longs.
- Amélioration de l'affichage des contacts.
- Ajout d'un loader de type "dots".
- Correction de l'affichage des couleurs des légendes. [#295](https://github.com/MTES-MCT/vizeau/pull/295)
- Correction de l'affichage du popup de contact. [#285](https://github.com/MTES-MCT/vizeau/pull/285)
- Correction d'un problème d'accès à l'utilisateur dans le front-end.
- Suppression de pictos inutiles.
- Ajout de la possibilité de stocker le centroïde de la parcelle lors de l'attribution. [#277](https://github.com/MTES-MCT/vizeau/pull/277)
