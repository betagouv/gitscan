## Changelog : portail-rse (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, les évolutions du portail RSE se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des exercices comptables et la qualification des entreprises. Des corrections ont été apportées pour gérer des cas spécifiques liés à l'API SIRENE et à l'affichage des données, tandis que des refactorisations techniques ont été réalisées pour simplifier le code et améliorer sa maintenabilité.

### Évolutions fonctionnelles
- Amélioration de l'affichage et de la navigation entre les exercices comptables pour les VSME [#9094c92](https://github.com/betagouv/portail-rse/commit/9094c92).
- Ajout de la consommation d'énergie comme critère de qualification pour les entreprises, avec un champ dédié dans le formulaire et l'affichage dans le résumé de l'entreprise [#a6d3808](https://github.com/betagouv/portail-rse/commit/a6d3808).
- Correction du message informatif affiché lors du changement d'exercice [#ef376a2](https://github.com/betagouv/portail-rse/commit/ef376a2).
- Gestion du cas où l'API SIRENE ne fournit pas le code postal du siège lors de la création d'une entreprise [#e6b9159](https://github.com/betagouv/portail-rse/commit/e6b9159).
- Ajout de l'année de clôture sur les rapports VSME [#228ac6b](https://github.com/betagouv/portail-rse/commit/228ac6b).
- Possibilité de modifier un utilisateur dans l'administration sans lui attribuer une fonction RSE [#5fde1d9](https://github.com/betagouv/portail-rse/commit/5fde1d9).
- Indication temporaire concernant la directive Omnibus dans le CSRD [#4c82506](https://github.com/betagouv/portail-rse/commit/4c82506).

### Évolutions techniques
- Refactorisation des vues de l'espace découverte de la réglementation VSME pour réutiliser du code mutualisé [#d3c150d](https://github.com/betagouv/portail-rse/commit/d3c150d).
- Simplification de la logique de qualification pour certaines réglementations VSME [#e6fe488](https://github.com/betagouv/portail-rse/commit/e6fe488).
- Uniformisation du fil d'arianne sur les différentes parties du tableau de bord [#4a25145](https://github.com/betagouv/portail-rse/commit/4a25145).
- Refactorisation du code lié à l'exercice comptable, avec déplacement de la logique dans l'application "entreprises" et renommage des variables pour plus de clarté [#938a117](https://github.com/betagouv/portail-rse/commit/938a117).
- Utilisation de la même logique pour déterminer si une entreprise est soumise à certaines réglementations [#e6a76a4](https://github.com/betagouv/portail-rse/commit/e6a76a4).
- Validation des champs de formulaire dans les méthodes dédiées de Django [#d50f330](https://github.com/betagouv/portail-rse/commit/d50f330).
- Coloration syntaxique du SQL dans la documentation [#ed9d129](https://github.com/betagouv/portail-rse/commit/ed9d129).

### Autres changements
- Suppression du code postal du profil affiché sur le tableau de bord [#d417c25](https://github.com/betagouv/portail-rse/commit/d417c25).
- Suppression du management de l'énergie [#6e1a505](https://github.com/betagouv/portail-rse/commit/6e1a505).
- Amélioration des messages d'avertissement lorsque le profil d'une entreprise est incomplet [#1a80acd](https://github.com/betagouv/portail-rse/commit/1a80acd).
- Ajout de tests pour la simulation [#16f1383](https://github.com/betagouv/portail-rse/commit/16f1383).
- Correction de liens et suppression de code inutile [#8b3782d](https://github.com/betagouv/portail-rse/commit/8b3782d), [#94f46b3](https://github.com/betagouv/portail-rse/commit/94f46b3), [#971a078](https://github.com/betagouv/portail-rse/commit/971a078), [#9588360](https://github.com/betagouv/portail-rse/commit/9588360), [#3780344](https://github.com/betagouv/portail-rse/commit/3780344).
- Documentation sur les étapes de synchronisation Metabase [#8d80fac](https://github.com/betagouv/portail-rse/commit/8d80fac).
- Amélioration du wording [#6777f71](https://github.com/betagouv/portail-rse/commit/6777f71).
- Ajout d'une description pour le champ de consommation d'énergie [#97febf0](https://github.com/betagouv/portail-rse/commit/97febf0).
- Refus des dates de clôture futures [#cd2cb4c](https://github.com/betagouv/portail-rse/commit/cd2cb4c).
