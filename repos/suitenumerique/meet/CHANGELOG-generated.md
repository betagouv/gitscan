## Changelog : meet (30 derniers jours, au 25 août 2026)

### Résumé
Ce mois-ci, meet a franchi une étape importante dans la gestion des réunions et l'expérience utilisateur mobile. Les utilisateurs bénéficient désormais de fonctionnalités de gestion de rôles en direct (promotion/rétrogradation de participants) et d'outils de diagnostic audio et de connexion plus performants. L'interface a été considérablement optimisée pour les appareils mobiles et la stabilité globale a été renforcée par des optimisations techniques majeures.

### Évolutions fonctionnelles
- **Gestion des participants et des réunions** :
    - Possibilité de promouvoir ou de rétrograder des participants directement pendant une réunion.
    - Les utilisateurs authentifiés peuvent désormais gérer le lobby dans les salles de confiance.
    - Introduction de badges pour identifier les participants non authentifiés.
    - Notification automatique des utilisateurs lors d'un changement de leur rôle dans la réunion.
    - Possibilité de définir des configurations par défaut pour les liens de réunion générés.
- **Expérience Mobile** :
    - Optimisation de l'interface pour les petits écrans : barre de contrôle repliable, boutons empilés verticalement et écran de feedback plus réactif.
    - Amélioration de l'affichage des éléments de contrôle sur les vues étroites.
- **Diagnostic et aide à l'utilisateur** :
    - Ajout d'un outil de test de connexion et de tests audio (jauge de microphone et test de haut-parleur).
    - Amélioration de l'accompagnement des utilisateurs lorsque le système d'exploitation bloque l'accès à la caméra ou au micro.
    - Meilleure gestion et communication des erreurs liées aux périphériques (caméra/micro déjà utilisés).
- **Interface Utilisateur (UI)** :
    - Amélioration visuelle des avatars (affichage de deux initiales en majuscules, centrage optimisé).
    - Affichage de l'identifiant de la réunion dans le titre de la page de jonction.

### Évolutions techniques
- **Optimisation des performances** :
    - Remplacement des commandes Redis bloquantes (`KEYS`) par une méthode basée sur les curseurs (`SCAN`) pour une meilleure scalabilité.
    - Réduction des re-rendus de l'interface (React) sur les composants critiques comme les tuiles de participants et les mises en page.
    - Application de contraintes de ressources ("frugal constraint") sur la piste audio active pour optimiser la consommation.
- **Architecture et Backend** :
    - Refactorisation de la gestion de la télémétrie pour encapsuler les appels PostHog.
    - Amélioration de la sécurité et de la gestion des permissions via l'intégration des rôles et de l'état d'authentification directement dans les tokens LiveKit.
    - Modularisation du code frontend (extraction de la logique du lobby et des sous-composants de participants).
    - Support du format `form-urlencoded` pour l'endpoint de jeton utilisateur.
- **Infrastructure et CI/CD** :
    - Optimisation du workflow de linting et nettoyage de la dette technique (SonarCloud).
    - Mise à jour de l'image Node pour les services d'envoi de mails.

### Autres changements
- **Documentation et Légal** : Mise à jour des conditions d'utilisation et correction de la documentation technique.
- **Maintenance et Conformité** : Ajout du fichier `publiccode.yml` et nettoyage de code (suppression de fonctions et de variables inutilisées).
