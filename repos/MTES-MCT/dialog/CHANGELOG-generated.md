## Changelog : dialog (30 derniers jours, au 23 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des restrictions de circulation, notamment pour les véhicules lourds et les restrictions géographiques sur des villes entières. L'API a été enrichie pour faciliter la gestion des arrêtés et des réglementations, et l'interface utilisateur a été améliorée pour une meilleure expérience de saisie et de visualisation des données.

### Évolutions fonctionnelles
- Correction d'une erreur empêchant l'affichage des pièces jointes (PJ) sur les arrêtés [#1990](https://github.com/MTES-MCT/dialog/issues/1990).
- Correction de l'affichage du filtre "type de véhicules" [#1992](https://github.com/MTES-MCT/dialog/issues/1992).
- Amélioration de la gestion des restrictions sur les villes entières [#1945](https://github.com/MTES-MCT/dialog/issues/1945) et gestion des exceptions liées à ces restrictions [#1949](https://github.com/MTES-MCT/dialog/issues/1949).
- Ajout d'un filtre pour les véhicules lourds sur la carte [#1975](https://github.com/MTES-MCT/dialog/issues/1975).
- Amélioration de la pré-remplissage du formulaire de localisation avec le type de route et la ville [#1951](https://github.com/MTES-MCT/dialog/issues/1951).
- Clarification de la sélection du modèle d'arrêté dans le formulaire [#1941](https://github.com/MTES-MCT/dialog/issues/1941).
- Ajout de nouvelles expressions pour reconnaître "toute la journée" dans l'analyse des périodes [#1952](https://github.com/MTES-MCT/dialog/issues/1952).
- Masquage du nom de l'éditeur si l'utilisateur n'est pas connecté [#1965](https://github.com/MTES-MCT/dialog/issues/1965).
- Correction de la recherche de tronçons de route et de voies nommées pour le calcul des lignes [#1954](https://github.com/MTES-MCT/dialog/issues/1954).
- Correction d'un problème de stockage des réglementations vides [#1857](https://github.com/MTES-MCT/dialog/issues/1857) [#1979](https://github.com/MTES-MCT/dialog/issues/1979).
- Amélioration des légendes de la carte [#1984](https://github.com/MTES-MCT/dialog/issues/1984).

### Évolutions techniques
- Introduction d'un endpoint API pour récupérer les ordres de réglementations par organisation [#1967](https://github.com/MTES-MCT/dialog/issues/1967).
- Mise en place d'une commande pour supprimer les réglementations via la base de données [#1947](https://github.com/MTES-MCT/dialog/issues/1947).
- Implémentation de la mise à jour d'une réglementation par son identifiant via l'API [#1928](https://github.com/MTES-MCT/dialog/issues/1928).
- Ajout du séparateur ":" pour les périodes dans le parseur Litteralis [#1966](https://github.com/MTES-MCT/dialog/issues/1966).
- Suppression de l'utilisateur "admin" [#1972](https://github.com/MTES-MCT/dialog/issues/1972).
- Amélioration de la récupération de l'ID d'interdiction de circulation (depuis et vers) à partir du nom [#1968](https://github.com/MTES-MCT/dialog/issues/1968).
