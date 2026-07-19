## Changelog : ami-notifications-api (30 derniers jours, au 17 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'API et à l'interface utilisateur, notamment autour de la gestion des événements, des notifications et de l'accessibilité. Des corrections et des refactorings ont également été effectués pour améliorer la performance et la maintenance du code. L'intégration de 17Cyber progresse avec des ajustements d'affichage et de compatibilité.

### Évolutions fonctionnelles
- Ajout du champ "sous-titre" aux événements de la version 2 de l'API. [#1033](https://github.com/numerique-gouv/ami-notifications-api/issues/1033)
- Amélioration de l'affichage de 17Cyber sur les appareils Android, assurant une utilisation optimale de la hauteur de l'écran. [#1013](https://github.com/numerique-gouv/ami-notifications-api/issues/1013)
- Implémentation du point de terminaison PUT pour les événements v2 de l'API. [#940](https://github.com/numerique-gouv/ami-notifications-api/issues/940)
- L'agent administrateur utilise maintenant l'API v2 des événements pour l'envoi des notifications. [#940](https://github.com/numerique-gouv/ami-notifications-api/issues/940)
- Gestion améliorée des icônes de notifications : l'API récupère l'icône à partir de l'élément associé ou utilise une icône par défaut. [#952](https://github.com/numerique-gouv/ami-notifications-api/issues/952)
- Ajout de l'ID utilisateur dans les données anonymisées pour les enregistrements et les notifications. [#964](https://github.com/numerique-gouv/ami-notifications-api/issues/964)
- Intégration de la fonctionnalité "Ami-FI" avec l'implémentation des vues d'autorisation et la simulation de la récupération des données utilisateur. [#992](https://github.com/numerique-gouv/ami-notifications-api/issues/992)
- Correction d'un bug empêchant l'affichage du message de succès après un appel API en cas d'erreur. [#940](https://github.com/numerique-gouv/ami-notifications-api/issues/940)
- Amélioration de la page d'accueil après la connexion, avec une attente de l'initialisation de l'utilisateur. [#1014](https://github.com/numerique-gouv/ami-notifications-api/issues/1014)

### Évolutions techniques
- Refactorisation de la navigation principale (main-nav) pour améliorer le style et la conformité RGAA. [#1037](https://github.com/numerique-gouv/ami-notifications-api/issues/1037)
- Renommage des bibliothèques et routes API pour une meilleure cohérence (catalog -> agenda, inventory -> followup, requests -> followup). [#1018](https://github.com/numerique-gouv/ami-notifications-api/issues/1018)
- Utilisation de `django-tasks-db` par défaut pour la gestion des tâches asynchrones, et ajout de la dépendance correspondante. [#956](https://github.com/numerique-gouv/ami-notifications-api/issues/956)
- Optimisation des performances de la liste des notifications en utilisant `select_related`. [#952](https://github.com/numerique-gouv/ami-notifications-api/issues/952)
- Configuration de Vite pour LightningCSS.
- Amélioration de la configuration de l'environnement de développement avec des ajustements de style pour 17Cyber. [#942](https://github.com/numerique-gouv/ami-notifications-api/issues/942)

### Autres changements
- Corrections de l'accessibilité (RGAA) : amélioration des types d'input (email) et ajout d'attributs `aria-label` pour les images. [#924](https://github.com/numerique-gouv/ami-notifications-api/issues/924), [#926](https://github.com/numerique-gouv/ami-notifications-api/issues/926), [#927](https://github.com/numerique-gouv/ami-notifications-api/issues/927), [#929](https://github.com/numerique-gouv/ami-notifications-api/issues/929)
- Suppression du retour de la description des Pull Requests dans les informations d'état, si l'auteur est Dependabot. [#981](https://github.com/numerique-gouv/ami-notifications-api/issues/981)
- Correction d'un problème de timeout dans les tests unitaires de ZonePreferences. [#789](https://github.com/numerique-gouv/ami-notifications-api/issues/789)
- Refactorisation des modals Request Item et Agenda Item. [#373](https://github.com/numerique-gouv/ami-notifications-api/issues/373), [#776](https://github.com/numerique-gouv/ami-notifications-api/issues/776)
