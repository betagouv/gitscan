## Changelog : portail-rse (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les évolutions du portail RSE se concentrent sur l'amélioration de l'expérience utilisateur pour les entreprises, notamment dans le cadre de la qualification VSME. Des améliorations ont été apportées à la navigation, à l'affichage des données (notamment la consommation d'énergie et le code postal), et à la gestion des exercices comptables. Des corrections et des refactorings techniques ont également été réalisés pour optimiser le code et améliorer la maintenance.

### Évolutions fonctionnelles
- **VSME :** Ajout de l'année de clôture sur les rapports VSME pour une meilleure identification. [#228ac6b](https://github.com/betagouv/portail-rse/commit/228ac6b)
- **VSME :** Simplification des vues de l'espace découverte de la réglementation VSME en réutilisant du code existant. [#d3c150d](https://github.com/betagouv/portail-rse/commit/d3c150d)
- **Navigation :** Uniformisation du fil d'arianne sur l'ensemble du tableau de bord pour une meilleure expérience utilisateur. [#4a25145](https://github.com/betagouv/portail-rse/commit/4a25145)
- **Qualification VSME :** Ajout d'une description pour guider l'utilisateur sur le champ consommation d'énergie. [#97febf0](https://github.com/betagouv/portail-rse/commit/97febf0)
- **Qualification VSME :** La consommation d'énergie est désormais un champ obligatoire pour qualifier une entreprise. [#739523d](https://github.com/betagouv/portail-rse/commit/739523d)
- **Tableau de bord :** Affichage de la consommation d'énergie dans le résumé de l'entreprise et dans le formulaire de qualification. [#492af87](https://github.com/betagouv/portail-rse/commit/492af87), [#0f21f90](https://github.com/betagouv/portail-rse/commit/0f21f90)
- **Profil entreprise :** Suppression du code postal du profil affiché sur le tableau de bord. [#d417c25](https://github.com/betagouv/portail-rse/commit/d417c25)
- **Exercices comptables :** Introduction du concept d'exercice (englobant des années) pour une meilleure gestion des données temporelles. Possibilité de sélectionner des exercices pour naviguer entre les années. [#80b36fa](https://github.com/betagouv/portail-rse/commit/80b36fa), [#b7963d7](https://github.com/betagouv/portail-rse/commit/b7963d7), [#6e8b122](https://github.com/betagouv/portail-rse/commit/6e8b122)
- **Préremplissage VSME :** Possibilité de préremplir un rapport VSME à partir de rapports précédents. [#19e0528](https://github.com/betagouv/portail-rse/commit/19e0528)
- **Administration :** Possibilité de modifier un utilisateur sans lui attribuer une fonction RSE. [#5fde1d9](https://github.com/betagouv/portail-rse/commit/5fde1d9)

### Évolutions techniques
- **Refactoring :** Simplification et factorisation du code dans divers modules, notamment pour la gestion de la réglementation VSME et des données. [#d3c150d](https://github.com/betagouv/portail-rse/commit/d3c150d), [#e6fe488](https://github.com/betagouv/portail-rse/commit/e6fe488), [#e6a76a4](https://github.com/betagouv/portail-rse/commit/e6a76a4), [#d50f330](https://github.com/betagouv/portail-rse/commit/d50f330), [#9588360](https://github.com/betagouv/portail-rse/commit/9588360), [#938a117](https://github.com/betagouv/portail-rse/commit/938a117), [#3780344](https://github.com/betagouv/portail-rse/commit/3780344)
- **Code postal :** Ajout et gestion du code postal des entreprises, avec des corrections pour les codes postaux incorrects et l'export dans Metabase. [#90738f3](https://github.com/betagouv/portail-rse/commit/90738f3), [#6ecb4df](https://github.com/betagouv/portail-rse/commit/6ecb4df), [#4001405](https://github.com/betagouv/portail-rse/commit/4001405), [#98a284f](https://github.com/betagouv/portail-rse/commit/98a284f), [#92b0e68](https://github.com/betagouv/portail-rse/commit/92b0e68), [#5da6cef](https://github.com/betagouv/portail-rse/commit/5da6cef)
- **Metabase :** Amélioration de l'export des données vers Metabase, notamment pour les rapports VSME et le code postal. [#228ac6b](https://github.com/betagouv/portail-rse/commit/228ac6b), [#8d80fac](https://github.com/betagouv/portail-rse/commit/8d80fac), [#6ecb4df](https://github.com/betagouv/portail-rse/commit/6ecb4df)
- **Proconnect :** Intégration de Proconnect pour l'édition d'entreprises existantes. [#a98c0de](https://github.com/betagouv/portail-rse/commit/a98c0de)

### Autres changements
- **Documentation :** Mise à jour de la documentation concernant la synchronisation avec Metabase et la configuration de Firewalld. [#8d80fac](https://github.com/betagouv/portail-rse/commit/8d80fac), [#674bd38](https://github.com/betagouv/portail-rse/commit/674bd38)
- **Templates :** Unification du template EFRAG pour l'app et le site vitrine. [#c27b5d7](https://github.com/betagouv/portail-rse/commit/c27b5d7)
- **Nettoyage :** Suppression de code et de fonctions inutilisées. [#971a078](https://github.com/betagouv/portail-rse/commit/971a078), [#94f46b3](https://github.com/betagouv/portail-rse/commit/94f46b3), [#daefdea](https://github.com/betagouv/portail-rse/commit/daefdea), [#4ebab4e](https://github.com/betagouv/portail-rse/commit/4ebab4e)
