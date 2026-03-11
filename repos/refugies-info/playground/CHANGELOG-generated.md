## Changelog : playground (30 derniers jours)

### Résumé
Ce mois-ci, le projet a connu une évolution significative, axée sur l'amélioration de l'expérience utilisateur pour les rédacteurs et traducteurs, la robustesse du pipeline d'ingestion de données, et la gestion des workflows de publication. Des fonctionnalités de prévisualisation de traduction, d'édition de métadonnées, et de suivi de l'état de publication ont été ajoutées. Des efforts importants ont également été consacrés à la sécurisation de l'accès aux données et à l'optimisation des performances.

### Évolutions fonctionnelles
- Ajout de la prévisualisation des traductions [#125](https://github.com/refugies-info/playground/pull/125).
- Implémentation de l'édition des métadonnées avec validation et sauvegarde automatique [#123](https://github.com/refugies-info/playground/pull/123), [#135](https://github.com/refugies-info/playground/pull/135).
- Amélioration du suivi de l'état de publication des documents, avec des mises à jour en temps réel et des messages d'erreur plus clairs [#148](https://github.com/refugies-info/playground/pull/148), [#153](https://github.com/refugies-info/playground/pull/153).
- Possibilité d'archiver les fiches, même celles qui n'ont jamais été publiées [#98](https://github.com/refugies-info/playground/pull/98).
- Ajout de filtres pour affiner la recherche et le traitement des fiches [#109](https://github.com/refugies-info/playground/pull/109).
- Ajout de champs pour la localisation (en ligne, départements spécifiques) dans les métadonnées [#151](https://github.com/refugies-info/playground/pull/151).
- Amélioration de l'interface utilisateur pour la sélection des thèmes et des besoins [#147](https://github.com/refugies-info/playground/pull/147).
- Ajout de la possibilité de voir l'auteur d'un document [#92](https://github.com/refugies-info/playground/pull/92).

### Évolutions techniques
- Refactorisation de la gestion des statuts des documents (compliance, travail, en ligne) [#91](https://github.com/refugies-info/playground/pull/91).
- Amélioration de la gestion des erreurs et de la persistance des données lors de la publication [#150](https://github.com/refugies-info/playground/pull/150).
- Mise en place de politiques de sécurité (RLS) plus strictes sur les tables de la base de données [#92](https://github.com/refugies-info/playground/pull/92).
- Optimisation des requêtes et des abonnements Supabase pour améliorer les performances [#153](https://github.com/refugies-info/playground/pull/153).
- Utilisation de l'agent Letta pour la génération automatique de métadonnées et la validation des données [#146](https://github.com/refugies-info/playground/pull/146).
- Mise en place d'un système de mémoire pour les agents Letta [#119](https://github.com/refugies-info/playground/pull/119).
- Amélioration de la gestion des erreurs et de la robustesse du pipeline d'ingestion de données [#113](https://github.com/refugies-info/playground/pull/113), [#121](https://github.com/refugies-info/playground/pull/121).
- Passage à des outils plus récents (Node, npm, pnpm) [#116](https://github.com/refugies-info/playground/pull/116).
- Utilisation de l'API REST Vercel au lieu de `curl` pour certaines opérations [#110](https://github.com/refugies-info/playground/pull/110).

### Autres changements
- Ajout de documentation pour les nouveaux workflows et fonctionnalités [#145](https://github.com/refugies-info/playground/pull/145).
- Mise à jour des guides de contribution pour l'utilisation de worktrees [#138](https://github.com/refugies-info/playground/pull/138).
- Amélioration de la configuration de l'environnement de développement avec l'ajout de fichiers `.env` et `.gitignore` [#115](https://github.com/refugies-info/playground/pull/115).
- Correction de bugs mineurs et amélioration de la qualité du code.
