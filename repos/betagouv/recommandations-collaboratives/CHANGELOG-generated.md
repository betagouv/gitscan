## Changelog : recommandations-collaboratives (30 derniers jours, au 24 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'expérience utilisateur dans les conversations, notamment avec l'ajout de fonctionnalités pour la gestion des fichiers, l'amélioration de l'affichage des documents et la correction de bugs liés à l'affichage et à la manipulation des informations. Des améliorations ont également été apportées à la gestion des communes et des recommandations, ainsi qu'à la sécurité et à la maintenance technique du projet.

### Évolutions fonctionnelles
- **Conversations :**
    - Ajout d'une fonctionnalité permettant d'ouvrir le panneau de brouillon lors de la création d'une recommandation à partir d'une conversation.
    - Amélioration de l'accessibilité des panneaux de ressources et de contenus partagés avec des rôles ARIA.
    - Ajout de surcouches (backdrops) aux panneaux de ressources et de contenus partagés, permettant de les fermer en cliquant en dehors.
    - Possibilité de publier une recommandation à partir d'une route spécifique, avec affichage d'un message de confirmation.
    - Amélioration de l'affichage des documents dans les conversations, avec ajout du titre.
    - Ajout d'une section pour les démarches numériques (DN) dans les cartes de recommandation.
    - Gestion des fichiers : amélioration de l'upload de fichiers, affichage des fichiers privés, et comptage des fichiers externes.
- **Gestion des communes :**
    - Amélioration du script de gestion des communes pour créer, mettre à jour et supprimer les communes en fonction des données de La Poste, corrigeant ainsi des problèmes de données manquantes.
- **Recommandations :**
    - Ajout de liens vers les conversations depuis les recommandations.
    - Amélioration de l'affichage des informations des invitations.
- **Autres :**
    - Correction d'un bug empêchant la fusion correcte des organisations.
    - Possibilité de masquer l'onglet "Recommandations".
    - Correction d'un problème d'affichage des ressources publiques.
    - Amélioration de la validation et de l'affichage des formulaires d'invitation (mot de passe, numéro de téléphone).

### Évolutions techniques
- **Refactoring :**
    - Refactorisation du code lié aux tâches et aux conversations pour améliorer la performance et la lisibilité.
    - Suppression de code mort et de conditions inutiles.
- **Dépendances :**
    - Mise à jour de plusieurs dépendances : Django (5.2.13), uv, lxml, nbconvert, cryptography, dompurify, axios, lodash, pytest, pillow, pygments.
- **Infrastructure :**
    - Mise à jour de la configuration de Vite.
    - Amélioration de la gestion des erreurs et de la performance dans les conversations.
    - Utilisation de `Alpine.store` pour un accès plus efficace aux données dans les composants Alpine.js.
- **Tests :**
    - Mise à jour des tests pour refléter les nouvelles fonctionnalités et corrections de bugs.
    - Ajout de tests pour les traces de rappel (reminders).

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés.
- Nettoyage du code et amélioration de la structure du projet.
- Correction de problèmes de sanitisation des données pour améliorer la sécurité.
- Mise à jour des URLs de la documentation pour les administrateurs et les conseillers.
- Suppression de références obsolètes à `dsFolder`.
- Amélioration de la gestion des migrations de base de données.
- Ajout de commentaires et de documentation pour faciliter la maintenance du code.
