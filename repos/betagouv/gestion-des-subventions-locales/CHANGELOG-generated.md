## Changelog : gestion-des-subventions-locales (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans la gestion des notifications, la recherche et le filtrage des dossiers, ainsi que sur des optimisations techniques pour la performance et la robustesse de l'application. Des corrections de bugs et des améliorations de la documentation ont également été apportées.

### Évolutions fonctionnelles
- **Notifications :**
    - Amélioration de la génération multiple de documents de notification, avec une interface modale plus conviviale et conforme aux maquettes Figma [#729].
    - Possibilité de générer à la fois des arrêtés et des lettres de notification en une seule opération.
    - Possibilité de choisir le format d'export des documents (arrêté, lettre, les deux).
    - Ajout d'une stratégie de remplacement des documents existants.
    - Rendre le QR code de suivi optionnel sur les documents générés [#720].
    - Découplage de la notification de refus/classement du changement de statut [#719].
    - Possibilité d'envoyer des alertes email aux administrateurs en cas d'actions sensibles sur l'application [#730].
- **Recherche et Filtrage :**
    - Recherche de dossiers par sous-chaîne du numéro de dossier [#728].
    - Ajout de filtres de recherche sur les listes de projets, simulations et programmations [#701].
    - Amélioration de la recherche avec prise en compte de l'intitulé, de la raison sociale et du numéro de dossier.
    - Réordonnement du champ de recherche dans les filtres de listes [#702].
- **Interface Utilisateur :**
    - Amélioration du formatage de l'adresse du demandeur dans les documents [#718].
    - Correction de l'ouverture du dropdown de statut dans la page projet pour éviter de casser les colonnes stickies [#717].
    - Ajout d'en-têtes de colonnes fixes (sticky) dans les listes de projets, simulations et programmations [#704].
    - Autorisation des tabulations dans les arrêtés/lettres de notification [#705].
- **Autres :**
    - Possibilité de changer le statut de dossiers en lot vers "refusé" ou "classé sans suite" [#726].
    - Action sur le back-office pour récupérer un dossier depuis DN [#696].

### Évolutions techniques
- **Architecture & Refactoring :**
    - Découpage du document GraphQL monolithique en documents par opération pour une meilleure maintenabilité [#721, #723].
    - Refactorisation du code pour utiliser `.active()` au lieu de `Active*Manager` pour les requêtes sur les dossiers actifs [#726].
    - Extraction des helpers de page dans la fonction `save_demarche_dossiers_from_ds` pour une meilleure organisation du code.
    - Suppression des pages d'administration sur l'application [#727].
- **Performance :**
    - Optimisation de la génération d'arrêtés/lettres en masse [#714].
    - Allègement de la requête GraphQL vers DN pour limiter les timeouts liés aux `GroupeInstructeur` [#691].
    - Évaluation paresseuse des choix dans les FilterSet pour améliorer la performance des filtres [#703].
- **Infrastructure & CI/CD :**
    - Mise à jour des dépendances vulnérables signalées par Dependabot [#710].
    - Introduction d'un AGENTS.md pour guider les agents de code [#715].
    - Documentation : usage des branches hotfix pour le déploiement par tag [#722].
    - Alignement des lock files et garde-fou CI contre la dérive [#713].
- **Sécurité :**
    - Restriction des champs Demarche et filtrage des dossiers supprimés dans le proxy DS [#692].
    - Restriction du scope des tokens du proxy DS au groupe instructeur plutôt qu'à la liste des instructeurs [#723].

### Autres changements
- Correction de bugs divers et amélioration de la FAQ [#707].
- Amélioration de la gestion des erreurs lors de la sauvegarde des curseurs depuis DN [#724].
- Correction de l'affichage des documents de l'autre dotation dans l'onglet Programmation [#694].
- Correction de l'affichage de la date de notification [#695].
- Correction pour permettre aux utilisateurs DN de mettre à jour leur adresse email [#700].
- Renommage de "Arrêté et lettre signés" en "Lettre et arrêté signés" [#693].
