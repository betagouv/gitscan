## Changelog : bhasile (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions de bhasile se concentrent sur l'amélioration de l'interface utilisateur, notamment pour la gestion des structures et des actes administratifs, ainsi que sur des corrections de bugs et des optimisations techniques. L'ajout de statistiques et d'indicateurs de qualité vise à faciliter le suivi et l'évaluation des données.

### Évolutions fonctionnelles
- Ajout de documents pour les opérateurs. [#1275](https://github.com/betagouv/bhasile/issues/1275)
- Ajout d'un CTA (Call To Action) pour les statistiques. [#1273](https://github.com/betagouv/bhasile/issues/1273)
- Amélioration de l'affichage des dates inférées à partir des actes administratifs. [#1260](https://github.com/betagouv/bhasile/issues/1260)
- Ajout de commentaires pour les documents financiers. [#1261](https://github.com/betagouv/bhasile/issues/1261)
- Ajout d'autres actes administratifs au CPOM (Contrat de Préstation d'Hébergement et d'Accompagnement). [#1266](https://github.com/betagouv/bhasile/issues/1266)
- Nouvelle structure d'en-tête pour les structures. [#1264](https://github.com/betagouv/bhasile/issues/1264)
- Possibilité de sélectionner plusieurs structures. [#1230](https://github.com/betagouv/bhasile/issues/1230)
- Nouvelle interface utilisateur pour l'importation d'adresses. [#1206](https://github.com/betagouv/bhasile/issues/1206)
- Possibilité d'étendre la date de fin avec des avenants. [#1211](https://github.com/betagouv/bhasile/issues/1211)
- Ajout de deux indicateurs de qualité pour les actes administratifs. [#1218](https://github.com/betagouv/bhasile/issues/1218)
- Nouvelle carte. [#1192](https://github.com/betagouv/bhasile/issues/1192)

### Évolutions techniques
- Déplacement de la logique par défaut de la structure côté serveur pour optimiser les performances. [#1272](https://github.com/betagouv/bhasile/issues/1272)
- Refactorisation des gestionnaires PUT pour respecter les conventions REST. [#1270](https://github.com/betagouv/bhasile/issues/1270)
- Extraction de l'état d'interaction de l'adresse dans un hook personnalisé `useAddressInteraction`. [#1271](https://github.com/betagouv/bhasile/issues/1271)
- Migration vers `StructureVersion`. [#1258](https://github.com/betagouv/bhasile/issues/1258)
- Limitation des logs d'activité utilisateur. [#1263](https://github.com/betagouv/bhasile/issues/1263)
- Passage à une architecture à 3 niveaux. [#1219](https://github.com/betagouv/bhasile/issues/1219)
- Ajout de routes client pour la transformation. [#1216](https://github.com/betagouv/bhasile/issues/1216)
- Mise à jour de TypeScript vers la version 6.0.3. [#1222](https://github.com/betagouv/bhasile/issues/1222)
- Suppression d'une option TypeScript obsolète. [#1235](https://github.com/betagouv/bhasile/issues/1235)
- Ajout de tests pour les routes et la page des formulaires. [#1210](https://github.com/betagouv/bhasile/issues/1210) et [#1203](https://github.com/betagouv/bhasile/issues/1203)

### Autres changements
- Correction de bugs liés à la redirection des opérateurs. [#1252](https://github.com/betagouv/bhasile/issues/1252), [#1251](https://github.com/betagouv/bhasile/issues/1251) et [#1241](https://github.com/betagouv/bhasile/issues/1241)
- Correction du problème d'affichage de la favicon "new". [#1248](https://github.com/betagouv/bhasile/issues/1248)
- Correction de bugs CSS sur la page d'utilisation et les statistiques des opérateurs. [#1233](https://github.com/betagouv/bhasile/issues/1233) et [#1213](https://github.com/betagouv/bhasile/issues/1213)
- Correction d'un bug de build pour la carte. [#1212](https://github.com/betagouv/bhasile/issues/1212)
- Suppression de l'avertissement multi-DNA lors de l'ajout. [#1228](https://github.com/betagouv/bhasile/issues/1228)
- Mise à jour de l'image de la base de données. [#1253](https://github.com/betagouv/bhasile/issues/1253)
- Déplacement des contacts vers les variables d'environnement. [#1208](https://github.com/betagouv/bhasile/issues/1208)
- Ajout d'un flag `isMissing` pour l'historique. [#1278](https://github.com/betagouv/bhasile/issues/1278)
- Correction de l'affichage du header sticky. [#1265](https://github.com/betagouv/bhasile/issues/1265)
