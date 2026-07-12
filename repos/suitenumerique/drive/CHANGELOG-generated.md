## Changelog : drive (30 derniers jours, au 8 juillet 2026)

### Résumé
Les dernières mises à jour de Drive se concentrent sur l'amélioration de la recherche de fichiers, notamment en ajoutant de nouveaux filtres (type de fichier, contact, date de modification, emplacement) et en optimisant la recherche dans la corbeille. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées, notamment au niveau des filtres et des tests automatisés. Une attention particulière a été portée à la sécurité avec la mise à jour de certaines dépendances.

### Évolutions fonctionnelles
- Ajout de filtres de recherche avancés : type de fichier, contact, date de modification et emplacement. [#21284be](https://github.com/suitenumerique/drive/commit/21284be)
- Amélioration de la recherche dans la corbeille pour inclure les éléments racine supprimés. [#8e5fb99](https://github.com/suitenumerique/drive/commit/8e5fb99)
- Exclusion des dossiers des résultats de recherche par type de fichier. [#ca6bbd5](https://github.com/suitenumerique/drive/commit/ca6bbd5)
- Ajout d'un menu d'aide dans le panneau latéral gauche. [#5c64f2b](https://github.com/suitenumerique/drive/commit/5c64f2b)
- Possibilité d'utiliser une plage de dates personnalisée pour filtrer les fichiers par date de modification. [#f191788](https://github.com/suitenumerique/drive/commit/f191788)
- Amélioration de la gestion des conversions de fichiers pendant l'analyse antivirus. [#d49b79a](https://github.com/suitenumerique/drive/commit/d49b79a)

### Évolutions techniques
- Mise à jour de la dépendance `PyJWT` et `cryptography` pour corriger des failles de sécurité. [#630209f](https://github.com/suitenumerique/drive/commit/630209f)
- Contrainte de version de `joserfc` à >=1.6.8 pour corriger une vulnérabilité (CVE-2026-49852). [#25e693b](https://github.com/suitenumerique/drive/commit/25e693b)
- Optimisation du streaming des fichiers exportés depuis S3 pour éviter la mise en mémoire tampon. [#dd7b20b](https://github.com/suitenumerique/drive/commit/dd7b20b)
- Refactorisation des filtres d'explorateur pour les rendre contrôlés et séparés. [#ae60204](https://github.com/suitenumerique/drive/commit/ae60204)
- Amélioration de la gestion des requêtes de conversion de fichiers pendant l'analyse. [#3587826](https://github.com/suitenumerique/drive/commit/3587826)

### Autres changements
- Amélioration de la documentation README pour plus de clarté et de cohérence. [#f53d80d](https://github.com/suitenumerique/drive/commit/f53d80d)
- Enrichissement des guidelines de contribution. [#1843036](https://github.com/suitenumerique/drive/commit/1843036)
- Corrections diverses de tests E2E et amélioration de la couverture des tests. [#625c545](https://github.com/suitenumerique/drive/commit/625c545) et autres commits E2E.
- Suppression de filtres de recherche obsolètes dans le modal de recherche. [#d04e2d3](https://github.com/suitenumerique/drive/commit/d04e2d3)
- Diverses corrections de bugs et améliorations de l'interface utilisateur.
