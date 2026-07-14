## Changelog : dialog (30 derniers jours, au 10 juillet 2026)

### Résumé
Les dernières mises à jour de dialog améliorent l'expérience utilisateur lors de la création et de la modification de réglementations de circulation. Des améliorations ont été apportées à la recherche de routes, à la gestion des périodes, et à la sélection des modèles d'arrêtés. Des fonctionnalités d'API ont également été ajoutées pour faciliter la gestion des réglementations par identifiant.

### Évolutions fonctionnelles
- Amélioration de la recherche de routes lors du calcul des tracés sur la base de données BDTopo, incluant la recherche dans `troncon_de_route` et `voie_nommee` [#1954](https://github.com/MTES-MCT/dialog/issues/1954).
- Pré-remplissage automatique du type de voie et de la commune dans le formulaire de localisation [#1951](https://github.com/MTES-MCT/dialog/issues/1951).
- Ajout de 3 nouvelles expressions pour reconnaître "toute la journée" dans l'analyse des périodes [#1952](https://github.com/MTES-MCT/dialog/issues/1952).
- Gestion des restrictions applicables à des villes entières [#1945](https://github.com/MTES-MCT/dialog/issues/1945).
- Clarification de la sélection du modèle d'arrêté dans le formulaire [#1941](https://github.com/MTES-MCT/dialog/issues/1941).
- Masquage du nom de l'éditeur dans le formulaire si l'utilisateur n'est pas connecté [#1965](https://github.com/MTES-MCT/dialog/issues/1965).
- Ajout d'un séparateur ":" pour les périodes dans le parseur Litteralis [#1966](https://github.com/MTES-MCT/dialog/issues/1966).
- Ajout d'une information concernant les sessions "Ask Me Anything" [#1935](https://github.com/MTES-MCT/dialog/issues/1935).

### Évolutions techniques
- Ajout d'une commande pour supprimer des réglementations via la ligne de commande [#1947](https://github.com/MTES-MCT/dialog/issues/1947).
- Implémentation d'une API pour récupérer une réglementation par son identifiant [#1927](https://github.com/MTES-MCT/dialog/issues/1927).
- Implémentation d'une API pour mettre à jour une réglementation par son identifiant [#1928](https://github.com/MTES-MCT/dialog/issues/1928).
- Mise à jour de Playwright dans le workflow CI [#1940](https://github.com/MTES-MCT/dialog/issues/1940).
- Ajout d'un script pour restaurer et anonymiser les sauvegardes de la base de données, suppression de la fonctionnalité "sync team" [#1901](https://github.com/MTES-MCT/dialog/issues/1901).

### Autres changements
- Aucun changement significatif à signaler.
