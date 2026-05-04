## Changelog : monitorfish (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions de monitorfish se concentrent sur l'amélioration des signalements d'infractions, la gestion des préavis, et l'expérience utilisateur globale. Des corrections et des améliorations ont été apportées à la fiche navire, aux alertes, et à la cartographie, avec un focus sur la gestion des navires inconnus et des observations courantes. Des optimisations techniques et des mises à jour de dépendances ont également été réalisées.

### Évolutions fonctionnelles
- **Signalements INN :**
    - Possibilité de signaler plusieurs infractions en une seule fois ([#5048](https://github.com/MTES-MCT/monitorfish/issues/5048)).
    - Améliorations diverses de l'interface et du fonctionnement des signalements ([#4994](https://github.com/MTES-MCT/monitorfish/issues/4994)).
    - Possibilité d'ajouter plusieurs NATINF à un signalement ([#5048](https://github.com/MTES-MCT/monitorfish/issues/5048)).
- **Préavis :**
    - Ajout de la raison pour laquelle un préavis est "à vérifier" ([#5033](https://github.com/MTES-MCT/monitorfish/issues/5033)).
    - Filtrage des préavis par type "préavis 0" ([#5050](https://github.com/MTES-MCT/monitorfish/issues/5050)).
    - Suppression des champs bloquants pour les préavis de non-débarquement et ajout de la raison du préavis ([#4948](https://github.com/MTES-MCT/monitorfish/issues/4948)).
- **Fiche navire :**
    - Amélioration de l'interface des modalités de contact ([#5051](https://github.com/MTES-MCT/monitorfish/issues/5051)).
    - Ajout d'un menu déroulant pour la nationalité en cas de navire inconnu ([#4993](https://github.com/MTES-MCT/monitorfish/issues/4993)).
- **Alertes :**
    - Possibilité de suppression automatique des alertes paramétrables ([#5027](https://github.com/MTES-MCT/monitorfish/issues/5027)).
    - Correction d'un bug où deux alertes étaient affichées au lieu d'une seule ([#5028](https://github.com/MTES-MCT/monitorfish/issues/5028)).
- **Observations :**
    - Possibilité de sélectionner les observations les plus courantes dans une liste ([#4989](https://github.com/MTES-MCT/monitorfish/issues/4989)).
- **Cartographie :**
    - Affichage de l'état du pavillon lorsque plusieurs navires sont signalés ([#5056](https://github.com/MTES-MCT/monitorfish/issues/5056)).
    - Correction de l'affichage des coordonnées lors de la modification d'un signalement.
- **Autres :**
    - Ajout de la catégorie d'infraction NATINF 22204 (RUN FLOW) ([#5056](https://github.com/MTES-MCT/monitorfish/issues/5056)).
    - Correction d'un bug d'affichage de la toolbox d'infraction ([#5052](https://github.com/MTES-MCT/monitorfish/issues/5052)).

### Évolutions techniques
- **Refactoring de la carte :** Refactoring du composant carte avec des hooks pour une meilleure maintenabilité et performance ([#5030](https://github.com/MTES-MCT/monitorfish/issues/5030)).
- **Mise à jour d'OpenLayers :** Mise à jour de la librairie OpenLayers ([#5021](https://github.com/MTES-MCT/monitorfish/issues/5021)).
- **Optimisation de la cartographie :** Améliorations de la gestion de la projection et des couches cartographiques pour éviter des problèmes d'affichage.
- **Correction de race condition :** Correction d'une race condition dans la fixture de la base de données des tests de pipeline ([#5023](https://github.com/MTES-MCT/monitorfish/issues/5023)).
- **Archivage des signalements IUU :** Archivage automatique des signalements IUU après 24 heures.

### Autres changements
- Mise à jour de dépendances frontend (ora, basic-ftp, vite).
- Suppression de dépendances inutiles.
- Amélioration de la documentation et des tests unitaires.
- Corrections de linter.
- Suppression de code mort.
- Amélioration de la gestion des tests Cypress.
