## Changelog : recommandations-collaboratives (30 derniers jours, au 9 juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de l'interface utilisateur du CRM, notamment la refonte de la liste des utilisateurs et des projets, ainsi que l'ajout de nouvelles fonctionnalités comme l'affichage du nombre de projets dans le Kanban. Des corrections de sécurité et des mises à jour de dépendances ont également été apportées pour assurer la stabilité et la sécurité de la plateforme.

### Évolutions fonctionnelles
- **CRM :** Refonte de la liste des utilisateurs avec affichage d'informations supplémentaires (organisation, statut, etc.) [#2025](https://github.com/betagouv/recommandations-collaboratives/pulls/2025)
- **CRM :** Refonte de la liste des projets avec affichage du nombre de projets dans chaque colonne du Kanban [#2070](https://github.com/betagouv/recommandations-collaboratives/pulls/2070) et [#2094](https://github.com/betagouv/recommandations-collaboratives/pulls/2094).
- **Authentification :** Amélioration de la gestion des emails lors de la réinitialisation du mot de passe pour les comptes inconnus [#2106](https://github.com/betagouv/recommandations-collaboratives/pulls/2106).
- **Notifications :** Délai de consommation des notifications amélioré [#2024](https://github.com/betagouv/recommandations-collaboratives/pulls/2024).
- **Interface utilisateur :** Ajout d'un lien vers le compte utilisateur dans les emails [#2104](https://github.com/betagouv/recommandations-collaboratives/pulls/2104).
- **Projets :** Possibilité d'afficher les projets supprimés avec les permissions appropriées.
- **Conviction :** Correction des droits d'accès au bouton d'ajout de recommandation [#2141](https://github.com/betagouv/recommandations-collaboratives/pulls/2141).
- **Formulaire de contact :** Le formulaire de contact est désormais uniquement accessible aux utilisateurs authentifiés [#2153](https://github.com/betagouv/recommandations-collaboratives/pulls/2153).

### Évolutions techniques
- **Sécurité :** Mise à jour de plusieurs dépendances pour corriger des vulnérabilités de sécurité (pywt, django, pyjwt, idna, wagtail) [#2163](https://github.com/betagouv/recommandations-collaboratives/pulls/2163), [#2169](https://github.com/betagouv/recommandations-collaboratives/pulls/2169), [#2129](https://github.com/betagouv/recommandations-collaboratives/pulls/2129), [#2104](https://github.com/betagouv/recommandations-collaboratives/pulls/2104).
- **CI/CD :** Amélioration de la configuration du CI pour l'utilisation de `uv` (gestionnaire de paquets Python) et ajout de `uv` à l'environnement CI.
- **Refactoring :** Refactorisation du code lié à la gestion des recommandations et suppression de code mort [#2080](https://github.com/betagouv/recommandations-collaboratives/pulls/2080).
- **Tests :** Ajout de tests unitaires et d'intégration, notamment pour les routes API et les tests Cypress.
- **Performance :** Optimisation des requêtes SQL pour l'API des projets.

### Autres changements
- **Documentation :** Mise à jour de la documentation concernant les webhooks.
- **Dépendances :** Mise à jour de plusieurs dépendances npm (tmp, js-cookie, systeminformation) et Python (urllib).
- **Style :** Amélioration du style de l'interface utilisateur (couleurs, mise en page).
- **Nettoyage de code :** Suppression de code inutile et amélioration de la lisibilité du code.
