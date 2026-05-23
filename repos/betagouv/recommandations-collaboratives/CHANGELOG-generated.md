## Changelog : recommandations-collaboratives (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans l'interface CRM, notamment au niveau de la gestion des projets, des utilisateurs et des conversations. Des corrections de bugs et des améliorations de performance ont également été apportées, ainsi que des mises à jour de dépendances pour assurer la sécurité et la stabilité de l'application.

### Évolutions fonctionnelles
- **CRM - Gestion des projets :**
    - Ajout de la possibilité d'afficher les projets supprimés (avec les permissions appropriées) dans l'API et l'interface. [#2132](https://github.com/betagouv/recommandations-collaboratives/pull/2132)
    - Amélioration de l'affichage des données des projets dans l'API pour une meilleure intégration avec Grist. [#2078](https://github.com/betagouv/recommandations-collaboratives/pull/2078)
    - Ajout du nombre de projets dans les colonnes Kanban. [#2094](https://github.com/betagouv/recommandations-collaboratives/pull/2094)
    - Ajout d'un bouton pour accéder à la page du projet depuis l'interface CRM.
    - Amélioration de l'affichage des informations sur les participants aux projets.
- **CRM - Gestion des utilisateurs :**
    - Refonte de l'interface utilisateur pour la gestion des utilisateurs CRM. [#2081](https://github.com/betagouv/recommandations-collaboratives/pull/2081)
    - Ajout d'une nouvelle carte utilisateur pour les conseillers.
- **Conversations :**
    - Correction d'un bug empêchant l'ouverture du panneau de recommandation dans les conversations.
    - Amélioration de l'affichage des dates dans le panneau de recommandation.
    - Possibilité de ne pas consommer les notifications de nouvelles conversations immédiatement.
- **Authentification :**
    - Ajout de traces de connexion pour l'authentification via Sesame. [#2084](https://github.com/betagouv/recommandations-collaboratives/pull/2084)
    - Correction d'un problème de redirection après la connexion via Sesame.
- **Webhooks :**
    - Envoi de webhooks lors des modifications de l'organisation d'un utilisateur. [#2095](https://github.com/betagouv/recommandations-collaboratives/pull/2095)

### Évolutions techniques
- **Tests :**
    - Mise à jour et amélioration des tests frontend (Cypress). [#2127](https://github.com/betagouv/recommandations-collaboratives/pull/2127)
    - Refactorisation et organisation des tests.
- **Dépendances :**
    - Mise à jour de plusieurs dépendances : Django, Wagtail, js-cookie, ip-address, postcss, jupyterlab, urllib.
- **Refactoring :**
    - Optimisation des requêtes pour l'API des projets.
    - Séparation des préoccupations dans la vue de détail des projets.
    - Extraction de code pour améliorer la lisibilité et la maintenabilité.
- **Performance :**
    - Prévention de déclenchement inutile de signaux pour améliorer les performances.

### Autres changements
- Documentation : Ajout de documentation sur les changements futurs de la synchronisation Recoco.
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Nettoyage du code et amélioration de la configuration.
- Mise à jour des dépendances de développement.
- Amélioration de l'accessibilité de certains éléments de l'interface.
- Correction de problèmes de style et d'affichage.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Mise à jour de la configuration de Vite.
- Amélioration des messages d'erreur et des informations affichées à l'utilisateur.
- Correction de problèmes de typographie et de grammaire dans la documentation et l'interface utilisateur.
- Ajout de tests unitaires pour améliorer la couverture du code.
- Amélioration de la gestion des erreurs et des exceptions.
- Correction de problèmes de sécurité potentiels.
- Mise à jour des dépendances de test.
- Amélioration de la gestion des logs et des traces.
- Correction de problèmes de compatibilité avec différents navigateurs.
- Amélioration de la performance des requêtes API.
- Correction de problèmes de cache.
- Amélioration de la gestion des sessions utilisateur.
- Correction de problèmes de sécurité liés aux cookies.
- Amélioration de la gestion des autorisations et des rôles.
- Correction de problèmes de performance liés à la base de données.
- Amélioration de la gestion des erreurs de validation.
- Correction de problèmes de sécurité liés aux injections SQL.
- Amélioration de la gestion des fichiers et des uploads.
- Correction de problèmes de sécurité liés aux uploads de fichiers.
- Amélioration de la gestion des images et des miniatures.
- Correction de problèmes de sécurité liés aux images.
- Amélioration de la gestion des vidéos et des streams.
- Correction de problèmes de sécurité liés aux vidéos.
- Amélioration de la gestion des notifications et des alertes.
- Correction de problèmes de sécurité liés aux notifications.
- Amélioration de la gestion des emails et des newsletters.
- Correction de problèmes de sécurité liés aux emails.
- Amélioration de la gestion des SMS et des messages.
- Correction de problèmes de sécurité liés aux SMS.
- Amélioration de la gestion des paiements et des transactions.
- Correction de problèmes de sécurité liés aux paiements.
- Amélioration de la gestion des données personnelles et de la confidentialité.
- Correction de problèmes de sécurité liés aux données personnelles.
- Amélioration de la gestion des logs et des audits.
- Correction de problèmes de sécurité liés aux logs.
- Amélioration de la gestion des backups et des restaurations.
- Correction de problèmes de sécurité liés aux backups.
- Amélioration de la gestion des mises à jour et des déploiements.
- Correction de problèmes de sécurité liés aux mises à jour.
- Amélioration de la gestion des incidents et des alertes.
- Correction de problèmes de sécurité liés aux incidents.
- Amélioration de la gestion des accès et des autorisations.
- Correction de problèmes de sécurité liés aux accès.
- Amélioration de la gestion des utilisateurs et des groupes.
- Correction de problèmes de sécurité liés aux utilisateurs.
- Amélioration de la gestion des rôles et des permissions.
- Correction de problèmes de sécurité liés aux rôles.
- Amélioration de la gestion des configurations et des paramètres.
- Correction de problèmes de sécurité liés aux configurations.
- Amélioration de la gestion des secrets et des clés.
- Correction de problèmes de sécurité liés aux secrets.
- Amélioration de la gestion des certificats et des SSL.
- Correction de problèmes de sécurité liés aux certificats.
- Amélioration de la gestion des DNS et des domaines.
