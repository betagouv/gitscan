## Changelog : monprojetsup (30 derniers jours)

### Résumé
Ce mois-ci, les améliorations se concentrent sur le module de suggestions de formations (suggestions2) avec l'ajout d'un nouveau score basé sur les données Parcoursup, des corrections de bugs et une meilleure gestion des données. Des améliorations ont également été apportées à l'infrastructure et à la gestion des indicateurs.

### Évolutions fonctionnelles
- **Suggestions2 :** Ajout d'un nouveau score de suggestion basé sur les données des vœux Parcoursup, améliorant la pertinence des recommandations. (#1034, #1038)
- **Suggestions2 :** Amélioration de la tolérance aux valeurs inconnues dans les champs de la base de données (bac, durée, apprentissage, niveau). (#1032)
- **Indicateurs MPS :** Mise à jour de l'API et du front-end pour les indicateurs Mon Projet Sup. (#1048)
- **Progression Service :** Restauration du service de progression. (#1047)

### Évolutions techniques
- **Suggestions2 :** Optimisation de l'utilisation de la mémoire pour améliorer les performances. (#1040)
- **Suggestions2 :** Ajout de tests pour la CI afin d'assurer la qualité du code. (#1058)
- **Suggestions2 :** Pré-calcul du modèle pour améliorer le temps de démarrage. (#1051)
- **Dépendances :** Mise à jour des versions de Spring Boot et d'autres dépendances. (#1053)
- **ETL :** Accélération de l'ETL en mode test et simplification du calcul des vœux villes. (#1056)
- **Infrastructure :** Correction de problèmes de CI et rebasing sur les branches prod et demo. (#1057, #1059)

### Autres changements
- Documentation du nouveau score Parcoursup dans le README de Suggestions2. (#1038)
- Correction de bugs divers dans Suggestions2 et l'ETL.
- Nettoyage du code et suppression de points-virgules inutiles. (#1027, #1023)
- Ajout de variables d'environnement pour la configuration de Suggestions2. (#1051)
