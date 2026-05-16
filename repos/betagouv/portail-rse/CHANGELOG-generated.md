## Changelog : portail-rse (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions du portail RSE se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des exercices comptables et l'affichage des données VSME. Des corrections ont été apportées pour gérer des cas spécifiques liés à l'API SIRENE et à la consommation d'énergie. Des refactorings techniques ont également été réalisés pour simplifier le code et améliorer sa maintenabilité.

### Évolutions fonctionnelles
- Amélioration de l'affichage et de la navigation entre les exercices comptables pour les VSME, avec la possibilité de sélectionner l'exercice souhaité. [#9094c92](https://github.com/betagouv/portail-rse/commit/9094c92)
- Ajout de l'année de clôture sur les rapports VSME dans Metabase. [#228ac6b](https://github.com/betagouv/portail-rse/commit/228ac6b)
- Affichage de la consommation d'énergie dans le formulaire de qualification et dans le résumé de l'entreprise. [#492af87](https://github.com/betagouv/portail-rse/commit/492af87) et [#0f21f90](https://github.com/betagouv/portail-rse/commit/0f21f90)
- Gestion du cas où l'API SIRENE ne fournit pas le code postal du siège lors de la création d'une entreprise. [#e6b9159](https://github.com/betagouv/portail-rse/commit/e6b9159)
- Amélioration des messages d'avertissement lorsque le profil d'une entreprise est incomplet. [#1a80acd](https://github.com/betagouv/portail-rse/commit/1a80acd)
- Indication temporaire concernant la directive Omnibus. [#4c82506](https://github.com/betagouv/portail-rse/commit/4c82506)

### Évolutions techniques
- Refactoring de la logique de validation des critères de conformité pour la réglementation VSME, en réutilisant du code mutualisé. [#e6fe488](https://github.com/betagouv/portail-rse/commit/e6fe488)
- Simplification des vues de l'espace découverte de la réglementation VSME. [#d3c150d](https://github.com/betagouv/portail-rse/commit/d3c150d)
- Refactoring du code lié à l'exercice comptable, avec déplacement de la logique dans l'application "entreprises". [#938a117](https://github.com/betagouv/portail-rse/commit/938a117)
- Coloration syntaxique du SQL dans la documentation. [#ed9d129](https://github.com/betagouv/portail-rse/commit/ed9d129)
- Suppression de code obsolète et nettoyage du code. Plusieurs commits de Stéphane et Emillumine contribuent à cette amélioration.

### Autres changements
- Ajout de tests pour la simulation. [#16f1383](https://github.com/betagouv/portail-rse/commit/16f1383)
- Documentation des étapes de synchronisation avec Metabase. [#8d80fac](https://github.com/betagouv/portail-rse/commit/8d80fac)
- Possibilité de modifier un utilisateur dans l'administration sans lui attribuer une fonction RSE. [#5fde1d9](https://github.com/betagouv/portail-rse/commit/5fde1d9)
