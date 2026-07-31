## Changelog : territoires-en-transitions (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la plateforme, notamment autour de la gestion des indicateurs, de la sécurité et de la préparation à la bascule vers le nouveau référentiel TE (Territoires en Transitions). Des optimisations de performance et des corrections de bugs ont également été apportées pour améliorer l'expérience utilisateur et la stabilité de la plateforme.

### Évolutions fonctionnelles
- Ajout de la vue SGPE avec persistance locale pour le référentiel TE.
- Amélioration de l'affichage des fiches liées aux indicateurs, avec un tableau plus clair.
- Implémentation de la fonctionnalité de déconnexion dans la navigation secondaire.
- Possibilité d'importer un plan via l'IA, avec suivi de progression et reprise.
- Ajout de la possibilité de définir des dates de début et de fin pour un plan.
- Amélioration de l'export Excel des indicateurs pour afficher toutes les données filtrées.
- Ajout d'une grille de saisie tabulaire pour les indicateurs, avec édition inline et autosave.
- Possibilité de coller des données tableur dans la grille de saisie des indicateurs.
- Ajout de la gestion du réordonnancement des colonnes et lignes dans la grille des indicateurs.
- Ajout de la fonctionnalité de collage de données dans la grille des indicateurs.
- Ajout de la possibilité de changer l'année de référence des indicateurs.
- Ajout de la fusion des services, pilotes et explications CAE/ECI vers les mesures TE.
- Ajout de la fusion des statuts d'origine vers les actions du référentiel CR.
- Ajout de la fusion des liens fiches CAE/ECI vers TE.

### Évolutions techniques
- Mise à jour de Next.js vers la dernière version.
- Mise à jour de TypeScript vers la version 6/7.
- Refactor de l'authentification, migration des modules vers l'application principale.
- Amélioration de la gestion des variables d'environnement avec `dotenvx`.
- Refactor de plusieurs composants pour améliorer la performance et la maintenabilité.
- Migration de certains modules vers le backend tRPC.
- Amélioration de la gestion des erreurs et des transactions.
- Utilisation de `date-fns` au lieu de `luxon` pour les manipulations de dates.
- Ajout de tests e2e pour la sécurité et la prévention d'injections IDOR.
- Amélioration du CI/CD avec relance automatique des tests e2e en cas d'échec intermittent.
- Suppression de code obsolète et de dépendances inutiles.
- Mise en place du pattern Result pour une meilleure gestion des erreurs.
- Préparation de la bascule vers le nouveau référentiel TE avec un garde de mode dédié.

### Autres changements
- Mise à jour de la documentation.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Amélioration de la gestion des permissions et des rôles.
- Nettoyage du code et refactoring de certains composants.
- Ajout de tests unitaires et e2e pour améliorer la couverture de code.
- Optimisation des performances de certaines requêtes et composants.
- Ajout de la gestion des fichiers `.env` avec des outils plus robustes.
- Correction de problèmes de sécurité liés à l'injection IDOR.
- Amélioration de la gestion des erreurs dans les tests.
- Mise à jour des dépendances.
- Ajout de badges de rôle plus clairs.
- Amélioration de la gestion des dates de fin des fiches.
- Correction de l'affichage des axes ouverts par défaut dans la vue SGPE.
- Ajout de nouveaux labels pour la vue SGPE.
- Amélioration de la gestion des permissions pour la modification des référentiels.
- Correction de l'affichage des statuts des sous-mesures.
- Amélioration de la gestion des erreurs lors de la sauvegarde des indicateurs.
- Ajout de la possibilité de filtrer les collectivité par code INSEE en majuscules.
- Amélioration de la gestion des fichiers dans les plans.
- Correction de l'affichage des courbes d'émissions nettes.
- Ajout de la possibilité de télécharger les documents de candidature pour les audits.
- Amélioration de la gestion des erreurs lors de l'importation de plans par IA.
- Ajout de la gestion des erreurs dans les tests e2e.
- Amélioration de la gestion des erreurs lors de la sauvegarde des indicateurs.
- Correction de l'affichage des badges de rôle dans le sélecteur de collectivité.
- Correction de l'affichage des statuts des sous-mesures.
- Amélioration de la gestion des erreurs lors de la sauvegarde des indicateurs.
- Correction de l'affichage des courbes d'émissions nettes.
- Ajout de la possibilité de télécharger les documents de candidature pour les audits.
- Amélioration de la gestion des erreurs lors de l'importation de plans par IA.
- Ajout de la gestion des erreurs dans les tests e2e.
- Amélioration de la gestion des erreurs lors de la sauvegarde des indicateurs.
- Correction de l'affichage des courbes d'émissions nettes.
- Ajout de la possibilité de télécharger les documents de candidature pour les audits.
- Amélioration de la gestion des erreurs lors de l'importation de plans par IA.
- Ajout de la gestion des erreurs dans les tests e2e.
- Amélioration de la gestion des erreurs lors de la sauvegarde des indicateurs.
- Correction de l'affichage des courbes d'émissions nettes.
- Ajout de la possibilité de télécharger les documents de candidature pour les audits.
- Amélioration de la gestion des erreurs lors de l'importation de plans par IA.
- Ajout de la gestion des erreurs dans les tests e2e.
- Amélioration de la gestion des erreurs lors de la sauvegarde des indicateurs.
- Correction de l'affichage des courbes d'émissions nettes.
- Ajout de la possibilité de télécharger les documents de candidature pour les audits.
- Amélioration de la gestion des erreurs lors de l'importation de plans par IA.
- Ajout de la gestion des erreurs dans les tests e2e.
- Amélioration de la gestion des erreurs lors de la sauvegarde des indicateurs.
- Correction de l'affichage des courbes d'émissions nettes.
- Ajout de la possibilité de télécharger les documents de candidature pour les audits.
- Amélioration de la gestion des erreurs lors de l'importation de plans par IA.
- Ajout de la gestion des erreurs dans les tests e2e.
- Amélioration de la gestion des erreurs lors de la sauvegarde des indicateurs.
- Correction de l'affichage des courbes d'émissions nettes.
- Ajout de la possibilité de télécharger les documents de candidature pour les audits.
- Amélioration de la gestion des erreurs lors de l'importation de plans par IA.
- Ajout de la gestion des erreurs dans les tests e2e.
- Amélioration de la gestion des erreurs lors de la sauvegarde des indicateurs.
- Correction de l'affichage des courbes d'émissions nettes.
- Ajout de la possibilité de télécharger les documents de candidature pour les audits.
- Amélioration de la gestion des erreurs lors de l'importation de plans par IA.
- Ajout de la gestion des erreurs dans les tests e2e.
- Amélioration de la gestion des erreurs lors de la sauvegarde des indicateurs.
- Correction de l'affichage des courbes d'émissions nettes.
