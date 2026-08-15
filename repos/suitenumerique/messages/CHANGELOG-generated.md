## Changelog : messages (30 derniers jours, au 13 août 2026)

### Résumé
Cette période est marquée par le passage à la version 0.9.0, apportant des avancées majeures pour l'usage mobile (applications iOS/Android, notifications push) et un renforcement significatif de la sécurité et de la robustesse du traitement des emails.

### Évolutions fonctionnelles
- **Expérience Mobile** :
    - Lancement du support des applications mobiles via Capacitor (iOS/Android) avec un système de mise à jour à distance (OTA) [#94d079b](https://github.com/suitenumerique/messages/commit/94d079b).
    - Mise en place des notifications push pour iOS, Android et le Web [#19cfa2d](https://github.com/suitenumerique/messages/commit/19cfa2d).
    - Amélioration de la gestion des sessions sur mobile (handoff OIDC et déconnexion personnalisée pour terminer la session IdP) [#31b51b5](https://github.com/suitenumerique/messages/commit/31b51b5) [#b7b5ff0](https://github.com/suitenumerique/messages/commit/b7b5ff0).
- **Interface et Expérience Utilisateur** :
    - Amélioration de la clarté des aperçus de messages et des extraits de fils de discussion [#bc96635](https://github.com/suitenumerique/messages/commit/bc96635) [#4611521](https://github.com/suitenumerique/messages/commit/4611521).
    - Optimisation du flux de connexion avec support du paramètre `next` pour reprendre la navigation après authentification [#302353e](https://github.com/suitenumerique/messages/commit/302353e).
    - Améliorations visuelles : gestion des couleurs BlockNote, masquage des statistiques du dossier "Envoyés" et vue "boîte vide" améliorée [#72b624e](https://github.com/suitenumerique/messages/commit/72b624e) [#5582246](https://github.com/suitenumerique/messages/commit/5582246).
- **Corrections** :
    - Résolution de problèmes de réécriture de sujet dans les réponses de fils de discussion [#a8d8e5b](https://github.com/suitenumerique/messages/pull/765).
    - Correction de conflits (race conditions) lors de l'envoi de messages avec des brouillons en cours de modification [#02225fa](https://github.com/suitenumerique/messages/commit/02225fa).
    - Correction du traitement des messages provenant d'Outlook Web [#1eb68ee](https://github.com/suitenumerique/messages/pull/754).

### Évolutions techniques
- **Sécurité et Traitement des Emails** :
    - Renforcement de la sécurité du parsing et de la composition via la bibliothèque `jmap-email` [#d03e56d](https://github.com/suitenumerique/messages/commit/d03e56d).
    - Durcissement de la configuration et des limites de `pymta` [#06e8bdb](https://github.com/suitenumerique/messages/pull/777).
    - Amélioration de la gestion de l'authentification entrante avec l'ajout de règles ARC relay-trust [#cf0b70e](https://github.com/suitenumerique/messages/pull/763).
    - Assouplissement de la vérification des espaces blancs DKIM pour les configurations DNS [#a8c8eb8](https://github.com/suitenumerique/messages/pull/778).
- **Infrastructure et Développement** :
    - Ajout d'un point de terminaison (endpoint) pour lister les enregistrements DNS de tous les domaines [#75c11c7](https://github.com/suitenumerique/messages/pull/780).
    - Optimisation du temps de configuration de l'environnement de développement (DevX) [#f4d2358](https://github.com/suitenumerique/messages/commit/f4d2358).
    - Amélioration de la gestion des builds avec l'ajout de cache-busting pour les versions sources [#7fdca12](https://github.com/suitenumerique/messages/commit/7fdca12).
    - Migration de la livraison du jeton CSRF via la session plutôt que par cookie [#5038dd9](https://github.com/suitenumerique/messages/commit/5038dd9).

### Autres changements
- Documentation complète ajoutée sur le processus de traitement du spam [#31144b1](https://github.com/suitenumerique/messages/commit/31144b1).
- Suppression de la fonctionnalité `TESTDOMAIN` [#07e906a](https://github.com/suitenumerique/messages/commit/07e906a).
- Mise à jour de certains titres de la documentation [#59d9321](https://github.com/suitenumerique/messages/commit/59d9321).
