## Changelog : ami-notifications-api (30 derniers jours, au 14/08/2026)

### Résumé
Ce mois-ci a été marqué par le déploiement majeur de la nouvelle section "Services", offrant une navigation enrichie et un rendu de contenu amélioré. L'interface d'administration a été considérablement renforcée pour permettre une gestion complète des services, tandis que l'expérience utilisateur a été fluidifiée par une refonte de l'écran de démarrage et une meilleure gestion des éléments de suivi. Enfin, la sécurité a été renforcée par l'introduction de nouveaux mécanismes de contrôle des clés d'accès.

### Évolutions fonctionnelles
- **Déploiement de la fonctionnalité "Services"** : ajout d'un menu dédié, de pages de détails avec rendu Markdown et de nouveaux points d'accès API [#943](https://github.com/numerique-gouv/ami-notifications-api/issues/943).
- **Amélioration de l'interface d'administration** : gestion complète du cycle de vie des services (ajout, modification, suppression, restriction d'accès) et mise en place de journaux d'audit pour les changements de service [#1054](https://github.com/numerique-gouv/ami-notifications-api/issues/1054).
- **Refonte de l'expérience utilisateur (UI/UX)** : 
    - Nouveau design de l'écran de démarrage pour plus de clarté [#1098](https://github.com/numerique-gouv/ami-notifications-api/issues/1098).
    - Amélioration de l'affichage et de la structure des éléments de suivi (follow-up) [#266](https://github.com/numerique-gouv/ami-notifications-api/issues/266).
    - Ajout de bannières informatives sur les pages d'édition [#769](https://github.com/numerique-gouv/ami-notifications-api/issues/769).
    - Amélioration de la navigation et des composants de modales [#979](https://github.com/numerique-gouv/ami-notifications-api/issues/979).
- **Nouveaux partenaires** : ajout du partenaire "RDV SP" [#1130](https://github.com/numerique-gouv/ami-notifications-api/issues/1130).
- **Corrections diverses** : résolution de problèmes d'affichage (bouton de préférence [#1107](https://github.com/numerique-gouv/ami-notifications-api/issues/1107), z-index de la navigation [#1091](https://github.com/numerique-gouv/ami-notifications-api/issues/1091)) et de l'initialisation des dates [#1076](https://github.com/numerique-gouv/ami-notifications-api/issues/1076).

### Évolutions techniques
- **Sécurité et accès** : mise en place d'un système de vérification des clés d'accès avec limitation de débit (rate limiting) et contrôle avant le chargement de l'application [#1096](https://github.com/numerique-gouv/ami-notifications-api/issues/1096).
- **API & Backend** : 
    - Finalisation de la migration des champs de notification vers la version 2 [#1005](https://github.com/numerique-gouv/ami-notifications-api/issues/1005).
    - Limitation du schéma API principal aux partenaires [#876](https://github.com/numerique-gouv/ami-notifications-api/issues/876).
    - Ajout de logs pour le suivi de la création des notifications et des événements [#1120](https://github.com/numerique-gouv/ami-notifications-api/issues/1120).
- **Architecture & Build** : 
    - Optimisation du développement avec le proxying des URLs Django via Vite [#1138](https://github.com/numerique-gouv/ami-notifications-api/issues/1138).
    - Passage à `sass-embedded` pour la gestion du CSS [#1123](https://github.com/numerique-gouv/ami-notifications-api/issues/1123).
    - Nettoyage des variables d'environnement publiques [#1138](https://github.com/numerique-gouv/ami-notifications-api/issues/1138).

### Autres changements
- **Documentation et corrections** : correction de coquilles dans la description de l'API [#876](https://github.com/numerique-gouv/ami-notifications-api/issues/876) et dans l'interface des préférences [#1157](https://github.com/numerique-gouv/ami-notifications-api/issues/1157).
- **Nettoyage du code** : suppression de fichiers d'icônes et de blocs de code inutilisés [#445](https://github.com/numerique-gouv/ami-notifications-api/issues/445) [#266](https://github.com/numerique-gouv/ami-notifications-api/issues/266).
