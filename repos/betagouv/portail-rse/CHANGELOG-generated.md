## Changelog : portail-rse (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions du portail RSE se concentrent sur l'amélioration de l'expérience utilisateur dans l'espace de qualification VSME, notamment avec une gestion plus fine des exercices comptables et de la consommation d'énergie. Des corrections et refactorisations techniques ont également été apportées pour optimiser le code et la maintenance du projet.

### Évolutions fonctionnelles
- **Qualification VSME :** Ajout de la prise en compte du critère de l'audit énergétique dans la qualification VSME [#a6d3808].
- **Consommation d'énergie :**
    - La consommation d'énergie est désormais un champ obligatoire pour la qualification d'une entreprise [#739523d].
    - Ajout d'une description pour guider l'utilisateur sur le champ de la consommation d'énergie [#97febf0].
    - Affichage de la consommation d'énergie dans le formulaire de qualification et dans le résumé de l'entreprise [#492af87, #0f21f90].
- **Exercices comptables :**
    - Introduction du concept d'Exercice regroupant des années pour une meilleure gestion des données [#80b36fa].
    - Possibilité de sélectionner et naviguer entre les exercices pour consulter les données des années précédentes [#b7963d7].
    - Affichage de l'exercice en cours sur les tableaux de bord et les pages de catégories VSME [#8b3782d, #6e8b122].
- **Profil utilisateur :** Suppression de l'affichage du code postal dans le profil utilisateur sur le tableau de bord [#d417c25].
- **Messages d'avertissement :** Amélioration des messages d'avertissement affichés lorsque le profil d'une entreprise est incomplet [#1a80acd].
- **Administration :** Possibilité de modifier un utilisateur sans lui attribuer une fonction RSE [#5fde1d9].
- **Metabase :** Ajout de l'année de clôture sur les rapports VSME [#228ac6b] et possibilité d'exporter la consommation d'énergie [#d168e0a].

### Évolutions techniques
- **Refactoring VSME :** Simplification des vues de l'espace découverte de la réglementation VSME en réutilisant du code mutualisé [#d3c150d].
- **Refactoring général :** Plusieurs refactorisations ont été effectuées pour améliorer la lisibilité et la maintenabilité du code, notamment au niveau de la gestion des exercices et des données [#9588360, #938a117, #3780344].
- **Validation :** Utilisation de la même logique que les autres réglementations pour les méthodes `criteres_remplis` et `est_soumis` [#e6fe488]. Validation d'un champ du formulaire dans la méthode dédiée prévue par Django [#d50f330].
- **Correction :** Correction du lien vers la VSME par défaut et réutilisation de l'exercice [#9094c92]. Correction d'un bug lié à l'affichage d'un message informatif lors du changement d'exercice [#ef376a2].
- **Documentation :** Ajout de la coloration syntaxique du SQL dans la documentation [#ed9d129] et documentation des étapes de synchronisation Metabase [#8d80fac].

### Autres changements
- Suppression du management de l'énergie [#6e1a505].
- Suppression du "par défaut" dans certains contextes [#94f46b3].
- Nettoyage et suppression de code inutilisé [#971a078].
- Amélioration du wording sur certaines parties de l'application [#6777f71].
- Ajout de tests pour la simulation [#16f1383].
- Correction d'une incohérence dans les tests [#9a2c5a0].
