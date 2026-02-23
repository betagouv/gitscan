## Changelog : ecobalyse-data (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives aux données et aux fonctionnalités d'Ecobalyse.  De nouvelles données ont été ajoutées concernant les pâturages permanents, les forêts et de nouveaux ingrédients avec des métadonnées prédictives. Des optimisations ont également été apportées pour améliorer la performance lors de l'exportation de données et pour la gestion des activités.

### Évolutions fonctionnelles
- Ajout de données pour les pâturages permanents (#213).
- Ajout de données concernant les compléments forestiers (#208).
- Intégration de nouveaux ingrédients avec des métadonnées prédictives (#196).
- Amélioration de l'affichage des noms des proxies dans la configuration (#202).
- Ajout de la masse par unité pour certains éléments (#204).

### Évolutions techniques
- Optimisation de la performance lors de l'exportation de toutes les données, évitant de ralentir le système (#212).
- Refactorisation pour ajouter une vérification des activités dupliquées (#205).
- Tri des activités dans le fichier `activities.json` pour une meilleure organisation (#216).
