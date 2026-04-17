## Changelog : monitorfish (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment dans la gestion des signalements (création, modification, affichage) et la cartographie (affichage des ZEE, correction de coordonnées). Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des mises à jour de dépendances pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- Possibilité de supprimer automatiquement les alertes position après une durée paramétrable [#5027](https://github.com/MTES-MCT/monitorfish/issues/5027).
- Affichage des coordonnées lors de la modification d'un signalement [#5029](https://github.com/MTES-MCT/monitorfish/issues/5029).
- Ajout d'un menu déroulant pour la nationalité des navires inconnus [#4993](https://github.com/MTES-MCT/monitorfish/issues/4993).
- Améliorations diverses de l'interface utilisateur pour les signalements INN [#4994](https://github.com/MTES-MCT/monitorfish/issues/4994).
- Ajout de la possibilité de filtrer la liste des navires par équipement VMS [#4990](https://github.com/MTES-MCT/monitorfish/issues/4990).
- Ajout de catégories d'infractions (NATINFs) [#4975](https://github.com/MTES-MCT/monitorfish/issues/4975).
- Ajout d'une sélection par liste des observations les plus courantes [#4989](https://github.com/MTES-MCT/monitorfish/issues/4989).
- Ajout de la ZEE SHOM et mise à jour de la ZEE monde [#4922](https://github.com/MTES-MCT/monitorfish/issues/4922).
- Affichage des signalements sur la carte uniquement pour les voyages actuels.
- Correction de l'affichage du signalement après sa création [#4919](https://github.com/MTES-MCT/monitorfish/issues/4919).
- Modification d'un signalement directement depuis la fiche navire [#4905](https://github.com/MTES-MCT/monitorfish/issues/4905).
- Extraction des données des espèces à bord des messages COE et COX [#4917](https://github.com/MTES-MCT/monitorfish/issues/4917).

### Évolutions techniques
- Mise à jour de OpenLayers [#5021](https://github.com/MTES-MCT/monitorfish/issues/5021).
- Correction de problèmes liés aux projections OpenLayers et à la simplification des géométries.
- Suppression de code mort et optimisation de la gestion des couches OpenLayers.
- Correction de fuites mémoires dans le frontend [#4883](https://github.com/MTES-MCT/monitorfish/issues/4883).
- Suppression de `useEffect` inutiles dans le frontend [#4912](https://github.com/MTES-MCT/monitorfish/issues/4912).
- Mise à jour de plusieurs dépendances : `vite`, `rollup`, `lodash`, `testcontainers`, `cryptography`, `weasyprint`, `black`, `pyopenssl`.
- Exclusions de Prefect des mises à jour dependabot pour éviter des incompatibilités.
- Ajout de dépendance manquante `greenlet` pour macOS.
- Amélioration des performances des requêtes SQL.
- Mise à jour de la configuration de dependabot.
- Ajout de tests Cypress pour améliorer la couverture et la fiabilité.

### Autres changements
- Correction de bugs mineurs dans l'interface utilisateur et les tests.
- Amélioration de la gestion des erreurs et des messages d'information.
- Mise à jour de la documentation.
- Correction de typos.
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
- Correction d'un bug dans le parser ERS lié aux fuseaux horaires.
- Ajout de vérifications de la validité des données.
- Ajout d'éléments de risque pour la pêche en zones fermées, les défaillances VMS et les PNO.
- Correction d'un bug de lecture de message CPS.
- Ajout de feature flags pour activer/désactiver certaines fonctionnalités.
