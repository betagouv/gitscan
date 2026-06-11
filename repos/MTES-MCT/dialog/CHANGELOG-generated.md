## Changelog : dialog (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur de la cartographie et de la gestion des arrêtés. Des corrections de bugs ont été apportées pour améliorer la fiabilité de l'application, notamment concernant le géocodage et la duplication de mesures. Des optimisations de performance ont également été réalisées pour fluidifier l'utilisation de la carte.

### Évolutions fonctionnelles
- Amélioration de la modal de publication d'arrêté avec ajout d'un oeil pour identifier les arrêtés publiés [#1915](https://github.com/MTES-MCT/dialog/issues/1915) et [#1914](https://github.com/MTES-MCT/dialog/issues/1914).
- Ajout d'un filtre "Brouillon" sur la cartographie pour faciliter la gestion des arrêtés en cours [#1899](https://github.com/MTES-MCT/dialog/issues/1899).
- Possibilité de rendre l'icône du véhicule sur la carte dynamique [#1905](https://github.com/MTES-MCT/dialog/issues/1905).
- Ajout d'un nouveau type de restriction "résident local" dans le formulaire [#1903](https://github.com/MTES-MCT/dialog/issues/1903).
- Amélioration de la synthèse de l'arrêté dans le formulaire [#1876](https://github.com/MTES-MCT/dialog/issues/1876).
- Mise à jour du wording GPS pour plus de clarté [#1880](https://github.com/MTES-MCT/dialog/issues/1880).
- Amélioration de la duplication de mesure [#1879](https://github.com/MTES-MCT/dialog/issues/1879) et correction de la duplication de mesure [#1900](https://github.com/MTES-MCT/dialog/issues/1900).
- Correction du géocodage sans `roadban id` depuis l'API [#1922](https://github.com/MTES-MCT/dialog/issues/1922).
- Correction de l'export de la cartographie vers Word [#1893](https://github.com/MTES-MCT/dialog/issues/1893).
- Amélioration des validations des limites de vitesse et du gabarit [#1881](https://github.com/MTES-MCT/dialog/issues/1881).
- Correction de l'ordre d'affichage de la popup sur la carte [#1885](https://github.com/MTES-MCT/dialog/issues/1885).
- Wording amélioré pour la modal de suppression d'arrêté officiel [#1882](https://github.com/MTES-MCT/dialog/issues/1882).
- Affichage des légendes en fonction des tracés [#1848](https://github.com/MTES-MCT/dialog/issues/1848).

### Évolutions techniques
- Switch des BDTOPO et mise à jour du script d'import [#1851](https://github.com/MTES-MCT/dialog/issues/1851).
- Améliorations des performances de la carte [#1842](https://github.com/MTES-MCT/dialog/issues/1842) et [#1890](https://github.com/MTES-MCT/dialog/issues/1890).
- Ajout de la taille du fichier et de la réponse HEAD pour augmenter la disponibilité des données Datex [#1874](https://github.com/MTES-MCT/dialog/issues/1874).
- Correction d'une fausse remontée d'erreur sur le champ intersection des localisations [#1871](https://github.com/MTES-MCT/dialog/issues/1871).
- Introduction d'un nouveau "skin" de mesure [#1887](https://github.com/MTES-MCT/dialog/issues/1887).
- Mise à jour des couleurs de la carte [#1849](https://github.com/MTES-MCT/dialog/issues/1849).
- Améliorations de la preview de la cartographie [#1852](https://github.com/MTES-MCT/dialog/issues/1852).
- Correction d'une erreur si la période de réglementation est vide [#1921](https://github.com/MTES-MCT/dialog/issues/1921).

### Autres changements
- Aucun changement significatif à signaler.
