## Changelog : dora (30 derniers jours, au 23 juillet 2026)

### Résumé
Ce mois-ci, les évolutions de Dora se concentrent sur l'amélioration de la recherche de services, la gestion des orientations et des structures, ainsi que des corrections de bugs et des mises à jour de conformité (CGU, accessibilité). Des efforts ont également été faits pour optimiser la performance et la stabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'un endpoint de synchronisation des statuts des orientations Les Emplois [#1169](https://github.com/gip-inclusion/dora/issues/1169).
- Mise à jour de la déclaration d’accessibilité [#1202](https://github.com/gip-inclusion/dora/issues/1202).
- Mise à jour des CGU [#1182](https://github.com/gip-inclusion/dora/issues/1182) et [#1135](https://github.com/gip-inclusion/dora/issues/1135).
- Publication de l'information de contact des services à data⋅inclusion [#1127](https://github.com/gip-inclusion/dora/issues/1127).
- Ajout d'un champ "source" sur la page d'orientation [#1155](https://github.com/gip-inclusion/dora/issues/1155).
- Possibilité de réactiver une structure obsolète [#1145](https://github.com/gip-inclusion/dora/issues/1145).
- Envoi de mails pour les orientations créées depuis les emplois [#1125](https://github.com/gip-inclusion/dora/issues/1125).
- Suppression des notifications de relance au prescripteur [#1136](https://github.com/gip-inclusion/dora/issues/1136).
- Implémentation d'une recherche par texte (en A/B test) [#1194](https://github.com/gip-inclusion/dora/issues/1194).

### Évolutions techniques
- Refactor de la recherche DORA et suppression de la recherche de services [#1201](https://github.com/gip-inclusion/dora/issues/1201).
- Suppression de code lié à la recherche unifiée et nettoyage post-refactor [#1095](https://github.com/gip-inclusion/dora/issues/1095) et [#1140](https://github.com/gip-inclusion/dora/issues/1140).
- Amélioration du `FakeDataInclusionClient` [#1198](https://github.com/gip-inclusion/dora/issues/1198).
- Passage des vues admin en lecture seule [#1179](https://github.com/gip-inclusion/dora/issues/1179).
- Utilisation de l'enum `ModeAccueil` de d·i [#1124](https://github.com/gip-inclusion/dora/issues/1124).
- Remplacement de la bibliothèque de génération de fichier Excel [#1191](https://github.com/gip-inclusion/dora/issues/1191).
- Mise à jour de la politique de confidentialité [#1149](https://github.com/gip-inclusion/dora/issues/1149).
- Correction d'une erreur 500 sur Safari lors du rechargement après déploiement [#1160](https://github.com/gip-inclusion/dora/issues/1160) et [#1164](https://github.com/gip-inclusion/dora/issues/1164).

### Autres changements
- Correction d'une typo [#1181](https://github.com/gip-inclusion/dora/issues/1181).
- Correction du tri des imports dans un fichier Python [#1200](https://github.com/gip-inclusion/dora/issues/1200).
- Suppression de l'app et des données Admin Express [#1154](https://github.com/gip-inclusion/dora/issues/1154).
- Suppression du message de non-cumulabilité des services DI [#1144](https://github.com/gip-inclusion/dora/issues/1144).
- Suppression d'un espace superflu dans l'affichage des informations de contact [#1148](https://github.com/gip-inclusion/dora/issues/1148).
- Correction d'un bug lié aux fausses erreurs Sentry [#1160](https://github.com/gip-inclusion/dora/issues/1160).
- Fix pour l'export pilotage sans renommage du schéma public [#1170](https://github.com/gip-inclusion/dora/issues/1170).
- Amélioration du bouton de suppression d’option sélectionnée dans le dropdown [#1156](https://github.com/gip-inclusion/dora/issues/1156).
- Mise à jour de la version de NPM à la version LTS 24 [#1166](https://github.com/gip-inclusion/dora/issues/1166).
- Définition de la nouvelle adresse API BAN comme constante [#1167](https://github.com/gip-inclusion/dora/issues/1167).
- Modification de la configuration pour permettre le téléchargement direct des dépendances NPM [#1168](https://github.com/gip-inclusion/dora/issues/1168).
- Mise à jour de la dépendance `itoutils` [#1165](https://github.com/gip-inclusion/dora/issues/1165).
- Bump de la dépendance `data-inclusion-schema` à la version 1.0.9 [#1131](https://github.com/gip-inclusion/dora/issues/1131).
