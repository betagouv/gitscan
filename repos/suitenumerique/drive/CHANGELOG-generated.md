## Changelog : drive (30 derniers jours, au 29 juin 2026)

### Résumé
Les dernières mises à jour de drive se concentrent sur l'amélioration de l'expérience de recherche et de filtrage des fichiers, ainsi que sur l'ajout d'un menu d'aide pour faciliter l'utilisation de l'application. Des améliorations ont également été apportées à la gestion des conversions de fichiers et à la sécurité.

### Évolutions fonctionnelles
- Ajout d'un menu d'aide dans le panneau latéral gauche pour une assistance rapide aux utilisateurs. [#issue](https://github.com/suitenumerique/drive/issues/)
- Amélioration du filtre de recherche avec la possibilité de filtrer par emplacement, type de fichier, contact et date de modification.
- Ajout de filtres de date prédéfinis pour la recherche (plus d'un an).
- Possibilité de filtrer les fichiers par date de modification dans l'explorateur de fichiers.
- Ajout d'un filtre par type de fichier dans l'explorateur de fichiers.
- Amélioration de la gestion des fichiers en cours d'analyse (conversion) : possibilité de lancer la conversion pendant l'analyse.
- Les fichiers en cours d'analyse restent accessibles aux utilisateurs.
- Amélioration de l'affichage des fichiers en cours d'analyse dans l'interface.
- Ajout de contacts fréquemment utilisés pour faciliter le partage de fichiers.

### Évolutions techniques
- Mise à jour de la bibliothèque d'interface utilisateur (ui-kit) vers la version 0.24.0.
- Amélioration de la gestion des requêtes de conversion OnlyOffice avec signature JWT pour plus de sécurité.
- Optimisation du streaming des fichiers exportés depuis S3 pour éviter les problèmes de mémoire.
- Amélioration de la gestion des healthchecks Collabora.
- Refactorisation du code pour séparer et contrôler les filtres de l'explorateur de fichiers.
- Extraction des requêtes de localisation des éléments pour une meilleure organisation du code.
- Mise à jour des dépendances PyJWT et cryptography pour corriger des failles de sécurité.

### Autres changements
- Amélioration de la documentation README pour plus de clarté et de cohérence.
- Enrichissement des guidelines de contribution.
- Correction de tests E2E pour assurer la stabilité de l'application.
- Correction d'erreurs mineures et améliorations de la qualité du code.
