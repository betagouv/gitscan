## Changelog : portail-rse (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions du portail RSE se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des exercices comptables et la qualification VSME. Des corrections ont été apportées pour gérer des cas spécifiques liés à l'API SIRENE et à la consommation d'énergie, et des refactorisations ont été effectuées pour simplifier et optimiser le code.

### Évolutions fonctionnelles
- Amélioration de la navigation entre les années pour la qualification VSME avec l'introduction du concept d'"Exercice" [#938a117](https://github.com/betagouv/portail-rse/commit/938a117).
- Affichage de l'exercice en cours sur les tableaux de bord et les pages de catégories VSME.
- Ajout de la consommation d'énergie comme critère nécessaire pour la qualification d'une entreprise, avec un champ dédié dans le formulaire et l'affichage dans le résumé de l'entreprise. [#492af87](https://github.com/betagouv/portail-rse/commit/492af87)
- Amélioration des messages d'avertissement lorsque le profil d'une entreprise est incomplet [#1a80acd](https://github.com/betagouv/portail-rse/commit/1a80acd).
- Correction d'un bug lié à l'affichage du message informatif lors du changement d'exercice [#ef376a2](https://github.com/betagouv/portail-rse/commit/ef376a2).
- Gestion du cas où l'API SIRENE ne fournit pas le code postal du siège lors de la création d'une entreprise [#e6b9159](https://github.com/betagouv/portail-rse/commit/e6b9159).
- Export de la consommation d'énergie dans Metabase [#d168e0a](https://github.com/betagouv/portail-rse/commit/d168e0a).
- Ajout d'une description pour guider l'utilisateur sur le champ consommation d'énergie [#97febf0](https://github.com/betagouv/portail-rse/commit/97febf0).
- Refus d'une date de clôture future [#cd2cb4c](https://github.com/betagouv/portail-rse/commit/cd2cb4c).
- Prise en compte du nouveau critère de l'audit énergétique [#a6d3808](https://github.com/betagouv/portail-rse/commit/a6d3808).
- Possibilité de modifier un utilisateur sans lui attribuer une fonction RSE dans l'administration [#5fde1d9](https://github.com/betagouv/portail-rse/commit/5fde1d9).
- Ajout de l'année de clôture sur les rapports VSME dans Metabase [#228ac6b](https://github.com/betagouv/portail-rse/commit/228ac6b).

### Évolutions techniques
- Refactorisation des vues de l'espace découverte de la réglementation VSME pour réutiliser du code mutualisé [#d3c150d](https://github.com/betagouv/portail-rse/commit/d3c150d).
- Uniformisation du fil d'arianne des différentes parties du tableau de bord [#4a25145](https://github.com/betagouv/portail-rse/commit/4a25145).
- Simplification de la logique pour les méthodes `criteres_remplis` et `est_soumis` dans la réglementation VSME [#e6fe488](https://github.com/betagouv/portail-rse/commit/e6fe488).
- Factorisation de la donnée valide pour éviter la duplication [#e6a76a4](https://github.com/betagouv/portail-rse/commit/e6a76a4).
- Validation des champs du formulaire dans les méthodes dédiées de Django [#d50f330](https://github.com/betagouv/portail-rse/commit/d50f330).
- Suppression du code postal du profil affiché sur le tableau de bord [#d417c25](https://github.com/betagouv/portail-rse/commit/d417c25).
- Suppression du management de l'énergie [#6e1a505](https://github.com/betagouv/portail-rse/commit/6e1a505).
- Déplacement de l'Exercice dans l'application entreprises [#938a117](https://github.com/betagouv/portail-rse/commit/938a117).
- Transformation d'une méthode en propriété [#3780344](https://github.com/betagouv/portail-rse/commit/3780344).

### Autres changements
- Documentation : coloration syntaxique du SQL [#ed9d129](https://github.com/betagouv/portail-rse/commit/ed9d129).
- Documentation : indication temporaire concernant la directive Omnibus [#4c82506](https://github.com/betagouv/portail-rse/commit/4c82506).
- Documentation : détails sur les étapes de synchronisation Metabase [#8d80fac](https://github.com/betagouv/portail-rse/commit/8d80fac).
- Documentation : note sur la configuration de firewalld sur la machine IA [#674bd38](https://github.com/betagouv/portail-rse/commit/674bd38).
- Nettoyage de code et suppression de code inutilisé.
- Tests: complétion des tests sur la simulation [#16f1383](https://github.com/betagouv/portail-rse/commit/16f1383).
- Correction de la cohérence entre le fonctionnement et le commentaire dans les tests [#9a2c5a0](https://github.com/betagouv/portail-rse/commit/9a2c5a0).
- Suppression d'une propriété inutilisée [#971a078](https://github.com/betagouv/portail-rse/commit/971a078).
- Suppression d'une fonction au profit d'une méthode sur l'Entreprise [#9588360](https://github.com/betagouv/portail-rse/commit/9588360).
- Suppression du "par défaut" [#94f46b3](https://github.com/betagouv/portail-rse/commit/94f46b3).
- Renommage pour correspondre à l'Exercice [#6dc28bc](https://github.com/betagouv/portail-rse/commit/6dc28bc).
- Affichage de l'exercice selon la date de clôture [#5f93670](https://github.com/betagouv/portail-rse/commit/5f93670).
- Wording [#6777f71](https://github.com/betagouv/portail-rse/commit/6777f71).
