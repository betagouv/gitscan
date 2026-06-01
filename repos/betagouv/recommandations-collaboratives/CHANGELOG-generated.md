## Changelog : recommandations-collaboratives (30 derniers jours, au 29 mai 2026)

### Résumé
Cette période a été marquée par une refonte significative de l'interface utilisateur du CRM (gestion des utilisateurs, des projets et des organisations), avec un accent sur l'amélioration de l'expérience utilisateur et l'ajout de nouvelles fonctionnalités. Des corrections de bugs et des améliorations de performance ont également été apportées, notamment au niveau de la gestion des notifications et de l'authentification.

### Évolutions fonctionnelles
- **CRM (Gestion des utilisateurs, projets et organisations):** Refonte complète de l'interface utilisateur, incluant l'affichage des utilisateurs, des organisations, des projets et des conversations [#2081](https://github.com/betagouv/recommandations-collaboratives/pull/2081), [#2070](https://github.com/betagouv/recommandations-collaboratives/pull/2070).
- **CRM - Détails du projet:** Ajout d'informations sur les sujets associés aux projets, amélioration de l'affichage des données et ajout de filtres [#2078](https://github.com/betagouv/recommandations-collaboratives/pull/2078).
- **Ordre des recommandations:** Possibilité de modifier l'ordre des recommandations en cours d'élaboration [#2131](https://github.com/betagouv/recommandations-collaboratives/pull/2131).
- **Authentification:** Amélioration de la gestion des adresses e-mail inconnues lors de la réinitialisation du mot de passe et de la création de compte [#2145](https://github.com/betagouv/recommandations-collaboratives/pull/2145).
- **Notifications:** Amélioration de la gestion et de l'affichage des notifications, notamment en supprimant un délai artificiel [#2024](https://github.com/betagouv/recommandations-collaboratives/pull/2024).
- **Kanban:** Ajout du nombre de projets dans chaque colonne du Kanban [#2094](https://github.com/betagouv/recommandations-collaboratives/pull/2094).
- **Interface utilisateur:** Amélioration de l'interface utilisateur générale, notamment au niveau des styles, des couleurs et de l'accessibilité.

### Évolutions techniques
- **Tests:** Ajout de nouveaux tests et mise à jour des tests existants, notamment pour l'interface utilisateur (Cypress) [#2141](https://github.com/betagouv/recommandations-collaboratives/pull/2141), [#2127](https://github.com/betagouv/recommandations-collaboratives/pull/2127).
- **Dépendances:** Mise à jour de plusieurs dépendances, notamment Django, Wagtail, js-cookie, axios, postcss et jupyterlab.
- **Refactoring:** Refactoring du code pour améliorer la lisibilité et la maintenabilité, notamment au niveau de la gestion des rôles utilisateurs dans le CRM et de la logique de recherche.
- **CI/CD:** Amélioration de la configuration du CI/CD.
- **API:** Optimisation des requêtes API pour améliorer les performances, notamment pour la récupération des projets.

### Autres changements
- **Documentation:** Mise à jour de la documentation, notamment pour les webhooks et les tests E2E.
- **Configuration:** Ajustement de la configuration pour améliorer la sécurité et la performance.
- **Nettoyage de code:** Suppression de code inutile et amélioration de la qualité du code.
- **Corrections de bugs:** Correction de plusieurs bugs mineurs, notamment liés à l'affichage de l'interface utilisateur et à la gestion des permissions.
- **Amélioration de l'accessibilité:** Amélioration de l'accessibilité de certains éléments de l'interface utilisateur.
