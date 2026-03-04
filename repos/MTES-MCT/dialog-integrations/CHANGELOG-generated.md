## Changelog : dialog-integrations (30 derniers jours)

### Résumé
Ce projet a connu une période d'activité intense, principalement axée sur l'intégration de nouvelles sources de données de dialogue, notamment pour les zones de Brest et de la Sarthe. Des améliorations significatives ont été apportées à la structure du code, à la gestion des données et à l'ajout de tests pour garantir la qualité et la fiabilité du système.

### Évolutions fonctionnelles
- Intégration des données de Brest, incluant l'URL associée aux informations. [#1](https://github.com/MTES-MCT/dialog-integrations/pull/1)
- Intégration des données de la Sarthe, avec correction du statut de publication et ajout des arrêtés pour les véhicules de tout tonnage.
- Intégration des limitations de gabarits pour le département de la Sarthe.
- Possibilité d'intégrer des données provenant de sources multiples.

### Évolutions techniques
- Refactorisation et harmonisation de plusieurs fonctions pour améliorer la lisibilité et la maintenabilité du code.
- Abstraction de la création de mesures et mutualisation de la création des DTO (Data Transfer Objects) pour les véhicules.
- Simplification des fonctions de création de mesures et de la logique de création de localisation.
- Ajout d'un framework de tests avec des tests unitaires et d'intégration.
- Utilisation de `uv run` pour l'exécution des commandes.
- Simplification de la configuration et utilisation de JSON compact pour le CI.
- Remplacement de la recherche dynamique par une approche plus directe.
- Rendu du JSON plus compact pour optimiser le CI.

### Autres changements
- Ajout d'un fichier `.gitignore` à la racine du projet.
- Amélioration du traitement des dates.
- Ajout d'une étape de pré-traitement des données.
- Ajout d'un workflow d'intégration continue.
- Renommage de `dp_sarthes` en `dp_sarthe` pour plus de cohérence.
- Mise à jour de la dépendance `nbconvert`.
