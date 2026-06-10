## Changelog : gestion-des-subventions-locales (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des documents (génération en masse, téléchargement, formats) et la recherche de dossiers. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. L'administration et la gestion des utilisateurs ont également été améliorées.

### Évolutions fonctionnelles
- **Gestion des documents :**
    - Ajout d'une entrée de menu dédiée au publipostage des modèles de documents.
    - Possibilité de générer des arrêtés et des lettres en masse dans une modale, avec choix du format d'export.
    - Amélioration du parcours de génération de documents en masse, avec la possibilité de choisir le format de fichier et de gérer les erreurs.
    - Possibilité d'ajouter un QR code de suivi optionnel sur les documents générés.
    - Prise en charge des tabulations dans les arrêtés et lettres de notification.
- **Recherche et filtrage :**
    - Ajout d'un filtre de recherche sur les listes de projets, simulations et programmations (intitulé, raison sociale, numéro de dossier).
    - Amélioration du réordonnement du champ de recherche dans les filtres de listes.
    - Possibilité de rechercher par sous-chaîne du numéro de dossier.
- **Administration :**
    - Journalisation des modifications des utilisateurs via l'admin Django.
    - Possibilité de bloquer/débloquer des utilisateurs via l'admin.
    - Affichage du périmètre, des dates Turgot et du statut du report dans l'admin.
- **Import de données :**
    - Possibilité d'importer des dossiers de tous les territoires gérés.
    - Import en masse des documents signés scannés via un upload direct S3.
    - Fusion des documents signés lors de l'import.
- **Simulation :**
    - Mise à jour des badges des simulations.
    - Possibilité de mettre à jour en masse le statut des simulations vers "refusé" ou "classé sans suite".
- **Notifications :**
    - Nommage du fichier PDF lors de la notification d'acceptation.
    - Possibilité de personnaliser le nom du fichier PDF lors de la notification d'acceptation.

### Évolutions techniques
- **Architecture et performance :**
    - Optimisation de la génération d'arrêtés/lettres en masse.
    - Amélioration de la performance des filtres avec une évaluation paresseuse des choix.
    - Suppression des rafraîchissements DS bloquants à l'ouverture des modales.
    - Mise en place d'un verrou anti-concurrence sur la synchronisation des dossiers DS.
    - Refactorisation du code GraphQL pour une meilleure organisation.
- **Infrastructure et CI/CD :**
    - Mise à jour des dépendances vulnérables signalées par Dependabot.
    - Correction d'erreurs de manifest staticfiles sur l'importmap.
    - Cache-busting des fichiers JS de l'importmap.
- **Code :**
    - Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
    - Utilisation de `{% static %}` pour le cache-busting des fichiers statiques.
    - Amélioration de la gestion des erreurs.
    - Correction de tests flaky.

### Autres changements
- Documentation : Ajout d'un fichier `AGENTS.md` pour guider les agents de code et documentation sur l'utilisation des branches hotfix pour le déploiement par tag.
- FAQ : Corrections et améliorations de la FAQ.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de logs structurés sur le proxy DS.
- Amélioration de l'affichage du tableau des enveloppes et masquage de la colonne d'actions sur certaines pages.
- Suppression des pages d'administration sur l'application.
- Correction du décochage silencieux des filtres de type ModelMultipleChoiceFilter.
- Ajout de titres de colonnes visibles au scroll dans les listes.
- Correction de la perte du curseur des dossiers supprimés sur les pages vides.
- Correction d'un bug empêchant la modification de l'adresse email des utilisateurs DN.
- Ajout d'une action sur le BO pour récupérer un dossier depuis DN.
