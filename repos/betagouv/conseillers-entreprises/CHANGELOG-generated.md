## Changelog : conseillers-entreprises (30 derniers jours, au 08 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations de la performance et de la stabilité de l'application, notamment avec le passage à esbuild pour le build frontend. Des corrections ont été apportées pour améliorer la gestion des données et l'expérience utilisateur, comme l'affichage de l'historique des besoins et la gestion des erreurs lors de la création d'entreprises et d'établissements. Des améliorations de la documentation et de l'architecture ont également été réalisées.

### Évolutions fonctionnelles
- Affichage de l'historique des besoins d'une entreprise, incluant les besoins inaccessibles [#4550](https://github.com/betagouv/conseillers-entreprises/issues/4550).
- Amélioration de l'affichage des statistiques d'évolution des besoins.
- Correction d'un bug empêchant la réutilisation d'un SIRET lors d'une sollicitation [#4524](https://github.com/betagouv/conseillers-entreprises/issues/4524).
- Ajout de témoignages d'experts sur les pages publiques [#4506](https://github.com/betagouv/conseillers-entreprises/issues/4506).
- Mise à jour de la page "équipe" avec des ajustements visuels et de contenu [#4513](https://github.com/betagouv/conseillers-entreprises/issues/4513).
- Amélioration de la gestion des erreurs lors de la création d'entreprises et d'établissements en cas d'échec des appels API [#4509](https://github.com/betagouv/conseillers-entreprises/issues/4509).
- Correction d'un bug lié à la correspondance des zones territoriales [#4559](https://github.com/betagouv/conseillers-entreprises/issues/4559).

### Évolutions techniques
- Passage du système de build Webpack à esbuild pour améliorer la performance et réduire la complexité [#4520](https://github.com/betagouv/conseillers-entreprises/issues/4520).
- Suppression de jQuery et remplacement par des alternatives modernes.
- Augmentation de la taille du pool de connexions à la base de données et du nombre de threads/processus Puma pour améliorer la concurrence.
- Refactoring du code lié à la gestion des durées (TimeDurationService) pour une meilleure organisation.
- Mise à jour des dépendances (undici, concurrent-ruby, nokogiri).
- Amélioration de la robustesse de la gestion des jobs Sidekiq.
- Suppression de code inutilisé.
- Mise à jour de la configuration de CircleCI pour améliorer les performances et la fiabilité des tests.
- Ajout d'un endpoint machine-readable `llms.txt` pour faciliter l'intégration avec des modèles de langage.

### Autres changements
- Mise à jour de la documentation de l'architecture du projet, incluant la clarification de la stack de production et des détails du pipeline.
- Correction de problèmes de style et de conformité avec les linters.
- Mise à jour des traductions françaises.
- Amélioration de la gestion des événements Matomo.
- Ajout de tests unitaires et d'intégration.
- Correction de bugs mineurs et améliorations de la qualité du code.
- Mise à jour de la configuration de la base de données pour utiliser le fichier `database.yml` en production.
- Suppression de fichiers inutiles.
