## Changelog : docs (30 derniers jours, au 22 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur avec l'ajout d'une barre latérale droite pour les commentaires et la table des matières, l'amélioration de l'accessibilité, ainsi que des optimisations de performance et des corrections de bugs. De nouvelles fonctionnalités comme la possibilité de quitter un document et le mode présentateur ont été implémentées. L'équipe a également travaillé sur l'intégration d'événements de suivi pour une meilleure analyse de l'utilisation.

### Évolutions fonctionnelles
- Ajout de la possibilité de quitter un document.
- Implémentation du mode présentateur pour faciliter les présentations.
- Les utilisateurs non authentifiés peuvent désormais effectuer des recherches.
- Ajout d'une barre latérale droite pour afficher les commentaires et la table des matières.
- Ajout d'une limite au nombre de réactions par commentaire.
- Ajout d'une fonctionnalité permettant de supprimer les relations d'un utilisateur lors de sa suppression.
- Ajout d'un breadcrumb dans les résultats de recherche.

### Évolutions techniques
- Optimisation des requêtes pour éviter le problème N+1 lors de la sérialisation des commentaires.
- Refactorisation de la gestion des événements PostHog.
- Amélioration de la gestion des connexions à la base de données lors des tests.
- Mise à jour de Blocknote à la version 0.51.4.
- Amélioration de la gestion des erreurs et des exceptions.
- Suppression du job de test E2E pour un autre navigateur.
- Amélioration de la configuration et du déploiement avec Helm.

### Autres changements
- Ajout d'un badge Snyk pour la sécurité.
- Améliorations de l'accessibilité de divers composants de l'interface utilisateur (liens, focus, titres, etc.).
- Mise à jour des chaînes de traduction.
- Correction de problèmes d'affichage et de mise en page.
- Ajout de tests unitaires et E2E pour les nouvelles fonctionnalités.
- Documentation mise à jour pour refléter les nouvelles fonctionnalités et configurations.
- Correction de bugs divers liés à l'interface utilisateur et au backend.
