## Changelog : benefriches (30 derniers jours, au 17 septembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de la gestion des sites existants, permettant aux utilisateurs de modifier leurs données plus facilement et en toute sécurité. Parallèlement, la précision des outils a été renforcée grâce à l'intégration de données statistiques plus récentes (ANCT, DVF 2025) et à l'ajustement des algorithmes de calcul d'impact pour garantir des résultats plus pertinents.

### Évolutions fonctionnelles
- **Amélioration de l'édition des sites** :
    - Ajout de points d'entrée "Modifier" sur les pages de résumé et d'évaluation.
    - Mise en place d'un système de sauvegarde d'état (save-state) et d'alertes en cas de modifications non enregistrées dans l'assistant de modification.
    - Prise en charge de l'édition des sites en zones urbaines personnalisées.
- **Précision des données et des calculs** :
    - Enrichissement des statistiques communales avec les données de l'ANCT (Observatoire des territoires).
    - Mise à jour des données foncières (DVF) incluant les transactions de 2025 et les données relatives aux terrains.
    - Actualisation de la base de données des communes françaises et intégration des zonages ALDO et ABC.
    - Affinement des seuils de calcul pour l'augmentation de la valeur foncière et les kilomètres évités afin d'éviter des calculs non significatifs.
- **Optimisation de l'expérience utilisateur (UX)** :
    - Amélioration de l'autocomplétion des adresses et synchronisation automatique de la ville lors de la saisie d'une adresse.
    - Meilleure visibilité des informations de modification (statut éditable/non éditable) sur les vues de sites et d'évaluations.

### Évolutions techniques
- **Sécurité et Authentification** :
    - Implémentation de la révocation des jetons d'authentification en attente [#01](https://github.com/incubateur-ademe/benefriches/issues/1).
- **Fiabilité de l'API et des données** :
    - Récupération (backfill) des contacts CRM pour les utilisateurs créés durant une interruption de service du CRM Connect.
    - Renforcement de la validation des configurations de l'API (URL de base du CRM).
- **Qualité et Tests** :
    - Extension de la couverture de tests de bout en bout (E2E) pour les flux de mise à jour de site et les scénarios d'inéligibilité [#14](https://github.com/incubateur-ademe/benefriches/issues/14).

### Autres changements
- **Documentation** : Fusion et simplification de la documentation relative aux scripts (manuels et programmés).
- **Organisation** : Restructuration des scripts de gestion des données communales pour une meilleure maintenance.
