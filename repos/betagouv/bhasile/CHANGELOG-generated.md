## Changelog : bhasile (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur l'amélioration de l'interface utilisateur, notamment au niveau de la gestion des adresses, des structures et des documents. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. L'ajout de tests et la refactorisation du code sont également des points importants de cette période.

### Évolutions fonctionnelles
- **Gestion des adresses :** Nouvelle fonctionnalité permettant une interaction plus fluide avec les adresses, incluant un hook dédié (`useAddressInteraction`) [#1271].
- **CPOM :** Ajout de la possibilité d'ajouter des "autres actes administratifs" dans le CPOM [#1266].
- **Structure :** Migration vers `StructureVersion` pour une meilleure gestion des versions [#1258].
- **Activité :** Nouveau bloc d'activité a été ajouté [#1262].
- **Dates des actes administratifs :** Affichage des dates inférées à partir des actes administratifs [#1260].
- **Documents financiers :** Ajout d'un commentaire pour les documents financiers [#1261].
- **Interface utilisateur :**
    - Masquage de l'en-tête collant lors du défilement vers le bas [#1265].
    - Nouvelle structure de l'en-tête [#1264].
    - Nouvelle interface pour l'importateur d'adresses [#1206].
    - Amélioration du formatage de l'input "places autorisées" [#1194].
- **Avenants :** Possibilité pour les avenants d'étendre la date de fin [#1211].
- **Opérateur :**
    - Ajout d'une recherche d'opérateur [#1182].
    - Corrections et améliorations de l'interface opérateur [#1252, #1251, #1196].
- **Carte :** Modification de la carte et correction d'un problème de build [#1192, #1212].
- **Indicateurs de qualité :** Ajout de deux indicateurs de qualité pour les actes administratifs [#1218].
- **Rapports :** Renommage de champs dans les rapports [#1189].

### Évolutions techniques
- **Routes REST :** Déplacement des gestionnaires PUT vers les routes `[id]` pour une meilleure conformité REST [#1270].
- **Architecture :** Passage à une architecture à 3 niveaux complète [#1219].
- **Tests :**
    - Ajout de tests pour les routes [#1210].
    - Ajout de nouveaux types de tests [#1178].
    - Ajout de tests pour le repository des structures [#1202].
    - Correction de tests et ajout de tests E2E [#1197, #1184].
- **Dépendances :** Mise à jour de plusieurs dépendances (TypeScript, @casl/react, @xmldom/xmldom, next)
- **Suppression de code obsolète :** Suppression d'une option TypeScript obsolète [#1235].
- **Optimisation :** Déplacement de la logique `isSubventionee/isAutorisee` côté serveur [#1188].
- **Logs :** Limitation des logs pour l'activité utilisateur [#1263].

### Autres changements
- **Documentation :** Mise à jour de l'image de la base de données [#1253].
- **CSS :** Corrections mineures de style CSS [#1249, #1233, #1213, #0de3abc].
- **Configuration :** Déplacement des contacts vers le fichier `.env` [#1208].
- **Nettoyage de code :** Suppression de dépendances inutiles [#1191].
- **Correction de bugs :** Correction d'un problème d'affichage de la favicon [#1248].
- **Correction de conversion latitude/longitude :** Correction d'un bug de conversion de latitude et longitude [#1186].
- **Correction de bug :** Correction d'un bug concernant les documents sans granularité [#1190, #1183].
- **Suppression d'éléments inutiles :** Suppression de "aucun(e)" dans les rapports [#1187].
