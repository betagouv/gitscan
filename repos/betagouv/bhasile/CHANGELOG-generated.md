## Changelog : bhasile (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, bhasile a bénéficié d'améliorations significatives en termes de gestion des structures, de l'expérience utilisateur et de la qualité du code. Des corrections de bugs ont été apportées, notamment concernant la recherche d'opérateurs et l'affichage de certaines informations. L'ajout de tests et la refactorisation du code visent à améliorer la stabilité et la maintenabilité de l'application.

### Évolutions fonctionnelles
- Possibilité de sélectionner plusieurs structures. [#1230](https://github.com/betagouv/bhasile/issues/1230)
- Amélioration de l'interface utilisateur pour l'importation d'adresses. [#1206](https://github.com/betagouv/bhasile/issues/1206)
- Possibilité d'étendre la date de fin des avenants. [#1211](https://github.com/betagouv/bhasile/issues/1211)
- Ajout d'une recherche d'opérateurs. [#1182](https://github.com/betagouv/bhasile/issues/1182)
- Affichage amélioré des documents financiers. [#1181](https://github.com/betagouv/bhasile/issues/1181)
- Ajout d'une modale de confirmation avant de quitter le formulaire de modification. [#1179](https://github.com/betagouv/bhasile/issues/1179)
- Affichage dynamique du libellé pour les cases à cocher DNA/FINESS. [#1175](https://github.com/betagouv/bhasile/issues/1175)
- Refonte de l'ordre des colonnes dans le tableau CPOM. [#1174](https://github.com/betagouv/bhasile/issues/1174)
- Ajout d'indicateurs de qualité pour les actes administratifs. [#1218](https://github.com/betagouv/bhasile/issues/1218)
- Calcul des dates des actes administratifs. [#1209](https://github.com/betagouv/bhasile/issues/1209)

### Évolutions techniques
- Refactorisation de l'architecture vers une approche à 3 niveaux. [#1219](https://github.com/betagouv/bhasile/issues/1219)
- Ajout de tests d'intégration pour les routes. [#1210](https://github.com/betagouv/bhasile/issues/1210)
- Ajout de tests pour la page des formulaires. [#1203](https://github.com/betagouv/bhasile/issues/1203)
- Ajout de tests pour le repository des structures. [#1202](https://github.com/betagouv/bhasile/issues/1202)
- Mise à jour de TypeScript vers la version 6.0.3. [#1222](https://github.com/betagouv/bhasile/issues/1222)
- Suppression d'une option TypeScript obsolète. [#1235](https://github.com/betagouv/bhasile/issues/1235)
- Amélioration de la gestion des granularités des documents financiers. [#1190](https://github.com/betagouv/bhasile/issues/1190) et [#1181](https://github.com/betagouv/bhasile/issues/1181)
- Déplacement de la logique `isSubventionee/isAutorisee` côté serveur. [#1188](https://github.com/betagouv/bhasile/issues/1188)
- Correction de la conversion latitude/longitude. [#1186](https://github.com/betagouv/bhasile/issues/1186)

### Autres changements
- Mise à jour de l'image de la base de données. [#1253](https://github.com/betagouv/bhasile/issues/1253)
- Correction de bugs liés à la redirection des opérateurs. [#1252](https://github.com/betagouv/bhasile/issues/1252) et [#1251](https://github.com/betagouv/bhasile/issues/1251)
- Correction de l'affichage de la nouvelle icône favicon. [#1248](https://github.com/betagouv/bhasile/issues/1248)
- Correction d'un bug CSS sur la page d'utilisation. [#1233](https://github.com/betagouv/bhasile/issues/1233)
- Correction de la construction pour la carte. [#1212](https://github.com/betagouv/bhasile/issues/1212)
- Suppression de "aucun(e)" dans les rapports. [#1187](https://github.com/betagouv/bhasile/issues/1187)
- Renommage des champs dans les rapports. [#1189](https://github.com/betagouv/bhasile/issues/1189)
- Déplacement des contacts vers les variables d'environnement. [#1208](https://github.com/betagouv/bhasile/issues/1208)
- Suppression d'indicateurs financiers du schéma de budget. [#1205](https://github.com/betagouv/bhasile/issues/1205)
- Tri alphabétique des codes DNA. [#1204](https://github.com/betagouv/bhasile/issues/1204)
- Correction d'un problème de `null` dans le tableau des FINESS. [#1207](https://github.com/betagouv/bhasile/issues/1207)
- Ajout de suivi d'utilisation. [#1177](https://github.com/betagouv/bhasile/issues/1177)
- Correction des tests E2E. [#1184](https://github.com/betagouv/bhasile/issues/1184) et [#1197](https://github.com/betagouv/bhasile/issues/1197)
- Correction d'un flash de loader entre les requêtes de recherche. [#1195](https://github.com/betagouv/bhasile/issues/1195)
- Amélioration du formatage de l'input "places autorisées". [#1194](https://github.com/betagouv/bhasile/issues/1194)
