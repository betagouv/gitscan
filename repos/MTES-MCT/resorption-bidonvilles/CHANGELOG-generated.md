## Changelog : resorption-bidonvilles (30 derniers jours, au 18 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la gestion des sites favoris, avec la possibilité de les épingler et de les retrouver facilement dans un onglet dédié. Des corrections et des refactorings ont été effectués sur l'interface utilisateur et l'API, notamment concernant la gestion des indicateurs et des phases préparatoires, ainsi que des corrections de validation et d'affichage.

### Évolutions fonctionnelles
- **Sites favoris :** Ajout de la fonctionnalité permettant aux utilisateurs d'épingler des sites pour un accès rapide. Un nouvel onglet "Mes sites" a été créé pour afficher les sites épinglés et les interventions associées. [#1501](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1501)
- **Filtres :** Ajout de l'option "Inconnu" au filtre "Type de propriétaire". [#1482](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1482)
- **Phases préparatoires :** Amélioration de l'affichage et de la gestion des phases préparatoires, avec une refonte de l'interface et des corrections de persistance des données. [#1493](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1493)
- **Indicateurs scolaires :** Amélioration de la validation et de l'affichage des indicateurs scolaires. [#1490](https://github.com/MTES-MCT/resorption-bidonvilles/issues/1490)

### Évolutions techniques
- **API :** Refactoring de l'API pour améliorer la gestion des droits d'accès au téléphone des utilisateurs et pour centraliser la logique de validation.
- **Frontend :** Refactoring du frontend pour améliorer la performance, la lisibilité et la maintenabilité du code, notamment en utilisant `structuredClone` au lieu de `cloneDeep` et en harmonisant les noms de champs.
- **Base de données :** Ajout de migrations pour supporter la nouvelle fonctionnalité de sites favoris et pour ajouter la phase "Diagnostic technique".
- **Tests :** Ajout de tests unitaires et d'intégration pour garantir la qualité du code.
- **Linting :** Corrections de linting pour améliorer la qualité du code.

### Autres changements
- Mise à jour des conditions d'utilisation.
- Ajout d'un bandeau d'information concernant la canicule.
- Correction de liens et de libellés.
- Mise à jour de la date de production et de la date limite du questionnaire.
- Amélioration de la documentation.
