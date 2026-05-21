## Changelog : recommandations-collaboratives (30 derniers jours, au 2026-05-20)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du CRM (gestion de la relation client) avec une refonte de l'interface utilisateur, l'ajout de nouvelles informations et la correction de bugs. Des améliorations ont également été apportées à la gestion des projets, des documents et des données géographiques, ainsi que des corrections de sécurité et des mises à jour de dépendances.

### Évolutions fonctionnelles
- **CRM :** Refonte de l'interface utilisateur avec l'ajout de nouvelles cartes utilisateurs, d'informations sur les rôles et des événements dans un fil d'actualité plus clair.
- **CRM :** Ajout de la possibilité de consulter les statistiques de conversation.
- **Projets :** Possibilité d'afficher les projets supprimés (avec les permissions appropriées) via l'API.
- **Documents :** Amélioration du comptage des documents dans le CRM.
- **Login :** Amélioration de la gestion des traces de connexion pour les liens Sesame.
- **Webhooks :** Envoi de webhooks lors des changements d'organisation d'un utilisateur.
- **Interface utilisateur :** Amélioration de l'accessibilité et de l'affichage sur différents écrans (responsive design).
- **Géolocalisation :** Amélioration du script de gestion des communes avec la prise en compte des fusions de La Poste.

### Évolutions techniques
- **API :** Extension de l'API des projets pour inclure les projets supprimés.
- **Tests :** Mise à jour et amélioration des tests frontend (Cypress) et backend.
- **Refactoring :** Plusieurs refactorings ont été effectués pour améliorer la qualité du code et la maintenabilité, notamment dans les modules CRM et de gestion des projets.
- **Performance :** Optimisation des requêtes pour l'API des projets.
- **Dépendances :** Mises à jour de plusieurs dépendances (Django, Wagtail, JupyterLab, etc.) pour bénéficier des dernières corrections de sécurité et améliorations.
- **CI/CD :** Amélioration de la configuration de l'intégration continue et du déploiement continu (GitHub Actions).

### Autres changements
- **Documentation :** Mise à jour de la documentation sur les webhooks et l'utilisation de l'API.
- **Nettoyage du code :** Suppression de code inutile et amélioration de la lisibilité du code.
- **Corrections de bugs :** Correction de plusieurs bugs mineurs dans l'interface utilisateur et le backend.
- **Configuration :** Ajustements de la configuration pour améliorer la sécurité et la performance.
