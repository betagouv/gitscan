## Changelog : dora (30 derniers jours, au 31 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de l'expérience utilisateur, notamment au niveau de la recherche et de l'affichage des services. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme. Plusieurs optimisations techniques et mises à jour de dépendances ont été réalisées en arrière-plan.

### Évolutions fonctionnelles
- Amélioration de la recherche : la recherche déclenche désormais lors de l'appui sur la touche Entrée [#1230](https://github.com/gip-inclusion/dora/issues/1230).
- Recherche unifiée : implémentation d'une recherche par texte (en A/B test) [#1194](https://github.com/gip-inclusion/dora/issues/1194).
- Services : exclusion des sources data·inclusion du formulaire Dora [#1225](https://github.com/gip-inclusion/dora/issues/1225).
- Services : affichage d'une erreur 404 pour un service inaccessible au lieu d'une redirection vers la connexion [#1224](https://github.com/gip-inclusion/dora/issues/1224).
- Orientations : ajout de la source de l'orientation sur la page [#1155](https://github.com/gip-inclusion/dora/issues/1155).
- Orientations : ajout d'un endpoint de synchronisation des statuts des orientations Les Emplois [#1169](https://github.com/gip-inclusion/dora/issues/1169).
- Orientations : envoi de mails pour les orientations créées depuis les emplois [#1125](https://github.com/gip-inclusion/dora/issues/1125).
- Structures : ajout d'une commande de suppression des anciennes structures orphelines [#1219](https://github.com/gip-inclusion/dora/issues/1219).
- Structures : possibilité de réactiver une structure obsolète [#1145](https://github.com/gip-inclusion/dora/issues/1145).
- Tableaux de bord : allègement du tableau des structures dans le TDB gestionnaires de territoire [#1229](https://github.com/gip-inclusion/dora/issues/1229).
- Mise à jour des CGU [#1182](https://github.com/gip-inclusion/dora/issues/1182) et [#1135](https://github.com/gip-inclusion/dora/issues/1135).
- Suppression des notifications de relance au prescripteur [#1136](https://github.com/gip-inclusion/dora/issues/1136).

### Évolutions techniques
- Optimisation de la recherche sémantique : exclusion des doublons [#1228](https://github.com/gip-inclusion/dora/issues/1228).
- Protection contre la suppression en cascade d'objets [#1220](https://github.com/gip-inclusion/dora/issues/1220).
- Stockage du code de la zone géographique de recherche (commune, département ou région) pour les statistiques [#1216](https://github.com/gip-inclusion/dora/issues/1216).
- Refactoring : retrait de la recherche DORA de la recherche de services [#1201](https://github.com/gip-inclusion/dora/issues/1201).
- Refactoring : retrait de la méthode `_map_dora_kinds_to_di` [#1199](https://github.com/gip-inclusion/dora/issues/1199).
- Refactoring : utilisation de `getitem` pour accéder à la distance dans `_get_unified_results` [#1140](https://github.com/gip-inclusion/dora/issues/1140).
- Refactoring : retrait d'un indice de type incorrect [#1132](https://github.com/gip-inclusion/dora/issues/1132).
- Refactoring : utilisation de l’enum `ModeAccueil` de d·i [#1124](https://github.com/gip-inclusion/dora/issues/1124).
- Refactoring : retrait du filtre `supported_service_kinds` [#1176](https://github.com/gip-inclusion/dora/issues/1176).
- Remplacement de la bibliothèque de génération de fichier Excel [#1191](https://github.com/gip-inclusion/dora/issues/1191).
- Ajout du champ `processing_date` à l'endpoint de synchronisation des statuts des orientations [#1172](https://github.com/gip-inclusion/dora/issues/1172).
- Mise à jour majeure de maplibe-gl de 5.24.0 à 6.1.0 [#1231](https://github.com/gip-inclusion/dora/issues/1231).

### Autres changements
- Amélioration de la couverture des tests pour les critères d'orientabilité des services DI [#1227](https://github.com/gip-inclusion/dora/issues/1227).
- Correction d'un double report des erreurs inattendues à Sentry [#1203](https://github.com/gip-inclusion/dora/issues/1203).
- Correction d'une typo [#1181](https://github.com/gip-inclusion/dora/issues/1181).
- Correction d'erreurs 500 de Safari lors du rechargement après déploiement [#1160](https://github.com/gip-inclusion/dora/issues/1160) et [#1164](https://github.com/gip-inclusion/dora/issues/1164).
- Suppression du message de non-cumulabilité des services DI [#1144](https://github.com/gip-inclusion/dora/issues/1144).
- Mise à jour de la politique de confidentialité [#1149](https://github.com/gip-inclusion/dora/issues/1149).
- Amélioration du `FakeDataInclusionClient` [#1198](https://github.com/gip-inclusion/dora/issues/1198).
- Correction du tri des imports dans un fichier Python [#1200](https://github.com/gip-inclusion/dora/issues/1200).
- Passage des vues admin en lecture seule [#1179](https://github.com/gip-inclusion/dora/issues/1179).
- Suppression de l'app et des données Admin Express [#1154](https://github.com/gip-inclusion/dora/issues/1154).
- Mise à jour de la dépendance itoutils [#1165](https://github.com/gip-inclusion/dora/issues/1165).
- Plusieurs mises à jour de dépendances mineures et correctives ont été appliquées.
