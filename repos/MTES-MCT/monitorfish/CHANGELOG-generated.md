## Changelog : monitorfish (30 derniers jours, au 01 Juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau des contrôles en mer et à la débarque avec la préparation de l'intégration e-ISR v1.3. Des améliorations techniques significatives ont également été apportées, notamment la migration vers des technologies plus récentes (Spring Boot 4, Hibernate 7) et l'amélioration de la qualité du code grâce à l'adoption de nouveaux linters (OxLint).

### Évolutions fonctionnelles
- Modification des contrôles en mer et à la débarque pour la version 1.3 d'e-ISR [#5175].
- Ajout de la possibilité de sauvegarder une infraction en attente lors de la création d'un rapport de contrôle [#1f3042b6].
- Amélioration des filtres dans la liste des signalements INN [#5151].
- Ajout du champ `is_under_jdp` à la table `analytics_missions` [#5162].
- Ajout du NATINF 4789 [#5149].
- Ajout du type de moyen des unités de contrôles [#5145].
- Affichage des navires sous AIS v1.2 [#5177].
- Ajout de groupes prioritaires pour les navires, avec une description et un affichage amélioré dans l'interface [#5231, #5215].
- Correction de bugs liés à la sauvegarde des contrôles après modification de la date de mission [#5237].
- Correction de l'affichage du champ infraction dans les rapports de contrôle [#5225].
- Correction de l'attribution des zones aux contrôles basée sur le JPE [#5226].
- Correction d'un bug sur le champ `position_type` de la table `last_positions` [#5229].

### Évolutions techniques
- Migration du linter vers `OxLint` (hybride avec `ESLint`) pour une meilleure qualité du code [#5233].
- Amélioration de l'exécution des linters en backend avec `ktlint` en ligne de commande et intégration dans le CI/CD [#5236].
- Mise à jour de plusieurs dépendances backend : Spring Boot 4, Security 7, Flyway 12, Ktor 3.5 [#5146, #5233].
- Amélioration de la gestion des dates dans les requêtes natives Hibernate [#0c902589].
- Optimisation de la performance du code, notamment en évitant les spread operators inutiles [#49d7098a, #1832eea9, #93a4a3cd].
- Amélioration de la configuration des tests et de la CI/CD.
- Correction de problèmes de sérialisation PATCH [#33861749].

### Autres changements
- Ajout d'un engin pour les navires auxiliaires à la campagne BFT [#5202].
- Ajout d'index pour l'import des notes de vente dans le data warehouse [#5196].
- Amélioration de l'UI des modals et harmonisation des composants Dialog [#5144].
- Correction de plusieurs tests Cypress et amélioration de la robustesse des tests e2e.
- Mise à jour de la documentation et des tests unitaires.
- Correction de problèmes mineurs d'UI et de wording.
- Suppression de dépendances inutiles et nettoyage du code.
- Mise à jour de la gestion des source maps pour Sentry.
