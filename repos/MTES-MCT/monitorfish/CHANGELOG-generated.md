## Changelog : monitorfish (30 derniers jours, au 07 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la gestion des signalements et des préavis, avec des corrections de bugs et des ajouts de fonctionnalités pour faciliter le travail des agents. Des optimisations techniques ont également été apportées, notamment des mises à jour de dépendances et des améliorations de l'interface utilisateur.

### Évolutions fonctionnelles
- **Signalements INN :**
    - Possibilité d'ajouter plusieurs NATINF à un signalement [#5048](https://github.com/MTES-MCT/monitorfish/issues/5048).
    - Diverses améliorations de l'interface et du fonctionnement [#4994](https://github.com/MTES-MCT/monitorfish/issues/4994).
    - Possibilité de faire des signalements "en lots" [#5053](https://github.com/MTES-MCT/monitorfish/issues/5053).
- **Préavis :**
    - Rendre obligatoire la date de fin et proposer des options de fin [#5079](https://github.com/MTES-MCT/monitorfish/issues/5079).
    - Invalidation des préavis "zéro" créés il y a plus de 24 heures [#5069](https://github.com/MTES-MCT/monitorfish/issues/5069).
    - Ajout de la mention "zéro" dans les mails, PDF et SMS si le PNO est à zéro [#4981](https://github.com/MTES-MCT/monitorfish/issues/4981).
    - Retrait des champs bloquants pour les préavis de non-débarquement et ajout de la raison du préavis [#4948](https://github.com/MTES-MCT/monitorfish/issues/4948).
    - Affichage de la raison pour laquelle un préavis est "à vérifier" [#5033](https://github.com/MTES-MCT/monitorfish/issues/5033).
    - Filtrage par "préavis 0" dans les types de préavis [#5050](https://github.com/MTES-MCT/monitorfish/issues/5050).
- **Alertes :**
    - Possibilité de suppression automatique des alertes paramétrables [#5027](https://github.com/MTES-MCT/monitorfish/issues/5027).
    - Correction d'un bug où plusieurs alertes étaient affichées en double [#5028](https://github.com/MTES-MCT/monitorfish/issues/5028).
- **Fiche navire :**
    - Ajustements de l'interface utilisateur pour les modalités de contact [#5051](https://github.com/MTES-MCT/monitorfish/issues/5051).
- **Cartographie :**
    - Ajout de l'Océan Pacifique aux façades [#5061](https://github.com/MTES-MCT/monitorfish/issues/5061).
- **Observations :**
    - MAJ de la liste des observations courantes [#5037](https://github.com/MTES-MCT/monitorfish/issues/5037).
- **Autres :**
    - Affichage des coordonnées lors de la modification d'un signalement.
    - Correction d'un bug où de nombreux signalements apparaissaient en dehors de la façade [#5044](https://github.com/MTES-MCT/monitorfish/issues/5044).

### Évolutions techniques
- **OpenLayers :** Mise à jour de la librairie OpenLayers [#5021](https://github.com/MTES-MCT/monitorfish/issues/5021).
- **Refactoring :** Refactoring du composant carte avec des hooks [#5030](https://github.com/MTES-MCT/monitorfish/issues/5030).
- **Dépendances :**
    - Mise à jour de `ora` en version 9.3.0.
    - Mise à jour de `basic-ftp` en version 5.2.2.
- **Tests :**
    - Amélioration des tests Cypress.
    - Correction d'une race condition dans la fixture de DB des tests de pipeline.
    - Ajout de timeout pour les tests E2E (30 minutes).
- **Backend :** Mise à jour des dépendances non-majeures [#5064](https://github.com/MTES-MCT/monitorfish/issues/5064).

### Autres changements
- Correction de typos et amélioration de la lisibilité du code.
- Suppression de code mort.
- Amélioration de la gestion des erreurs et des assertions dans les tests.
- Exlusion de Prefect des montées de version dependabot.
- Ajout d'une dépendance manquante (greenlet) sur macOS.
- Correction de problèmes de rendu de la carte.
- Archivage automatique des signalements IUU après 24 heures.
