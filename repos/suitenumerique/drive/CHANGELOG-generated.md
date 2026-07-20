## Changelog : drive (30 derniers jours, au 15 juillet 2026)

### Résumé
Cette version apporte des améliorations significatives à la recherche de fichiers, avec l'ajout de filtres par type de fichier, contact, date de modification et emplacement. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la performance, notamment concernant l'indexation des fichiers et le streaming des exports. La sécurité a été renforcée avec la mise à jour de dépendances critiques.

### Évolutions fonctionnelles
- Ajout de filtres de recherche avancés : type de fichier, contact, date de modification et emplacement. [#issue à retrouver]
- Amélioration de la recherche dans la corbeille pour inclure les éléments racine supprimés.
- Correction d'un bug empêchant l'exclusion des dossiers des résultats de recherche par type de fichier.
- Possibilité de convertir un fichier pendant son analyse anti-malware.
- Amélioration de la gestion des exports de fichiers depuis S3, avec un streaming plus efficace.
- Ajout d'un menu d'aide dans le panneau latéral gauche.
- Possibilité d'utiliser une plage de dates personnalisée pour filtrer les fichiers par date de modification.

### Évolutions techniques
- Mise à jour de la dépendance `PyJWT` et `cryptography` pour corriger des failles de sécurité.
- Contrainte de version de `joserfc` à >=1.6.8 pour corriger une vulnérabilité (CVE-2026-49852).
- Refactorisation des filtres d'explorateur pour les rendre contrôlés et séparés.
- Amélioration de la gestion des requêtes de conversion de fichiers.
- Optimisation du streaming des fichiers exportés depuis S3.
- Utilisation de la bibliothèque `ui-kit` pour les icônes de fichiers et les prévisualisations.

### Autres changements
- Amélioration de la documentation README pour plus de clarté et de cohérence.
- Enrichissement des guidelines de contribution.
- Correction d'erreurs mineures dans les tests E2E.
- Suppression de filtres de recherche inutilisés dans le frontend.
- Amélioration des tests E2E pour la conversion de fichiers WOPI.
- Correction d'un bug lié à l'affichage des icônes de coche dans les dropdowns.
- Correction d'un bug lié au comportement du filtre "modifié" lors de sa désélection.
