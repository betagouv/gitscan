## Changelog : ecobalyse-data (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'enrichissement et la correction des données d'ACV, notamment en ajoutant de nouveaux processus, ingrédients et transformations, ainsi qu'en améliorant la cohérence et la qualité des données existantes. Plusieurs corrections ont été apportées suite à des vérifications d'intégrité de la base de données.

### Évolutions fonctionnelles
- Correction d'ingrédients spécifiques pour améliorer la précision des données. [#256](https://github.com/MTES-MCT/ecobalyse-data/issues/256)
- Correction de l'irrigation pour le coton biologique. [#255](https://github.com/MTES-MCT/ecobalyse-data/issues/255)
- Ajout de processus de recyclage pour une meilleure couverture des cycles de vie. [#243](https://github.com/MTES-MCT/ecobalyse-data/issues/243)
- Correction de la localisation des activités créées. [#236](https://github.com/MTES-MCT/ecobalyse-data/issues/236)
- Ajout de processus d'utilisation des aliments. [#241](https://github.com/MTES-MCT/ecobalyse-data/issues/241)
- Alignement des noms affichés (displayName) pour une meilleure lisibilité et cohérence. [#258](https://github.com/MTES-MCT/ecobalyse-data/issues/258)
- Ajout de transformations pour la cuisson des aliments. [#260](https://github.com/MTES-MCT/ecobalyse-data/issues/260)
- Ajout de compléments pour le lait. [#266](https://github.com/MTES-MCT/ecobalyse-data/issues/266)
- Ajout de compléments pour l'alimentation animale. [#245](https://github.com/MTES-MCT/ecobalyse-data/issues/245)
- Ajout de cellules de batterie. [#272](https://github.com/MTES-MCT/ecobalyse-data/issues/272)

### Évolutions techniques
- Refactorisation pour corriger les scopes suite à des vérifications d'intégrité de la base de données. [#251](https://github.com/MTES-MCT/ecobalyse-data/issues/251)
- Synchronisation des processus. [#276](https://github.com/MTES-MCT/ecobalyse-data/issues/276)
- Ajout de la catégorie de matériaux aux ingrédients. [#250](https://github.com/MTES-MCT/ecobalyse-data/issues/250)
- Modification du type de matériau. [#253](https://github.com/MTES-MCT/ecobalyse-data/issues/253)
- Correction des activités de fin de vie (EoL). [#273](https://github.com/MTES-MCT/ecobalyse-data/issues/273) et [#267](https://github.com/MTES-MCT/ecobalyse-data/issues/267)
- Ajout de transformations de métaux et autres. [#257](https://github.com/MTES-MCT/ecobalyse-data/issues/257)
- Remplacement du fichier `activities.json` par des fichiers LCI atomiques pour une meilleure organisation. [#279](https://github.com/MTES-MCT/ecobalyse-data/issues/279)
- Correction des alias EoL. [#275](https://github.com/MTES-MCT/ecobalyse-data/issues/275)
- Correction des alias manquants. [#270](https://github.com/MTES-MCT/ecobalyse-data/issues/270)
- Remplissage des alias vides. [#261](https://github.com/MTES-MCT/ecobalyse-data/issues/261)

### Autres changements
- Masquage des animaux vivants dans les données. [#259](https://github.com/MTES-MCT/ecobalyse-data/issues/259)
- Correction des doublons de processus dans l'explorateur. [#249](https://github.com/MTES-MCT/ecobalyse-data/issues/249)
- Rendre les chemins des données utilisées dans les tests plus explicites. [#278](https://github.com/MTES-MCT/ecobalyse-data/issues/278)
