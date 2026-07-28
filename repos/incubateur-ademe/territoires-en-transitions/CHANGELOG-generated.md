## Changelog : territoires-en-transitions (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité, la refactorisation technique pour une meilleure maintenabilité et performance, et l'ajout de nouvelles fonctionnalités pour les indicateurs et les référentiels, notamment en préparation de la bascule vers le référentiel Climat Ressources. Des améliorations significatives ont été apportées à l'interface utilisateur, notamment pour la gestion des audits et des preuves.

### Évolutions fonctionnelles
- Ajout de la possibilité de définir des dates de début et de fin pour un plan ([#7490](https://github.com/incubateur-ademe/territoires-en-transitions/issues/7490)).
- Implémentation de la fonctionnalité de déconnexion dans la navigation secondaire.
- Amélioration de l'export Excel des indicateurs pour afficher tous les indicateurs filtrés dans un format consolidé ([#7414](https://github.com/incubateur-ademe/territoires-en-transitions/issues/7414)).
- Possibilité de modifier l'année de référence des indicateurs directement dans la grille de saisie.
- Ajout d'une grille de saisie tabulaire pour les indicateurs, permettant l'édition et l'autosave des valeurs par cellule.
- Amélioration de la gestion des preuves d'audit : suppression des archives expirées, affichage des plus récentes en bas de liste, et possibilité pour l'auditeur de remplacer le rapport.
- Amélioration de l'interface de gestion des audits et des labellisations, avec édition inline des notes de l'auditeur et remplacement du rapport.
- Ajout de la possibilité d'importer un plan via l'IA, avec suivi de la progression et reprise.
- Amélioration de l'affichage des badges de rôle et des statuts dans l'interface.
- Correction du tri des actions et sous-actions dans le rapport PPT.
- Correction de l'affichage des sous-thématiques et des temps de mise en œuvre dans les fiches.

### Évolutions techniques
- Refactorisation du module d'authentification et migration vers l'application principale.
- Mise à jour de Next.js vers la dernière version.
- Mise à jour de TypeScript vers la version 6/7.
- Suppression de l'utilisation de Luxon au profit de date-fns pour une meilleure performance et compatibilité.
- Refactorisation de plusieurs composants pour améliorer la maintenabilité et la lisibilité du code.
- Amélioration de la gestion des variables d'environnement avec `dotenvx`.
- Optimisation des tests E2E pour une exécution plus rapide et fiable.
- Suppression de dépendances obsolètes et simplification de la configuration.
- Ajout de tests de sécurité pour prévenir les injections IDOR.
- Migration vers le pattern Result pour une meilleure gestion des erreurs.
- Amélioration de la gestion des permissions et de la sécurité des données.
- Refactorisation de l'architecture des référentiels pour préparer la bascule vers le référentiel Climat Ressources.
- Ajout de jalons pour la bascule vers le référentiel Climat Ressources.

### Autres changements
- Mise à jour de la documentation et des labels.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Amélioration de la gestion des erreurs et des logs.
- Optimisation des performances de l'application.
- Ajout de tests unitaires et d'intégration.
- Suppression de code mort et nettoyage du code source.
- Correction de problèmes de compatibilité avec différents navigateurs.
- Amélioration de l'accessibilité de l'application.
- Correction de problèmes de sécurité potentiels.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Suppression de configurations obsolètes.
- Mise à jour des dépendances.
