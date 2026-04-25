## Changelog : ecobalyse (30 derniers jours, au 2026-04-24)

### Résumé
Les dernières mises à jour d'ecobalyse se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout d'une recherche avancée (faceted search) et la possibilité d'éditer les éléments directement dans une fenêtre modale. Des corrections de données et des améliorations de l'interface utilisateur ont également été apportées, ainsi que des optimisations techniques et des mises à jour de dépendances.

### Évolutions fonctionnelles
- Ajout d'une recherche avancée (faceted search) dans l'explorateur de données. [#2125](https://github.com/MTES-MCT/ecobalyse/issues/2125)
- Possibilité d'éditer les éléments directement dans une fenêtre modale dédiée. [#2111](https://github.com/MTES-MCT/ecobalyse/issues/2111)
- Amélioration de l'expérience utilisateur lors de l'édition d'éléments (modal). [#2128](https://github.com/MTES-MCT/ecobalyse/issues/2128)
- Ajout de la possibilité de visualiser les impacts de la distribution. [#1963](https://github.com/MTES-MCT/ecobalyse/issues/1963)
- Ajout de compléments de processus dans l'explorateur. [#1966](https://github.com/MTES-MCT/ecobalyse/issues/1966)
- Ajout du pays "Europe et Maghreb". [#2085](https://github.com/MTES-MCT/ecobalyse/issues/2085)
- Ajout de compléments pour les aliments animaux. [#1944](https://github.com/MTES-MCT/ecobalyse/issues/1944)

### Évolutions techniques
- Refactorisation de l'authentification : suppression de l'authentification par cookie. [#2110](https://github.com/MTES-MCT/ecobalyse/issues/2110)
- Mise à jour des dépendances Python. [#2112](https://github.com/MTES-MCT/ecobalyse/issues/2112)
- Mise à jour des dépendances npm. [#2014](https://github.com/MTES-MCT/ecobalyse/issues/2014), [#2080](https://github.com/MTES-MCT/ecobalyse/issues/2080), [#2092](https://github.com/MTES-MCT/ecobalyse/issues/2092)
- Amélioration des messages d'erreur du backend de contribution. [#2092](https://github.com/MTES-MCT/ecobalyse/issues/2092)
- Amélioration de la configuration de dependabot pour gérer les branches et les écosystèmes. [#1977](https://github.com/MTES-MCT/ecobalyse/issues/1977)
- Mise à jour de la dépendance `lodash`. [#2017](https://github.com/MTES-MCT/ecobalyse/issues/2017)
- Mise à jour de la dépendance `picomatch`. [#1962](https://github.com/MTES-MCT/ecobalyse/issues/1962)

### Autres changements
- Corrections de données pour les ingrédients. [#2022](https://github.com/MTES-MCT/ecobalyse/issues/2022)
- Corrections de données pour le coton biologique avec irrigation. [#2021](https://github.com/MTES-MCT/ecobalyse/issues/2021)
- Corrections de données pour les activités de fin de vie (EoL). [#2120](https://github.com/MTES-MCT/ecobalyse/issues/2120), [#2105](https://github.com/MTES-MCT/ecobalyse/issues/2105), [#2041](https://github.com/MTES-MCT/ecobalyse/issues/2041)
- Suppression de certains pays dans food1. [#2101](https://github.com/MTES-MCT/ecobalyse/issues/2101)
- Ajout d'un pays inconnu dans food1. [#2102](https://github.com/MTES-MCT/ecobalyse/issues/2102)
- Ajout de transformations de cuisson. [#2069](https://github.com/MTES-MCT/ecobalyse/issues/2069)
- Ajout de processus de recyclage. [#2005](https://github.com/MTES-MCT/ecobalyse/issues/2005)
- Ajout de nouveaux types de matériaux. [#1980](https://github.com/MTES-MCT/ecobalyse/issues/1980)
- Modification des types de matériaux. [#1965](https://github.com/MTES-MCT/ecobalyse/issues/1965)
- Ajout de catégories de matériaux aux ingrédients. [#1972](https://github.com/MTES-MCT/ecobalyse/issues/1972)
- Correction de l'emplacement des activités créées. [#1919](https://github.com/MTES-MCT/ecobalyse/issues/1919)
- Correction de la synchronisation des données ecobalyse-data. [#1979](https://github.com/MTES-MCT/ecobalyse/issues/1979)
- Amélioration de la lisibilité du modèle de rapport d'incident. [#2122](https://github.com/MTES-MCT/ecobalyse/issues/2122)
- Correction de l'alignement des alias EoL. [#2123](https://github.com/MTES-MCT/ecobalyse/issues/2123)
- Mise à jour de heat-europe. [#2117](https://github.com/MTES-MCT/ecobalyse/issues/2117)
- Ajout de compléments de lait. [#2108](https://github.com/MTES-MCT/ecobalyse/issues/2108)
- Correction de la distance par défaut des routes pour la France. [#2109](https://github.com/MTES-MCT/ecobalyse/issues/2109), [#2099](https://github.com/MTES-MCT/ecobalyse/issues/2099), [#2068](https://github.com/MTES-MCT/ecobalyse/issues/2068)
- Correction d'un processus par défaut erroné dans food1. [#2065](https://github.com/MTES-MCT/ecobalyse/issues/2065)
- Correction de la suppression des impacts détaillés de l'archive de publication. [#2039](https://github.com/MTES-MCT/ecobalyse/issues/2039)
- Masquage des animaux vivants. [#2053](https://github.com/MTES-MCT/ecobalyse/issues/2053)
- Correction des doublons de processus dans l'explorateur. [#1968](https://github.com/MTES-MCT/ecobalyse/issues/1968)
- Ajout de vérifications d'intégrité de la base de données JSON aux CI. [#1953](https://github.com/MTES-MCT/ecobalyse/issues/1953)
- Correction d'un bug concernant les impacts détaillés sur object/veli. [#1709](https://github.com/MTES-MCT/ecobalyse/issues/1709)
