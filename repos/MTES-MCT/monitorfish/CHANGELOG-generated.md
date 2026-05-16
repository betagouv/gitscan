## Changelog : monitorfish (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions de monitorfish se concentrent sur l'amélioration de la gestion des préavis, des signalements et des alertes, ainsi que sur des optimisations techniques de l'infrastructure et de l'interface utilisateur. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment au niveau de l'affichage des données et de la gestion des formulaires.

### Évolutions fonctionnelles
- **Préavis :**
    - Ajout de la mention "zéro" dans les emails, PDF et SMS pour les préavis PNO à zéro. [#4981](https://github.com/MTES-MCT/monitorfish/issues/4981)
    - Possibilité de filtrer les préavis par type "préavis 0". [#5050](https://github.com/MTES-MCT/monitorfish/issues/5050)
    - Affichage de la raison pour laquelle un préavis est "à vérifier". [#5033](https://github.com/MTES-MCT/monitorfish/issues/5033)
    - Retrait des champs bloquants pour les préavis de non-débarquement et ajout de la raison du préavis. [#4948](https://github.com/MTES-MCT/monitorfish/issues/4948)
- **Signalements :**
    - Possibilité de faire des signalements "en lots". [#5053](https://github.com/MTES-MCT/monitorfish/issues/5053)
    - Correction d'un problème où de nombreux signalements apparaissaient en dehors de la façade. [#5044](https://github.com/MTES-MCT/monitorfish/issues/5044)
- **Alertes :**
    - Possibilité de suppression automatique des alertes paramétrables. [#5027](https://github.com/MTES-MCT/monitorfish/issues/5027)
- **Fiche navire :** Amélioration de l'interface utilisateur pour les modalités de contact. [#5051](https://github.com/MTES-MCT/monitorfish/issues/5051)
- **Cartographie :**
    - Ajout de l'Océan Pacifique aux façades. [#5061](https://github.com/MTES-MCT/monitorfish/issues/5061)
    - Amélioration de l'affichage des données sur la carte.
- **Gestion des infractions :**
    - Correction d'un bug dans le flow des catégories d'infractions. [#5082](https://github.com/MTES-MCT/monitorfish/issues/5082)
    - Correction d'un problème d'overflow masquant la toolbox d'infraction. [#5052](https://github.com/MTES-MCT/monitorfish/issues/5052)
- **Environnement d'intégration :** Mise en avant de l'environnement d'intégration dans l'interface utilisateur. [#5024](https://github.com/MTES-MCT/monitorfish/issues/5024)

### Évolutions techniques
- **Base de données :** Montée de version de TimescaleDB et PostGIS. [#5096](https://github.com/MTES-MCT/monitorfish/issues/5096)
- **CI/CD :** Mise à jour du workflow de la base de données.
- **Tests :**
    - Augmentation du timeout pour les tests E2E à 30 minutes.
    - Corrections et améliorations des tests Cypress.
- **Refactoring :** Refactoring du composant carte avec des hooks. [#5030](https://github.com/MTES-MCT/monitorfish/issues/5030)
- **OpenLayers :** Mise à jour de la librairie OpenLayers. [#5021](https://github.com/MTES-MCT/monitorfish/issues/5021)
- **Dépendances :** Mise à jour des dépendances backend non-majeures. [#5064](https://github.com/MTES-MCT/monitorfish/issues/5064)

### Autres changements
- Correction de typos et amélioration de la lisibilité du code.
- Ajout d'une bannière d'erreur en cas d'échec de l'upload. [#5091](https://github.com/MTES-MCT/monitorfish/issues/5091)
- Suppression de code mort et nettoyage général du code.
- Amélioration de la gestion des erreurs et des validations.
- Mise à jour de la documentation.
