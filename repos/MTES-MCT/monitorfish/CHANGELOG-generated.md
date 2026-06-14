## Changelog : monitorfish (30 derniers jours, au 11 juin 2026)

### Résumé
Ce mois-ci, les évolutions de monitorfish se concentrent sur l'amélioration de la gestion des contrôles, notamment en mer et à terre, avec l'ajout de nouveaux champs et la correction de plusieurs bugs. Des améliorations significatives ont également été apportées à l'intégration des données AIS, permettant désormais l'affichage des navires et de leurs positions sur la carte. Enfin, des corrections et des améliorations ont été apportées à l'interface utilisateur et à la gestion des signalements INN.

### Évolutions fonctionnelles
- Ajout de champs pour les contrôles en mer et à terre liés à l'e-ISR, incluant la possibilité de spécifier si le navire a débarqué ou non. [#5161](https://github.com/MTES-MCT/monitorfish/issues/5161)
- Amélioration de l'affichage des raisons de vérification des préavis. [#5108](https://github.com/MTES-MCT/monitorfish/issues/5108)
- Ajout de la mention "Préavis zéro" dans l'objet des emails de notification. [#5104](https://github.com/MTES-MCT/monitorfish/issues/5104)
- Ajout de la possibilité de rechercher par type et base lors de la création d'un nouveau moyen pour les unités. [#5110](https://github.com/MTES-MCT/monitorfish/issues/5110)
- Amélioration des filtres dans la liste des signalements INN, avec la possibilité de filtrer par type de signalement et d'exiger l'ID du navire dans le formulaire. [#5113](https://github.com/MTES-MCT/monitorfish/issues/5113)
- Intégration de l'affichage des navires sous AIS sur la carte, avec la possibilité de visualiser leurs dernières positions. [#5090](https://github.com/MTES-MCT/monitorfish/issues/5090)
- Ajout de la gestion des notes de vente FLUX et correction du parser. [#5173](https://github.com/MTES-MCT/monitorfish/issues/5173)
- Ajout du champ `is_under_jdp` à la table `analytics_missions`. [#5162](https://github.com/MTES-MCT/monitorfish/issues/5162)

### Évolutions techniques
- Mise à jour des dépendances frontend : uuid 14, TS-ESLint 7, ol 10.9, fuse.js 7.3, styled-components 6.4 et monitor-ui 24.50. [#5147](https://github.com/MTES-MCT/monitorfish/issues/5147)
- Mise à jour des dépendances backend : Spring Boot 4, Security 7, Flyway 12, Ktor 3.5. [#5146](https://github.com/MTES-MCT/monitorfish/issues/5146)
- Correction de la sérialisation PATCH. [#5174](https://github.com/MTES-MCT/monitorfish/issues/5174)
- Correction des schémas Zod. [#5174](https://github.com/MTES-MCT/monitorfish/issues/5174)
- Amélioration de la gestion des erreurs lors du téléchargement des source maps Sentry.
- Correction de plusieurs tests Cypress et Jest.
- Ajout de variables d'environnement pour Kafka et la génération de certificats.
- Refactoring du code pour améliorer la lisibilité et la maintenabilité.

### Autres changements
- Amélioration de l'UI des nouvelles modales. [#5169](https://github.com/MTES-MCT/monitorfish/issues/5169)
- Correction de problèmes d'accessibilité. [#5144](https://github.com/MTES-MCT/monitorfish/issues/5144)
- Ajout d'un README pour la génération du fichier .p12. [#5123](https://github.com/MTES-MCT/monitorfish/issues/5123)
- Correction de la mention "Drone" dans l'interface utilisateur.
- Harmonisation du composant Dialog.
- Correction de plusieurs tests E2E.
- Ajout du NATINF 4789 et mise à jour du NATINF 30013. [#5149](https://github.com/MTES-MCT/monitorfish/issues/5149) et [#5167](https://github.com/MTES-MCT/monitorfish/issues/5167)
