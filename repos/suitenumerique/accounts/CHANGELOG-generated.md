## Changelog : accounts (30 derniers jours, au 14 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de nouvelles pages d'interface (profil et connexion intermédiaire) et une gestion plus fluide et sécurisée des déconnexions. Le socle technique a également été renforcé par des optimisations de l'authentification OIDC et une mise à jour des environnements de développement et d'infrastructure.

### Évolutions fonctionnelles
- **Interface utilisateur** :
    - Ajout d'une page d'accueil pour le profil utilisateur.
    - Ajout d'une page de connexion intermédiaire.
    - Correction des routes d'export statique du frontend pour assurer une navigation fluide.
- **Gestion des sessions** :
    - Amélioration du processus de déconnexion : support de la déconnexion initiée par le client (RP-initiated logout) et déconnexion automatique des fournisseurs d'identité externes (upstream IdP).
    - Transmission de la confirmation de déconnexion vers l'interface utilisateur.

### Évolutions techniques
- **Authentification & OIDC** :
    - Optimisation du protocole OIDC : génération d'identifiants `sub` personnalisés, transmission du `login_hint` et amélioration de la gestion des paramètres d'introspection.
    - Nettoyage et correction des URIs de redirection pour Keycloak.
- **Infrastructure & Environnement** :
    - Mise à jour des images de base (MinIO) et des outils de gestion de projet (Python et `uv`).
    - Fixation de la version Node.js pour garantir la stabilité du frontend.
- **Core & Tests** :
    - Ajout d'utilitaires internes pour la gestion des URLs et des états (state).
    - Amélioration de la robustesse des tests : suppression des avertissements de compatibilité Django et optimisation de la gestion des paramètres de requête.
