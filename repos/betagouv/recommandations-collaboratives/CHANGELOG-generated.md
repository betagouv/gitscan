## Changelog : recommandations-collaboratives (30 derniers jours, au 27 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment au niveau de l'interface CRM et de la gestion des projets. Des corrections de bugs et des optimisations de performance ont également été apportées, ainsi que des améliorations de la sécurité avec l'ajout de traçage des connexions via Sesame. Les tests frontend ont été mis à jour et de nombreuses dépendances ont été actualisées.

### Évolutions fonctionnelles

*   **CRM :**
    *   Refonte de l'interface utilisateur pour la gestion des utilisateurs CRM [#2081](https://github.com/betagouv/recommandations-collaboratives/pull/2081).
    *   Amélioration de l'affichage des informations des utilisateurs et des projets dans le CRM.
    *   Correction d'un bug empêchant l'accès aux boutons de recommandation dans l'éditeur de conversation [#2078](https://github.com/betagouv/recommandations-collaboratives/pull/2078).
    *   Ajout de la possibilité de filtrer les utilisateurs par rôle dans le CRM.
    *   Correction du comptage des documents liés à une conversation dans le CRM.
*   **Gestion des projets :**
    *   Possibilité d'afficher les projets supprimés avec les permissions appropriées [#2084](https://github.com/betagouv/recommandations-collaboratives/pull/2084).
    *   Ajout de nouvelles colonnes Grist pour les projets [#2078](https://github.com/betagouv/recommandations-collaboratives/pull/2078).
    *   Affichage du nombre de projets dans les colonnes Kanban [#2094](https://github.com/betagouv/recommandations-collaboratives/pull/2094).
    *   Amélioration de l'API pour inclure des données supplémentaires pour Grist.
*   **Authentification :**
    *   Ajout du traçage des connexions via Sesame pour une meilleure sécurité [#2084](https://github.com/betagouv/recommandations-collaboratives/pull/2084).
*   **Notifications :**
    *   Correction du comportement de consommation des notifications de conversation [#2024](https://github.com/betagouv/recommandations-collaboratives/pull/2024).
*   **Webhooks :**
    *   Envoi de webhooks lors des modifications de l'organisation d'un utilisateur [#2078](https://github.com/betagouv/recommandations-collaboratives/pull/2078).

### Évolutions techniques

*   **Tests :**
    *   Mise à jour des tests frontend (Cypress) pour une meilleure couverture et fiabilité [#2027](https://github.com/betagouv/recommandations-collaboratives/pull/2027).
    *   Refactorisation et amélioration de la structure des tests.
*   **Dépendances :**
    *   Mise à jour de plusieurs dépendances : Django, Wagtail, js-cookie, systeminformation, postcss, jupyterlab, urllib, etc.
*   **Refactoring :**
    *   Optimisation des requêtes pour l'API des projets.
    *   Séparation des préoccupations pour l'affichage des projets supprimés.
    *   Amélioration de la lisibilité du code et suppression de code inutile.
*   **CI/CD :**
    *   Mise en place d'un workflow CI/CD plus robuste.

### Autres changements

*   Documentation :
    *   Mise à jour de la documentation sur les webhooks.
    *   Documentation des changements futurs pour la synchronisation Recoco.
*   Correction de bugs mineurs et améliorations de l'interface utilisateur.
*   Amélioration des messages de log.
*   Correction de problèmes d'accessibilité.
*   Amélioration de la gestion des erreurs.
*   Ajout de commentaires et de documentation au code.
