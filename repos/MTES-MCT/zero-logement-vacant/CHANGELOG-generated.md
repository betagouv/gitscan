## Changelog : zero-logement-vacant (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration des performances, la correction de bugs et l'enrichissement des fonctionnalités de l'application, notamment en ce qui concerne la gestion des propriétaires, la correspondance des adresses et la documentation technique. Des améliorations significatives ont également été apportées à l'infrastructure et aux outils de développement.

### Évolutions fonctionnelles
- Amélioration de la correspondance des adresses avec des règles de normalisation et un seuil abaissé à 0.85 [#5fc692aa](https://github.com/MTES-MCT/zero-logement-vacant/commit/5fc692aa).
- Ajout de notifications lors de la création d'une campagne et de la suppression d'un groupe [#74b243c7](https://github.com/MTES-MCT/zero-logement-vacant/commit/74b243c7).
- Correction de l'affichage des noms de périmètres dans le filtre, affichant désormais les types de périmètres au lieu des entités individuelles [#2994936b](https://github.com/MTES-MCT/zero-logement-vacant/commit/2994936b).
- Correction de l'affichage des pourcentages avec une décimale par défaut [#a3a3e940](https://github.com/MTES-MCT/zero-logement-vacant/commit/a3a3e940).
- Correction de l'affichage des images en brouillon lors du téléchargement [#fe370bdf](https://github.com/MTES-MCT/zero-logement-vacant/commit/fe370bdf).
- Amélioration de la gestion des droits d'accès et de l'authentification avec l'intégration de la plateforme Portail DF [#d1200176](https://github.com/MTES-MCT/zero-logement-vacant/commit/d1200176).
- Correction de l'état actif de la navigation pour la section "Parc de logements" [#e0e8e663](https://github.com/MTES-MCT/zero-logement-vacant/commit/e0e8e663).

### Évolutions techniques
- Refonte de la configuration du serveur avec remplacement de `convict` par `Zod` pour une meilleure validation et gestion des configurations [#3328bf9a](https://github.com/MTES-MCT/zero-logement-vacant/commit/3328bf9a).
- Migration de la spécification OpenAPI de TypeScript vers YAML avec remplacement de Swagger UI par Scalar [#443e46c0](https://github.com/MTES-MCT/zero-logement-vacant/commit/443e46c0).
- Amélioration des performances de la base de données avec la matérialisation des tables "gold" et de `owner_matching` en tant que TABLE pour une meilleure efficacité mémoire [#7000d604](https://github.com/MTES-MCT/zero-logement-vacant/commit/7000d604).
- Optimisation des requêtes Dbt pour éviter les erreurs de mémoire insuffisante (OOM) en divisant les processus de correspondance [#399797ce](https://github.com/MTES-MCT/zero-logement-vacant/commit/399797ce).
- Ajout de triggers pour précalculer les nombres de logements et de propriétaires associés à un groupe, améliorant ainsi les performances des requêtes [#dbddaa2e](https://github.com/MTES-MCT/zero-logement-vacant/commit/dbddaa2e).
- Mise à jour de Vite en version 8 et des plugins associés [#c914149a](https://github.com/MTES-MCT/zero-logement-vacant/commit/c914149a).
- Amélioration de la couverture des tests unitaires et d'intégration.
- Mise à jour des dépendances et des outils de développement.

### Autres changements
- Ajout de documentation technique complète, incluant des diagrammes et des guides d'utilisation [#7de10e71](https://github.com/MTES-MCT/zero-logement-vacant/commit/7de10e71).
- Ajout de la documentation pour l'implémentation des pipelines EETL et des propriétaires [#f47183fb](https://github.com/MTES-MCT/zero-logement-vacant/commit/f47183fb).
- Suppression de colonnes obsolètes dans les événements [#0a5e4a84](https://github.com/MTES-MCT/zero-logement-vacant/commit/0a5e4a84).
- Ajout de factories pour la création d'objets de test (utilisateurs, groupes, logements, etc.) [#677194ad](https://github.com/MTES-MCT/zero-logement-vacant/commit/677194ad).
- Nettoyage du code et suppression de code mort.
- Mise à jour de la configuration CI/CD pour améliorer la robustesse et l'efficacité des builds.
