## Changelog : playground (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en termes d'expérience utilisateur, notamment sur l'écran de liste des fiches avec l'ajout de filtres, de tris, de champs supplémentaires et une recherche. L'architecture a également été revue avec l'implémentation de Storybook pour les composants UI et une refonte du système d'icônes. Des corrections ont été apportées pour améliorer la stabilité et la fiabilité, notamment concernant la gestion des traductions et la génération de métadonnées.

### Évolutions fonctionnelles
- Ajout d'une recherche pour filtrer la liste des documents [#181](https://github.com/refugies-info/playground/pull/181).
- Ajout de filtres et d'options de tri à la liste des documents [#172](https://github.com/refugies-info/playground/pull/172).
- Ajout de colonnes "Lieu" et "Entrées/Sorties" à la liste des documents [#176](https://github.com/refugies-info/playground/pull/176).
- Ajout d'une colonne "ID externe" avec possibilité de copier le contenu dans le presse-papier [#176](https://github.com/refugies-info/playground/pull/176).
- Amélioration de la navigation sur la liste des traductions avec un clic sur une ligne pour accéder à la fiche [#175](https://github.com/refugies-info/playground/pull/175).
- Correction d'un bug empêchant le bon fonctionnement des traductions [#191](https://github.com/refugies-info/playground/pull/191).
- Correction de l'affichage du label "Brouillon" qui est maintenant affiché en violet [#178](https://github.com/refugies-info/playground/pull/178).
- Amélioration de l'attribution de l'auteur lors de la modification des métadonnées [#180](https://github.com/refugies-info/playground/pull/180).
- Correction d'une typo dans le label "Permanente" [#179](https://github.com/refugies-info/playground/pull/179).
- Ajout du nombre de mots à la liste des documents et possibilité de trier par ce critère [#192](https://github.com/refugies-info/playground/pull/192).

### Évolutions techniques
- Implémentation de Storybook pour le développement et la documentation des composants UI [#182](https://github.com/refugies-info/playground/pull/182).
- Refonte du système d'icônes avec l'intégration du DSFR (Design System Français) [#176](https://github.com/refugies-info/playground/pull/176).
- Refactorisation de l'architecture de la liste des documents avec l'introduction de composants réutilisables et de "column factories".
- Mise à jour de la configuration de Storybook vers TypeScript.
- Amélioration de la gestion des erreurs lors de la mise à jour des workflows Supabase [#194](https://github.com/refugies-info/playground/pull/194).
- Refonte du système de streaming éditorial avec l'utilisation de Supabase Realtime et un fallback de polling [#194](https://github.com/refugies-info/playground/pull/194).
- Ajout d'un hook GitLeaks pour détecter les secrets dans le code [#188](https://github.com/refugies-info/playground/pull/188).
- Optimisation de la gestion des tâches en arrière-plan pour éviter la surcharge du système [#187](https://github.com/refugies-info/playground/pull/187).
- Amélioration de la gestion des dépendances et du workflow de build.

### Autres changements
- Amélioration de la documentation et de l'organisation des composants Storybook [#186](https://github.com/refugies-info/playground/pull/186).
- Mise à jour des dépendances et des outils de développement.
- Nettoyage du code et suppression des éléments inutilisés.
- Amélioration de la gestion des types TypeScript pour une meilleure robustesse.
- Ajout d'un script pour générer les types Supabase.
- Mise à jour des textes et des labels pour une meilleure clarté et cohérence.
