## Changelog : portail-rse (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans l'espace VSME (Vitrine des Savoir-faire Métiers de l'Environnement), notamment en facilitant la navigation entre les exercices comptables et en affichant des informations plus claires sur la consommation d'énergie. Des corrections et refactorisations techniques ont également été apportées pour améliorer la robustesse et la maintenabilité du code.

### Évolutions fonctionnelles
- **VSME :** Ajout de l'année de clôture sur les rapports VSME [#228ac6b](https://github.com/betagouv/portail-rse/commit/228ac6b).
- **VSME :** Amélioration du fil d'arianne pour une navigation plus intuitive [#4a25145](https://github.com/betagouv/portail-rse/commit/4a25145).
- **VSME :** Affichage de la consommation d'énergie dans le formulaire de qualification et dans le résumé de l'entreprise [#492af87](https://github.com/betagouv/portail-rse/commit/492af87), [#0f21f90](https://github.com/betagouv/portail-rse/commit/0f21f90).
- **VSME :** La consommation d'énergie est désormais un champ obligatoire pour qualifier une entreprise [#739523d](https://github.com/betagouv/portail-rse/commit/739523d).
- **VSME :** Modification des messages d'avertissement lorsque le profil d'une entreprise est incomplet [#1a80acd](https://github.com/betagouv/portail-rse/commit/1a80acd).
- **VSME :** Possibilité de sélectionner et naviguer entre différents exercices comptables [#8b3782d](https://github.com/betagouv/portail-rse/commit/8b3782d), [#9a2c5a0](https://github.com/betagouv/portail-rse/commit/9a2c5a0).
- **Administration :** Possibilité de modifier un utilisateur sans lui attribuer de fonction RSE [#5fde1d9](https://github.com/betagouv/portail-rse/commit/5fde1d9).
- **Metabase :** Ajout de la possibilité d'exporter la consommation d'énergie [#d168e0a](https://github.com/betagouv/portail-rse/commit/d168e0a).

### Évolutions techniques
- **Refactoring VSME :** Simplification des vues de l'espace découverte de la réglementation VSME en mutualisant le code [#d3c150d](https://github.com/betagouv/portail-rse/commit/d3c150d).
- **Refactoring VSME :** Utilisation d'une logique commune pour déterminer si une entreprise est soumise à la réglementation [#e6fe488](https://github.com/betagouv/portail-rse/commit/e6fe488).
- **Refactoring VSME :** Validation des champs de formulaire via les méthodes dédiées de Django [#d50f330](https://github.com/betagouv/portail-rse/commit/d50f330).
- **Refactoring général :** Déplacement de la logique liée aux exercices dans une nouvelle application dédiée [#938a117](https://github.com/betagouv/portail-rse/commit/938a117).
- **Refactoring général :** Suppression de code obsolète et simplification de certaines fonctions [#9588360](https://github.com/betagouv/portail-rse/commit/9588360), [#94f46b3](https://github.com/betagouv/portail-rse/commit/94f46b3).
- **Correction :** Correction d'un bug lié au lien vers la VSME par défaut [#9094c92](https://github.com/betagouv/portail-rse/commit/9094c92).
- **Correction :** Correction d'un message informatif incorrect lors du changement d'exercice [#ef376a2](https://github.com/betagouv/portail-rse/commit/ef376a2).
- **Documentation :** Ajout de la coloration syntaxique du SQL dans la documentation [#ed9d129](https://github.com/betagouv/portail-rse/commit/ed9d129).
- **Documentation :** Ajout d'informations sur la configuration de firewalld sur la machine IA [#674bd38](https://github.com/betagouv/portail-rse/commit/674bd38).

### Autres changements
- **Tests :** Ajout de tests pour la simulation VSME [#16f1383](https://github.com/betagouv/portail-rse/commit/16f1383).
- **Template EFRAG :** Unification du template EFRAG entre l'application et le site vitrine [#c27b5d7](https://github.com/betagouv/portail-rse/commit/c27b5d7).
- **Mises à jour de dépendances :** Mises à jour mineures de Pillow, pytest et cryptography (mises à jour automatiques).
