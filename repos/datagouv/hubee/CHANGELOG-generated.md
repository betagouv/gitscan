## Changelog : hubee (30 derniers jours, au 28 septembre 2026)

### Résumé
Ce mois-ci, Hubee a considérablement amélioré la gestion des documents et la sécurité des accès. Les utilisateurs disposent désormais de fonctionnalités plus complètes pour manipuler les pièces jointes (téléchargement, archivage, consultation) et une navigation plus intuitive dans les dossiers. La sécurité a également été renforcée par l'introduction de l'authentification à deux facteurs (MFA) pour les comptes sensibles et une modernisation des protocoles d'échange.

### Évolutions fonctionnelles
- **Gestion des pièces jointes** : 
    - Possibilité de télécharger les pièces reçues [#163] et d'en consulter le contenu [#162].
    - Amélioration de la visibilité des types de fichiers et ajout de liens de téléchargement direct via DSFR.
    - Nouvelle fonctionnalité permettant de télécharger des archives regroupant les pièces reçues.
- **Gestion des dossiers (télédossiers)** :
    - Transition de la terminologie "démarches" vers "télédossiers" pour plus de clarté.
    - Amélioration de la recherche et du filtrage (recherche par numéro partiel, filtrage multi-flux et tri amélioré).
    - Nouvelles actions disponibles : accuser réception d'un nouveau dossier et faire avancer un dossier directement depuis sa page de détail.
- **Sécurité et accès** :
    - Renforcement de la sécurité avec l'exigence du second facteur (MFA) pour les comptes à privilèges.
    - Amélioration de la visibilité des droits d'accès et de l'identité de l'agent connecté.

### Évolutions techniques
- **Sécurité et API** :
    - Mise en place du socle OAuth2 (client credentials) et protection des endpoints par token.
    - Montée en version majeure et itérative de la dépendance `hub-api-v1` (passage aux versions 3, 4 et 5).
    - Transition vers le protocole OIDC pour les échanges avec ProConnect.
- **Architecture et Infrastructure** :
    - Migration des images de runtime Docker vers une base *distroless* pour renforcer la sécurité.
    - Refactorisation importante du portail via l'utilisation de patterns "Organizer" pour la gestion des listes et des détails de dossiers.
    - Optimisation de la gestion des sessions et de la traçabilité des événements.
- **CI/CD** :
    - Mise en place et correction du système de "review apps" pour les tests de Pull Requests.

### Autres changements
- **Documentation** : 
    - Rédaction de nouveaux guides (runbooks) pour l'utilisation de l'API.
    - Amélioration de la documentation technique concernant la lecture des démarches et la couche d'authentification.
