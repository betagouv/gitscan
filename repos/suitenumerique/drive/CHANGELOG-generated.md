## Changelog : drive (30 derniers jours, au 8 juillet 2026)

### Résumé
Les dernières mises à jour de Drive se concentrent sur l'amélioration de l'expérience de recherche, avec l'ajout de filtres par type de fichier, contact, date de modification et emplacement. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la fiabilité de l'application, notamment concernant la gestion des fichiers supprimés et l'analyse des fichiers. Des améliorations de sécurité ont été intégrées avec la mise à jour de certaines dépendances.

### Évolutions fonctionnelles
- Ajout de filtres de recherche par type de fichier, contact, date de modification et emplacement. [#21284be](https://github.com/suitenumerique/drive/commit/21284be), [#cc947d4](https://github.com/suitenumerique/drive/commit/cc947d4), [#b88bd75](https://github.com/suitenumerique/drive/commit/b88bd75), [#66692b3](https://github.com/suitenumerique/drive/commit/66692b3), [#650a29a](https://github.com/suitenumerique/drive/commit/650a29a)
- Possibilité de filtrer les résultats de recherche par date de modification avec des options prédéfinies (plus d'un an). [#77b3156](https://github.com/suitenumerique/drive/commit/77b3156)
- Ajout d'un menu d'aide dans le panneau latéral gauche. [#5c64f2b](https://github.com/suitenumerique/drive/commit/5c64f2b)
- Amélioration de la recherche dans la corbeille pour inclure les éléments racine supprimés. [#8e5fb99](https://github.com/suitenumerique/drive/commit/8e5fb99)

### Évolutions techniques
- Mise à jour de la dépendance `PyJWT` et `cryptography` pour corriger des failles de sécurité. [#630209f](https://github.com/suitenumerique/drive/commit/630209f)
- Contrainte de version de `joserfc` à >=1.6.8 pour corriger une CVE. [#25e693b](https://github.com/suitenumerique/drive/commit/25e693b)
- Optimisation du streaming des fichiers exportés depuis S3 pour éviter le buffering. [#dd7b20b](https://github.com/suitenumerique/drive/commit/dd7b20b)
- Amélioration de la gestion des requêtes de conversion de fichiers pendant l'analyse. [#d49b79a](https://github.com/suitenumerique/drive/commit/d49b79a), [#3587826](https://github.com/suitenumerique/drive/commit/3587826), [#1dbcf31](https://github.com/suitenumerique/drive/commit/1dbcf31)
- Suppression de code inutilisé dans le modal de recherche. [#d04e2d3](https://github.com/suitenumerique/drive/commit/d04e2d3)

### Autres changements
- Amélioration de la documentation README pour plus de clarté. [#f53d80d](https://github.com/suitenumerique/drive/commit/f53d80d)
- Enrichissement des guidelines de contribution. [#1843036](https://github.com/suitenumerique/drive/commit/1843036)
- Diverses corrections et améliorations des tests E2E. [#625c545](https://github.com/suitenumerique/drive/commit/625c545), [#f3b12b5](https://github.com/suitenumerique/drive/commit/f3b12b5), [#c9f86d9](https://github.com/suitenumerique/drive/commit/c9f86d9), [#ab45c32](https://github.com/suitenumerique/drive/commit/ab45c32), [#524bac7](https://github.com/suitenumerique/drive/commit/524bac7), [#44c73de](https://github.com/suitenumerique/drive/commit/44c73de), [#1301c6a](https://github.com/suitenumerique/drive/commit/1301c6a), [#8ef9fe8](https://github.com/suitenumerique/drive/commit/8ef9fe8)
- Correction d'un problème d'affichage des icônes de sélection dans les dropdowns. [#cdc71c9](https://github.com/suitenumerique/drive/commit/cdc71c9)
- Correction d'un bug empêchant la suppression des éléments après la suppression du dossier parent.
- Amélioration de la stabilité du sélecteur de date de modification personnalisé. [#330a782](https://github.com/suitenumerique/drive/commit/330a782)
