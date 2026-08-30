## Changelog : interop (30 derniers jours, au 28 août 2026)

### Résumé
Ce mois-ci a été consacré à l'initialisation du projet et à la mise en place de l'environnement de développement. Les efforts se sont concentrés sur l'orchestration des services via Docker, la configuration des mécanismes d'authentification et l'automatisation de certaines tâches pour faciliter le travail des développeurs.

### Évolutions techniques
- **Infrastructure et conteneurisation** : Initialisation de la configuration Docker Compose, ajout d'un réseau pour le service `mailcatcher` et suppression du service `node`.
- **Authentification** : Configuration du client OIDC pour LaSuite Drive et harmonisation des sous-domaines Keycloak pour les services front et back de Drive.
- **Environnement de développement** : Mise en place de sous-domaines `localhost`, configuration des URLs locales pour les services Menshen et ajout d'une commande `realm-update` dans le Makefile pour simplifier la gestion des environnements.

### Autres changements
- Documentation : Correction de fautes de frappe dans le README.
- Légal : Mise à jour du copyright de la licence.
