## Changelog : messages (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, le projet franchit une étape majeure avec l'introduction des notifications push et le lancement du support mobile via Capacitor. Les capacités de gestion des emails ont été renforcées par une meilleure sécurité et une gestion plus robuste des messages entrants, tout en améliorant l'expérience de développement et la stabilité de l'interface.

### Évolutions fonctionnelles
- **Notifications :** Mise en place d'un système de notifications push pour iOS, Android et le Web.
- **Expérience utilisateur :**
    - Amélioration de l'aperçu du texte pour une lecture plus claire.
    - Amélioration de l'affichage de l'interface lorsqu'aucune boîte de réception n'est sélectionnée.
    - Prise en charge du paramètre de redirection après la connexion pour retrouver la page consultée.
- **Corrections :**
    - Résolution d'un problème d'affichage lié à la logique de décodage d'Outlook Web [#754](https://github.com/suitenumerique/messages/issues/754).
    - Correction du comportement de l'enregistrement automatique qui s'activait de manière inappropriée lors de la fenêtre d'envoi.
    - Correction des retours d'authentification pour les utilisateurs sans compte.
- **Suppression :** Retrait de la fonctionnalité `TESTDOMAIN`.

### Évolutions techniques
- **Support Mobile :** 
    - Initialisation des applications mobiles via Capacitor.
    - Mise en place d'une chaîne de mise à jour à distance (OTA) auto-hébergée.
    - Gestion de la transition de session OIDC pour les appareils mobiles.
- **Sécurité et Protocoles Email :**
    - Renforcement du parsing et de la composition des messages (via `jmap-email`) pour contrer les contenus malveillants.
    - Ajout de règles de confiance ARC pour l'authentification des messages entrants [#763](https://github.com/suitenumerique/messages/issues/763).
    - Assouplissement des vérifications d'espacement DKIM pour les configurations DNS [#778](https://github.com/suitenumerique/messages/issues/778).
    - Migration de la livraison du jeton CSRF via la session plutôt que par cookie.
- **Architecture et Développement :**
    - Refonte du code d'importation (gestion des tentatives, mode continu, interface de liste) [#742](https://github.com/suitenumerique/messages/issues/742).
    - Optimisation du temps de configuration de l'environnement de développement (*DevX*).
    - Amélioration du processus de build (cache-busting et support de versions de navigateurs plus anciennes [#750](https://github.com/suitenumerique/messages/issues/750)).
    - Résolution d'un conflit de synchronisation (*race condition*) lors de l'envoi de messages avec des destinataires.

### Autres changements
- Ajout d'une documentation complète sur le processus de traitement du spam.
