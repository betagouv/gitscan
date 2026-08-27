## Changelog : mobilic (30 derniers jours, au 26/08/2026)

### Résumé
Ce mois-ci, les développements ont principalement porté sur l'amélioration de la fluidité de saisie pour les utilisateurs et la précision de l'affichage des données. Les fonctionnalités de fractionnement d'activité ont été affinées, la gestion des notifications a été corrigée pour une meilleure visibilité, et l'expérience de saisie des dates a été optimisée. Côté infrastructure, l'introduction de nouveaux outils de test automatisés permet une validation plus rapide des changements.

### Évolutions fonctionnelles
- **Gestion des activités et fractionnement** :
  - Amélioration de la gestion du fractionnement d'activité avec l'ajout d'un tag "MODIFICATION" pour identifier les changements [#912](https://github.com/MTES-MCT/mobilic/pull/912).
  - Correction de l'affichage de l'historique des activités pour garantir la cohérence avec les exports PDF [#930](https://github.com/MTES-MCT/mobilic/pull/930).
  - Optimisation de la gestion des pauses et de la modification des temps de pause [#897](https://github.com/MTES-MCT/mobilic/pull/897).
- **Interface et Notifications** :
  - Correction de l'affichage et de la mise en page de la barre de notifications pour une meilleure lisibilité [#932](https://github.com/MTES-MCT/mobilic/pull/932).
  - Suppression de la fenêtre modale de mission longue pour simplifier le parcours utilisateur [#908](https://github.com/MTES-MCT/mobilic/pull/908).
- **Formulaires** :
  - Optimisation de la saisie de la date de naissance avec un système de focus automatique amélioré sur les champs mois/jour [#924](https://github.com/MTES-MCT/mobilic/pull/924).
- **Administration** :
  - Amélioration de la précision des statuts de mission, notamment pour la gestion des pauses et la priorité des statuts administrateur [#913](https://github.com/MTES-MCT/mobilic/pull/913).
- **Nouvelle fonctionnalité** :
  - Intégration de la fonctionnalité MEP (05/08/2026) [#916](https://github.com/MTES-MCT/mobilic/pull/916).

### Évolutions techniques
- **Infrastructure et CI/CD** :
  - Mise en place des "Review Apps" sur Scalingo, permettant de tester chaque modification dans un environnement isolé avant fusion [#904](https://github.com/MTES-MCT/mobilic/pull/904).
  - Amélioration de la robustesse des scripts de détection de branche dans le pipeline CI.
- **Observabilité et Maintenance** :
  - Amélioration de la capture et du suivi des erreurs liées aux jetons de rafraîchissement (refresh tokens) via Sentry [#914](https://github.com/MTES-MCT/mobilic/pull/914).
- **Refactoring** :
  - Centralisation de la logique de calcul des statuts de mission pour assurer une cohérence totale entre les différentes vues administratives.
  - Simplification du code lié au fractionnement d'activité et nettoyage des fonctions de calcul de statut.

### Autres changements
- Nettoyage du code (suppression de code mort, renommage de propriétés pour plus de clarté).
- Corrections de style et de syntaxe sur le front-end.
