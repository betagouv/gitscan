## Changelog : ami-notifications-api (30 derniers jours, au 16 juillet 2026)

### Résumé
Les dernières mises à jour de l'API de notifications se concentrent sur l'amélioration de l'expérience utilisateur de l'interface web "17cyber", l'ajout de fonctionnalités pour la gestion des événements (v2), l'amélioration de l'affichage des icônes de notifications et la correction de problèmes liés à l'authentification et à la gestion des données. Des améliorations de conformité RGAA ont également été apportées.

### Évolutions fonctionnelles
- **Notifications :** Amélioration de l'affichage des icônes de notifications en utilisant l'icône de l'élément si disponible, ou une icône par défaut en cas d'inconnu. [#952]
- **API Événements :** Implémentation d'un point de terminaison PUT pour la gestion des événements v2, incluant la validation des champs parent. [#940]
- **Interface 17cyber :**
    - Correction de problèmes d'affichage de la hauteur de la page sur certains appareils Android. [#1013]
    - Ajout d'une meta tag pour le referrer. [#942]
    - Amélioration de la navigation après la connexion, en attendant l'initialisation de l'utilisateur. [#1014]
- **Suivi (Follow-up) :** Ajout de la possibilité d'identifier de manière unique un suivi via son type et son ID externe. [#690]
- **Réplication :** Ajout de l'ID utilisateur dans les données de réplication des enregistrements et des notifications. [#964]

### Évolutions techniques
- **Refactoring :** Renommage des librairies et routes liées aux agendas et aux suivis pour une meilleure cohérence. [#1018]
- **Authentification :** Amélioration de la gestion de la déconnexion pour éviter les erreurs d'intégrité. [#971]
- **Tests :** Correction d'un timeout dans les tests unitaires des préférences de zone. [#789]
- **Performances :** Optimisation de la récupération des notifications en utilisant `select_related`. [#952]
- **Infrastructure :** Mise à jour de plusieurs dépendances (esbuild, @sveltejs/vite-plugin-svelte, vite, @vitejs/plugin-basic-ssl, webob, pyjwt, ujson, msgpack, brace-expansion, undici, dompurify, js-yaml, cryptography).

### Autres changements
- **Documentation :** Mise à jour de la documentation pour refléter les changements de l'API.
- **RGAA :** Corrections pour améliorer l'accessibilité de l'interface utilisateur (balises `alt` et `aria-label` pour les images, wording). [#924, #926, #929]
- **Outils :** Configuration de Vite pour LightningCSS.
- **Tâches asynchrones :** Utilisation de `django-tasks-db` pour la gestion des tâches asynchrones. [#956]
- **Logs :** Amélioration des logs pour les tâches d'envoi de notifications.
