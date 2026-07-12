## Changelog : ami-notifications-api (30 derniers jours, au 02 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'interface utilisateur, notamment une refonte de la gestion des suivis et des requêtes, ainsi que l'implémentation d'une authentification via FranceConnect pour un nouveau cas d'usage (ami-fi). Des corrections d'accessibilité (RGAA) et des optimisations de performance ont également été réalisées.

### Évolutions fonctionnelles
- **Gestion des suivis et requêtes :** Refonte complète de l'interface utilisateur pour la gestion des suivis (anciennement "inventory") et des requêtes (anciennement "requests"). Cela inclut l'ajout d'une page d'archivage, la possibilité d'archiver des éléments, et une simplification de l'affichage. [#776]
- **Authentification FranceConnect (ami-fi) :** Implémentation d'un nouveau flux d'authentification via FranceConnect pour le cas d'usage "ami-fi", incluant la gestion des providers, des tokens et la redirection après authentification. [#907, #917]
- **Icônes de notifications :** Amélioration de la gestion des icônes de notifications, avec la possibilité de déduire l'icône à partir de l'état de l'élément associé ou du partenaire. [#952]
- **API Événements v2 :** Implémentation d'un nouvel endpoint PUT pour les événements v2, avec des validations renforcées sur les champs parent. [#940]
- **Page d'accueil après login :** Amélioration de l'expérience utilisateur après la connexion, avec un chargement plus fluide de la page d'accueil. [#1014]

### Évolutions techniques
- **Refactoring du code front-end :** Renommage de plusieurs librairies et routes front-end pour une meilleure cohérence (agenda, followup, requests). [#1018]
- **Optimisation des performances :** Ajout de `select_related` dans l'API de listage des notifications pour améliorer les performances. [#952]
- **Utilisation de django-tasks-db :** Intégration de `django-tasks-db` pour la gestion des tâches asynchrones. [#956]
- **Mises à jour de dépendances :** Mises à jour de plusieurs dépendances, notamment `ujson`, `msgpack`, `pyjwt`, `webob`, et des dépendances de développement.
- **Configuration Vite :** Configuration de Vite pour LightningCSS.

### Autres changements
- **Accessibilité (RGAA) :** Corrections d'accessibilité pour améliorer la conformité aux normes RGAA (titres, boutons, attributs alt des images). [#924, #926, #927, #929]
- **Documentation :** Amélioration de la documentation et du code.
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Tests :** Amélioration des tests unitaires, notamment pour la page de préférences de zone. [#789]
- **Gestion des logs :** Amélioration de la gestion des logs pour les tâches d'envoi de notifications.
- **Suppression de messages de succès inutiles :** Suppression des messages de succès affichés en cas d'erreur lors des appels API. [#940]
- **Exclusion des notifications expirées :** Exclusion des notifications avec une date de validité dépassée lors de la récupération en liste. [#674]
- **Amélioration du traitement des erreurs :** Amélioration de la gestion des erreurs lors de la déconnexion. [#971]
- **Suppression des cookies inutiles :** Suppression des cookies inutiles lors de la connexion ami-fi. [#907]
- **Amélioration des descriptions des PR :** Exclusion des descriptions des PR Dependabot dans les logs. [#981]
