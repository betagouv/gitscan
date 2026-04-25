## Changelog : monitorfish (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur, notamment sur la gestion des signalements et des observations, ainsi que sur la cartographie avec la mise à jour d'OpenLayers et l'ajout de la ZEE SHOM. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Signalements :** Correction de l'affichage des signalements hors façade. [#5044](https://github.com/MTES-MCT/monitorfish/issues/5044)
- **Observations :** Mise à jour de la liste des observations courantes. [#5037](https://github.com/MTES-MCT/monitorfish/issues/5037)
- **Alertes :** Possibilité de suppression automatique des alertes paramétrables. [#5027](https://github.com/MTES-MCT/monitorfish/issues/5027)
- **Coordonnées :** Affichage des coordonnées lors de la modification d'un signalement. [#5029](https://github.com/MTES-MCT/monitorfish/issues/5029)
- **Catégories d'infractions :** Ajout de trois nouvelles catégories d'infractions NATINFs. [#4975](https://github.com/MTES-MCT/monitorfish/issues/4975)
- **Cartographie :** Ajout de la ZEE SHOM et mise à jour de la ZEE monde. [#4922](https://github.com/MTES-MCT/monitorfish/issues/4922)
- **Liste des navires :** Ajout d'un filtre "Equipé VMS" pour la gestion des navires tiers. [#4990](https://github.com/MTES-MCT/monitorfish/issues/4990)
- **Signalements INN :** Diverses améliorations apportées. [#4994](https://github.com/MTES-MCT/monitorfish/issues/4994)
- **Contrôle :** Ajout d'un menu déroulant "nationalité" pour les navires inconnus. [#4993](https://github.com/MTES-MCT/monitorfish/issues/4993)

### Évolutions techniques
- **OpenLayers :** Mise à jour de la librairie OpenLayers. [#5021](https://github.com/MTES-MCT/monitorfish/issues/5021)
- **Refactoring :** Refactoring du composant carte avec des hooks. [#5030](https://github.com/MTES-MCT/monitorfish/issues/5030)
- **Docker :** Mise à jour de l'action Docker pour le build et le push. [#4957](https://github.com/MTES-MCT/monitorfish/issues/4957)
- **Keycloak :** Correction pour éviter que SSL ne soit requis pendant le développement. [#4941](https://github.com/MTES-MCT/monitorfish/issues/4941)
- **Tests :** Correction d'une race condition dans la fixture de base de données des tests de pipeline. [#5023](https://github.com/MTES-MCT/monitorfish/issues/5023)
- **Dépendances :** Mise à jour de plusieurs dépendances frontend (ora, basic-ftp, vite, rollup, lodash, lodash-es, got).
- **Prefect :** Rétrogradation de Prefect en version 3.6.9 pour résoudre des problèmes de compatibilité. [#4938](https://github.com/MTES-MCT/monitorfish/issues/4938) et [#4937](https://github.com/MTES-MCT/monitorfish/issues/4937)

### Autres changements
- Correction de bugs mineurs et améliorations de la performance SQL.
- Suppression de code mort et simplification de certaines parties du code.
- Mise à jour de la documentation.
- Correction de problèmes de marge dans l'interface utilisateur.
- Correction de l'affichage des alertes dans la fiche d'un navire. [#5028](https://github.com/MTES-MCT/monitorfish/issues/5028)
- Correction de l'affichage des champs dans l'overlay de reporting.
- Amélioration de la gestion des timezones dans le parser ERS. [#4946](https://github.com/MTES-MCT/monitorfish/issues/4946)
- Ajout de cooldown sur les mises à jour de dépendances.
