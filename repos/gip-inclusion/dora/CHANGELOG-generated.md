## Changelog : dora (30 derniers jours, au 20 août 2026)

### Résumé
Ce mois-ci, le projet a été marqué par une refonte majeure de la gestion des données relatives aux publics afin d'améliorer la précision et la performance du système. L'expérience de recherche a été optimisée pour être plus intuitive, et plusieurs améliorations d'interface ont été apportées pour faciliter le travail des professionnels et des gestionnaires de territoire.

### Évolutions fonctionnelles
- **Optimisation de la recherche** : tests de la recherche textuelle (A/B test) [#1194, #1246, #1254], limitation du nombre de résultats pour une meilleure lisibilité [#1245], déclenchement de la recherche via la touche "Entrée" [#1230] et suppression des doublons dans la recherche sémantique [#1228].
- **Amélioration de la visibilité des services** : affichage des précisions sur les publics dans les pages de détails [#1264], correction du filtrage des services "tous publics" [#1261] et nettoyage du balisage Markdown dans les descriptions courtes [#1221].
- **Expérience utilisateur et accessibilité** : allègement du tableau des structures dans le tableau de bord des gestionnaires [#1229], gestion plus explicite des erreurs 404 pour les services inaccessibles [#1224] et mise à jour de la déclaration d'accessibilité [#1202].
- **Statistiques et exports** : ajout de l'export des orientations "Les Emplois" [#1209] et intégration de la zone géographique de recherche dans les statistiques [#1216].

### Évolutions techniques
- **Migration de données majeure** : refonte complète de la structure des "Publics" et du champ de type de service (`kind`), passant d'un modèle complexe à une structure simplifiée et plus performante [#1237, #1267, #1252, #1257, #1266, #1249].
- **Performances** : parallélisation des appels API pour accélérer le chargement des pages d'édition des services et des modèles [#1281].
- **Refactoring et maintenance** : partage de types communs entre les modèles Service et Model [#1265], migration des champs de recherche vers des types `ArrayField` [#1247] et suppression de nombreux composants, commandes et codes obsolètes [#1278, #1285, #1260, #1201, #1199].
- **Sécurité et robustesse** : ajout d'une commande de normalisation des mots de passe [#1271], protection des suppressions d'objets en cascade [#1220] et optimisation du reporting d'erreurs vers Sentry [#1203].

### Autres changements
- **Nettoyage** : suppression de fichiers de signaux en doublon [#1263].
