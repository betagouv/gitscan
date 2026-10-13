## Changelog : drive (30 derniers jours, au 09/10/2026)

### Résumé
Cette période a été marquée par une amélioration majeure des performances, particulièrement pour la gestion de grands volumes de données et de hiérarchies complexes. Les administrateurs bénéficient désormais d'outils de gestion du stockage plus précis, tandis que la fiabilité et la sécurité des processus de téléchargement ont été renforcées.

### Évolutions fonctionnelles
- **Gestion du stockage (Admin) :** Amélioration de la visibilité sur l'utilisation de l'espace (affichage des quotas complets, des fichiers les plus volumineux) et possibilité de gérer les exclusions de quota pour certains éléments ou dossiers.
- **Contrôle d'accès :** Restriction de la création de nouveaux éléments pour les utilisateurs ne disposant pas des droits de téléchargement nécessaires.
- **Localisation :** Amélioration de la gestion des langues et des paramètres régionaux selon la configuration du navigateur.

### Évolutions techniques
- **Performances :** Optimisations massives des requêtes de base de données pour accélérer l'affichage des listes d'éléments, des favoris, des éléments récents et la résolution des chemins hiérarchiques (ancêtres/descendants).
- **Observabilité :** Intégration de nouveaux événements de suivi (PostHog) pour analyser les actions clés (suppression d'éléments, export de dossiers, édition de documents, etc.).
- **Sécurité et Fiabilité :** 
    - Mise en place de limites de débit (*rate limiting*) sur la création d'éléments.
    - Réservation de l'espace disque avant l'autorisation d'un téléchargement.
    - Sécurisation du service des fichiers WOPI via des téléchargements en mode "sandbox".
    - Amélioration du nettoyage automatique des fichiers temporaires lors des téléchargements.
- **Infrastructure et DevOps :**
    - Optimisation de la gestion des connexions à la base de données avec l'implémentation du pool de connexions `psycopg`.
    - Transition vers RustFS pour le stockage d'objets local.
    - Automatisation de la planification des tâches de maintenance via Celery Beat.
- **Tests :** Renforcement de la couverture des tests de bout en bout (e2e), notamment sur les processus de téléchargement et la gestion de la corbeille.

### Autres changements
- **Documentation :** Mise à jour de la documentation technique concernant les exemples de serveurs de ressources et la gestion des tailles de fichiers.
