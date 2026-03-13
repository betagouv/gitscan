## Changelog : playground (30 derniers jours)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en termes de gestion des métadonnées, de workflows de publication et d'intégration avec des outils d'IA comme Letta et Claude. Des corrections de bugs et des optimisations ont également été apportées pour améliorer la stabilité et la performance de la plateforme. L'accent a été mis sur l'amélioration de l'expérience utilisateur, notamment pour les traducteurs et les éditeurs.

### Évolutions fonctionnelles
- Ajout de la possibilité d'éditer les métadonnées des documents, avec des champs dédiés pour la fréquence, les sessions, les thèmes et les besoins. [#135](https://github.com/refugies-info/playground/pull/135)
- Implémentation de la publication des traductions avec des mises à jour en temps réel et des messages d'erreur détaillés. [#125](https://github.com/refugies-info/playground/pull/125)
- Ajout d'un système d'enregistrement automatique des modifications avant la publication ou l'archivage d'un document. [#123](https://github.com/refugies-info/playground/pull/123)
- Possibilité de visualiser la carte des points d'intérêt (POI) directement dans la fiche d'un document. [#152](https://github.com/refugies-info/playground/pull/152)
- Amélioration de la gestion des statuts de conformité des fiches RCO lors de l'ingestion. [#106](https://github.com/refugies-info/playground/pull/106)
- Ajout de la prise en charge de la langue russe pour l'IA. [#101](https://github.com/refugies-info/playground/pull/101)
- Ajout de filtres supplémentaires lors de l'ingestion des fiches RCO. [#105](https://github.com/refugies-info/playground/pull/105)

### Évolutions techniques
- Refactorisation de la gestion des statuts des documents pour une meilleure cohérence et conformité avec les workflows. [#119](https://github.com/refugies-info/playground/pull/119)
- Mise en place d'un système de gestion de la mémoire des agents Letta pour une meilleure performance et scalabilité. [#99](https://github.com/refugies-info/playground/pull/99)
- Intégration de Claude Code avec l'outil Entire CLI. [#100](https://github.com/refugies-info/playground/pull/100)
- Amélioration de la gestion des erreurs et des validations pour les champs de métadonnées. [#153](https://github.com/refugies-info/playground/pull/153)
- Optimisation des requêtes Supabase pour améliorer la performance des workflows.
- Mise à jour des dépendances et des outils de développement (Node, npm, pnpm, Turbo). [#116](https://github.com/refugies-info/playground/pull/116)
- Utilisation de variables d'environnement pour la configuration de Vercel. [#114](https://github.com/refugies-info/playground/pull/114)

### Autres changements
- Ajout de documentation pour les nouveaux workflows et fonctionnalités.
- Amélioration des tests et de la couverture de code.
- Correction de bugs mineurs et améliorations de l'expérience utilisateur.
- Ajout de commentaires et de documentation pour faciliter la maintenance et la compréhension du code.
- Mise à jour des fichiers de configuration (gitignore, vercel.json, turbo.json).
- Refactorisation du code pour une meilleure lisibilité et maintenabilité.
- Ajout de la possibilité de générer des données de test pour Supabase.
- Ajout de la gestion des noms d'utilisateur pour les comptes utilisateurs. [#128](https://github.com/refugies-info/playground/pull/128)
- Ajout d'un panneau de débogage configurable. [#127](https://github.com/refugies-info/playground/pull/127)
