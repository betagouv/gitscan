## Changelog : recommandations-collaboratives (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'interface utilisateur du CRM, notamment la refonte de la gestion des utilisateurs et des projets. Des corrections de bugs et des améliorations de performance ont également été apportées, ainsi que des ajustements pour faciliter les tests et la maintenance du code. L'intégration des traces de connexion via Sesame a été améliorée.

### Évolutions fonctionnelles
- **CRM :** Refonte de l'affichage des utilisateurs et des projets, avec de nouvelles cartes utilisateurs et une meilleure présentation des informations. [#2081](https://github.com/betagouv/recommandations-collaboratives/pull/2081)
- **CRM :** Ajout d'un bouton pour accéder directement à la page du projet depuis le CRM.
- **CRM :** Amélioration de l'affichage des documents et des tags dans le CRM.
- **Notifications :** Correction du comportement des notifications dans les conversations, notamment lors de l'ouverture du panneau de notifications.
- **Authentification :** Amélioration de l'intégration des traces de connexion via Sesame, notamment pour les liens. [#2084](https://github.com/betagouv/recommandations-collaboratives/pull/2084)
- **Projets :** Possibilité d'afficher les projets supprimés (avec les permissions appropriées) dans l'API et l'interface utilisateur. [#2090](https://github.com/betagouv/recommandations-collaboratives/pull/2090)
- **Webhooks :** Envoi de webhooks lors des modifications de l'organisation d'un utilisateur. [#2025](https://github.com/betagouv/recommandations-collaboratives/pull/2025)
- **Kanban :** Affichage du nombre de projets dans chaque colonne du Kanban. [#2094](https://github.com/betagouv/recommandations-collaboratives/pull/2094)

### Évolutions techniques
- **Tests :** Mise à jour et amélioration des tests frontend (Cypress), avec correction de plusieurs tests et ajout de nouveaux tests. [#2044](https://github.com/betagouv/recommandations-collaboratives/pull/2044), [#2092](https://github.com/betagouv/recommandations-collaboratives/pull/2092), [#2093](https://github.com/betagouv/recommandations-collaboratives/pull/2093)
- **Dépendances :** Mise à jour de plusieurs dépendances : Django, Wagtail, js-cookie, urllib, jupyterlab, postcss, ip-address, axios.
- **Refactoring :** Optimisation des requêtes pour l'API des projets.
- **Performance :** Prévention de déclenchement inutile de signaux pour améliorer la performance.
- **Code :** Nettoyage du code et suppression de code obsolète.
- **Documentation :** Ajout de documentation sur les changements à venir concernant la synchronisation Recoco.

### Autres changements
- Correction de problèmes d'affichage sur les écrans larges.
- Amélioration de la lisibilité du code.
- Correction de bugs mineurs dans l'interface utilisateur.
- Mise à jour de la documentation pour refléter les changements apportés.
- Ajustements de style et d'accessibilité.
- Correction de typos et amélioration de la formulation dans les tests et la documentation.
