## Changelog : gestion-des-subventions-locales (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau des simulations, des projets et des filtres. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la sécurité et de l'infrastructure. L'outil a également évolué pour mieux s'intégrer avec les services de l'administration, notamment via l'ajout de fonctionnalités liées à Turgot.

### Évolutions fonctionnelles
- Ajout de filtres par date sur les listes de projets, simulations et programmation [#625].
- Possibilité de trier les colonnes de tableaux sur toutes les colonnes visibles [#624].
- Ajout de filtres par catégorie DETR/DSIL sur les listes de projets [#634].
- Ajout de filtres pour le budget vert, la dotation sollicitée et le dossier complet [#640].
- Affichage du nombre de projets notifiés au niveau des simulations [#619].
- Ajout de la colonne "Taux sollicité" dans l'export [#636].
- Possibilité de programmer les projets acceptés 2026 vers l'enveloppe 2025 [#654].
- Ajout de la civilité du porteur de projet [#630].
- Amélioration de la mise en page des arrêtés et lettres [#659].
- Correction de l'affichage des co-financements sur la page projet [#633].
- Correction de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Possibilité de fermer la modale « Vous ne faites pas partie du groupe d'instructeurs » [#690].
- Ajout d'une FAQ initiale [#672].
- Modification de statuts en masse sur la page de simulation [#661].
- Changement de statut en masse asynchrone pour les transitions impliquant Démarches Numériques [#677].
- Possibilité de fermer la modale « not instructor » [#682].
- Correction de l'ouverture de la modale "déjà en cours" après un démarrage en masse [#691].

### Évolutions techniques
- Refactoring de l'utilisation de `personne_morale` au lieu de `projet demandeur` [#646].
- Mise à jour de l'enveloppe lorsqu'on modifie les montants des projets acceptés [#674].
- Utilisation de `django-query-counter` pour le profiling des requêtes SQL [#671].
- Ajout de tests pour la tâche de nettoyage des projets programmés sur des enveloppes antérieures [#650].
- Amélioration de la performance de la page projet (BO) [#637].
- Refactoring du système de mentions de publipostage [#632].
- Ajout d'une commande `just release-dry-run` pour prévisualiser les releases [#680].
- Ajout de déploiement automatique sur l'environnement de démo [#653].
- Ajout de la gestion des erreurs GraphQL du proxy DS [#678].
- Correction de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Ajout de tests unitaires et d'intégration.
- Amélioration de la configuration CI/CD.
- Correction de bugs liés à la synchronisation des données avec Turgot.
- Optimisation des requêtes SQL pour améliorer les performances.
- Suppression des logs verbeux de fontTools en production [#684].
- Mise à jour des templates DGCL [#685].
- Suppression des URLs de login non utilisés [#623].
- Ajout d'un script pour sauvegarder le code source chiffré [#626].
- Correction de l'exécution des tests en parallèle avec pytest-xdist [#648].

### Autres changements
- Documentation mise à jour.
- Correction de typos et amélioration de la lisibilité du code.
- Suppression de code obsolète.
- Ajout de commentaires pour améliorer la compréhension du code.
- Correction de l'affichage du statut du projet dans l'onglet notifications [#655].
- Ajout de la librairie django-query-counter [#671].
- Ajout de filtres cofinancement, zonage et contractualisation [#642].
- Changement des titres des pages (Gestion des Subventions Locales -> Turgot) [#639].
- Ajout de la gestion des erreurs partielles dans le proxy DS [#683].
- Ajout de la gestion des nœuds nuls dans le proxy DS [#683].
- Ajout de la persistance de l'ordre de tri sur la page de simulation [#689].
- Ajout de la persistance de l'ordre de tri et des filtres sur la page de simulation [#689].
- Correction de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Ajout de la possibilité d'exécuter les tests sur les branches hotfix/* [#686].
- Correction de l'affichage des cofinancements sur la page projet [#633].
- Ajout de la gestion des erreurs GraphQL du proxy DS [#678].
- Ajout de la gestion des nœuds nuls dans le proxy DS [#683].
- Correction de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Ajout de la possibilité d'exécuter les tests sur les branches hotfix/* [#686].
- Correction de l'affichage des cofinancements sur la page projet [#633].
- Ajout de la gestion des erreurs GraphQL du proxy DS [#678].
- Ajout de la gestion des nœuds nuls dans le proxy DS [#683].
- Correction de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Ajout de la possibilité d'exécuter les tests sur les branches hotfix/* [#686].
- Correction de l'affichage des cofinancements sur la page projet [#633].
- Ajout de la gestion des erreurs GraphQL du proxy DS [#678].
- Ajout de la gestion des nœuds nuls dans le proxy DS [#683].
- Correction de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Ajout de la possibilité d'exécuter les tests sur les branches hotfix/* [#686].
- Correction de l'affichage des cofinancements sur la page projet [#633].
- Ajout de la gestion des erreurs GraphQL du proxy DS [#678].
- Ajout de la gestion des nœuds nuls dans le proxy DS [#683].
- Correction de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Ajout de la possibilité d'exécuter les tests sur les branches hotfix/* [#686].
- Correction de l'affichage des cofinancements sur la page projet [#633].
- Ajout de la gestion des erreurs GraphQL du proxy DS [#678].
- Ajout de la gestion des nœuds nuls dans le proxy DS [#683].
- Correction de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Ajout de la possibilité d'exécuter les tests sur les branches hotfix/* [#686].
- Correction de l'affichage des cofinancements sur la page projet [#633].
- Ajout de la gestion des erreurs GraphQL du proxy DS [#678].
- Ajout de la gestion des nœuds nuls dans le proxy DS [#683].
- Correction de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Ajout de la possibilité d'exécuter les tests sur les branches hotfix/* [#686].
- Correction de l'affichage des cofinancements sur la page projet [#633].
- Ajout de la gestion des erreurs GraphQL du proxy DS [#678].
- Ajout de la gestion des nœuds nuls dans le proxy DS [#683].
- Correction de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Ajout de la possibilité d'exécuter les tests sur les branches hotfix/* [#686].
- Correction de l'affichage des cofinancements sur la page projet [#633].
- Ajout de la gestion des erreurs GraphQL du proxy DS [#678].
- Ajout de la gestion des nœuds nuls dans le proxy DS [#683].
- Correction de l'URL du script HeatmapSessionRecording de Matomo [#687].
- Ajout de la possibilité d'exécuter les tests sur les branches hotfix/* [#686].
