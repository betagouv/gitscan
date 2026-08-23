## Changelog : dora (30 derniers jours, au 22 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante dans la simplification de sa structure de données, notamment via une refonte majeure de la gestion des publics et des catégories de services. Les utilisateurs bénéficieront d'une recherche plus performante et de résultats mieux affichés, tandis que les gestionnaires disposent d'outils de pilotage et d'exportation enrichis.

### Évolutions fonctionnelles
- **Recherche & Filtres**
  - Amélioration de la recherche textuelle avec une meilleure gestion des doublons pour des résultats plus précis [#1228](https://github.com/gip-inclusion/dora/issues/1228).
  - Limitation du nombre de résultats de recherche pour améliorer la lisibilité et l'expérience utilisateur [#1245](https://github.com/gip-inclusion/dora/issues/1245).
  - Correction du comportement de la recherche lors de l'appui sur la touche "Entrée" [#1230](https://github.com/gip-inclusion/dora/issues/1230).
  - Correction de l'affichage des services "tous publics" dans les filtres [#1261](https://github.com/gip-inclusion/dora/issues/1261).
- **Gestion des Services & Structures**
  - Affichage des précisions concernant les publics sur la page de détail des services [#1264](https://github.com/gip-inclusion/dora/issues/1264).
  - Suppression de la limite du nombre de catégories par service [#1289](https://github.com/gip-inclusion/dora/issues/1289).
  - Filtrage du balisage Markdown dans les descriptions courtes des services [#1221](https://github.com/gip-inclusion/dora/issues/1221).
  - Allègement de l'affichage du tableau des structures pour les gestionnaires de territoire [#1229](https://github.com/gip-inclusion/dora/issues/1229).
  - Accès facilité pour les gestionnaires de territoire vers les pages d'administration des structures [#1286](https://github.com/gip-inclusion/dora/issues/1286).
- **Statistiques & Orientations**
  - Ajout de la possibilité de stocker le code de la zone géographique (commune, département ou région) pour les recherches [#1216](https://github.com/gip-inclusion/dora/issues/1216).
  - Nouvelle commande d'exportation des orientations "Les Emplois" [#1209](https://github.com/gip-inclusion/dora/issues/1209).
  - Ajout de la date de traitement (`processing_date`) pour la synchronisation des statuts des orientations [#1212](https://github.com/gip-inclusion/dora/issues/1212).
- **Corrections d'expérience utilisateur**
  - Gestion correcte des erreurs 404 pour les services inaccessibles au lieu d'une redirection vers la connexion [#1224](https://github.com/gip-inclusion/dora/issues/1224).
  - Garantie de l'unicité des critères d'admission [#1243](https://github.com/gip-inclusion/dora/issues/1243).

### Évolutions techniques
- **Refonte de la gestion des données (Publics & Services)**
  - Migration majeure de la gestion des "Publics" vers le nouveau référentiel DI [#1237](https://github.com/gip-inclusion/dora/issues/1237).
  - Simplification du modèle de données des services via l'introduction d'un champ de type unique (`kind`) et la suppression des anciens modèles et relations M2M (`ServiceKind`, `kinds`) [#1249](https://github.com/gip-inclusion/dora/issues/1249), [#1266](https://github.com/gip-inclusion/dora/issues/1266), [#1257](https://github.com/gip-inclusion/dora/issues/1257).
  - Migration des champs de recherche (`SavedSearch`, `SearchView`) vers un format `ArrayField` pour plus d'efficacité [#1247](https://github.com/gip-inclusion/dora/issues/1247).
- **Optimisations & Performance**
  - Parallélisation des appels API pour accélérer le chargement des pages d'édition de services et de modèles [#1281](https://github.com/gip-inclusion/dora/issues/1281).
  - Partage des types de données communs entre les entités `Service` et `Model` [#1265](https://github.com/gip-inclusion/dora/issues/1265).
- **Maintenance & Sécurité**
  - Protection contre la suppression en cascade d'objets [#1220](https://github.com/gip-inclusion/dora/issues/1220).
  - Ajout d'une commande de normalisation des mots de passe [#1271](https://github.com/gip-inclusion/dora/issues/1271).
  - Réduction des doublons de rapports d'erreurs vers Sentry [#1203](https://github.com/gip-inclusion/dora/issues/1203).

### Autres changements
- **Nettoyage du code**
  - Suppression de diverses commandes d'import/export et de code obsolète (services d'inclusion numérique, anciennes structures orphelines, etc.) [#1285](https://github.com/gip-inclusion/dora/issues/1285), [#1278](https://github.com/gip-inclusion/dora/issues/1278), [#1260](https://github.com/gip-inclusion/dora/issues/1260), [#1219](https://github.com/gip-inclusion/dora/issues/1219).
  - Renommage de champs pour une meilleure clarté (`full_desc` vers `description`) [#1282](https://github.com/gip-inclusion/dora/issues/1282).
