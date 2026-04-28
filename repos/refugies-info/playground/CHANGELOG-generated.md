## Changelog : playground (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, le projet a connu une évolution significative avec l'introduction d'une barre latérale persistante, l'amélioration du filtrage des documents (type d'entrée, thèmes, besoins), et une refonte de l'interface utilisateur avec l'intégration du système d'icônes DSFR et l'implémentation de Storybook pour le développement des composants. Des améliorations de sécurité et de performance ont également été apportées, notamment concernant l'authentification Supabase et l'optimisation du chargement des données.

### Évolutions fonctionnelles
- Ajout d'une barre latérale persistante avec un état replié mémorisable [#202](https://github.com/refugies-info/playground/pull/202).
- Implémentation d'un filtre par type d'entrée dans la liste des documents [#198](https://github.com/refugies-info/playground/pull/198).
- Ajout d'un filtre pour exclure les IDs de thèmes et de besoins "hallucinés" pour garantir l'intégrité des données [#197](https://github.com/refugies-info/playground/pull/197).
- Amélioration de la gestion des liens d'invitation Supabase : affichage des erreurs et redirection correcte [#195](https://github.com/refugies-info/playground/pull/195).
- Ajout d'un champ de recherche pour filtrer la liste des documents [#181](https://github.com/refugies-info/playground/pull/181).
- Ajout d'un filtre pour les entrées "en cours" (brouillon) [#199](https://github.com/refugies-info/playground/pull/199).
- Ajout d'un comptage de mots pour chaque document, avec affichage dans la liste et possibilité de tri [#193](https://github.com/refugies-info/playground/pull/193).
- Refonte de l'habillage de la liste des fiches et de l'en-tête avec l'intégration du design système DSFR [#189](https://github.com/refugies-info/playground/pull/189), [#186](https://github.com/refugies-info/playground/pull/186), [#182](https://github.com/refugies-info/playground/pull/182).

### Évolutions techniques
- Refactorisation de la gestion des rôles et des permissions (RBAC) avec stockage dans la table `profiles` et utilisation de fonctions RLS centralisées [#196](https://github.com/refugies-info/playground/pull/196).
- Mise en place d'un système d'icônes DSFR et intégration dans les composants de l'interface utilisateur [#180](https://github.com/refugies-info/playground/pull/180).
- Implémentation de Storybook pour le développement et la documentation des composants UI [#182](https://github.com/refugies-info/playground/pull/182).
- Migration de la configuration de Storybook vers TypeScript [#185](https://github.com/refugies-info/playground/pull/185).
- Amélioration de la performance du chargement des données en limitant le nombre de requêtes simultanées pour les audits [#184](https://github.com/refugies-info/playground/pull/184).
- Refactorisation de la gestion des états et des effets avec `useEffect` et `useUrlFilters`.
- Utilisation de `Object.hasOwn` pour des vérifications de propriétés plus sûres.
- Mise à jour de la configuration Supabase avec des URLs de redirection pour le développement local.
- Ajout d'un hook personnalisé pour la gestion des tokens d'accès RBAC.

### Autres changements
- Ajout d'un hook GitLeaks pour la détection de secrets dans le code [#188](https://github.com/refugies-info/playground/pull/188).
- Amélioration de la documentation et de l'organisation des composants dans Storybook [#186](https://github.com/refugies-info/playground/pull/186).
- Mise à jour des dépendances et des configurations de build.
- Correction de bugs mineurs et amélioration de la qualité du code.
- Ajout de tests unitaires avec Vitest et intégration avec Storybook.
- Mise à jour de la configuration Chromatic pour les tests de régression visuelle.
- Correction de labels et de textes d'interface pour une meilleure clarté.
