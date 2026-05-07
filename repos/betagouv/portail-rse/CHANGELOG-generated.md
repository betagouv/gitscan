## Changelog : portail-rse (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur concernant la qualification VSME, notamment la gestion des exercices comptables et l'affichage de la consommation d'énergie. Des améliorations techniques ont également été apportées pour simplifier le code et optimiser certaines fonctionnalités.

### Évolutions fonctionnelles
- **VSME :** Ajout de la possibilité de sélectionner et naviguer entre différents exercices comptables pour la qualification VSME [#9a2c5a0](https://github.com/betagouv/portail-rse/commit/9a2c5a0).
- **VSME :** Affichage de l'exercice en cours sur les tableaux de bord et les pages de catégories VSME [#8b3782d](https://github.com/betagouv/portail-rse/commit/8b3782d).
- **Qualification :** Intégration de la consommation d'énergie comme critère de qualification, avec affichage dans le formulaire et le résumé de l'entreprise [#a6d3808](https://github.com/betagouv/portail-rse/commit/a6d3808), [#492af87](https://github.com/betagouv/portail-rse/commit/492af87), [#739523d](https://github.com/betagouv/portail-rse/commit/739523d), [#0f21f90](https://github.com/betagouv/portail-rse/commit/0f21f90).
- **Messages d'information :** Amélioration des messages informatifs affichés lorsque le profil d'une entreprise est incomplet [#1a80acd](https://github.com/betagouv/portail-rse/commit/1a80acd).
- **Admin :** Possibilité de modifier un utilisateur sans lui attribuer une fonction RSE [#5fde1d9](https://github.com/betagouv/portail-rse/commit/5fde1d9).
- **Metabase :** Ajout de l'année de clôture sur les rapports VSME [#228ac6b](https://github.com/betagouv/portail-rse/commit/228ac6b).
- **Metabase :** Export de la consommation d'énergie [#d168e0a](https://github.com/betagouv/portail-rse/commit/d168e0a).

### Évolutions techniques
- **Refactoring VSME :** Simplification des vues de l'espace découverte de la réglementation VSME en réutilisant du code mutualisé [#d3c150d](https://github.com/betagouv/portail-rse/commit/d3c150d).
- **Refactoring :** Uniformisation du fil d'arianne sur les différentes parties du tableau de bord [#4a25145](https://github.com/betagouv/portail-rse/commit/4a25145).
- **Refactoring :** Utilisation d'une logique commune pour les méthodes `criteres_remplis` et `est_soumis` pour les réglementations [#e6fe488](https://github.com/betagouv/portail-rse/commit/e6fe488).
- **Refactoring :** Factorisation de la donnée valide pour éviter les duplications [#e6a76a4](https://github.com/betagouv/portail-rse/commit/e6a76a4).
- **Refactoring :** Validation des champs de formulaire dans les méthodes dédiées de Django [#d50f330](https://github.com/betagouv/portail-rse/commit/d50f330).
- **Refactoring :** Déplacement de la logique d'exercice dans l'application `entreprises` [#938a117](https://github.com/betagouv/portail-rse/commit/938a117).
- **Refactoring :** Suppression de code obsolète et simplification de la logique liée aux exercices [#94f46b3](https://github.com/betagouv/portail-rse/commit/94f46b3), [#9588360](https://github.com/betagouv/portail-rse/commit/9588360), [#971a078](https://github.com/betagouv/portail-rse/commit/971a078), [#3780344](https://github.com/betagouv/portail-rse/commit/3780344).

### Autres changements
- **Documentation :** Ajout de la coloration syntaxique du SQL dans la documentation [#ed9d129](https://github.com/betagouv/portail-rse/commit/ed9d129).
- **Documentation :** Ajout de notes sur la configuration de firewalld sur la machine IA [#674bd38](https://github.com/betagouv/portail-rse/commit/674bd38).
- **Documentation :** Documentation des étapes de synchronisation Metabase [#8d80fac](https://github.com/betagouv/portail-rse/commit/8d80fac).
- **Template EFRAG :** Unification du template EFRAG entre l'application et le site vitrine [#c27b5d7](https://github.com/betagouv/portail-rse/commit/c27b5d7).
- **Correction :** Correction d'un bug dans le message affiché lors du changement d'exercice [#ef376a2](https://github.com/betagouv/portail-rse/commit/ef376a2).
- **Correction :** Correction du lien vers la VSME par défaut [#9094c92](https://github.com/betagouv/portail-rse/commit/9094c92).
- **Tests :** Ajout de tests pour la simulation [#16f1383](https://github.com/betagouv/portail-rse/commit/16f1383).
- **Refus de date future :** Empêche la saisie d'une date de clôture future [#cd2cb4c](https://github.com/betagouv/portail-rse/commit/cd2cb4c).
