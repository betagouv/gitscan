## Changelog : dialog (30 derniers jours, au 20 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'API pour la gestion des réglementations, notamment l'ajout de points d'accès pour récupérer et mettre à jour les informations. Des améliorations ont également été apportées à l'interface utilisateur pour faciliter la saisie et la visualisation des données, ainsi qu'à l'importation des données via Litteralis.

### Évolutions fonctionnelles
- Ajout d'un point d'API pour récupérer les arrêtés de circulation par organisme [#1967](https://github.com/MTES-MCT/dialog/issues/1967).
- Pré-remplissage du type de voie et de la ville dans le formulaire de localisation [#1951](https://github.com/MTES-MCT/dialog/issues/1951).
- Amélioration de la gestion des restrictions sur les villes entières [#1945](https://github.com/MTES-MCT/dialog/issues/1949).
- Clarification de la sélection du modèle d'arrêté dans le formulaire [#1941](https://github.com/MTES-MCT/dialog/issues/1941).
- Ajout d'informations sur les sessions "Ask Me Anything" dans l'interface [#1935](https://github.com/MTES-MCT/dialog/issues/1935).
- Ajout de 3 nouvelles expressions pour identifier "toute la journée" dans le parseur de périodes [#1952](https://github.com/MTES-MCT/dialog/issues/1952).
- Ajout d'un point d'API pour récupérer un arrêté par son identifiant [#1927](https://github.com/MTES-MCT/dialog/issues/1927).
- Ajout d'un point d'API pour mettre à jour un arrêté par son identifiant [#1928](https://github.com/MTES-MCT/dialog/issues/1928).
- Masquage du nom de l'éditeur si l'utilisateur n'est pas connecté [#1965](https://github.com/MTES-MCT/dialog/issues/1965).

### Évolutions techniques
- Amélioration de la recherche de tronçons de route et de voies nommées pour le calcul des lignes sur BDTopo [#1954](https://github.com/MTES-MCT/dialog/issues/1954).
- Ajout d'une commande pour supprimer des arrêtés via la ligne de commande [#1947](https://github.com/MTES-MCT/dialog/issues/1947).
- Correction de la gestion des exceptions lors de la gestion des restrictions sur les villes entières [#1949](https://github.com/MTES-MCT/dialog/issues/1949).
- Ajout d'un séparateur ":" pour les périodes dans le parseur Litteralis [#1966](https://github.com/MTES-MCT/dialog/issues/1966).
- Mise à jour de Playwright dans la configuration CI [#1940](https://github.com/MTES-MCT/dialog/issues/1940).
