## Changelog : gestion-des-subventions-locales (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des notifications, notamment la génération de documents en masse, et l'optimisation de la synchronisation des données avec DN (Données Nationales). Des améliorations ont également été apportées à l'expérience utilisateur, avec l'ajout de filtres de recherche et l'amélioration de la navigation dans les listes de dossiers. Enfin, des corrections de bugs et des optimisations techniques ont été réalisées pour améliorer la stabilité et la performance de l'application.

### Évolutions fonctionnelles
- **Notifications :** Possibilité de générer plusieurs documents (arrêtés et lettres) simultanément depuis une modale dédiée. Le nom des fichiers générés est désormais personnalisable et respecte les caractères valides.
- **Notifications :** Amélioration de la gestion des erreurs lors de la génération de documents.
- **Recherche :** Ajout d'un filtre de recherche sur les listes de projets, simulations et programmations, permettant de rechercher par intitulé, raison sociale et numéro de dossier.
- **Filtres :** Correction du décochage silencieux des filtres de type `ModelMultipleChoiceFilter`.
- **Filtres :** Amélioration de l'ordre du champ de recherche après l'utilisation du bouton "Réinitialiser les filtres".
- **Interface utilisateur :** Les titres de colonnes restent visibles lors du défilement dans les listes de projets, simulations et programmations.
- **DN :** Possibilité pour les utilisateurs de DN de mettre à jour leur adresse email.
- **DN :** Ajout d'une action dans le back-office pour récupérer un dossier depuis DN.
- **Adresse :** Amélioration du formatage de l'adresse du demandeur dans les documents.

### Évolutions techniques
- **Synchronisation DS :** Ajout d'un verrou (Redis lock) pour empêcher les synchronisations concurrentes de dossiers DS, améliorant ainsi la stabilité.
- **Historique :** Traçabilité des actions significatives sur les projets.
- **GraphQL :** Découpage du document GraphQL monolithique en fichiers par opération pour une meilleure organisation et maintenabilité.
- **Tests :** Correction d'un test flaky lié à la génération d'emails pour les collègues.
- **Code :** Refactorisation du code pour améliorer la lisibilité et la maintenabilité, notamment dans la gestion des statuts et des filtres.
- **Déploiement :** Documentation sur l'utilisation des branches hotfix pour le déploiement par tag.
- **Sécurité :** Mise à jour des dépendances vulnérables signalées par Dependabot.
- **Architecture :** Utilisation de managers `.active()` pour simplifier les requêtes et améliorer la performance.

### Autres changements
- **Documentation :** Introduction d'un fichier `AGENTS.md` pour guider les agents de code.
- **FAQ :** Correction de la FAQ.
- **Tableaux TipTap :** Amélioration de la gestion des tableaux dans l'éditeur TipTap pour l'export PDF.
- **QR Code :** Possibilité de rendre le QR code de suivi optionnel sur les documents générés.
- **Gestion des statuts :** Possibilité de changer le statut de plusieurs projets en "refusé" ou "classé sans suite" en lot.
- **Fichiers de configuration :** Alignement des fichiers de lock et ajout d'un garde-fou CI contre la dérive.
