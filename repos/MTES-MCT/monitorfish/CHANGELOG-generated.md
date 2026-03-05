## Changelog : monitorfish (30 derniers jours)

### Résumé
Les dernières mises à jour de monitorfish se concentrent sur l'amélioration de l'interface utilisateur, l'ajout de nouvelles fonctionnalités pour le contrôle des navires de pêche (notamment pour les infractions et les signalements), et la correction de bugs. Des améliorations techniques ont également été apportées, notamment des mises à jour de dépendances et la restauration de la connexion aux bases de données Oracle.

### Évolutions fonctionnelles
- Ajout d'informations concernant le dernier chalutage dans le contrôle des navires [#4850](https://github.com/MTES-MCT/monitorfish/issues/4850).
- Affichage des signalements INN sur la carte [#4877](https://github.com/MTES-MCT/monitorfish/issues/4877).
- Ajout d'un filtre pour identifier les navires IUU (pêche illégale).
- Ajout d'un bouton radio "Contrôle INN" dans le formulaire de contrôle [#4858](https://github.com/MTES-MCT/monitorfish/issues/4858).
- Amélioration de l'affichage des catégories d'infractions [#4834](https://github.com/MTES-MCT/monitorfish/issues/4834).
- Correction de l'affichage de la note de probabilité [#4817](https://github.com/MTES-MCT/monitorfish/issues/4817).
- Mise à jour de l'Act-Rep MED [#4816](https://github.com/MTES-MCT/monitorfish/issues/4816).
- Ajout d'un suivi Matomo des signalements [#4844](https://github.com/MTES-MCT/monitorfish/issues/4844).
- Ajout d'événements Matomo sur les alertes [#4852](https://github.com/MTES-MCT/monitorfish/issues/4852).
- Suppression des infractions "en attente" dans les préavis diffusés [#4826](https://github.com/MTES-MCT/monitorfish/issues/4826).
- Fermeture des menus cartos lors de l'ouverture d'une fiche navire [#4828](https://github.com/MTES-MCT/monitorfish/issues/4828).
- Correction de l'affichage des alertes paramétrables lorsque les critères sont vides [#4838](https://github.com/MTES-MCT/monitorfish/issues/4838).

### Évolutions techniques
- Restauration des requêtes aux bases Oracle [#4868](https://github.com/MTES-MCT/monitorfish/issues/4868).
- Activation du mode "thick" pour la connexion à Oracle.
- Restauration des connexions aux bases Oracle (balises, navires) [#4865](https://github.com/MTES-MCT/monitorfish/issues/4865).
- Ajout de l'Oracle Instant Client.
- Mise à jour des dépendances backend et frontend (plusieurs commits).
- Mise à jour de Webpack dans le frontend [#4851](https://github.com/MTES-MCT/monitorfish/issues/4851).
- Mise à jour de @jest/globals dans le frontend [#4806](https://github.com/MTES-MCT/monitorfish/issues/4806).
- Mise à jour de pyarrow dans le pipeline [#4765](https://github.com/MTES-MCT/monitorfish/issues/4765).
- Mise à jour de virtualenv dans le pipeline [#4827](https://github.com/MTES-MCT/monitorfish/issues/4827).
- Refactorisation de la logique NO_FACADE.
- Migration des types vers Zod.
- Suppression de la dépendance Kepler.gl.
- Changement de cx_oracle vers oracledb.

### Autres changements
- Améliorations et corrections de tests Cypress.
- Corrections de tests unitaires.
- Mise à jour de la documentation.
- Corrections de typographie et de code.
- Mise à jour de la version de monitorenv pour les tests Puppeteer.
- Mise à jour des URLs de registre Docker.
- Application du linter.
