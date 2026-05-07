## Changelog : monitorfish (30 derniers jours, au 06 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'amélioration de la gestion des signalements, des préavis et des observations, ainsi que sur la correction de bugs et l'optimisation de l'interface utilisateur. Des améliorations techniques ont également été apportées, notamment des mises à jour de dépendances et des refactorings pour améliorer la performance et la maintenabilité du code.

### Évolutions fonctionnelles
- **Signalements INN :**
    - Ajout de la possibilité de signaler plusieurs infractions en une seule fois ([#5053](https://github.com/MTES-MCT/monitorfish/issues/5053)).
    - Améliorations diverses de l'interface et du flux de signalement ([#4994](https://github.com/MTES-MCT/monitorfish/issues/4994)).
    - Possibilité d'ajouter le nombre de navires lors d'un signalement.
- **Préavis :**
    - Ajout de la mention "zéro" dans les mails, PDF et SMS si le numéro d'identification du navire (PNO) est zéro ([#4981](https://github.com/MTES-MCT/monitorfish/issues/4981)).
    - Retrait des champs bloquants pour les préavis de non-débarquement et ajout de la raison du préavis ([#4948](https://github.com/MTES-MCT/monitorfish/issues/4948)).
    - Filtrage des préavis par "préavis 0" dans les types de préavis ([#5050](https://github.com/MTES-MCT/monitorfish/issues/5050)).
    - Affichage de la raison pour laquelle un préavis est "à vérifier" ([#5033](https://github.com/MTES-MCT/monitorfish/issues/5033)).
    - Invalidation automatique des préavis "zéro" créés il y a plus de 24 heures ([#5069](https://github.com/MTES-MCT/monitorfish/issues/5069)).
- **Observations :**
    - Possibilité de sélectionner les observations les plus courantes dans une liste ([#4989](https://github.com/MTES-MCT/monitorfish/issues/4989)).
- **Fiche navire :**
    - Améliorations de l'interface utilisateur des modalités de contact ([#5051](https://github.com/MTES-MCT/monitorfish/issues/5051)).
- **Cartographie :**
    - Ajout de l'Océan Pacifique aux façades ([#5061](https://github.com/MTES-MCT/monitorfish/issues/5061)).
- **Alertes :**
    - Possibilité de suppression automatique des alertes paramétrables ([#5027](https://github.com/MTES-MCT/monitorfish/issues/5027)).

### Évolutions techniques
- **OpenLayers :** Mise à jour de la librairie OpenLayers ([#5021](https://github.com/MTES-MCT/monitorfish/issues/5021)).
- **Refactoring :** Refactoring du composant carte avec des hooks ([#5030](https://github.com/MTES-MCT/monitorfish/issues/5030)).
- **Dépendances :** Mises à jour de plusieurs dépendances frontend (ora, basic-ftp, vite) ([#5008](https://github.com/MTES-MCT/monitorfish/issues/5008), [#5019](https://github.com/MTES-MCT/monitorfish/issues/5019), [#4983](https://github.com/MTES-MCT/monitorfish/issues/4983)).
- **Backend :** Mise à jour des dépendances non majeures du backend ([#5064](https://github.com/MTES-MCT/monitorfish/issues/5064)).
- **Tests :** Améliorations et corrections des tests Cypress et unitaires.
- **CI/CD :** Correction d'une race condition dans la fixture de base de données des tests de pipeline.

### Autres changements
- Ajout d'une nouvelle catégorie d'infraction (NATINF 22204 - RUN FLOW) ([#5056](https://github.com/MTES-MCT/monitorfish/issues/5056)).
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Suppression de l'archivage automatique des signalements IUU après 24 heures.
- Diverses corrections et optimisations du code.
