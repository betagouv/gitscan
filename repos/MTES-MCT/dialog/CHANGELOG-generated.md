## Changelog : dialog (30 derniers jours, au 2026-07-15)

### Résumé
Cette version apporte des améliorations significatives à la gestion des restrictions de circulation, notamment pour les villes entières. L'interface utilisateur a été améliorée avec un pré-remplissage des informations de localisation et une clarification de la sélection des modèles d'arrêté. Des corrections ont également été apportées pour améliorer la recherche de routes et la gestion des périodes.

### Évolutions fonctionnelles
- Amélioration de la gestion des restrictions sur les villes entières [#1945](https://github.com/MTES-MCT/dialog/issues/1945).
- Ajout de nouvelles phrases pour reconnaître les périodes "tous les jours" dans le parseur Litteralis [#1952](https://github.com/MTES-MCT/dialog/issues/1952).
- Pré-remplissage du type de voie et de la ville dans la localisation lors de la création d'un arrêté [#1951](https://github.com/MTES-MCT/dialog/issues/1951).
- Clarification de la sélection du modèle d'arrêté dans le formulaire [#1941](https://github.com/MTES-MCT/dialog/issues/1941).
- Ajout d'un message d'information concernant les sessions "Ask Me Anything" [#1935](https://github.com/MTES-MCT/dialog/issues/1935).
- Possibilité de masquer le nom de l'éditeur du formulaire si l'utilisateur n'est pas connecté [#1965](https://github.com/MTES-MCT/dialog/issues/1965).

### Évolutions techniques
- Amélioration de la recherche de routes dans BDTopo en incluant `troncon_de_route` et `voie_nommee` [#1954](https://github.com/MTES-MCT/dialog/issues/1954).
- Ajout d'une commande pour supprimer des réglementations via la ligne de commande [#1947](https://github.com/MTES-MCT/dialog/issues/1947).
- Implémentation de la mise à jour d'une réglementation par son identifiant via l'API [#1928](https://github.com/MTES-MCT/dialog/issues/1928).
- Implémentation de la récupération d'une réglementation par son identifiant via l'API [#1927](https://github.com/MTES-MCT/dialog/issues/1927).
- Gestion des exceptions lors de la gestion des restrictions de villes entières [#1949](https://github.com/MTES-MCT/dialog/issues/1949).
- Mise à jour de Playwright dans le workflow CI [#1940](https://github.com/MTES-MCT/dialog/issues/1940).
- Ajout du séparateur ":" pour les périodes dans le parseur Litteralis [#1966](https://github.com/MTES-MCT/dialog/issues/1966).
