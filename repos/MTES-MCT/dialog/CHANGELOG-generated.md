## Changelog : dialog (30 derniers jours, au 25 juin 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer les fonctionnalités de gestion des réglementations de circulation, notamment au niveau de l'API, de la cartographie et de la gestion des arrêtés. Des corrections ont été apportées pour améliorer la stabilité et l'expérience utilisateur, ainsi que des optimisations de performance sur la cartographie.

### Évolutions fonctionnelles
- Possibilité de mettre à jour une réglementation par son identifiant via l'API. [#1928](https://github.com/MTES-MCT/dialog/issues/1928)
- Gestion des restrictions sur des villes entières. [#1945](https://github.com/MTES-MCT/dialog/issues/1945)
- Clarification de la sélection du modèle d'arrêté dans le formulaire. [#1941](https://github.com/MTES-MCT/dialog/issues/1941)
- Ajout d'un message d'information concernant une session "Ask Me Anything". [#1935](https://github.com/MTES-MCT/dialog/issues/1935)
- Possibilité de récupérer une réglementation par son identifiant via l'API. [#1927](https://github.com/MTES-MCT/dialog/issues/1927)
- Ajout d'un nouveau type d'exception de restriction : résident local. [#1903](https://github.com/MTES-MCT/dialog/issues/1903)
- Ajout d'un filtre "Brouillon" sur la cartographie. [#1899](https://github.com/MTES-MCT/dialog/issues/1899)
- Amélioration de la modal de publication d'arrêté. [#1915](https://github.com/MTES-MCT/dialog/issues/1915)
- Ajout d'un indicateur visuel pour les arrêtés publiés. [#1914](https://github.com/MTES-MCT/dialog/issues/1914)
- Introduction d'un nouveau "skin" pour les mesures. [#1887](https://github.com/MTES-MCT/dialog/issues/1887)
- Possibilité d'exporter un iframe de la cartographie DiaLog. [#1891](https://github.com/MTES-MCT/dialog/issues/1891)
- Icône du véhicule sur la carte désormais dynamique. [#1905](https://github.com/MTES-MCT/dialog/issues/1905)

### Évolutions techniques
- Mise à jour de Playwright dans la configuration CI. [#1940](https://github.com/MTES-MCT/dialog/issues/1940)
- Switch vers les nouvelles BDTOPO et mise à jour du script d'import associé. [#1851](https://github.com/MTES-MCT/dialog/issues/1851)
- Correction du géocodage en l'absence de `roadban id` depuis l'API. [#1922](https://github.com/MTES-MCT/dialog/issues/1922)
- Correction d'une erreur qui se produisait si la période de réglementation était vide. [#1921](https://github.com/MTES-MCT/dialog/issues/1921)
- Amélioration des performances de la cartographie. [#1890](https://github.com/MTES-MCT/dialog/issues/1890)
- Correction de la duplication de mesures. [#1900](https://github.com/MTES-MCT/dialog/issues/1900)
- Correction de l'ordre d'affichage de la popup sur la carte. [#1885](https://github.com/MTES-MCT/dialog/issues/1885)
- Amélioration des validations des limites de vitesse et du gabarit. [#1881](https://github.com/MTES-MCT/dialog/issues/1881)
- Correction de l'export de la cartographie vers Word. [#1893](https://github.com/MTES-MCT/dialog/issues/1893)

### Autres changements
- Ajout d'un script pour restaurer et anonymiser les sauvegardes de la base de données, suppression de la fonctionnalité "sync team". [#1901](https://github.com/MTES-MCT/dialog/issues/1901)
- Ajout de la taille du fichier et de la réponse HEAD pour augmenter la disponibilité des données Datex. [#1874](https://github.com/MTES-MCT/dialog/issues/1874)
