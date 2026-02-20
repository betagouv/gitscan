## Changelog : verseau2 (30 derniers jours)

### Résumé
Ce changelog présente les améliorations apportées à verseau2 au cours des 30 derniers jours. Les principales évolutions concernent l'ajout de nouvelles fonctionnalités pour la gestion des contrôles, l'amélioration des performances et de la robustesse de l'application, ainsi que l'ajout d'un tableau de bord d'indicateurs. Des corrections de bugs et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un accès administrateur pour les "expert national verseau" permettant le téléchargement de fichiers XML (#18).
- Implémentation de l'envoi d'un fichier d'accusé de réception après le transfert d'un fichier XML (#17).
- Ajout d'un tableau de bord d'indicateurs avec la possibilité de filtrer par année de référence (#9).
- Ajout d'une pagination dans les groupes de contrôles pour une meilleure navigation (#20).
- Ajout de la gestion du cache via un interceptor pour améliorer les performances (#21).
- Normalisation des adresses email reçues de Cerbere en les convertissant en minuscules.
- Ajout du contrôle 054 - CBPO.
- Ajout de la gestion de plusieurs erreurs lors de l'envoi d'emails.
- Ajout d'icônes aux contrôles Sandre pour une meilleure identification visuelle.

### Évolutions techniques
- Migration des contrôles avec données live vers l'API MASA (#20).
- Refactor de l'enveloppe MASA pour les contrôles V2 afin d'utiliser une liste au lieu d'une map.
- Amélioration des performances de la requête d'indicateurs (#9).
- Ajout d'index sur certaines colonnes de la base de données pour optimiser les requêtes.
- Mise à jour des dépendances vulnérables (#36).
- Utilisation du `LoggerService` et ajout d'un décorateur `TraceCalls` pour une meilleure journalisation.
- Amélioration de la gestion des erreurs et des logs.
- Refactor des tests avec mutualisation des mocks et des datasets.
- Ajout de tests E2E pour l'API et le worker, ainsi que pour les droits d'utilisateur.
- Correction d'une race condition potentielle lors de la mise à jour d'un dépôt.
- Passage du service logger à Transient pour éviter des problèmes de scaling.
- Correction d'une erreur de résolution qui empêchait l'application de démarrer.
- Suppression du correlation id dans traceCalls.

### Autres changements
- Ajout d'une documentation AGENTS.md adaptée à une structure mémoire de type 3 couches.
- Correction de bugs mineurs et améliorations de la structure du code.
- Ajout de vérification du contenu du dump avant la restauration.
- Correction de typos et amélioration de la lisibilité du code.
- Correction de problèmes de typage dans les tests.
- Suppression de throw pour éviter un retry de la file.
- Ajout d'une librairie commune non orientée domaine pour partager du code entre le backend et le frontend.
- Correction d'un problème de test du LoggerService.
- Ajout de tests unitaires et d'intégration.
