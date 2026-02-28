## Changelog : monprojetsup (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à Mon Projet Sup au cours des 30 derniers jours. Les principales évolutions concernent l'amélioration des suggestions de formations, notamment grâce à l'intégration de nouvelles données Parcoursup et l'optimisation des performances. Des corrections de bugs et des ajustements techniques ont également été effectués pour améliorer la stabilité et la qualité du service.

### Évolutions fonctionnelles
- Amélioration des suggestions de formations avec un nouveau score basé sur les données Parcoursup (#1034, #1038).
- Mode expert activé et fonctionnel (#1064).
- Correction d'un bug dans les suggestions2 (#1036, #1037).
- Restauration du service de progression (#1047).
- Mise à jour de l'API front (#1048).

### Évolutions techniques
- Optimisation de l'utilisation de la mémoire dans les suggestions2 (#1040).
- Pré-calcul des modèles pour améliorer le temps de démarrage des suggestions2 (#1051).
- Mise à jour des versions de Spring Boot et d'autres dépendances, incluant la correction de `excludedGroups` et l'accélération de l'ETL en mode test (#1053).
- Simplification du calcul des vœux villes (#1050).
- Ajout de tests pour les suggestions2 (#1058).
- Intégration continue améliorée pour les suggestions2.
- Refactorisation du code pour réduire l'utilisation de la mémoire dans les suggestions2.
- Ajout d'une variable d'environnement `MODELS_DIR` pour configurer le répertoire des modèles des suggestions2.

### Autres changements
- Ajout de logs pour le mode expert (#1062).
- Modification des indicateurs demandés par Laura (#1061).
- Suppression de code hardcodé pour l'année (#1066, #1067).
- Correction de tests (#1059, #1066).
- Rebase des branches `prod` et `demo` (#1068, #1070).
- Ajout de fichiers manquants (#1044, #1047).
- Linting du code.
- Documentation mise à jour pour le nouveau score Parcoursup.
