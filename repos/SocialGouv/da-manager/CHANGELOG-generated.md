## Changelog : da-manager (30 derniers jours)

### Résumé
Ce changelog couvre une période d'intense développement pour da-manager. L'équipe a mis en place les fondations pour le déploiement continu (CI/CD), amélioré l'automatisation avec l'intégration de Claude pour la gestion des pull requests, et ajouté de nombreuses fonctionnalités d'interface utilisateur, notamment la gestion des utilisateurs, l'exportation en PDF, et l'amélioration de l'expérience d'édition de schémas.  Des corrections de bugs et des améliorations de la structure du projet ont également été apportées.

### Évolutions fonctionnelles
- Ajout d'un footer à l'application (#5).
- Renommage de "da" (Document d'Architecture) (#5).
- Ajout de la fonctionnalité d'exportation en PDF.
- Ajout d'une page de gestion des utilisateurs avec la possibilité d'attribuer des rôles.
- Ajout d'une page pour créer de nouveaux documents d'architecture.
- Amélioration de la liste des documents d'architecture.
- Ajout d'une fonctionnalité de sauvegarde et de chargement de schémas.
- Ajout d'un menu de pas (stepper) pour guider l'utilisateur.
- Ajout de la possibilité de passer en mode plein écran pour Excalidraw.
- Correction de problèmes d'affichage en mode sombre.
- Correction de problèmes d'URL d'authentification.

### Évolutions techniques
- Mise en place d'un workflow CI/CD complet avec des checks de déploiement et des workflows pour les environnements de production et de pré-production.
- Intégration de Claude pour l'automatisation de la création de pull requests et la gestion des commentaires.
- Ajout de workflows GitHub pour la désactivation, la pré-production, la production et la publication.
- Configuration de l'outil Kontinuous.
- Utilisation de tokenbureau pour l'authentification.
- Ajout de tests unitaires avec Vitest (#3).
- Refonte de l'authentification avec NextAuth.
- Mise à jour de la configuration Dockerfile.
- Ajout de secrets pour la configuration de l'application.

### Autres changements
- Ajout d'un favicon.
- Ajout de prettier pour le formatage du code.
- Ajout d'un fichier `claude.md` pour la documentation de l'intégration de Claude.
- Suppression des composants React DSFR et chargement de la version vanilla.
- Suppression du bouton de suppression d'utilisateur.
- Amélioration de la liste des administrateurs.
- Ajout de valeurs factices pour les tests.
- Correction de styles divers (menu, couleurs, outline, etc.).
- Ajout de commentaires et de logs pour faciliter le débogage.
- Initialisation du projet avec Create Next App.
