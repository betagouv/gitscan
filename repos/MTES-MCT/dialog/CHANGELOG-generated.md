## Changelog : dialog (30 derniers jours, au 29 juillet 2026)

### Résumé
Les récentes mises à jour de dialog se concentrent sur l'amélioration de l'API, la correction de bugs liés à l'affichage et au stockage des données, ainsi que sur l'amélioration de l'importation et du parsing des données réglementaires. Des améliorations ont également été apportées à l'interface utilisateur pour faciliter la saisie et la visualisation des informations.

### Évolutions fonctionnelles
- L'API permet désormais de récupérer les réglementations par organisation. [#1967](https://github.com/MTES-MCT/dialog/issues/1967)
- Les réglementations sont maintenant correctement stockées, corrigeant un problème d'enregistrement vide. [#1979](https://github.com/MTES-MCT/dialog/issues/1979)
- Correction de l'affichage du filtre de type de véhicules sur la cartographie. [#1992](https://github.com/MTES-MCT/dialog/issues/1992)
- Amélioration des légendes de la cartographie pour une meilleure clarté. [#1984](https://github.com/MTES-MCT/dialog/issues/1984)
- Correction d'une erreur empêchant l'affichage des pièces jointes (PJ) sur les arrêtés. [#1990](https://github.com/MTES-MCT/dialog/issues/1990)
- Le formulaire de localisation pré-remplit maintenant le type de voie et la ville. [#1951](https://github.com/MTES-MCT/dialog/issues/1951)
- Le nom de l'éditeur est masqué dans le formulaire si l'utilisateur n'est pas connecté. [#1965](https://github.com/MTES-MCT/dialog/issues/1965)
- Ajout de nouvelles expressions pour identifier "toute la journée" dans le parseur de périodes. [#1952](https://github.com/MTES-MCT/dialog/issues/1952)
- Possibilité de filtrer les véhicules lourds sur la cartographie. [#1975](https://github.com/MTES-MCT/dialog/issues/1975)

### Évolutions techniques
- Correction d'un bug dans la recherche de tronçons de route et de voies nommées pour le calcul des lignes sur la base de données BDTopo. [#1954](https://github.com/MTES-MCT/dialog/issues/1954)
- Correction d'un problème avec l'opérateur `andwhere` dans le code. [#1985](https://github.com/MTES-MCT/dialog/issues/1985)
- Correction pour récupérer l'ID de l'interdiction de circulation (depuis et vers) à partir du nom. [#1968](https://github.com/MTES-MCT/dialog/issues/1968)
- Gestion des exceptions pour les restrictions sur des villes entières. [#1949](https://github.com/MTES-MCT/dialog/issues/1949)
- Ajout d'un séparateur ":" pour les périodes dans le parseur Litteralis. [#1966](https://github.com/MTES-MCT/dialog/issues/1966)
- Suppression de l'envoi automatique des rapports IGN. [#1991](https://github.com/MTES-MCT/dialog/issues/1991)
- Ajout d'une commande bash pour supprimer les réglementations de la base de données. [#1947](https://github.com/MTES-MCT/dialog/issues/1947)
- Les réglementations JSON sont maintenant publiques. [#1997](https://github.com/MTES-MCT/dialog/issues/1997)

### Autres changements
- Tri des utilisateurs administrateurs. [#1972](https://github.com/MTES-MCT/dialog/issues/1972)
- Correction d'un bug où la mesure n'appartenait pas à l'enregistrement de la commande. [#1983](https://github.com/MTES-MCT/dialog/issues/1983)
