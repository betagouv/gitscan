## Changelog : monitorfish (30 derniers jours, au 09 juin 2026)

### Résumé
Ce mois-ci, monitorfish a bénéficié d'améliorations significatives en termes de fonctionnalités et de stabilité. Les principales évolutions concernent l'ajout de nouvelles données (NATINF 30013, 4789), l'amélioration de l'interface utilisateur (dialogs, filtres, affichage des navires AIS), et des corrections de bugs pour une meilleure expérience utilisateur. Des mises à jour techniques importantes ont également été réalisées, notamment la mise à jour des dépendances backend et l'amélioration de l'infrastructure Kafka.

### Évolutions fonctionnelles
- Ajout de la prise en charge du NATINF 30013. [#5167](https://github.com/MTES-MCT/monitorfish/issues/5167)
- Ajout du NATINF 4789. [#5149](https://github.com/MTES-MCT/monitorfish/issues/5149)
- Amélioration de l'UI des nouvelles modals. [#5169](https://github.com/MTES-MCT/monitorfish/issues/5169)
- Amélioration des filtres dans la liste des signalements INN, permettant une recherche plus facile par type et base. [#5151](https://github.com/MTES-MCT/monitorfish/issues/5151)
- Possibilité de mettre à jour les signalements INN directement depuis Navpro. [#5113](https://github.com/MTES-MCT/monitorfish/issues/5113)
- Ajout du type de moyen des unités de contrôles. [#5145](https://github.com/MTES-MCT/monitorfish/issues/5145)
- Ajout de la mention "Préavis zéro" dans l'objet des emails de préavis. [#5104](https://github.com/MTES-MCT/monitorfish/issues/5104)
- Ré-ajout des champs liés aux espèces dans le formulaire manuel de préavis en cas de non-débarquement. [#5088](https://github.com/MTES-MCT/monitorfish/issues/5088)
- Affichage de la raison pour laquelle un préavis est "à vérifier" (note, signalement, port état tiers). [#5108](https://github.com/MTES-MCT/monitorfish/issues/5108)
- Ajout de la possibilité de rechercher les unités par "type" et "base". [#5110](https://github.com/MTES-MCT/monitorfish/issues/5110)
- Affichage d'une bannière d'erreur en cas d'échec de l'upload de documents. [#5091](https://github.com/MTES-MCT/monitorfish/issues/5091)
- Ajout de l'affichage des navires sous AIS sur la carte. [#5090](https://github.com/MTES-MCT/monitorfish/issues/5090)

### Évolutions techniques
- Mise à jour de monitor-ui pour corriger un problème d'accessibilité.
- Mise à jour des dépendances backend : Spring Boot 4, Security 7, Flyway 12, Ktor 3.5. [#5146](https://github.com/MTES-MCT/monitorfish/issues/5146)
- Harmonisation du composant Dialog et nettoyage du code associé. [#5144](https://github.com/MTES-MCT/monitorfish/issues/5144)
- Montée de version de TimescaleDB et PostGIS. [#5096](https://github.com/MTES-MCT/monitorfish/issues/5096)
- Amélioration de la gestion des erreurs lors du chargement des source maps Sentry.
- Correction d'un test flaky sur la pipeline. [#5148](https://github.com/MTES-MCT/monitorfish/issues/5148)
- Ajout de variables d'environnement pour Kafka. [#5115](https://github.com/MTES-MCT/monitorfish/issues/5115)
- Amélioration de la lecture des coordonnées WKT pour l'affichage AIS.
- Correction de problèmes liés à l'importation de modules.

### Autres changements
- Ajout d'un README pour la génération du fichier .p12. [#5123](https://github.com/MTES-MCT/monitorfish/issues/5123)
- Ajout d'une bannière d'environnement d'intégration. [#5024](https://github.com/MTES-MCT/monitorfish/issues/5024)
- Correction de labels et de wording dans l'interface utilisateur.
- Diverses corrections de tests (Cypress, E2E).
- Mise à jour des données de test.
- Ajout du champ `is_under_jdp` à la table `analytics_missions`. [#5162](https://github.com/MTES-MCT/monitorfish/issues/5162)
- Mise à jour de la table `last_positions` avec la position AIS la plus récente.
- Ajout d'un agrégat continu des positions AIS horaires.
- Correction de la migration des données.
- Suppression de fichiers Uncefact inutilisés.
- Ajout de fonctions d'aide pour le parsing des notes de vente.
- Correction de bugs et améliorations diverses de l'interface utilisateur.
