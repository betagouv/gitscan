## Changelog : dialog-integrations (30 derniers jours)

### Résumé
Ce projet a connu des avancées significatives au cours des dernières semaines, notamment l'intégration de nouvelles sources de données (Brest et Sarthe) et l'amélioration de la robustesse et de la maintenabilité du code. Des tests unitaires et d'intégration ont été ajoutés pour garantir la qualité du code et faciliter les futures évolutions.

### Évolutions fonctionnelles
- Intégration des données de Brest avec l'ajout de l'URL associée (#1).
- Intégration des données de la Sarthe, incluant la gestion des arrêtés avec un tonnage de 0.
- Prise en charge de sources de données multiples.
- Intégration des limitations de gabarits pour le département de la Sarthe.

### Évolutions techniques
- Refactorisation et harmonisation de fonctions pour une meilleure lisibilité et maintenabilité.
- Ajout de tests unitaires et d'intégration pour valider le bon fonctionnement du code.
- Abstraction de la création de mesures et mutualisation de la création de DTO (Data Transfer Object) pour les véhicules.
- Simplification des fonctions de création de mesures et de la logique de création de localisation.
- Utilisation de `uv run` pour l'exécution des commandes.
- Amélioration de la configuration et simplification des paramètres.
- Mise en place d'un workflow d'intégration continue (CI).
- Remplacement de la recherche dynamique de fichiers par une approche plus directe.
- Utilisation de JSON compact pour les fichiers de configuration dans le CI.

### Autres changements
- Renommage de `dp_sarthes` en `dp_sarthe` pour une meilleure cohérence.
- Ajout d'un pré-processing step pour le département de la Sarthe.
- Modification du format JSON pour une meilleure lisibilité.
- Ajout d'un framework de test.
- Rendre l'ID de `dp_sarthes` déterministe.
- Mutualisation du code pour le calcul des dates de mesures.
