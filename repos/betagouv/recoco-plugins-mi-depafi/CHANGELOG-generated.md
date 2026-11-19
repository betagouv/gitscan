## Changelog : recoco-plugins-mi-depafi (30 derniers jours, au 18 novembre 2026)

### Résumé
Cette période a été marquée par l'enrichissement des réalisations grâce à la gestion des documents PDF et par une amélioration significative de la recherche. Les utilisateurs peuvent désormais filtrer plus précisément les contenus par catégorie et interagir plus facilement avec la carte, rendant la navigation plus intuitive.

### Évolutions fonctionnelles
- **Gestion documentaire** : Ajout de la possibilité de télécharger et de prévisualiser des fichiers PDF pour les réalisations, directement depuis les formulaires, la liste ou une fenêtre modale [#23](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/23).
- **Recherche et filtrage** : 
    - Amélioration de la recherche des réalisations [#2612](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/68).
    - Ajout de filtres par catégorie pour les réalisations et sur la carte.
- **Cartographie** : 
    - Les noms des sites sont désormais cliquables pour faciliter la navigation [#2561](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/65).
    - Corrections d'affichage de la carte et du sélecteur de départements.

### Évolutions techniques
- **Refactorisation du filtrage** : Optimisation de la gestion des périmètres de filtrage et déplacement des templates vers le noyau (core) pour une meilleure cohérence.
- **Architecture des données** : 
    - Introduction d'un modèle enfant pour les réalisations afin de garantir l'association systématique à un site.
    - Amélioration du schéma de configuration des plugins.
- **Optimisation des imports** : 
    - Amélioration de la robustesse des scripts d'importation (gestion de l'idempotence et détection automatique des noms de fichiers).
    - Amélioration de la sélection des référents via l'utilisation du périmètre.
- **Traçabilité et administration** : 
    - Amélioration du suivi (tracing) lors de la création de réalisations [#2609](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/67).
    - Ajout d'un filtre par périmètre dans l'interface d'administration [#2480](https://github.com/betagouv/recoco-plugins-mi-depafi/pull/63).

### Autres changements
- Mise à jour de la documentation.
- Passage à la version 0.7.0.
- Nettoyage du code (imports, styles CSS et rationalisation des tests).
