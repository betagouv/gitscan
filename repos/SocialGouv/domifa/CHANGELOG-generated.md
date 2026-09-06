## Changelog : domifa (30 derniers jours, au 05/09/2026)

### Résumé
Ce mois a été marqué par une amélioration significative de l'expérience utilisateur et de la sécurité de la plateforme. Les utilisateurs bénéficient de nouvelles fonctionnalités comme l'ajout d'un kit de communication dans la FAQ et une gestion simplifiée de leurs adresses email. Parallèlement, la plateforme a gagné en robustesse grâce à des optimisations techniques majeures sur les processus d'importation de données et une meilleure gestion des déploiements pour garantir une disponibilité continue.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités** :
    - Ajout d'un onglet "Kit de communication" dans la section FAQ [#4261](https://github.com/SocialGouv/domifa/pull/4261).
    - Mise en place d'un nouveau formulaire de contact pour le support.
    - Possibilité pour les structures de modifier leurs propres adresses email de manière sécurisée.
    - Ajout de nouvelles statistiques disponibles sur le portail.
    - Notification automatique des utilisateurs lors de la suppression d'un compte.
- **Améliorations de l'expérience utilisateur (UX/UI)** :
    - Optimisation du parcours de connexion : les membres des rôles DGCS, DDETS et DREETS sont désormais redirigés directement vers le portail de pilotage.
    - Mise à jour de la navigation : le lien "Admin" a été remplacé par "Pilotage" dans la barre de menu.
    - Amélioration du processus de sécurité OTP (code à usage unique) avec l'ajout d'un compte à rebours et de consignes plus claires.
    - Diverses corrections d'affichage sur l'accueil, les actualités, les témoignages et les résultats de recherche.
- **Sécurité et accès** :
    - Renforcement du processus de mise à jour des adresses email.
    - Affinement des règles d'accès pour le flag du portail superviseur.

### Évolutions techniques
- **Performance et stabilité du backend** :
    - Optimisation du processus d'importation de données via l'utilisation de *worker threads* pour éviter le blocage de l'event loop.
    - Amélioration de la gestion de la concurrence et du nettoyage des fichiers lors des téléchargements (uploads).
    - Renforcement de la sécurité des données par l'application systématique de la validation et de la sanitization des DTO.
- **Infrastructure et CI/CD** :
    - Amélioration de la CI/CD pour détecter les pods backend figés et garantir des déploiements sans interruption de service (*zero-downtime*).
    - Routage des requêtes d'importation vers des pods dédiés (`backend-export`) pour isoler la charge [#4249](https://github.com/SocialGouv/domifa/pull/4249).
    - Intégration du fichier `robots.txt` dans les builds des portails administrateur et statistiques.
- **Base de données et maintenance** :
    - Exécution de plusieurs migrations de base de données, notamment pour la gestion des utilisateurs sans mise à jour récente de mot de passe [#4241](https://github.com/SocialGouv/domifa/pull/4241).
    - Suppression de la documentation Swagger pour alléger le backend.
- **Tests** :
    - Amélioration et clarification des suites de tests unitaires et d'intégration sur le backend.

### Autres changements
- Refactorisation de composants frontend (notamment la gestion de l'affichage des grands nombres).
- Nettoyage de migrations de base de données inutiles.
