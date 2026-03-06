## Changelog : ecobalyse (30 derniers jours)

### Résumé
Les dernières mises à jour d'ecobalyse apportent des améliorations fonctionnelles significatives, notamment l'ajout de la gestion des favoris (export/import), l'amélioration de l'affichage des impacts pour certains types de données (textile, packaging) et l'introduction d'une nouvelle portée "food2". Des corrections de bugs ont également été implémentées pour améliorer la stabilité et l'expérience utilisateur, ainsi que des optimisations techniques et de sécurité.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter et d'importer les favoris [#1784](https://github.com/MTES-MCT/ecobalyse/issues/1784)
- Introduction de la portée "food2" pour les données alimentaires [#1861](https://github.com/MTES-MCT/ecobalyse/issues/1861)
- Affichage des impacts des trims pour les données textiles [#1835](https://github.com/MTES-MCT/ecobalyse/issues/1835)
- Ajout de la possibilité d'exprimer la masse des vêtements textiles en grammes [#1818](https://github.com/MTES-MCT/ecobalyse/issues/1818)
- Amélioration de l'autofocus dans les champs de recherche de certains modals [#1824](https://github.com/MTES-MCT/ecobalyse/issues/1824) et [#1834](https://github.com/MTES-MCT/ecobalyse/issues/1834)
- Ajout d'une bannière d'avertissement lorsque les conditions d'utilisation ne sont pas acceptées [#1817](https://github.com/MTES-MCT/ecobalyse/issues/1817)
- Ajout de nouveaux ingrédients dans les données [#1670](https://github.com/MTES-MCT/ecobalyse/issues/1670)
- Amélioration des icônes des favoris [#1823](https://github.com/MTES-MCT/ecobalyse/issues/1823)

### Évolutions techniques
- Standardisation du shebang pour les scripts Python [#1874](https://github.com/MTES-MCT/ecobalyse/issues/1874)
- Mise à jour de la documentation d'installation [#1355](https://github.com/MTES-MCT/ecobalyse/issues/1355)
- Ajout de toutes les régions à la verticale "food" [#1856](https://github.com/MTES-MCT/ecobalyse/issues/1856)
- Amélioration de la gestion des erreurs d'authentification (ne plus les logger dans Sentry) [#1858](https://github.com/MTES-MCT/ecobalyse/issues/1858)
- Mise à jour des dépendances NodeJS [#1842](https://github.com/MTES-MCT/ecobalyse/issues/1842)
- Refactorisation pour utiliser "stage" au lieu de "step" dans le code [#1738](https://github.com/MTES-MCT/ecobalyse/issues/1738)
- Suppression du code de version legacy [#1792](https://github.com/MTES-MCT/ecobalyse/issues/1792)
- Suppression des actions de création de release [#1783](https://github.com/MTES-MCT/ecobalyse/issues/1783)
- Ajout d'une authentification obligatoire pour les appels API [#1779](https://github.com/MTES-MCT/ecobalyse/issues/1779)
- Amélioration du template de rapport de bug avec des sections supplémentaires [#1873](https://github.com/MTES-MCT/ecobalyse/issues/1873)

### Autres changements
- Correction d'un bug qui supprimait les données de session lors de la navigation entre les versions de l'application [#1756](https://github.com/MTES-MCT/ecobalyse/issues/1756)
- Correction d'un bug lié à l'affichage des impacts détaillés pour les objets/veli [#1709](https://github.com/MTES-MCT/ecobalyse/issues/1709)
- Correction d'un bug qui empêchait la fermeture des modals en cliquant en dehors [#1825](https://github.com/MTES-MCT/ecobalyse/issues/1825)
- Correction d'un bug lié à l'affichage des données de score_history en cas d'échec d'authentification [#1845](https://github.com/MTES-MCT/ecobalyse/issues/1845)
- Correction d'un bug qui empêchait l'application d'accepter toutes les valeurs pour le paramètre `sslmode` dans la chaîne de connexion PostgreSQL [#1852](https://github.com/MTES-MCT/ecobalyse/issues/1852)
- Correction d'un bug lié à l'affichage d'un message de bannière erroné [#1822](https://github.com/MTES-MCT/ecobalyse/issues/1822)
- Suppression d'une transition CSS sur les modals d'autocomplétion [#1826](https://github.com/MTES-MCT/ecobalyse/issues/1826)
- Correction d'un bug lié à l'exportation des données après les corrections d'encodage [#1857](https://github.com/MTES-MCT/ecobalyse/issues/1857)
- Correction d'un bug lié à la nouvelle exportation utilisant la nouvelle base de données Ginko [#1820](https://github.com/MTES-MCT/ecobalyse/issues/1820)
- Suppression d'un rapport de bug inutile [#1875](https://github.com/MTES-MCT/ecobalyse/issues/1875)
