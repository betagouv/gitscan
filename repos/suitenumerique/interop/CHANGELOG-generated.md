## Changelog : interop (30 derniers jours, au 4 septembre 2026)

### Résumé
Ce mois a été marqué par l'initialisation du projet et la mise en place d'un environnement de développement local robuste. Les efforts se sont concentrés sur la stabilisation de l'authentification via Keycloak et l'optimisation de l'orchestration des services pour faciliter l'interopérabilité entre les composants de LaSuite.

### Évolutions fonctionnelles
- Intégration du client OIDC pour LaSuite Drive.

### Évolutions techniques
- **Authentification (Keycloak) :**
    - Unification des sous-domaines pour les services front et back-end de Drive.
    - Optimisation de la gestion des URLs de redirection (gestion des sous-domaines et correction du flux de déconnexion pour Menshen).
- **Infrastructure et DevOps :**
    - Initialisation du dépôt et mise en place d'une configuration Docker Compose de base.
    - Amélioration de l'automatisation via l'ajout de règles Makefile (notamment pour la mise à jour des realms).
    - Optimisation de l'environnement de développement local (utilisation de sous-domaines `localhost` et correction de la configuration réseau pour le service `mailcatcher`).
    - Nettoyage de l'architecture par la suppression du service `node`.

### Autres changements
- Mise à jour de la licence et corrections de la documentation (README).
