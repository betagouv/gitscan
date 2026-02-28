## Changelog : recommandations-collaboratives (30 derniers jours)

### Résumé
Cette version apporte des améliorations significatives à l'interface utilisateur, notamment au niveau de la gestion des ressources et des projets. Des corrections de bugs ont été implémentées pour améliorer la stabilité et l'expérience utilisateur, en particulier concernant les notifications, les filtres et la gestion des erreurs. Des améliorations de performance et des mises à jour de sécurité ont également été apportées.

### Évolutions fonctionnelles
- Possibilité de dupliquer une ressource (#1895).
- Ajout d'un indicateur de nombre de conversations non lues (#1924).
- Amélioration du filtre de projet pour une meilleure expérience utilisateur (#1931).
- Suppression du filtre temporel sur le kanban des projets (#1925).
- Ajout de la possibilité d'utiliser une ressource dans plusieurs projets (#1905).
- Ajout de nouvelles actions aux notifications (#1914).
- Possibilité de rechercher et filtrer les ressources par département (#1830, #1861).
- Ajout d'un bouton pour créer une nouvelle ressource dans la liste des ressources.
- Amélioration de la gestion des erreurs et des messages d'information dans l'interface utilisateur.
- Ajout d'un système d'alerte lors de la déconnexion de l'utilisateur (#1874).
- Possibilité de supprimer un compte utilisateur avec une alerte préalable (#1877).
- Amélioration de l'affichage des titres et des informations dans les cartes Kanban (#1878).
- Ajout d'un indicateur visuel pour les ressources utilisées (#1889).
- Amélioration de l'interface d'édition des ressources (#1814, #1870).
- Ajout de la possibilité de télécharger des fichiers ZIP (#1830).
- Amélioration de l'affichage des commentaires des tâches (#1842).
- Suppression de l'ancien tutoriel (#1843).
- Amélioration de l'affichage des libellés des notifications des projets (#1850).

### Évolutions techniques
- Refactorisation du code pour améliorer la performance et la maintenabilité.
- Mise à jour des dépendances (Django, Celery, Redis, PostgreSQL, BeautifulSoup4) pour bénéficier des dernières corrections de sécurité et améliorations.
- Amélioration de la gestion des erreurs et de la journalisation.
- Optimisation des requêtes à la base de données.
- Amélioration de la gestion des migrations de base de données.
- Mise en place de tests unitaires pour garantir la qualité du code.
- Amélioration de la sécurité en corrigeant des vulnérabilités potentielles.
- Utilisation de PrimaryKeyRelatedField pour les sérialiseurs de ressources.
- Refactorisation de la gestion des URL et des chemins d'accès.

### Autres changements
- Mise à jour de la documentation.
- Nettoyage du code et suppression du code obsolète.
- Amélioration de la configuration du projet.
- Correction de problèmes de style et d'affichage.
- Amélioration de l'accessibilité de l'interface utilisateur.
- Mise à jour des messages d'aide et des textes d'information.
- Correction de bugs mineurs et amélioration de la stabilité générale.
- Mise à jour des dépendances npm et yarn (lodash, tar).
- Amélioration de la gestion des erreurs Sentry.
- Suppression de code non utilisé.
- Amélioration de la gestion des notifications RGPD.
- Correction de problèmes liés à l'affichage des titres et des informations dans l'interface utilisateur.
