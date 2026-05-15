## Changelog : recommandations-collaboratives (30 derniers jours, au 12 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur et de l'expérience utilisateur, notamment au niveau du CRM (gestion de la relation client) avec une refonte significative. Des corrections de bugs et des optimisations ont également été apportées, ainsi que des mises à jour de dépendances pour assurer la sécurité et la stabilité de la plateforme.

### Évolutions fonctionnelles
- **CRM :** Refonte majeure de l'interface utilisateur du CRM, incluant :
    - Ajout d'une nouvelle carte utilisateur pour les conseillers.
    - Amélioration de l'affichage des projets et des utilisateurs.
    - Ajout de bannières d'information et de gestion des projets.
    - Affichage du nombre de documents associés aux conversations.
    - Ajout d'indicateurs visuels pour l'état des projets.
    - Ajout de la possibilité de filtrer les utilisateurs.
- **Recommandations :**
    - Ajout d'un lien vers le compte utilisateur dans les notifications par email.
    - Amélioration de l'affichage des recommandations dans les conversations.
    - Possibilité de masquer l'onglet "Recommandations".
- **Fichiers :** Amélioration du chargement de fichiers pour les conseillers.
- **Interface Générale :**
    - Ajout d'informations contextuelles (infobulles) sur les éléments de l'interface.
    - Amélioration de l'accessibilité et de l'ergonomie de certains composants.
    - Ajout d'un indicateur de nombre de projets dans les colonnes Kanban.
- **Géomatique :** Amélioration de la synchronisation des données de communes avec la base de données LaPoste.
- **Tâches :** Correction de l'affichage des tâches liées aux recommandations.

### Évolutions techniques
- **Dépendances :** Mises à jour de plusieurs dépendances, notamment Django, Wagtail, JupyterLab, et divers paquets npm, pour bénéficier des dernières corrections de sécurité et améliorations de performance.
- **Tests :** Mise à jour des tests frontend (Cypress) pour assurer la couverture des nouvelles fonctionnalités et corrections de bugs.
- **CI/CD :** Amélioration du processus de CI/CD.
- **Refactoring :**
    - Simplification du code et suppression de code obsolète.
    - Amélioration de la structure du code pour une meilleure maintenabilité.
    - Refactorisation de la gestion des rôles dans le CRM.
- **Documentation :** Mise à jour de la documentation.

### Autres changements
- Correction de bugs mineurs dans l'interface utilisateur.
- Amélioration de la gestion des erreurs et des messages d'information.
- Nettoyage du code et amélioration de la lisibilité.
- Ajout de commentaires et de documentation pour faciliter la compréhension du code.
- Mise à jour des fichiers de configuration.
- Amélioration de la gestion des URLs et des liens.
- Correction de problèmes liés à l'affichage des dates et des heures.
- Amélioration de la gestion des autorisations et des accès.
- Ajout de tests unitaires pour certaines fonctionnalités.
- Correction de problèmes de compatibilité avec différents navigateurs.
