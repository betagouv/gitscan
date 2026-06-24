## Changelog : dialog (30 derniers jours, au 23 juin 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application Dialog avec un focus sur la cartographie, la gestion des arrêtés et l'API. Des améliorations de performance ont été apportées à la cartographie, et de nouvelles fonctionnalités ont été ajoutées pour faciliter la publication et la visualisation des arrêtés. L'API a également été enrichie avec la possibilité de récupérer une réglementation par identifiant.

### Évolutions fonctionnelles
- Ajout d'un message informant de la réunion "Ask Me Anything" concernant le projet. [#1935](https://github.com/MTES-MCT/dialog/issues/1935)
- Possibilité de récupérer une réglementation par identifiant via l'API. [#1927](https://github.com/MTES-MCT/dialog/issues/1927)
- Export de l'iframe de la cartographie DiaLog. [#1891](https://github.com/MTES-MCT/dialog/issues/1891)
- Icône du véhicule sur la carte désormais dynamique. [#1905](https://github.com/MTES-MCT/dialog/issues/1905)
- Ajout d'un nouveau type de restriction exceptionnelle : résident local. [#1903](https://github.com/MTES-MCT/dialog/issues/1903)
- Ajout d'un filtre "Brouillon" sur la cartographie. [#1899](https://github.com/MTES-MCT/dialog/issues/1899)
- Amélioration de la modal de publication d'arrêté (ajout d'un oeil pour visualiser les arrêtés publiés). [#1915](https://github.com/MTES-MCT/dialog/issues/1915) [#1914](https://github.com/MTES-MCT/dialog/issues/1914)
- Introduction d'un nouveau "skin" de mesure. [#1887](https://github.com/MTES-MCT/dialog/issues/1887)
- Amélioration des validations des limites de vitesse et du gabarit. [#1881](https://github.com/MTES-MCT/dialog/issues/1881)
- Amélioration de la synthèse de l'arrêté. [#1876](https://github.com/MTES-MCT/dialog/issues/1876)
- Mise à jour du wording concernant le GPS. [#1880](https://github.com/MTES-MCT/dialog/issues/1880)
- Amélioration de la duplication de mesure. [#1879](https://github.com/MTES-MCT/dialog/issues/1879)
- Modification du wording de la modal de suppression d'arrêté officiel. [#1882](https://github.com/MTES-MCT/dialog/issues/1882)

### Évolutions techniques
- Mise à jour des BDTOPO et du script d'import associé. [#1851](https://github.com/MTES-MCT/dialog/issues/1851)
- Correction du géocodage sans `roadban id` depuis l'API. [#1922](https://github.com/MTES-MCT/dialog/issues/1922)
- Correction d'une erreur qui remontait incorrectement sur le champ intersection des localisations. [#1871](https://github.com/MTES-MCT/dialog/issues/1871)
- Correction de la duplication de mesure. [#1900](https://github.com/MTES-MCT/dialog/issues/1900)
- Correction de l'ordre d'affichage de la popup sur la carte. [#1885](https://github.com/MTES-MCT/dialog/issues/1885)
- Correction de l'export de la cartographie vers Word. [#1893](https://github.com/MTES-MCT/dialog/issues/1893)
- Amélioration des performances de la cartographie. [#1890](https://github.com/MTES-MCT/dialog/issues/1890)
- Ajout d'un script pour restaurer et anonymiser les sauvegardes de la base de données, suppression de la fonctionnalité "équipe sync". [#1901](https://github.com/MTES-MCT/dialog/issues/1901)
- Correction de l'utilisation de Playwright dans la CI. [#1940](https://github.com/MTES-MCT/dialog/issues/1940)
- Amélioration de la preview de la cartographie. [#1852](https://github.com/MTES-MCT/dialog/issues/1852)
- Ajout de la taille du fichier et de la réponse HEAD pour augmenter la disponibilité de datex. [#1874](https://github.com/MTES-MCT/dialog/issues/1874)
- Gestion des cas où la période de réglementation est vide (lancement d'une erreur). [#1921](https://github.com/MTES-MCT/dialog/issues/1921)
