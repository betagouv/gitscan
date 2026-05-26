## Changelog : bhasile (30 derniers jours, au 22 mai 2026)

### Résumé
Le mois écoulé a été marqué par d'importantes améliorations de l'interface utilisateur, notamment au niveau de la gestion des structures et des adresses. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. L'ajout de tests unitaires et d'intégration renforce la qualité du code et facilite les évolutions futures.

### Évolutions fonctionnelles
- **Gestion des structures :**
    - Nouvelle interface pour la gestion des structures, incluant un en-tête structuré [#1264](https://github.com/betagouv/bhasile/issues/1264).
    - Migration vers le modèle `StructureVersion` pour une meilleure gestion des versions [#1258](https://github.com/betagouv/bhasile/issues/1258).
    - Possibilité de sélectionner plusieurs structures [#1230](https://github.com/betagouv/bhasile/issues/1230).
    - Ajout d'indicateurs de qualité pour les actes administratifs [#1218](https://github.com/betagouv/bhasile/issues/1218).
- **Gestion des adresses :**
    - Nouvelle interface pour l'importation d'adresses [#1206](https://github.com/betagouv/bhasile/issues/1206).
    - Extraction de l'état d'interaction avec l'adresse dans un hook réutilisable `useAddressInteraction` [#1271](https://github.com/betagouv/bhasile/issues/1271).
- **CPOM :**
    - Ajout de la possibilité d'ajouter des "autres actes administratifs" au CPOM [#1266](https://github.com/betagouv/bhasile/issues/1266).
    - Affichage des dates déduites des actes administratifs [#1260](https://github.com/betagouv/bhasile/issues/1260).
- **Divers :**
    - Ajout d'un nouveau bloc "activité" [#1262](https://github.com/betagouv/bhasile/issues/1262).
    - Masquage de l'en-tête collant lors du défilement vers le bas [#1265](https://github.com/betagouv/bhasile/issues/1265).
    - Ajout d'un commentaire pour les documents financiers [#1261](https://github.com/betagouv/bhasile/issues/1261).
    - Possibilité pour les avenants d'étendre la date de fin [#1211](https://github.com/betagouv/bhasile/issues/1211).
    - Tri alphabétique des codes DNA [#1204](https://github.com/betagouv/bhasile/issues/1204).

### Évolutions techniques
- **Architecture :** Passage à une architecture à 3 niveaux complète [#1219](https://github.com/betagouv/bhasile/issues/1219).
- **Routes :** Déplacement des gestionnaires PUT vers les routes `[id]` pour une meilleure conformité REST [#1270](https://github.com/betagouv/bhasile/issues/1270).
- **Tests :**
    - Ajout de tests pour les routes [#1210](https://github.com/betagouv/bhasile/issues/1210).
    - Ajout de tests pour la page des formulaires [#1203](https://github.com/betagouv/bhasile/issues/1203).
    - Ajout de tests pour le repository des structures [#1202](https://github.com/betagouv/bhasile/issues/1202).
- **Performances :** Limitation des logs pour l'activité utilisateur [#1263](https://github.com/betagouv/bhasile/issues/1263).
- **TypeScript :** Suppression d'une option TypeScript obsolète [#1235](https://github.com/betagouv/bhasile/issues/1235).

### Autres changements
- Mise à jour de l'image de la base de données [#1253](https://github.com/betagouv/bhasile/issues/1253).
- Corrections de style CSS mineures [#1249](https://github.com/betagouv/bhasile/issues/1249), [#1233](https://github.com/betagouv/bhasile/issues/1233), [#1213](https://github.com/betagouv/bhasile/issues/1213), [#1214](https://github.com/betagouv/bhasile/issues/1214).
- Correction de bugs liés à la redirection de l'opérateur [#1252](https://github.com/betagouv/bhasile/issues/1252), [#1251](https://github.com/betagouv/bhasile/issues/1251), [#1241](https://github.com/betagouv/bhasile/issues/1241).
- Correction de l'affichage de la favicon "new" [#1248](https://github.com/betagouv/bhasile/issues/1248).
- Déplacement des contacts vers le fichier `.env` [#1208](https://github.com/betagouv/bhasile/issues/1208).
- Correction d'un bug de build pour la carte [#1212](https://github.com/betagouv/bhasile/issues/1212).
- Correction d'un problème avec les valeurs nulles dans le tableau des numéros FINESS [#1207](https://github.com/betagouv/bhasile/issues/1207).
