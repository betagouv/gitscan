## Changelog : dora (30 derniers jours, au 14 août 2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié d'améliorations significatives pour faciliter la recherche de services et la consultation des informations liées aux publics. L'expérience utilisateur a été fluidifiée par des corrections sur les filtres et l'interface de recherche, tandis que des travaux de fond ont été menés pour moderniser la structure des données et optimiser la gestion des services et des orientations.

### Évolutions fonctionnelles
- **Recherche et navigation**
  - Expérimentation de la recherche par texte (A/B test) [#1194](https://github.com/gip-inclusion/dora/issues/1194).
  - Limitation du nombre de résultats de recherche pour éviter de submerger les utilisateurs [#1245](https://github.com/gip-inclusion/dora/issues/1245).
  - Activation de la recherche lors de l'appui sur la touche "Entrée" [#1230](https://github.com/gip-inclusion/dora/issues/1230).
  - Correction des filtres pour assurer l'affichage correct des services "tous-publics" [#1261](https://github.com/gip-inclusion/dora/issues/1261).
  - Suppression des doublons dans les résultats de recherche sémantique [#1228](https://github.com/gip-inclusion/dora/issues/1228).
- **Consultation des services**
  - Affichage des précisions concernant les publics sur les pages de détails des services [#1264](https://github.com/gip-inclusion/dora/issues/1264).
  - Nettoyage du balisage Markdown dans les descriptions courtes des services [#1221](https://github.com/gip-inclusion/dora/issues/1221).
  - Amélioration de la gestion des erreurs : affichage d'une page 404 explicite pour les services inaccessibles [#1224](https://github.com/gip-inclusion/dora/issues/1224).
- **Gestion et conformité**
  - Allègement de l'affichage du tableau des structures dans le tableau de bord des gestionnaires de territoire [#1229](https://github.com/gip-inclusion/dora/issues/1229).
  - Ajout de la possibilité d'exporter les orientations "Les Emplois" [#1209](https://github.com/gip-inclusion/dora/issues/1209).
  - Mise à jour des Conditions Générales d'Utilisation (CGU) [#1182](https://github.com/gip-inclusion/dora/issues/1182) et de la déclaration d'accessibilité [#1202](https://github.com/gip-inclusion/dora/issues/1202).

### Évolutions techniques
- **Refonte du modèle de données**
  - Migration progressive des données "Publics" vers le nouveau référentiel DI [#1237](https://github.com/gip-inclusion/dora/issues/1237).
  - Introduction d'un champ unique `kind` pour définir le type de service [#1249](https://github.com/gip-inclusion/dora/issues/1249).
  - Optimisation du stockage des recherches sauvegardées via le passage au format `ArrayField` [#1247](https://github.com/gip-inclusion/dora/issues/1247).
  - Migration de la lecture des publics vers de nouvelles colonnes de base de données [#1252](https://github.com/gip-inclusion/dora/issues/1252).
- **Backend et API**
  - Amélioration de la synchronisation des statuts des orientations avec l'ajout d'une date de traitement [#1212](https://github.com/gip-inclusion/dora/issues/1212).
  - Sécurisation de la suppression des objets en cascade [#1220](https://github.com/gip-inclusion/dora/issues/1220).
  - Partage de types communs entre les modèles et les services pour renforcer la cohérence du code [#1265](https://github.com/gip-inclusion/dora/issues/1265).
- **Infrastructure et outils**
  - Mise à jour majeure de la bibliothèque cartographique MapLibre GL [#1231](https://github.com/gip-inclusion/dora/issues/1231).
  - Remplacement de la bibliothèque de génération de fichiers Excel [#1191](https://github.com/gip-inclusion/dora/issues/1191).
  - Augmentation de la couverture de tests sur les critères d'orientabilité des services [#1227](https://github.com/gip-inclusion/dora/issues/1227).

### Autres changements
- Nettoyage du code : suppression de commandes d'import inutilisées [#1260](https://github.com/gip-inclusion/dora/issues/1260) et de fichiers de signaux en doublon [#1263](https://github.com/gip-inclusion/dora/issues/1263).
- Ajout d'une commande pour supprimer les anciennes structures orphelines [#1219](https://github.com/gip-inclusion/dora/issues/1219).
