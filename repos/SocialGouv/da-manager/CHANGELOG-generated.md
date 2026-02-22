## Changelog : da-manager (30 derniers jours)

### Résumé
Le projet da-manager a connu une période d'activité intense ces 30 derniers jours, principalement axée sur la mise en place d'une infrastructure CI/CD robuste avec l'intégration de Claude pour l'automatisation des revues de code et la gestion des pull requests.  De nombreuses améliorations ont également été apportées à l'interface utilisateur, notamment l'ajout de nouveaux composants, l'amélioration de l'expérience utilisateur et la correction de bugs visuels.  Enfin, les fondations pour la gestion des utilisateurs et l'authentification ont été posées.

### Évolutions fonctionnelles
- Ajout d'un footer à l'application (#5).
- Ajout d'une page pour la gestion des utilisateurs.
- Ajout d'une liste d'utilisateurs avec la possibilité de basculer leur rôle.
- Ajout d'une fonctionnalité de création automatique de pull requests.
- Ajout de la possibilité de créer des documents d'architecture.
- Ajout de la fonctionnalité d'exportation en PDF.
- Ajout de la fonctionnalité d'édition de schémas.
- Amélioration de la liste des documents d'architecture.
- Amélioration de la popup de création de documents d'architecture.
- Correction de problèmes d'affichage en mode sombre.
- Correction de problèmes d'URL d'authentification.
- Correction de bugs concernant l'affichage des cadres 2, 3, 4, 11 et 12.
- Correction de problèmes d'outline sur les inputs des tableaux.
- Correction de problèmes d'affichage du stepper.
- Correction de problèmes d'affichage en plein écran.

### Évolutions techniques
- Mise en place d'un workflow CI/CD complet avec l'intégration de Claude pour la revue de code et la gestion des pull requests.
- Ajout de workflows pour les environnements de production et de pré-production.
- Ajout d'un workflow pour la désactivation des pull requests.
- Ajout de tests unitaires avec Vitest.
- Suppression des composants React DSFR et chargement de la version vanilla.
- Mise à jour de la configuration Dockerfile.
- Ajout de secrets pour la configuration de l'application.
- Ajout de la gestion des versions.
- Ajout de l'outil de linting Prettier.
- Utilisation de Tokenbureau pour l'authentification.
- Ajout de la librairie Kontinuous.

### Autres changements
- Ajout d'un favicon.
- Ajout de la documentation pour l'utilisation de Claude.
- Ajout de commentaires et de logs pour faciliter le débogage.
- Suppression de la suppression des utilisateurs.
- Ajout de valeurs factices pour les tests.
- Ajout d'une configuration Oblik.
- Suppression du code inutile.
- Amélioration de la structure du code.
- Ajout de la gestion des couleurs pour les rôles utilisateurs.
- Ajout de la possibilité d'ajouter des utilisateurs factices.
- Ajout d'un menu latéral.
- Ajout d'une mise en page PDF.
- Ajout d'une page utilisateur.
- Ajout de liens dans les tableaux.
- Ajout de toggles pour les rôles utilisateurs.
- Ajout de la gestion des migrations de la base de données.
- Ajout d'un composant textarea.
- Ajout d'une image rootless.
- Modification de la cible du projet Fabrique.
- Modification des valeurs par défaut.
- Ajout d'un composant hero.
- Ajout d'un header.
- Ajout de la possibilité d'afficher les schémas en plein écran.
- Ajout de la gestion des noms uniques.
