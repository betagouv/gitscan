## Changelog : recommandations-collaboratives (30 derniers jours, au 24 avril 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de l'expérience utilisateur, notamment au niveau de la gestion des conversations, des documents et des recommandations. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des mises à jour de l'infrastructure et des dépendances.

### Évolutions fonctionnelles
- **Conversations :**
    - Ajout d'un lien direct vers la conversation avec le panneau d'action ouvert depuis l'ancienne page d'action [#2076](https://github.com/betagouv/recommandations-collaboratives/pull/2076).
    - Possibilité de suggérer des ressources dans une conversation.
    - Amélioration de l'accessibilité des panneaux de ressources et de contenu partagé avec des rôles ARIA.
    - Ajout de superpositions (backdrops) aux panneaux de ressources et de contenu partagé, permettant de les fermer en cliquant à l'extérieur.
    - Publication de recommandations brouillon avec gestion des erreurs et mise à jour du nombre de brouillons.
    - Amélioration de la gestion du chargement et de l'affichage des fichiers privés dans le panneau de contenu partagé.
- **Documents :**
    - Amélioration de l'affichage des cartes de documents avec le titre.
    - Possibilité de télécharger des documents traditionnels avec envoi d'un message.
    - Correction d'un bug empêchant l'accès aux documents privés par les collaborateurs.
    - Ajout d'un identifiant unique (hash) lors de la navigation vers les détails d'une recommandation pour éviter des problèmes de cache [#2071](https://github.com/betagouv/recommandations-collaboratives/pull/2071).
- **Tâches :**
    - Amélioration de la gestion des tâches et des statuts dans les conversations.
    - Correction d'un bug lié à la redirection après la suppression d'une tâche.
- **Gestion des Communes :**
    - Amélioration des scripts de gestion des communes pour créer, mettre à jour et supprimer les communes en fonction du fichier LaPoste, corrigeant ainsi les données manquantes [#2067](https://github.com/betagouv/recommandations-collaboratives/pull/2067).
- **Invitations :**
    - Ajout d'informations supplémentaires lors de l'acceptation d'une invitation [#2013](https://github.com/betagouv/recommandations-collaboratives/pull/2013).
    - Ajout d'un formulaire d'acceptation d'invitation avec mot de passe et email.
    - Amélioration de la validation du numéro de téléphone et de l'espacement du formulaire.
- **Ressources :**
    - Ajout d'un indicateur de brouillon aux ressources.
    - Amélioration de l'affichage des ressources publiques.

### Évolutions techniques
- **Refactoring :**
    - Refactorisation du code pour améliorer la lisibilité et la maintenabilité.
    - Suppression de code mort.
    - Remplacement de `formatDateFrench` par `formatDate` pour une cohérence accrue.
    - Utilisation d'Alpine.store pour un accès plus efficace aux données dans les composants.
- **Infrastructure :**
    - Mise à jour de Django en version 5.2.13.
    - Mise à jour de plusieurs dépendances (uv, cryptography, pillow, pytest, lodash, axios, dompurify, nbconvert, lxml).
    - Synchronisation des fichiers `requirements.txt` générés par `uv`.
- **Tests :**
    - Mise à jour des tests pour refléter les nouveaux comportements et fonctionnalités de la gestion des communes.
    - Adaptation des tests à la nouvelle syntaxe ORM.

### Autres changements
- Nettoyage du code et des commentaires.
- Correction de problèmes de sanitisation des données pour éviter les failles XSS.
- Mise à jour de la documentation.
- Suppression de références obsolètes à `dsFolder`.
- Ajout d'un identifiant unique (hash) aux liens des démarches numériques.
- Correction de typos et amélioration de la clarté du code.
- Suppression de conditions inutiles.
- Amélioration de la gestion des erreurs.
- Ajout de commentaires pour clarifier le code.
- Mise à jour des liens vers la documentation.
- Amélioration de la gestion des URL.
- Ajout de tests unitaires.
- Mise à jour des fichiers `.gitignore`.
- Suppression de code obsolète.
- Amélioration de la gestion des migrations de base de données.
- Ajout de traces pour les rappels (reminders) dans le CRM.
- Correction de bugs mineurs.
