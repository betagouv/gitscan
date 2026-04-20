## Changelog : ecobalyse (30 derniers jours, au 2026-04-19)

### Résumé
Ce mois-ci, l'équipe a continué d'enrichir la base de données d'Ecobalyse avec de nouveaux processus, matériaux et compléments, notamment dans les domaines de l'alimentation, du textile et de la gestion des déchets. Des améliorations ont également été apportées à l'interface utilisateur et à l'API, notamment pour faciliter l'intégration avec d'autres systèmes et améliorer l'expérience utilisateur. Des corrections de bugs ont été implémentées pour assurer la stabilité et la fiabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout du pays "Europe et Maghreb" pour une meilleure granularité géographique. [#2085](https://github.com/MTES-MCT/ecobalyse/issues/2085)
- Possibilité de configurer la visibilité de la documentation de l'API Food1 (legacy). [#2088](https://github.com/MTES-MCT/ecobalyse/issues/2088)
- Amélioration des messages d'erreur du backend pour les contributions. [#2092](https://github.com/MTES-MCT/ecobalyse/issues/2092)
- Ajout de 500km de transport routier par défaut pour certains pays, améliorant la précision des calculs. [#2099](https://github.com/MTES-MCT/ecobalyse/issues/2099)
- Ajout de compléments de processus dans l'explorateur, offrant une vue plus complète des données. [#1966](https://github.com/MTES-MCT/ecobalyse/issues/1966)
- Ajout de la possibilité d'activer les étapes EOL via la configuration. [#1915](https://github.com/MTES-MCT/ecobalyse/issues/1915)
- Ajout d'animaux vivants dans les données. [#1932](https://github.com/MTES-MCT/ecobalyse/issues/1932)
- Ajout de processus de distribution alimentaire. [#1931](https://github.com/MTES-MCT/ecobalyse/issues/1922)
- Ajout de compléments d'impacts pour les processus. [#1895](https://github.com/MTES-MCT/ecobalyse/issues/1895)

### Évolutions techniques
- Refactor de la gestion des scopes génériques pour une meilleure maintenabilité. [#1929](https://github.com/MTES-MCT/ecobalyse/issues/1929)
- Amélioration de la gestion des clés JSON des compléments dans les réponses de l'API. [#1954](https://github.com/MTES-MCT/ecobalyse/issues/1954)
- Mise à jour des dépendances npm et Elm. [#2014](https://github.com/MTES-MCT/ecobalyse/issues/2014), [#2080](https://github.com/MTES-MCT/ecobalyse/issues/2080), [#2004](https://github.com/MTES-MCT/ecobalyse/issues/2004), [#1997](https://github.com/MTES-MCT/ecobalyse/issues/1997)
- Suppression de l'ordre `auth2` et nettoyage du code Elm. [#1583](https://github.com/MTES-MCT/ecobalyse/issues/1583)
- Ajout de tests d'intégrité de la base de données JSON à la CI. [#1953](https://github.com/MTES-MCT/ecobalyse/issues/1953)
- Modification des types de matériaux. [#1965](https://github.com/MTES-MCT/ecobalyse/issues/1965)
- Ajout de processus de recyclage. [#2005](https://github.com/MTES-MCT/ecobalyse/issues/2005)
- Implémentation du calcul des impacts de la distribution. [#1963](https://github.com/MTES-MCT/ecobalyse/issues/1963)

### Autres changements
- Correction de la fin de vie des activités (EoL). [#2105](https://github.com/MTES-MCT/ecobalyse/issues/2105)
- Correction des données pour le coton biologique avec irrigation. [#2021](https://github.com/MTES-MCT/ecobalyse/issues/2021)
- Correction d'un bug empêchant l'archivage des impacts détaillés. [#2039](https://github.com/MTES-MCT/ecobalyse/issues/2039)
- Correction de l'emplacement des activités créées. [#1919](https://github.com/MTES-MCT/ecobalyse/issues/1919)
- Correction de la duplication de processus dans l'explorateur. [#1968](https://github.com/MTES-MCT/ecobalyse/issues/1968)
- Correction d'un bug dans le processus Food1 par défaut. [#2065](https://github.com/MTES-MCT/ecobalyse/issues/2065)
- Ajout de la catégorie de matériaux aux ingrédients. [#1972](https://github.com/MTES-MCT/ecobalyse/issues/1972)
- Suppression des animaux vivants de l'affichage. [#2053](https://github.com/MTES-MCT/ecobalyse/issues/2053)
- Mise à jour des exemples Veli. [#1716](https://github.com/MTES-MCT/ecobalyse/issues/1716)
- Synchronisation des données ecobalyse-data. [#1979](https://github.com/MTES-MCT/ecobalyse/issues/1979)
- Correction de l'alignement des impacts dans le simulateur d'objets. [#1720](https://github.com/MTES-MCT/ecobalyse/issues/1720)
- Ajout de processus de transformation des métaux. [#2041](https://github.com/MTES-MCT/ecobalyse/issues/2041)
- Modification des types de matériaux. [#1965](https://github.com/MTES-MCT/ecobalyse/issues/1965)
