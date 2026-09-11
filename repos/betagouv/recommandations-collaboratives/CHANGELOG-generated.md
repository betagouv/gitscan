## Changelog : recommandations-collaboratives (30 derniers jours, au 10 septembre 2026)

### Résumé
Ce mois-ci, l'effort s'est concentré sur la sécurisation massive de la plateforme, notamment pour garantir que les données restent strictement cloisonnées entre les différents sites et projets. Des améliorations de performance et de l'interface d'administration ont également été apportées pour fluidifier l'expérience des gestionnaires.

### Évolutions fonctionnelles
- **Administration :** Ajout de filtres dans l'interface Nimda pour identifier plus facilement les utilisateurs supprimés et les organisations spécifiques [#2343](https://github.com/betagouv/recommandations-collaboratives/issues/2343).
- **CRM :** Amélioration de la précision des compteurs (projets, membres) et de la visibilité des données selon les rôles des utilisateurs.
- **Flux RSS :** Sécurisation des flux via un système d'authentification et filtrage automatique des ressources en mode brouillon.
- **Expérience utilisateur :** Corrections sur le système de notifications (cloche de modération), les demandes d'accès pour les conseillers et l'intégration des portails embarqués.

### Évolutions techniques
- **Sécurité :** Correction de plusieurs vulnérabilités critiques de type IDOR pour empêcher l'accès non autorisé à des ressources, projets ou documents appartenant à d'autres entités [#2380](https://github.com/betagouv/recommandations-collaboratives/issues/2380), [#2397](https://github.com/betagouv/recommandations-collaboratives/issues/2397), [#2378](https://github.com/betagouv/recommandations-collaboratives/issues/2378), [#2376](https://github.com/betagouv/recommandations-collaboratives/issues/2376).
- **Sécurité :** Mise en place d'une politique de sécurité du contenu (CSP) et renforcement de la désinfection (sanitization) des contenus HTML et Markdown pour prévenir les injections.
- **Performance :** Optimisation des requêtes de base de données (prefetching) pour accélérer l'affichage des projets et des détails utilisateurs.
- **Refactoring :** Migration de composants vers la version 3 et amélioration de la gestion des listes et tableaux [#2319](https://github.com/betagouv/recommandations-collaboratives/issues/2319).
- **Communication :** Sécurisation de l'envoi d'emails via Brevo (protection contre l'injection de paramètres dans les templates).

### Autres changements
- **Tests :** Renforcement significatif de la couverture de tests, particulièrement sur les scénarios de régression liés à la sécurité.
- **Maintenance :** Nettoyage du code (suppression de code mort) et mise en conformité du style (linting).
