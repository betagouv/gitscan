## Changelog : zero-logement-vacant (30 derniers jours, au 09 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'intégration des données Metabase via de nouveaux types de graphiques (barres, tables, secteurs), l'importation des données LOVAC 2026, l'optimisation des performances et la refactorisation du code pour une meilleure maintenabilité. Des améliorations significatives ont également été apportées à l'interface utilisateur, notamment pour la gestion des campagnes et la visualisation des données sur la carte.

### Évolutions fonctionnelles
- **Intégration Metabase :** Ajout de la prise en charge de nouveaux types de graphiques Metabase : diagrammes à barres, tableaux et diagrammes circulaires, permettant une visualisation plus riche des données.
- **Import LOVAC 2026 :** Implémentation complète de l'importation des données LOVAC 2026, incluant la transformation et le chargement des données.
- **Campagnes :**
    - Amélioration de l'alignement des boutons dans la gestion des campagnes.
    - Ajout d'une colonne "Statut d'envoi" pour les destinataires des campagnes.
    - Différenciation de l'exportation des données pour les groupes et les campagnes.
    - Ajout de colonnes supplémentaires (date de naissance du propriétaire, ville) à l'exportation des groupes.
- **Carte :**
    - Ajout d'une légende à la carte pour une meilleure interprétation des données.
    - Possibilité de basculer vers une vue tableau en cliquant sur un groupe sur la carte.
- **Interface utilisateur :** Amélioration de l'UX de la légende de la carte et ajout d'un état de chargement au bouton de connexion.

### Évolutions techniques
- **Refactorisation :**
    - Suppression du préfixe `/api` des routes et des appels API pour simplifier l'architecture.
    - Refactorisation du code lié à la gestion des campagnes.
    - Simplification de l'importation des données LOVAC en utilisant des formats de fichiers plus efficaces (Parquet).
- **Performances :**
    - Optimisation des requêtes SQL pour l'importation des données LOVAC.
    - Réduction de la taille du bundle frontend en utilisant le lazy loading pour les routes.
- **Tests :**
    - Ajout et amélioration des tests unitaires et d'intégration.
    - Correction de tests défaillants.
- **Dépendances :** Mise à jour des dépendances du projet.
- **Infrastructure :** Amélioration de la configuration de l'environnement de développement et de déploiement.
- **CI/CD :** Amélioration du pipeline CI/CD pour automatiser les tests et le déploiement.
- **Architecture :** Utilisation de DuckDB pour la transformation des données LOVAC.

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés au projet.
- Ajout de nouvelles compétences et amélioration des compétences existantes dans le cadre du programme beta.gouv.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Ajout de règles de linting et de formattage pour assurer la cohérence du code.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Ajout de nouvelles métriques et de nouveaux tableaux de bord pour surveiller les performances du projet.
- Suppression de code obsolète et de dépendances inutiles.
- Correction de problèmes de typographie (utilisation des apostrophes françaises).
- Ajout de la possibilité de désactiver la synchronisation quotidienne des données BAN.
