## Changelog : messages (30 derniers jours, au 06/08/2026)

### Résumé
Cette période est marquée par le passage en version 0.9.0, qui introduit une étape majeure : le support des applications mobiles (iOS et Android) avec un système de notifications push. La plateforme renforce également sa sécurité, notamment sur le traitement des emails et l'authentification, tout en améliorant la fluidité de l'interface utilisateur.

### Évolutions fonctionnelles
- **Support Mobile :** Disponibilité des applications mobiles (iOS/Android) et mise en place d'un système de notifications push (iOS, Android et Web).
- **Sécurité Utilisateur :** Ajout d'un avertissement avant la redirection vers un lien textuel détecté dans un corps de message HTML [#744](https://github.com/suitenumerique/messages/issues/744).
- **Améliorations de l'interface :** 
    - Aperçu de texte plus propre.
    - Meilleure gestion de la vue "aucune boîte de réception".
    - Réinitialisation automatique de la recherche lors du changement de boîte de réception [#743](https://github.com/suitenumerique/messages/issues/743).
    - Prise en charge du paramètre de redirection après la connexion.
    - Feedback explicite en cas de problème d'authentification.

### Évolutions techniques
- **Infrastructure Mobile :** Intégration de Capacitor, mise en place d'une chaîne de mise à jour à distance (OTA) auto-hébergée et gestion du transfert de session OIDC pour le mobile.
- **Sécurité et Email :** 
    - Renforcement du parsing et de la composition des emails via `jmap-email` pour contrer les contenus malveillants.
    - Ajout de la règle de confiance ARC pour l'authentification des messages entrants [#763](https://github.com/suitenumerique/messages/issues/763).
    - Transfert du jeton CSRF via la session plutôt que par cookie.
- **Architecture et Refactoring :** 
    - Refactorisation du code d'importation (gestion des tentatives, mode continu, interface de liste) [#742](https://github.com/suitenumerique/messages/issues/742).
    - Configuration du frontend pilotée directement par le backend [#734](https://github.com/suitenumerique/messages/issues/734).
    - Support étendu des navigateurs (Chrome >= 109) [#750](https://github.com/suitenumerique/messages/issues/750).
- **Corrections de bugs :** 
    - Résolution d'un conflit de synchronisation (race condition) lors de l'envoi de messages concernant les destinataires.
    - Correction du gestionnaire Outlook Web dans la logique de décodage [#754](https://github.com/suitenumerique/messages/issues/754).
    - Correction de l'autosave qui s'activait indûment dans la fenêtre d'envoi.
- **Expérience Développeur (DevX) :** Optimisation du temps de configuration via la commande `make bootstrap`.

### Autres changements
- Documentation complète sur le processus de traitement du spam.
- Suppression de la fonctionnalité `TESTDOMAIN`.
