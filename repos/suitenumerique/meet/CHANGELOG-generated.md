## Changelog : meet (30 derniers jours, au 06/08/2026)

### Résumé
Les récentes évolutions se concentrent sur une meilleure maîtrise des réunions par les utilisateurs, notamment via la gestion des rôles et la personnalisation des paramètres par défaut. Un nouvel outil de test de connexion a été introduit pour faciliter le diagnostic technique. Parallèlement, un travail important de refactorisation et d'optimisation a été mené pour rendre l'interface plus fluide et réactive.

### Évolutions fonctionnelles
- **Gestion des réunions et paramètres** :
    - Introduction d'une fenêtre de configuration lors de la création d'une réunion.
    - Possibilité pour les utilisateurs de définir des configurations par défaut pour leurs liens de réunion générés.
    - Personnalisation de la couleur d'arrière-plan de l'iframe du calendrier via le SDK.
- **Gestion des participants** :
    - Possibilité de promouvoir ou de rétrograder des participants authentifiés en cours de réunion.
    - Ajout de badges pour identifier les participants non authentifiés.
    - Notifications automatiques lorsqu'un utilisateur voit son rôle changer.
- **Nouvelles fonctionnalités et UX** :
    - Ajout d'un outil de test de connexion pour vérifier la qualité de l'environnement avant ou pendant un appel.
    - Amélioration de l'affichage des avatars (gestion des initiales en majuscules et support de l'Unicode).
    - Améliorations visuelles : affichage du curseur de type "pointer" sur les éléments interactifs et correction de l'alignement des icônes.
- **Corrections** :
    - Résolution d'un crash lié à une incompatibilité de version MediaPipe WASM.
    - Correction du comportement de l'application installée qui réouvrait indûment les anciennes sessions.

### Évolutions techniques
- **Performances et fluidité** :
    - Optimisation massive du rendu de l'interface pour réduire les re-renders inutiles, notamment sur la liste des participants et les composants de mise en page.
    - Virtualisation des messages du chat pour limiter la taille du DOM et améliorer la réactivité.
- **Backend et API** :
    - Création de nouveaux endpoints pour le test de connexion et la mise à jour des rôles des participants.
    - Amélioration de la sécurité et de la gestion des sessions en intégrant les informations d'authentification et de rôle directement dans les tokens LiveKit.
    - Renommage du service de téléphonie en `SIPManagement`.
- **Architecture et Refactoring** :
    - Refactorisation majeure du système de chat et restructuration des composants de la liste des participants pour une meilleure maintenance.
    - Optimisation de la gestion des assets MediaPipe (chemins versionnés et configuration du cache).
- **CI/CD et Développement** :
    - Nettoyage des étapes de sécurité inutiles dans la CI et optimisation des workflows de linting.

### Autres changements
- **Légal et Documentation** : Mise à jour des conditions générales d'utilisation et ajout de liens de documentation configurables.
- **Métadonnées** : Ajout du fichier `publiccode.yml` et de notes de version pour les PR importantes (ex: [#1510](https://github.com/suitenumerique/meet/pull/1510)).
- **Qualité de code** : Nettoyage de la dette technique liée au linting et résolution des alertes de fiabilité SonarCloud.
