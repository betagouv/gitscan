## Changelog : dora (30 derniers jours, au 13 août 2026)

### Résumé
Ce mois-ci, les évolutions ont principalement porté sur la modernisation de la gestion des données, notamment via la migration du référentiel des "Publics". L'expérience utilisateur a été affinée grâce à des améliorations de la recherche, une meilleure gestion des erreurs et des tableaux de bord plus lisibles pour les gestionnaires de territoire.

### Évolutions fonctionnelles
- **Recherche et navigation** :
    - Expérimentation et ajustements de la recherche textuelle [#1194](https://github.com/gip-inclusion/dora/issues/1194) [#1246](https://github.com/gip-inclusion/dora/issues/1246) [#1254](https://github.com/gip-inclusion/dora/issues/1254).
    - Limitation du nombre de résultats de recherche pour éviter la surcharge d'informations [#1245](https://github.com/gip-inclusion/dora/issues/1245).
    - Activation de la recherche via la touche "Entrée" pour une navigation plus fluide [#1230](https://github.com/gip-inclusion/dora/issues/1230).
- **Expérience utilisateur (UX)** :
    - Allègement du tableau des structures dans le tableau de bord des gestionnaires de territoire [#1229](https://github.com/gip-inclusion/dora/issues/1229).
    - Amélioration de la gestion des erreurs : affichage d'une page 404 pour les services inaccessibles au lieu d'une redirection vers la connexion [#1224](https://github.com/gip-inclusion/dora/issues/1224).
    - Nettoyage de l'affichage des descriptions de services via le filtrage du balisage Markdown [#1221](https://github.com/gip-inclusion/dora/issues/1221).
- **Nouvelles fonctionnalités et accessibilité** :
    - Mise à jour de la déclaration d'accessibilité de la plateforme [#1202](https://github.com/gip-inclusion/dora/issues/1202).
    - Ajout d'une fonction d'export des orientations pour "Les Emplois" [#1209](https://github.com/gip-inclusion/dora/issues/1209).
    - Passage des vues administratives de statistiques en mode lecture seule [#1179](https://github.com/gip-inclusion/dora/issues/1179).

### Évolutions techniques
- **Migration et gestion des données** :
    - Migration majeure des données "Publics" vers le nouveau référentiel DI [#1237](https://github.com/gip-inclusion/dora/issues/1237) et basculement vers de nouvelles colonnes de lecture [#1252](https://github.com/gip-inclusion/dora/issues/1252).
    - Refactorisation de la gestion des types de services (`kind`) et des recherches sauvegardées pour optimiser le stockage en base de données [#1247](https://github.com/gip-inclusion/dora/issues/1247) [#1249](https://github.com/gip-inclusion/dora/issues/1249).
    - Sécurisation de l'intégrité des données : garantie de l'unicité des critères d'admission [#1243](https://github.com/gip-inclusion/dora/issues/1243) et protection contre les suppressions d'objets en cascade [#1220](https://github.com/gip-inclusion/dora/issues/1220).
- **Backend et API** :
    - Ajout de la date de traitement (`processing_date`) dans le flux de synchronisation des statuts des orientations [#1212](https://github.com/gip-inclusion/dora/issues/1212).
    - Exclusion de certaines sources de données du formulaire Dora [#1225](https://github.com/gip-inclusion/dora/issues/1225).
- **Analytique et Statistiques** :
    - Amélioration du suivi statistique par l'intégration du code de zone géographique (commune, département, région) [#1216](https://github.com/gip-inclusion/dora/issues/1216).
    - Synchronisation de la table des données d'orientation des emplois [#1190](https://github.com/gip-inclusion/dora/issues/1190) et correction de l'export de pilotage [#1170](https://github.com/gip-inclusion/dora/issues/1170).
- **Qualité logicielle** :
    - Augmentation de la couverture de tests sur les critères d'orientabilité des services [#1227](https://github.com/gip-inclusion/dora/issues/1227).

### Autres changements
- **Maintenance et nettoyage** :
    - Suppression des commandes d'import inutilisées [#1260](https://github.com/gip-inclusion/dora/issues/1260) et nettoyage des anciennes structures orphelines [#1219](https://github.com/gip-inclusion/dora/issues/1219).
    - Remplacement de la bibliothèque de génération de fichiers Excel [#1191](https://github.com/gip-inclusion/dora/issues/1191).
