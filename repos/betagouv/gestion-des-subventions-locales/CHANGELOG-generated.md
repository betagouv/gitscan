## Changelog : gestion-des-subventions-locales (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de l'import de documents, de la gestion des statuts des projets et de la génération de documents. Des optimisations techniques ont également été apportées pour améliorer la performance et la robustesse de l'application, ainsi que la gestion des erreurs.

### Évolutions fonctionnelles
- **Import de documents :** Amélioration significative de l'import de documents signés scannés, avec la possibilité de télécharger directement via S3 et un suivi de la progression pour chaque fichier. Import possible de dossiers de tous les territoires gérés.
- **Gestion des statuts :** Possibilité de modifier en masse le statut des projets vers "refusé" ou "classé sans suite".
- **Notifications :**
    - Possibilité de personnaliser le nom du fichier PDF lors de la génération de notifications d'acceptation.
    - Découplage de la notification de refus/classement du changement de statut.
    - Ajout d'un QR code optionnel sur les documents générés pour faciliter le rattachement des scans signés.
- **Interface utilisateur :**
    - Masquage de la colonne d'actions sur les pages de programmation et de simulation pour une meilleure clarté.
    - Amélioration de l'affichage du tableau des enveloppes.
    - Réduction de la taille du header et du footer.
    - Correction du dropdown de sélection de statut dans la page projet.
    - Correction du décochage silencieux des filtres de type ModelMultipleChoiceFilter.
    - Amélioration du formatage de l'adresse du demandeur dans les documents.
- **Navigation :** Création d'une entrée de menu dédiée pour les modèles de publipostage.
- **Recherche :** Possibilité de rechercher un dossier par sous-chaîne de son numéro.
- **Admin :**
    - Journalisation des modifications des utilisateurs via l'admin Django.
    - Affichage du périmètre, des dates Turgot et du statut du report dans l'admin.

### Évolutions techniques
- **Performance :** Priorisation des tâches Celery en fonction du contexte d'appel.
- **Refactoring :**
    - Unification de la page de détail d'un projet, pilotée par son état.
    - Remplacement des FBV de détail de projet par une base DetailView.
    - Découpage du document GraphQL monolithique en documents par opération.
    - Extraction des helpers de pagination dans la fonction `save_demarche_dossiers_from_ds`.
    - Remplacement des `Active*Manager` par des méthodes `queryset .active()`.
- **Sécurité :**
    - Limitation de la portée des tokens du proxy DS au groupe instructeur.
    - Alertes email aux administrateurs sur les actions sensibles.
- **Infrastructure :**
    - Verrou anti-concurrence sur la synchronisation des dossiers DS avec Redis.
    - Mise à jour des dépendances vulnérables signalées par Dependabot.
- **Tests :** Correction d'un test flaky lié à la génération d'emails.

### Autres changements
- Ajout d'un fichier `AGENTS.md` pour guider les agents de code.
- Documentation sur l'utilisation des branches hotfix pour le déploiement par tag.
- Correction d'erreurs de manifest staticfiles.
- Cache-busting des fichiers JS de l'importmap.
- Suppression des rafraîchissements DS bloquants à l'ouverture des modales.
- Correction de la perte du curseur des dossiers supprimés sur les pages vides.
- Autorisation des tabulations dans les arrêtés/lettres de notification.
- Correctifs de la FAQ.
