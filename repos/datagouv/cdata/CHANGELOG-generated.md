## Changelog : cdata (30 derniers jours, au 25 septembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience de recherche et d'exploration des données, notamment grâce à l'ajout de filtres temporels et une meilleure accessibilité. L'interface d'administration a été enrichie pour offrir une meilleure visibilité sur les discussions et les graphiques, tandis que des optimisations techniques ont renforcé la stabilité du rendu et la performance du cache.

### Évolutions fonctionnelles

**Exploration & Recherche**
- Ajout d'un filtre de date (calendrier) dans l'explorateur tabulaire [#1227](https://github.com/datagouv/cdata/issues/1227).
- Amélioration du filtrage pour gérer correctement les valeurs manquantes dans les cellules vides [#1241](https://github.com/datagouv/cdata/issues/1241).
- Exclusion des pages de thématiques de l'index de recherche pour éviter les résultats non pertinents [#1239](https://github.com/datagouv/cdata/issues/1239).
- Ajout d'une prévisualisation des mises à jour de tableaux de bord [#1218](https://github.com/datagouv/cdata/issues/1218).

**Gestion des Ressources**
- Possibilité de définir une URL externe pour les ressources [#1222](https://github.com/datagouv/cdata/issues/1222), [#1215](https://github.com/datagouv/cdata/issues/1215).
- Ajout d'explications sur la notion d'URL stable dans les métadonnées des ressources [#1230](https://github.com/datagouv/cdata/issues/1230).
- Extension de l'attribution des points de contact aux jeux de données et services de données publiés directement [#1189](https://github.com/datagouv/cdata/issues/1189).
- Suggestion de l'hébergement des fichiers OpenAPI sur `fichiers.numerique.gouv.fr` [#1226](https://github.com/datagouv/cdata/issues/1226).

**Interface & Accessibilité**
- Amélioration de l'accessibilité (a11y) pour l'explorateur de données [#1216](https://github.com/datagouv/cdata/issues/1216).
- Correction de l'affichage du bouton de recherche dans la barre de recherche (DSFR) [#1236](https://github.com/datagouv/cdata/issues/1236).
- Correction de l'attribution sur les cartes [#1224](https://github.com/datagouv/cdata/issues/1224) et de l'affichage du domaine météo [#1246](https://github.com/datagouv/cdata/issues/1246).
- Correction de doublons d'informations (élections sénatoriales) [#1233](https://github.com/datagouv/cdata/issues/1233).
- Gestion plus propre des erreurs 404 sur les pages de listes inexistantes [#1199](https://github.com/datagouv/cdata/issues/1199).
- Correction de la gestion des doublons lors de l'acceptation d'adhésions [#1209](https://github.com/datagouv/cdata/issues/1209).

**Administration**
- Affichage des cartes de graphiques dans l'interface d'administration [#1210](https://github.com/datagouv/cdata/issues/1210).
- Affichage du dernier commentaire et du titre dans le tableau d'administration des discussions [#1225](https://github.com/datagouv/cdata/issues/1225).
- Correction de crashs sur les pages admin lors de la gestion de demandes de transfert anciennes [#1248](https://github.com/datagouv/cdata/issues/1248).
- Possibilité de désactiver le lien vers l'organisation sur les cartes [#1242](https://github.com/datagouv/cdata/issues/1242).

### Évolutions techniques

**Performance & Cache**
- Mise en place d'un cache `stale-while-revalidate` d'une heure pour les pages afin de réduire la charge sur GitHub [#1200](https://github.com/datagouv/cdata/issues/1200).

**Stabilité & Rendu**
- Correction des erreurs d'hydratation liées aux fuseaux horaires via l'utilisation systématique du composant `FormattedDate` [#1198](https://github.com/datagouv/cdata/issues/1198).
- Correction de problèmes de rendu côté serveur (SSR) pour les cartes de survol des lignes de ressources [#1208](https://github.com/datagouv/cdata/issues/1208).
- Correction de crashs sur les profils tabulaires utilisant le format Parquet [#1211](https://github.com/datagouv/cdata/issues/1211).
- Amélioration de la détection de l'encodage des données structurées [#1237](https://github.com/datagouv/cdata/issues/1237).
- Correction de la gestion du défilement (scroll) pour assurer la compatibilité avec Nuxt [#1207](https://github.com/datagouv/cdata/issues/1207).

**CI/CD & Sécurité**
- Ajout d'un tag Docker `latest` sur la branche main [#1221](https://github.com/datagouv/cdata/issues/1221).
- Optimisation du processus de publication de `datagouv-components` pour éviter les conflits lors de runs simultanés [#1206](https://github.com/datagouv/cdata/issues/1206).
- Correction de la gestion des vulnérabilités auditées [#1217](https://github.com/datagouv/cdata/issues/1217).

### Autres changements
- Mise à jour de `datagouv-components` en version 1.4.0 [#1243](https://github.com/datagouv/cdata/issues/1243).
