## Changelog : monitorfish (30 derniers jours, au 19 juin 2026)

### Résumé
Ce mois-ci, les évolutions de monitorfish se concentrent sur l'amélioration de l'expérience utilisateur pour les contrôles en mer et à la débarque, notamment avec l'intégration de nouvelles fonctionnalités liées à e-ISR et la gestion des signalements INN. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. Enfin, l'intégration des données AIS a été améliorée et des corrections ont été apportées à la gestion des cartes et des données cartographiques.

### Évolutions fonctionnelles
- **Contrôles en mer et débarque (e-ISR):** Modifications des APIs publiques et des contrôles pour supporter la version 1.2 d'e-ISR [#5170](https://github.com/MTES-MCT/monitorfish/issues/5170), [#5175](https://github.com/MTES-MCT/monitorfish/issues/5175), [#5161](https://github.com/MTES-MCT/monitorfish/issues/5161).
- **Signalements INN:** Amélioration des filtres dans la liste des signalements INN et possibilité pour le pôle INN de mettre à jour les signalements liés à Navpro [#5113](https://github.com/MTES-MCT/monitorfish/issues/5113).
- **AIS:** Affichage des navires sous AIS v1.2 [#5177](https://github.com/MTES-MCT/monitorfish/issues/5177).
- **Missions:** Ajout du type de moyen des unités de contrôles [#5145](https://github.com/MTES-MCT/monitorfish/issues/5145).
- **Vaisseaux auxiliaires:** Ajout d'un engin pour les navires auxiliaires à la campagne BFT [#5202](https://github.com/MTES-MCT/monitorfish/issues/5202).
- **Notifications:** Ajout d'une mention correctif dans les notifications de préavis [#4982](https://github.com/MTES-MCT/monitorfish/issues/4982).
- **Gestion des espèces:** Amélioration de l'interface pour la gestion des espèces, notamment lors de la saisie des contrôles en mer et à la débarque. Ajout d'une option pour indiquer si une espèce n'est pas débarquée.

### Évolutions techniques
- **Mise à jour des dépendances:** Mises à jour de plusieurs dépendances backend (Spring Boot, Security, Flyway, Ktor) et frontend (uuid, TS-ESLint, ol, fuse.js, styled-components, monitor-ui) pour bénéficier des dernières corrections et améliorations de sécurité.
- **Refactoring:** Refactoring du code frontend pour migrer vers les dernières versions des librairies et améliorer la cohérence du code.
- **CI/CD:** Amélioration du workflow CI/CD pour la gestion des certificats Sentry et la publication des source maps.
- **Base de données:** Ajout d'index pour optimiser les performances des requêtes sur la table des notes de vente.
- **AIS:** Correction de la lecture des coordonnées WKT et amélioration de la gestion des données AIS.
- **Backend:** Correction de la sérialisation PATCH et amélioration de la gestion des schémas Zod.
- **Tests:** Correction de tests Cypress et Jest pour améliorer la couverture et la fiabilité des tests.

### Autres changements
- Ajout d'un README pour la génération du fichier .p12 utilisé pour la signature des certificats.
- Amélioration de l'UI des modals et harmonisation des composants Dialog.
- Correction de problèmes d'accessibilité.
- Correction de divers bugs et améliorations mineures de l'interface utilisateur.
- Ajout de variables d'environnement pour la configuration de Kafka.
- Correction de la gestion des fuseaux horaires dans les tests.
- Ajout du natinf 30013 et 4789.
- Correction du parser des notes de vente FLUX.
- Correction de la gestion des devises dans les notes de vente.
