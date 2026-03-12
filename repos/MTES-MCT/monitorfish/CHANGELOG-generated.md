## Changelog : monitorfish (30 derniers jours)

### Résumé
Les dernières mises à jour de monitorfish se concentrent sur l'amélioration de la gestion des signalements (INN), l'enrichissement des données affichées (dernière opération de pêche, éléments de risque), et la correction de bugs liés à l'affichage et au fonctionnement de certaines fonctionnalités. Des améliorations techniques ont également été apportées, notamment au niveau de la gestion des couches cartographiques et de l'infrastructure.

### Évolutions fonctionnelles
- Ajout d'un bouton radio "Contrôle INN" dans le formulaire de contrôle pour faciliter la saisie des informations. ([#4897](https://github.com/MTES-MCT/monitorfish/issues/4897))
- Affichage des signalements INN directement sur la carte pour une meilleure visualisation. ([#4893](https://github.com/MTES-MCT/monitorfish/issues/4893) et [#4877](https://github.com/MTES-MCT/monitorfish/issues/4877))
- Ajout d'une indication visuelle (pastille) sur l'onglet de la fiche navire pour signaler la présence de signalements.
- Amélioration de l'Act-Rep MED avec l'ajout de codes ISR et de leur référentiel. ([#4816](https://github.com/MTES-MCT/monitorfish/issues/4816))
- Implémentation du calcul des éléments de risque pour une meilleure évaluation des navires. ([#4887](https://github.com/MTES-MCT/monitorfish/issues/4887))
- Correction de la détection de liens morts dans l'email de vérification de la réglementation. ([#4840](https://github.com/MTES-MCT/monitorfish/issues/4840))
- Ajout d'événements Matomo pour le suivi des alertes et des signalements, permettant une meilleure analyse de l'utilisation de l'application. ([#4852](https://github.com/MTES-MCT/monitorfish/issues/4852) et [#4844](https://github.com/MTES-MCT/monitorfish/issues/4844))
- Les alertes paramétrables ne s'exécutent plus si aucun paramètre n'est défini. ([#4838](https://github.com/MTES-MCT/monitorfish/issues/4838))

### Évolutions techniques
- Refactorisation de la gestion des propriétés des couches cartographiques pour une meilleure maintenabilité. ([#4879](https://github.com/MTES-MCT/monitorfish/issues/4879))
- Mise à jour de la documentation du serveur du CROSS. ([#4889](https://github.com/MTES-MCT/monitorfish/issues/4889))
- Rétablissement des connexions aux bases Oracle (balises, navires). ([#4865](https://github.com/MTES-MCT/monitorfish/issues/4865))
- Rétablissement des requêtes aux bases Oracle. ([#4868](https://github.com/MTES-MCT/monitorfish/issues/4868))
- Mise à jour de plusieurs dépendances frontend et backend (webpack, jest, virtualenv).
- Amélioration de la gestion des types avec Zod.
- Correction de bugs divers et optimisations mineures.

### Autres changements
- Mise à jour des URLs du registre Docker.
- Ajustement de la version de monitorenv pour les tests Puppeteer.
- Ajout de données de test pour le pipeline.
- Correction de tests Cypress.
- Mise à jour des données de test.
