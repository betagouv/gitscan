## Changelog : zero-logement-vacant (30 derniers jours, au 07 mai 2026)

### Résumé
Cette période a été marquée par des améliorations significatives des performances, notamment au niveau du calcul du nombre de logements et de la gestion des propriétaires multiples. Des efforts importants ont également été consacrés à la documentation technique, à la suppression de code obsolète et à la modernisation de l'infrastructure, incluant l'intégration de nouveaux outils et la mise à jour des dépendances. Enfin, des corrections de bugs et des améliorations de l'expérience utilisateur ont été apportées.

### Évolutions fonctionnelles
- Amélioration de la gestion des propriétaires multiples : prise en charge des propriétaires multiples et affichage correct des informations associées. [#1798](https://github.com/MTES-MCT/zero-logement-vacant/issues/1798)
- Correction du traitement du statut des logements : gestion améliorée des logements "jamais contactés" pour une meilleure cohérence des données. [#1794](https://github.com/MTES-MCT/zero-logement-vacant/issues/1794)
- Amélioration de l'affichage des noms de périmètres : remplacement des noms de périmètres par des types plus clairs pour une meilleure compréhension. [#1757](https://github.com/MTES-MCT/zero-logement-vacant/issues/1757)
- Ajout de notifications : notifications sur la création de campagnes et la suppression de groupes. [#74b243c7](https://github.com/MTES-MCT/zero-logement-vacant/commit/74b243c7)
- Correction de l'affichage des images en brouillon : les images en brouillon sont maintenant correctement prévisualisées.
- Correction de l'affichage des pourcentages : les pourcentages sont maintenant affichés avec un seul chiffre après la virgule.

### Évolutions techniques
- **Performances:**
    - Optimisation significative du temps de calcul du nombre de logements, réduisant le temps d'exécution de 4 à 36% selon les filtres. [#1793](https://github.com/MTES-MCT/zero-logement-vacant/issues/1793)
    - Remplacement de l'index geo-code par une colonne `is_multi_owner` pour améliorer les performances des requêtes sur les propriétaires multiples.
    - Utilisation de triggers au niveau des instructions pour les comptages de groupes, évitant ainsi des insertions en masse coûteuses.
- **Infrastructure & Outils:**
    - Mise à jour de Vite à la version 8 et des plugins associés.
    - Intégration de Knip pour l'analyse des dépendances et la suppression des dépendances inutilisées.
    - Mise à jour des actions GitHub pour bénéficier des dernières fonctionnalités et corrections de sécurité.
    - Ajout de codecov pour le suivi de la couverture de tests.
- **Architecture & Code:**
    - Suppression de code obsolète, notamment les anciens flux de campagne et les paramètres d'établissement.
    - Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
    - Migration de la spécification OpenAPI de TypeScript vers YAML et remplacement de Swagger UI par Scalar.
    - Remplacement de convict par Zod pour la gestion de la configuration.
    - Utilisation de p-memoize pour la mise en cache des résultats de l'API Geo.
- **Tests:**
    - Amélioration de la couverture des tests, notamment pour les DTOs partagés et les filtres geoCodes.

### Autres changements
- Ajout de documentation technique complète, incluant des diagrammes et des descriptions détaillées des différents composants.
- Mise à jour de la documentation pour refléter les changements apportés au code.
- Ajout d'une configuration Worktrunk pour faciliter le développement et les tests.
- Ajout d'un plan d'implémentation pour les "superpowers" (fonctionnalités avancées).
- Correction de plusieurs erreurs mineures et améliorations de la qualité du code.
- Ajout de la gestion des variables d'environnement via `.env.example`.
- Ajout de la prise en charge de l'authentification SSO.
- Intégration de Claude pour l'analyse des données et l'amélioration de la qualité des données.
- Ajout de la gestion des droits d'accès via Portail DF.
