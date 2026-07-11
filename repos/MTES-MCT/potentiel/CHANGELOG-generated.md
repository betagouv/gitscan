## Changelog : potentiel (30 derniers jours, au 10 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment en facilitant l'export de données, la gestion des documents de raccordement et la navigation. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de la plateforme. Des optimisations techniques ont été réalisées pour améliorer la performance et la maintenance du code.

### Évolutions fonctionnelles
- Ajout de la possibilité d'exporter en CSV la liste des candidats non notifiés. [#4406](https://github.com/MTES-MCT/potentiel/issues/4406)
- Ajout de la possibilité d'exporter en PDF la liste des candidats lauréats d'une nouvelle période. [#4409](https://github.com/MTES-MCT/potentiel/issues/4409)
- Amélioration de la gestion des documents de raccordement : transmission, modification et affichage. [#4385](https://github.com/MTES-MCT/potentiel/issues/4385)
- Suppression de la possibilité de supprimer un document de raccordement. [#4413](https://github.com/MTES-MCT/potentiel/issues/4413)
- Amélioration de l'affichage et de la navigation dans les garanties financières. [#4356](https://github.com/MTES-MCT/potentiel/issues/4356)
- Ajout d'un bloc d'information pour les producteurs avant de demander la mainlevée des gfs. [#4410](https://github.com/MTES-MCT/potentiel/issues/4410)
- Amélioration de l'affichage des coordonnées géodésiques. [#4363](https://github.com/MTES-MCT/potentiel/issues/4363)
- Ajout de l'opérateur PG between pour les requêtes. [#4349](https://github.com/MTES-MCT/potentiel/issues/4349)
- Simplification du calcul du volume réservé et de la note du dernier retenu. [#4391](https://github.com/MTES-MCT/potentiel/issues/4391)
- Amélioration de l'accessibilité : labels pour les documents, navigation au clavier du Multiselect, hiérarchie des titres. [#4331](https://github.com/MTES-MCT/potentiel/issues/4331), [#4346](https://github.com/MTES-MCT/potentiel/issues/4346), [#4348](https://github.com/MTES-MCT/potentiel/issues/4348)

### Évolutions techniques
- Intégration des dernières modifications des versions 3.82, 3.83 et 3.84. [#4427](https://github.com/MTES-MCT/potentiel/issues/4427), [#4424](https://github.com/MTES-MCT/potentiel/issues/4424), [#4399](https://github.com/MTES-MCT/potentiel/issues/4399)
- Refactoring du code lié au raccordement (front et back). [#4368](https://github.com/MTES-MCT/potentiel/issues/4368)
- Mise en place du monitoring du CRON datagouv. [#4418](https://github.com/MTES-MCT/potentiel/issues/4418)
- Amélioration de la gestion des backups S3. [#4370](https://github.com/MTES-MCT/potentiel/issues/4370)
- Suppression de code obsolète : adapter getIdentifiantProjetFromLegacyId, page de redirection legacy, script de migration des détails de candidature. [#4338](https://github.com/MTES-MCT/potentiel/issues/4338), [#4337](https://github.com/MTES-MCT/potentiel/issues/4337)
- Rendre le script de restauration de DB accessible aux review apps. [#4405](https://github.com/MTES-MCT/potentiel/issues/4405)

### Autres changements
- Correction de bugs liés aux routes de téléchargement de documents en mainlevée. [#4426](https://github.com/MTES-MCT/potentiel/issues/4426)
- Correction de la puissance appelée P11 éolien et P12 bat. [#4423](https://github.com/MTES-MCT/potentiel/issues/4423)
- Correction de l'affichage des notes des derniers retenus. [#4388](https://github.com/MTES-MCT/potentiel/issues/4388)
- Correction de la redirection après accès à un projet éliminé. [#4357](https://github.com/MTES-MCT/potentiel/issues/4357)
- Correction de la redirection après demande/passage en instruction de mainlevée. [#4412](https://github.com/MTES-MCT/potentiel/issues/4412)
- Correction de l'affichage des lauréats dans la synthèse de période. [#4416](https://github.com/MTES-MCT/potentiel/issues/4416)
- Correction d'un problème de filtre pour contacter les utilisateurs. [#4379](https://github.com/MTES-MCT/potentiel/issues/4379)
- Correction d'un problème de pagination. [#4374](https://github.com/MTES-MCT/potentiel/issues/4374)
- Renommage "démarches simplifiées" en "Démarche Numérique". [#4403](https://github.com/MTES-MCT/potentiel/issues/4403)
- Mise à jour des dépendances npm/yarn. [#4366](https://github.com/MTES-MCT/potentiel/issues/4366), [#4365](https://github.com/MTES-MCT/potentiel/issues/4365)
