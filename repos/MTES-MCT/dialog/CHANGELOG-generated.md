## Changelog : dialog (30 derniers jours, au 30 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des réglementations de circulation, notamment au niveau de l'API, de la cartographie et des formulaires. Des corrections ont été apportées pour améliorer la précision du géocodage et la publication des arrêtés. De nouvelles fonctionnalités ont été ajoutées pour faciliter l'export de la cartographie et la gestion des exceptions de restrictions.

### Évolutions fonctionnelles
- Possibilité de supprimer des réglementations via une commande bash. [#1947](https://github.com/MTES-MCT/dialog/issues/1947)
- Amélioration de la sélection du modèle d'arrêté dans le formulaire. [#1941](https://github.com/MTES-MCT/dialog/issues/1941)
- Gestion des restrictions sur les villes entières. [#1945](https://github.com/MTES-MCT/dialog/issues/1945)
- Ajout d'un filtre "Brouillon" sur la cartographie pour ne visualiser que les arrêtés non publiés. [#1899](https://github.com/MTES-MCT/dialog/issues/1899)
- Amélioration de la modal de publication d'arrêté. [#1915](https://github.com/MTES-MCT/dialog/issues/1915)
- Ajout d'un indicateur visuel (oeil) pour identifier les arrêtés publiés. [#1914](https://github.com/MTES-MCT/dialog/issues/1914)
- Ajout de nouvelles phrases pour la période "toute la journée" dans le parser de période. [#1952](https://github.com/MTES-MCT/dialog/issues/1952)
- Possibilité d'exporter un iframe de la cartographie DiaLog. [#1891](https://github.com/MTES-MCT/dialog/issues/1891)
- Ajout d'un nouveau type d'exception de restriction : "résident local". [#1903](https://github.com/MTES-MCT/dialog/issues/1903)

### Évolutions techniques
- Mise à jour de la BDTOPO et du script d'import associé. [#1851](https://github.com/MTES-MCT/dialog/issues/1851)
- Implémentation de la récupération d'une réglementation par son identifiant via l'API. [#1927](https://github.com/MTES-MCT/dialog/issues/1927)
- Implémentation de la mise à jour d'une réglementation par son identifiant via l'API. [#1928](https://github.com/MTES-MCT/dialog/issues/1928)
- Correction du géocodage en l'absence de `roadban id` depuis l'API. [#1922](https://github.com/MTES-MCT/dialog/issues/1922)
- Rendre l'icône du véhicule sur la carte dynamique. [#1905](https://github.com/MTES-MCT/dialog/issues/1905)
- Ajout d'un script pour restaurer et anonymiser les sauvegardes de la base de données, suppression de la fonctionnalité "sync team". [#1901](https://github.com/MTES-MCT/dialog/issues/1901)
- Correction d'une erreur qui se produisait si la période d'une réglementation était vide. [#1921](https://github.com/MTES-MCT/dialog/issues/1921)
- Correction de la duplication de mesures. [#1900](https://github.com/MTES-MCT/dialog/issues/1900)
- Correction de l'ordre d'affichage de la popup sur la carte. [#1885](https://github.com/MTES-MCT/dialog/issues/1885)
- Amélioration des validations des limites de vitesse et du gabarit. [#1881](https://github.com/MTES-MCT/dialog/issues/1881)
- Correction de l'export de la cartographie vers Word. [#1893](https://github.com/MTES-MCT/dialog/issues/1893)
- Introduction d'un nouveau "skin" de mesure. [#1887](https://github.com/MTES-MCT/dialog/issues/1887)
- Amélioration de la disponibilité de datex en ajoutant la taille du fichier et la réponse HEAD. [#1874](https://github.com/MTES-MCT/dialog/issues/1874)
- Mise à jour de Playwright dans la configuration CI. [#1940](https://github.com/MTES-MCT/dialog/issues/1940)

### Autres changements
- Ajout d'informations concernant une réunion "Ask Me Anything". [#1935](https://github.com/MTES-MCT/dialog/issues/1935)
