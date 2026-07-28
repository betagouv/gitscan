## Changelog : dora (30 derniers jours, au 27 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la recherche, des corrections de bugs et des mises à jour de la configuration et des dépendances. Des efforts ont également été déployés pour améliorer la qualité des données et l'expérience utilisateur, notamment en affinant l'affichage des informations et en optimisant les performances. Enfin, la conformité légale a été renforcée avec la mise à jour des CGU et de la déclaration d'accessibilité.

### Évolutions fonctionnelles
- **Recherche :** Implémentation d'une recherche par texte (en A/B test) [#1194](https://github.com/gip-inclusion/dora/issues/1194).
- **Orientations Emplois :** Ajout d'un endpoint de synchronisation des statuts des orientations Les Emplois [#1169](https://github.com/gip-inclusion/dora/issues/1169) et envoi de mails pour les orientations créées depuis les emplois [#1125](https://github.com/gip-inclusion/dora/issues/1125).
- **Structures :** Possibilité de réactiver une structure obsolète [#1145](https://github.com/gip-inclusion/dora/issues/1145).
- **Informations de contact :** Publication de l'information de contact des services à data⋅inclusion [#1127](https://github.com/gip-inclusion/dora/issues/1127).
- **CGU et Accessibilité :** Mise à jour des Conditions Générales d'Utilisation [#1182](https://github.com/gip-inclusion/dora/issues/1182) et de la déclaration d’accessibilité [#1202](https://github.com/gip-inclusion/dora/issues/1202).
- **Notifications :** Suppression des notifications de relance au prescripteur [#1136](https://github.com/gip-inclusion/dora/issues/1136).

### Évolutions techniques
- **Refactoring :** Retrait de la recherche DORA de la recherche de services [#1201](https://github.com/gip-inclusion/dora/issues/1201) et de la méthode `_map_dora_kinds_to_di` [#1199](https://github.com/gip-inclusion/dora/issues/1199). Simplification du code lié aux services et à la distance dans les résultats unifiés [#1140](https://github.com/gip-inclusion/dora/issues/1140), [#1132](https://github.com/gip-inclusion/dora/issues/1132).
- **Statistiques :** Passage des vues admin en lecture seule [#1179](https://github.com/gip-inclusion/dora/issues/1179).
- **Dépendances :** Mise à jour de plusieurs dépendances (actions/setup-python, @sveltejs/kit, boto3, pygraphviz, etc.).
- **Configuration :** Nouvelle adresse API BAN définie comme constante [#1167](https://github.com/gip-inclusion/dora/issues/1167) et version de NPM fixée à 24 LTS [#1166](https://github.com/gip-inclusion/dora/issues/1166).
- **Build :** Remplacement de p7zip par 7zip pour compatibilité scalingo [#1150](https://github.com/gip-inclusion/dora/issues/1150).

### Autres changements
- **Documentation :** Amélioration du FakeDataInclusionClient [#1198](https://github.com/gip-inclusion/dora/issues/1198).
- **Corrections :** Correction de typos [#1181](https://github.com/gip-inclusion/dora/issues/1181) et suppression d'un message de non-cumulabilité des services DI [#1144](https://github.com/gip-inclusion/dora/issues/1144).
- **Sentry :** Correction de fausses erreurs 500 remontées à Sentry dans Safari [#1164](https://github.com/gip-inclusion/dora/issues/1164) et [#1160](https://github.com/gip-inclusion/dora/issues/1160).
- **Code :** Amélioration du tri des imports [#1200](https://github.com/gip-inclusion/dora/issues/1200) et nettoyage post recherche unifiée [#1095](https://github.com/gip-inclusion/dora/issues/1095).
- **Analytics :** Synchronisation de la table `orientations_emploisorientationdata` [#1190](https://github.com/gip-inclusion/dora/issues/1190) et correction de l'export pilotage sans renommage du schéma public [#1170](https://github.com/gip-inclusion/dora/issues/1170).
- **UI :** Amélioration du bouton de suppression d’option sélectionnée dans le dropdown [#1156](https://github.com/gip-inclusion/dora/issues/1156).
- **Contact :** Suppression de l'espace entre le nom du contact et les autres infos de contact [#1148](https://github.com/gip-inclusion/dora/issues/1148).
