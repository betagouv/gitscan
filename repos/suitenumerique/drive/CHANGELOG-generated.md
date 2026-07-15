## Changelog : drive (30 derniers jours, au 8 juillet 2026)

### Résumé
Les dernières mises à jour de Drive se concentrent sur l'amélioration de la recherche de fichiers, avec l'ajout de filtres par type de fichier, contact, date de modification et localisation. Des corrections de bugs ont également été apportées pour améliorer la stabilité et la performance, notamment concernant l'analyse des fichiers et le streaming d'exportations depuis S3. Une attention particulière a été portée à la sécurité avec la mise à jour de certaines dépendances.

### Évolutions fonctionnelles
- Ajout d'un menu d'aide dans le panneau latéral gauche.
- Possibilité de filtrer les résultats de recherche par :
    - Type de fichier
    - Contact partageant le fichier
    - Date de modification (avec des options prédéfinies comme "plus d'un an")
    - Localisation du fichier
- Amélioration de la recherche dans la corbeille pour inclure les éléments racine supprimés.
- Possibilité de convertir un fichier pendant son analyse.
- Amélioration de la gestion des fichiers lors de l'analyse antivirus.
- Amélioration de l'expérience d'upload avec une barre de progression et la possibilité d'annuler.

### Évolutions techniques
- Mise à jour de la dépendance `PyJWT` et `cryptography` pour corriger des failles de sécurité.
- Contrainte de version de `joserfc` à >=1.6.8 pour corriger une vulnérabilité (CVE-2026-49852).
- Optimisation du streaming d'exportations depuis S3 pour éviter la mise en mémoire tampon.
- Refactorisation des filtres d'explorateur pour les rendre contrôlés et séparés.
- Utilisation de composants `ui-kit` pour les icônes et prévisualisations de fichiers.
- Amélioration de la gestion des requêtes de conversion de fichiers.

### Autres changements
- Amélioration de la documentation README pour plus de clarté.
- Enrichissement des guidelines de contribution.
- Corrections de tests E2E et ajustements des baselines.
- Suppression de filtres de recherche inutilisés dans le modal de recherche.
- Mise à jour de la version de `ui-kit` à 0.24.0.
- Correction d'erreurs liées à la gestion des chemins d'exportation et des cibles pseudo dans les tests.
