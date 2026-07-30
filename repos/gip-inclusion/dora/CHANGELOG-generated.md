## Changelog : dora (30 derniers jours, au 29 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la stabilité et de la performance, notamment concernant la gestion des erreurs et la synchronisation des données. Plusieurs corrections ont été apportées pour améliorer l'expérience utilisateur, en particulier concernant la recherche et l'affichage des informations. Des efforts ont également été déployés pour optimiser l'infrastructure et la gestion des dépendances.

### Évolutions fonctionnelles
- Ajout d'une commande pour supprimer les anciennes structures orphelines [#1219](https://github.com/gip-inclusion/dora/issues/1219).
- Ajout du champ `processing_date` à l'endpoint de synchronisation des statuts des orientations [#1212](https://github.com/gip-inclusion/dora/issues/1212).
- Ajout d'un endpoint de synchronisation des statuts des orientations Les Emplois [#1169](https://github.com/gip-inclusion/dora/issues/1169).
- Ajout de la source de l'orientation sur la page d'affichage [#1155](https://github.com/gip-inclusion/dora/issues/1155).
- Mise à jour des CGU [#1182](https://github.com/gip-inclusion/dora/issues/1182) et [#1135](https://github.com/gip-inclusion/dora/issues/1135).
- Ajout d'une commande d'export des orientations Les Emplois [#1209](https://github.com/gip-inclusion/dora/issues/1209).
- Implémentation d'une recherche par texte (en A/B test) [#1194](https://github.com/gip-inclusion/dora/issues/1194).
- Suppression des notifications de relance au prescripteur [#1136](https://github.com/gip-inclusion/dora/issues/1136).
- Envoi de mails pour les orientations créées depuis les emplois [#1125](https://github.com/gip-inclusion/dora/issues/1125).
- Stockage du code de la zone géographique de recherche (commune, département ou région) [#1216](https://github.com/gip-inclusion/dora/issues/1216).

### Évolutions techniques
- Protection contre la suppression en cascade d'objets [#1220](https://github.com/gip-inclusion/dora/issues/1220).
- Remplacement de la bibliothèque de génération de fichier Excel [#1191](https://github.com/gip-inclusion/dora/issues/1191).
- Refactor de la recherche de services et suppression de code obsolète [#1201](https://github.com/gip-inclusion/dora/issues/1201), [#1199](https://github.com/gip-inclusion/dora/issues/1199), [#1176](https://github.com/gip-inclusion/dora/issues/1176), [#1175](https://github.com/gip-inclusion/dora/issues/1175), [#1140](https://github.com/gip-inclusion/dora/issues/1140), [#1132](https://github.com/gip-inclusion/dora/issues/1132).
- Amélioration du FakeDataInclusionClient [#1198](https://github.com/gip-inclusion/dora/issues/1198).
- Passage des vues admin en lecture seule [#1179](https://github.com/gip-inclusion/dora/issues/1179).
- Utilisation de l’enum ModeAccueil de d·i [#1124](https://github.com/gip-inclusion/dora/issues/1124).
- Suppression de l'espace entre le nom du contact et les autres infos de contact [#1148](https://github.com/gip-inclusion/dora/issues/1148).
- Suppression de l'app et des données Admin Express [#1154](https://github.com/gip-inclusion/dora/issues/1154).
- Remplacement de p7zip par 7zip pour compatibilité scalingo-22/26 [#1150](https://github.com/gip-inclusion/dora/issues/1150).

### Autres changements
- Correction d'un bug qui provoquait le double report des erreurs inattendues à Sentry [#1203](https://github.com/gip-inclusion/dora/issues/1203).
- Correction d'une typo [#1181](https://github.com/gip-inclusion/dora/issues/1181).
- Correction d'un bug qui remontait des fausses erreurs 500 lors du rechargement après déploiement [#1160](https://github.com/gip-inclusion/dora/issues/1160).
- Suppression du message de non-cumulabilité des services DI [#1144](https://github.com/gip-inclusion/dora/issues/1144).
- Mise à jour de la déclaration d’accessibilité [#1202](https://github.com/gip-inclusion/dora/issues/1202).
- Correction du tri des imports dans un fichier Python [#1200](https://github.com/gip-inclusion/dora/issues/1200).
- Amélioration du bouton de suppression d’option sélectionnée dans le dropdown [#1156](https://github.com/gip-inclusion/dora/issues/1156).
- Correction pour ne plus remonter à Sentry les erreurs de fetch des scripts tiers [#1146](https://github.com/gip-inclusion/dora/issues/1146).
- Plusieurs mises à jour de dépendances (actions/checkout, actions/setup-python, actions/setup-node, @babel/core, @sveltejs/kit, boto3, data-inclusion-schema, lint-staged, pygraphviz) ont été effectuées.
