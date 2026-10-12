## Changelog : messages (30 derniers jours, au 06/10/2026)

### Résumé
Ce mois a été marqué par une refonte majeure de l'interface mobile et l'introduction de nouvelles manières de composer des messages, notamment via des fenêtres flottantes. Parallèlement, des mesures de sécurité importantes ont été déployées pour renforcer le contrôle des accès et des données, tout en améliorant la stabilité globale de l'application et de son infrastructure.

### Évolutions fonctionnelles
- **Expérience Mobile** : Refonte complète de l'interface utilisateur (navigation, gestes de balayage, barre d'outils) et amélioration de l'affichage en mode paysage.
- **Composition de messages** : Introduction de la composition dans des fenêtres flottantes pour gérer plusieurs brouillons simultanément.
- **Améliorations UX** : 
    - Ajout d'une confirmation avant la suppression d'un brouillon [#817](https://github.com/suitenumerique/messages/issues/817).
    - Persistance de la dernière boîte de réception active lors de la navigation.
    - Amélioration de la gestion des messages non lus (badge favicon) et de la navigation lors du changement de boîte.
- **Corrections** :
    - Résolution de problèmes de focus du clavier et de l'éditeur sur les appareils tactiles.
    - Correction de bugs d'affichage sur les menus déroulants [#808](https://github.com/suitenumerique/messages/issues/808), les popovers de recherche sur tablette et les suggestions de l'utilisateur.
    - Correction des traductions néerlandaises manquantes ou incorrectes.
    - Amélioration de la gestion des mots-clés et du support du format MBOX.

### Évolutions techniques
- **Sécurité** : 
    - Renforcement du périmètre d'accès, des requêtes sortantes et de la gestion des clés API personnelles [#804](https://github.com/suitenumerique/messages/issues/804).
    - Mise en place d'une liste blanche d'IP (Caddy) pour sécuriser l'accès à la console d'administration Keycloak [#793](https://github.com/suitenumerique/messages/issues/793).
- **Infrastructure & Mobile** :
    - Mise à jour de Keycloak [#813](https://github.com/suitenumerique/messages/issues/813) et [#798](https://github.com/suitenumerique/messages/issues/798).
    - Mise à jour de Capacitor vers la version 8.5.
    - Automatisation de la publication des mises à jour mobiles (OTA) via les déploiements Scalingo.
    - Amélioration des outils de release pour le Play Store.
- **Optimisations Backend & Frontend** :
    - Déplacement des tâches d'exportation vers le worker d'importation pour une meilleure gestion des ressources [#805](https://github.com/suitenumerique/messages/issues/805).
    - Migration du frontend vers les nouveaux packages `ui-kit`.
    - Optimisation du redimensionnement des iframes de mail via `ResizeObserver`.

### Autres changements
- **Documentation** : Restructuration de la documentation mobile en séparant les guides d'onboarding des guides de release.
