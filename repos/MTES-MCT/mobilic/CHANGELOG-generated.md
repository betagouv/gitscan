## Changelog : mobilic (30 derniers jours, au 03 août 2026)

### Résumé
Ce mois-ci, la plateforme a franchi une étape importante avec l'ajout de fonctionnalités clés pour les salariés, notamment la gestion des demandes de détachement et la possibilité d'initier des contestations. L'interface a également été affinée pour offrir une meilleure navigation et une plus grande clarté dans la consultation des historiques d'activité, tant sur mobile que sur ordinateur.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités**
    - Mise en place du système de demande de détachement pour les salariés, incluant l'interface dédiée, la gestion des délais de carence et les relances [#898](https://github.com/MTES-MCT/mobilic/pull/898).
    - Ajout de la possibilité pour les salariés d'initier des procédures de contestation [#884](https://github.com/MTES-MCT/mobilic/pull/884).
- **Améliorations et corrections**
    - **Expérience Salarié & PWA** : Harmonisation de l'historique d'activité avec les exports PDF, meilleure gestion de l'affichage des activités sur les journées multi-missions et masquage automatique des données liées aux missions supprimées.
    - **Interface & Navigation** : Refonte du header et du footer de la page d'accueil (conformité DSFR) et amélioration de l'ergonomie des menus de navigation (styles de survol et états actifs).
    - **Notifications** : Optimisation de l'affichage sur petits écrans et ajustement du positionnement des éléments d'information pour une meilleure accessibilité.
    - **Administration & Contrôle** : Amélioration des outils d'impersonation (traçabilité accrue et visibilité de l'auteur des actions) [#901](https://github.com/MTES-MCT/mobilic/pull/901) [#910](https://github.com/MTES-MCT/mobilic/pull/910) et enrichissement de la bannière de contestation pour les administrateurs.
    - **Simplification** : Suppression de la fenêtre modale d'avertissement concernant les missions longues pour les salariés [#908](https://github.com/MTES-MCT/mobilic/pull/908).

### Évolutions techniques
- **CI/CD & Infrastructure** : Intégration des "review apps" Scalingo pour faciliter les tests de branches [#904](https://github.com/MTES-MCT/mobilic/pull/904) et ajustements de la détection de branche dans le pipeline CI. Retour à la configuration WAF OGO [#877](https://github.com/MTES-MCT/mobilic/pull/877).
- **Qualité du code & Performance** : Refactorisation de composants clés de la PWA (notamment `DurationDisplay`) pour réduire la complexité du code et amélioration du filtrage des erreurs Sentry pour réduire le bruit de monitoring [#891](https://github.com/MTES-MCT/mobilic/pull/891).
