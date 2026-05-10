## Changelog : bhasile (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment au niveau des tableaux et des formulaires, ainsi que sur l'ajout de nouvelles fonctionnalités comme la gestion des opérateurs et l'importation d'adresses. Des corrections de bugs et des optimisations de performance ont également été apportées pour une meilleure expérience utilisateur et une plus grande stabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'une page pour la gestion des opérateurs, incluant la recherche et la mise à jour des descriptions. [#1148](https://github.com/betagouv/bhasile/issues/1148)
- Amélioration de la gestion des adresses avec une nouvelle interface utilisateur pour l'importation. [#1206](https://github.com/betagouv/bhasile/issues/1206)
- Possibilité de sélectionner plusieurs structures simultanément. [#1230](https://github.com/betagouv/bhasile/issues/1230)
- Ajout de la possibilité d'étendre la date de fin des avenants. [#1211](https://github.com/betagouv/bhasile/issues/1211)
- Ajout d'indicateurs de qualité pour les actes administratifs. [#1218](https://github.com/betagouv/bhasile/issues/1218)
- Ajout d'un modal de confirmation lors de la modification d'un formulaire. [#1179](https://github.com/betagouv/bhasile/issues/1179)
- Ajout de la gestion des filiales dans la base de données et de leur affichage. [#1145](https://github.com/betagouv/bhasile/issues/1145)
- Ajout de notes. [#1146](https://github.com/betagouv/bhasile/issues/1146)
- Amélioration de l'affichage des documents financiers. [#1181](https://github.com/betagouv/bhasile/issues/1181)
- Ajout d'une notion de prévisionnel/réalisé pour les indicateurs financiers. [#1154](https://github.com/betagouv/bhasile/issues/1154)
- Possibilité de sélectionner un code DNA via un select au lieu d'une saisie textuelle. [#1144](https://github.com/betagouv/bhasile/issues/1144)

### Évolutions techniques
- Refonte de l'architecture vers une architecture à 3 niveaux. [#1219](https://github.com/betagouv/bhasile/issues/1219)
- Ajout de routes tests. [#1210](https://github.com/betagouv/bhasile/issues/1210)
- Ajout de tests unitaires pour le repository des structures. [#1202](https://github.com/betagouv/bhasile/issues/1202)
- Amélioration des pipelines CI/CD pour accélérer les builds. [#1168](https://github.com/betagouv/bhasile/issues/1168), [#1170](https://github.com/betagouv/bhasile/issues/1170), [#1172](https://github.com/betagouv/bhasile/issues/1172)
- Suppression d'une option TypeScript obsolète. [#1235](https://github.com/betagouv/bhasile/issues/1235)
- Suppression de dépendances inutiles. [#1191](https://github.com/betagouv/bhasile/issues/1191)
- Suppression d'indicateurs financiers du schéma de budget. [#1205](https://github.com/betagouv/bhasile/issues/1205)
- Déplacement de la logique de détermination de `isSubventionee` et `isAutorisee` côté serveur. [#1188](https://github.com/betagouv/bhasile/issues/1188)

### Autres changements
- Correction de bugs d'affichage CSS sur la page d'utilisation et la carte. [#1233](https://github.com/betagouv/bhasile/issues/1233), [#1212](https://github.com/betagouv/bhasile/issues/1212)
- Correction d'un bug empêchant le build de la carte. [#1212](https://github.com/betagouv/bhasile/issues/1212)
- Correction d'un problème de conversion de latitude/longitude. [#1186](https://github.com/betagouv/bhasile/issues/1186)
- Correction d'un flash de loader entre les requêtes de recherche. [#1195](https://github.com/betagouv/bhasile/issues/1195)
- Amélioration du style des statistiques des opérateurs. [#1213](https://github.com/betagouv/bhasile/issues/1213)
- Corrections cosmétiques sur la carte. [#1214](https://github.com/betagouv/bhasile/issues/1214)
- Mise à jour de la documentation et des tests.
- Correction de la gestion des documents sans granularité. [#1190](https://github.com/betagouv/bhasile/issues/1190), [#1193](https://github.com/betagouv/bhasile/issues/1193)
- Suppression du texte "aucun(e)". [#1187](https://github.com/betagouv/bhasile/issues/1187)
- Centrage des colonnes dans les tableaux. [#1157](https://github.com/betagouv/bhasile/issues/1157)
- Correction de la gestion des valeurs nulles dans les tableaux de FINESS. [#1207](https://github.com/betagouv/bhasile/issues/1207)
- Mise à jour des dépendances (typescript, @casl/react, hono, next, xmldom/xmldom).
