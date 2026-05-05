## Changelog : bhasile (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment au niveau des tableaux et des formulaires, ainsi que sur l'ajout de nouvelles fonctionnalités comme la gestion des opérateurs et des filiales. Des corrections de bugs et des optimisations de performance ont également été apportées, en particulier concernant l'affichage des données financières et la gestion des adresses. L'architecture a été revue pour une meilleure séparation des responsabilités.

### Évolutions fonctionnelles
- Ajout d'une nouvelle page pour la gestion des opérateurs avec possibilité de recherche et de mise à jour de la description. [#1148](https://github.com/betagouv/bhasile/issues/1148)
- Ajout de la gestion des filiales, avec un seed initial et une intégration dans la base de données. [#1145](https://github.com/betagouv/bhasile/issues/1145)
- Amélioration de l'interface utilisateur pour l'importation d'adresses, avec une nouvelle interface plus intuitive. [#1206](https://github.com/betagouv/bhasile/issues/1206)
- Possibilité d'étendre la date de fin des avenants. [#1211](https://github.com/betagouv/bhasile/issues/1211)
- Ajout d'indicateurs de qualité pour les actes administratifs. [#1218](https://github.com/betagouv/bhasile/issues/1218)
- Amélioration du style des statistiques des opérateurs. [#1213](https://github.com/betagouv/bhasile/issues/1213)
- Amélioration de l'affichage de la carte. [#1214](https://github.com/betagouv/bhasile/issues/1214)
- Ajout d'une modal de confirmation lors de la fermeture d'un formulaire de modification. [#1179](https://github.com/betagouv/bhasile/issues/1179)
- Ajout d'un sélecteur pour le code DNA au lieu d'un champ texte. [#1144](https://github.com/betagouv/bhasile/issues/1144)
- Ajout de notes. [#1146](https://github.com/betagouv/bhasile/issues/1146)
- Amélioration de l'affichage des données financières avec un tableau par type de structure. [#1130](https://github.com/betagouv/bhasile/issues/1130)
- Ajout de la notion de prévisionnel/réalisé pour les indicateurs financiers. [#1154](https://github.com/betagouv/bhasile/issues/1154)

### Évolutions techniques
- Refactorisation de l'architecture vers une architecture à trois niveaux. [#1219](https://github.com/betagouv/bhasile/issues/1219)
- Ajout d'un routage client pour la transformation. [#1216](https://github.com/betagouv/bhasile/issues/1216)
- Suppression des indicateurs financiers du schéma budget. [#1205](https://github.com/betagouv/bhasile/issues/1205)
- Déplacement de la logique de détermination de `isSubventionee` et `isAutorisee` côté serveur. [#1188](https://github.com/betagouv/bhasile/issues/1188)
- Amélioration des performances des pipelines CI/CD. [#1172](https://github.com/betagouv/bhasile/issues/1172), [#1170](https://github.com/betagouv/bhasile/issues/1170), [#1169](https://github.com/betagouv/bhasile/issues/1169)
- Séparation du schéma Prisma. [#1142](https://github.com/betagouv/bhasile/issues/1142)
- Normalisation des dates et correction d'un champ inutile pour l'upload de fichiers. [#1136](https://github.com/betagouv/bhasile/issues/1136)

### Autres changements
- Ajout de tests unitaires et E2E pour diverses fonctionnalités. [#1203](https://github.com/betagouv/bhasile/issues/1203), [#1202](https://github.com/betagouv/bhasile/issues/1202), [#1197](https://github.com/betagouv/bhasile/issues/1197), [#1184](https://github.com/betagouv/bhasile/issues/1184), [#1178](https://github.com/betagouv/bhasile/issues/1178), [#1135](https://github.com/betagouv/bhasile/issues/1135), [#1131](https://github.com/betagouv/bhasile/issues/1131)
- Correction de bugs divers, notamment concernant l'affichage des tableaux, la gestion des adresses et la conversion de latitude/longitude. [#1220](https://github.com/betagouv/bhasile/issues/1220), [#1195](https://github.com/betagouv/bhasile/issues/1195), [#1194](https://github.com/betagouv/bhasile/issues/1194), [#1193](https://github.com/betagouv/bhasile/issues/1193), [#1190](https://github.com/betagouv/bhasile/issues/1190), [#1186](https://github.com/betagouv/bhasile/issues/1186), [#1166](https://github.com/betagouv/bhasile/issues/1166), [#1165](https://github.com/betagouv/bhasile/issues/1165), [#1162](https://github.com/betagouv/bhasile/issues/1162)
- Mise à jour de certaines dépendances.
- Correction de la construction pour la carte. [#1212](https://github.com/betagouv/bhasile/issues/1212)
- Suppression d'une dépendance inutile. [#1191](https://github.com/betagouv/bhasile/issues/1191)
- Correction d'un problème de z-index entre le tableau et l'en-tête. [#1171](https://github.com/betagouv/bhasile/issues/1171)
- Correction d'une faute de frappe dans les tableaux de budget. [#1163](https://github.com/betagouv/bhasile/issues/1163)
- Déplacement des contacts vers les variables d'environnement. [#1208](https://github.com/betagouv/bhasile/issues/1208)
- Ajout de tests pour les formulaires. [#1203](https://github.com/betagouv/bhasile/issues/1203)
- Correction d'un bug lié à la présence de valeurs nulles dans les tableaux de finesses. [#1207](https://github.com/betagouv/bhasile/issues/1207)
- Suppression de "aucun(e)". [#1187](https://github.com/betagouv/bhasile/issues/1187)
- Amélioration de l'affichage des colonnes dans les tableaux CPOM. [#1174](https://github.com/betagouv/bhasile/issues/1174)
- Ajout d'un message d'accès refusé amélioré. [#1105](https://github.com/betagouv/bhasile/issues/1105)
