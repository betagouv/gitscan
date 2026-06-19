## Changelog : dialog (30 derniers jours, au 18 juin 2026)

### Résumé
Ce mois-ci, les évolutions de Dialog se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de la cartographie et de la gestion des arrêtés. Des corrections de bugs et des optimisations de performance ont également été apportées pour une meilleure stabilité et fluidité de l'application.

### Évolutions fonctionnelles
- **Cartographie :**
    - Possibilité d'exporter un iframe de la cartographie Dialog pour l'intégrer facilement dans d'autres applications. [#1891](https://github.com/MTES-MCT/dialog/issues/1891)
    - Ajout d'un filtre permettant d'afficher uniquement les arrêtés en brouillon sur la carte. [#1899](https://github.com/MTES-MCT/dialog/issues/1899)
    - Amélioration de la popup affichée sur la carte pour une meilleure lisibilité. [#1885](https://github.com/MTES-MCT/dialog/issues/1885)
    - Rendre l'icône du véhicule sur la carte dynamique. [#1905](https://github.com/MTES-MCT/dialog/issues/1905)
- **Gestion des arrêtés :**
    - Amélioration de la modal de publication d'un arrêté pour une expérience plus intuitive. [#1915](https://github.com/MTES-MCT/dialog/issues/1915)
    - Ajout d'un indicateur visuel (oeil) pour identifier les arrêtés déjà publiés. [#1914](https://github.com/MTES-MCT/dialog/issues/1914)
    - Ajout d'un nouveau type d'exception de restriction : résident local. [#1903](https://github.com/MTES-MCT/dialog/issues/1903)
    - Amélioration de la synthèse de l'arrêté. [#1876](https://github.com/MTES-MCT/dialog/issues/1876)
    - Amélioration du wording lié au GPS. [#1880](https://github.com/MTES-MCT/dialog/issues/1880)
    - Amélioration de la duplication de mesure. [#1879](https://github.com/MTES-MCT/dialog/issues/1879) et [#1900](https://github.com/MTES-MCT/dialog/issues/1900)
    - Modification du wording de la modal de suppression d'arrêté officiel. [#1882](https://github.com/MTES-MCT/dialog/issues/1882)
- **Formulaires :**
    - Introduction d'une nouvelle apparence (skin) pour les mesures. [#1887](https://github.com/MTES-MCT/dialog/issues/1887)
    - Correction d'une erreur de validation sur le champ "intersection" des localisations. [#1871](https://github.com/MTES-MCT/dialog/issues/1871)
- **Autres :**
    - Correction du géocodage en l'absence d'ID Roadban. [#1922](https://github.com/MTES-MCT/dialog/issues/1922)
    - Correction d'une erreur qui empêchait de signaler correctement une période de réglementation vide. [#1921](https://github.com/MTES-MCT/dialog/issues/1921)
    - Amélioration des validations des limites de vitesse et du gabarit. [#1881](https://github.com/MTES-MCT/dialog/issues/1881)
    - Correction de l'export de la cartographie vers Word. [#1893](https://github.com/MTES-MCT/dialog/issues/1893)

### Évolutions techniques
- Mise à jour des BDTOPO et du script d'import associé. [#1851](https://github.com/MTES-MCT/dialog/issues/1851)
- Amélioration des performances de la cartographie. [#1890](https://github.com/MTES-MCT/dialog/issues/1890)
- Ajout d'un script pour restaurer et anonymiser les sauvegardes de la base de données. [#1901](https://github.com/MTES-MCT/dialog/issues/1901)
- Ajout de la taille du fichier et de la réponse HEAD pour augmenter la disponibilité des données Datex. [#1874](https://github.com/MTES-MCT/dialog/issues/1874)
- Amélioration de la preview de la cartographie. [#1852](https://github.com/MTES-MCT/dialog/issues/1852)

### Autres changements
- Aucun changement significatif à signaler.
