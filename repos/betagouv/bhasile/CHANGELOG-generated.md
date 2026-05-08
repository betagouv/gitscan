## Changelog : bhasile (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'interface utilisateur, notamment au niveau des tableaux de données, de la gestion des adresses et des documents financiers. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la gestion des opérateurs et des structures. L'ajout de tests automatisés a été une priorité.

### Évolutions fonctionnelles
- Possibilité de sélectionner plusieurs structures. [#1230](https://github.com/betagouv/bhasile/issues/1230)
- Nouvelle interface utilisateur pour l'importation d'adresses. [#1206](https://github.com/betagouv/bhasile/issues/1206)
- Possibilité d'étendre la date de fin des avenants. [#1211](https://github.com/betagouv/bhasile/issues/1211)
- Ajout d'indicateurs de qualité pour les actes administratifs. [#1218](https://github.com/betagouv/bhasile/issues/1218)
- Amélioration de l'affichage des statistiques des opérateurs. [#1213](https://github.com/betagouv/bhasile/issues/1213)
- Ajout de la recherche d'opérateurs. [#1182](https://github.com/betagouv/bhasile/issues/1182)
- Ajout de notes. [#1146](https://github.com/betagouv/bhasile/issues/1146)
- Ajout de la gestion des filiales. [#1145](https://github.com/betagouv/bhasile/issues/1145)
- Possibilité de sélectionner un code DNA via un select au lieu d'une saisie textuelle. [#1144](https://github.com/betagouv/bhasile/issues/1144)
- Ajout d'une notion de prévisionnel/réalisé pour les indicateurs financiers. [#1154](https://github.com/betagouv/bhasile/issues/1154)
- Possibilité d'ajouter plusieurs adresses collectives. [#1160](https://github.com/betagouv/bhasile/issues/1160)

### Évolutions techniques
- Refactorisation de l'architecture vers une architecture à 3 niveaux. [#1219](https://github.com/betagouv/bhasile/issues/1219)
- Ajout de routes tests. [#1210](https://github.com/betagouv/bhasile/issues/1210)
- Ajout de tests unitaires pour le repository des structures. [#1202](https://github.com/betagouv/bhasile/issues/1202)
- Amélioration du pipeline CI/CD pour accélérer les builds. [#1168](https://github.com/betagouv/bhasile/issues/1168), [#1170](https://github.com/betagouv/bhasile/issues/1170), [#1172](https://github.com/betagouv/bhasile/issues/1172)
- Suppression d'une option TypeScript obsolète. [#1235](https://github.com/betagouv/bhasile/issues/1235)
- Déplacement de la logique de détermination de `isSubventionee` et `isAutorisee` côté serveur. [#1188](https://github.com/betagouv/bhasile/issues/1188)
- Suppression de dépendances inutiles. [#1191](https://github.com/betagouv/bhasile/issues/1191)
- Séparation du schéma Prisma. [#1142](https://github.com/betagouv/bhasile/issues/1142)

### Autres changements
- Correction de bugs CSS sur la page d'utilisation et dans la vue des qualités de structure. [#1233](https://github.com/betagouv/bhasile/issues/1233), [#1220](https://github.com/betagouv/bhasile/issues/1220)
- Correction d'un bug empêchant le build de la carte. [#1212](https://github.com/betagouv/bhasile/issues/1212)
- Correction d'un bug lié à la conversion de latitude/longitude. [#1186](https://github.com/betagouv/bhasile/issues/1186)
- Suppression de l'avertissement concernant les DNA multiples lors de l'ajout. [#1228](https://github.com/betagouv/bhasile/issues/1228)
- Correction d'un problème de z-index dans les tableaux. [#1171](https://github.com/betagouv/bhasile/issues/1171)
- Amélioration de l'affichage des documents financiers. [#1181](https://github.com/betagouv/bhasile/issues/1181)
- Correction d'un bug dans les tests de finalisation de formulaire. [#1197](https://github.com/betagouv/bhasile/issues/1197)
- Correction d'un flash de loader entre les requêtes de recherche. [#1195](https://github.com/betagouv/bhasile/issues/1195)
- Amélioration du formatage des champs "places autorisées". [#1194](https://github.com/betagouv/bhasile/issues/1194)
- Correction d'un bug empêchant la saisie de valeurs avec deux décimales. [#1165](https://github.com/betagouv/bhasile/issues/1165)
- Correction d'un bug lié à la présence de valeurs nulles dans le tableau des finesses. [#1207](https://github.com/betagouv/bhasile/issues/1207)
- Mise à jour de la documentation et des contacts dans le fichier `.env`. [#1208](https://github.com/betagouv/bhasile/issues/1208)
- Suppression du mot "aucun(e)". [#1187](https://github.com/betagouv/bhasile/issues/1187)
- Capitalisation des CPOMs. [#1143](https://github.com/betagouv/bhasile/issues/1143)
- Ajout de tests E2E pour la connexion Proconnect. [#1131](https://github.com/betagouv/bhasile/issues/1131)
