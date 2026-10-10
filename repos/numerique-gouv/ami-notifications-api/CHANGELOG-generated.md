## Changelog : ami-notifications-api (30 derniers jours, au 09/10/2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'une amélioration majeure de ses fonctionnalités de suivi (followup) et de checklists, rendant l'expérience plus fluide et informative pour les agents. La sécurité et la fiabilité du système ont également été renforcées grâce à une meilleure surveillance des erreurs et à un durcissement des politiques de protection des données.

### Évolutions fonctionnelles
- **Checklists :** Amélioration complète de la gestion des checklists, incluant l'ajout de nouveaux contenus (F2485, F39617), la gestion des liens et une interface d'administration dédiée pour les gérer [#1381, #1464, #1511].
- **Suivi (Followup) :** Enrichissement du module de suivi avec la gestion des dates clés (milestones), l'affichage des messages dans les éléments parents et une meilleure intégration des éléments personnels dans l'agenda [#268, #1144, #1279].
- **Gestion des consentements :** Refonte de l'interface de gestion des consentements pour simplifier l'expérience utilisateur (bouton "Tout sélectionner", affichage clair des partenaires et gestion des avertissements en cas de retrait) [#1273, #1497, #1539].
- **Notifications :** Amélioration de l'interface utilisateur, ajout d'icônes personnalisées et redirection automatique vers les pages concernées lors de la réception d'une notification [#1299, #1302].
- **Expérience Utilisateur (UX) :** 
    - Création d'un nouveau centre d'aide [#1080].
    - Refonte de la page de contact et amélioration de l'accessibilité (RGAA) [#800, #1431, #1440].
    - Amélioration de la gestion des erreurs avec des pages plus explicites [#595].
- **Navigation :** Optimisation de la navigation via des alias d'URLs pour une meilleure cohérence entre l'application mobile et le web [#1027].

### Évolutions techniques
- **Sécurité :** 
    - Renforcement de la protection contre les attaques via l'implémentation de politiques CSP [#1583].
    - Durcissement de la gestion des cookies (politique SameSite) et limitation des payloads API au format JSON [#1507, #1544, #1505].
    - Mise en place d'une liste blanche d'adresses IP pour sécuriser les appels des partenaires [#1255].
- **Observabilité et Monitoring :** 
    - Amélioration significative du suivi des erreurs et de la télémétrie (intégration Sentry enrichie, ajout de logs de débogage pour l'authentification et traçage des événements frontend) [#985, #1407, #1429].
- **Infrastructure et Performance :** 
    - Automatisation de la gestion des certificats SSL avec Let's Encrypt [#1494].
    - Optimisation des performances de la base de données par l'ajout d'index sur les tables utilisateurs et notifications [#1414].
- **Architecture :** 
    - Amélioration du processus de déconnexion (notamment pour FranceConnect) [#1380, #1542].
    - Correction de problèmes de gestion de l'asynchronisme dans le middleware JWT [#1558].

### Autres changements
- **Maintenance :** Nettoyage du code (suppression de code mort et de paramètres inutilisés) et ajout de commandes de nettoyage pour la base de données [#1333, #1279, #1417, #1332].
