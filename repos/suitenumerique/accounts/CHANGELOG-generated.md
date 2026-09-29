## Changelog : accounts (30 derniers jours, au 24/09/2026)

### Résumé
Ce mois-ci marque le passage en version 0.1.0. Les développements se sont concentrés sur l'amélioration de l'interface utilisateur (nouvelles pages de profil et de connexion) et sur la robustesse du système d'authentification, notamment pour assurer une déconnexion fluide et synchronisée avec les fournisseurs d'identité externes.

### Évolutions fonctionnelles
- **Interface utilisateur** : Ajout d'une page d'accueil de profil, d'une page de connexion intermédiaire et d'un menu utilisateur dans le pied de page.
- **Gestion de la déconnexion** : Amélioration du processus de déconnexion avec le support de la déconnexion initiée par l'application (RP-initiated logout) et la déconnexion automatique auprès des fournisseurs d'identité (IdP) externes.

### Évolutions techniques
- **Authentification & OIDC** : Amélioration de la gestion des flux OIDC (support des requêtes POST pour la déconnexion, transmission du `login_hint`) et mise en place de la génération personnalisée de l'identifiant `sub`.
- **Infrastructure & Environnement** : Mise à jour des outils de développement (Python, Node.js, uv) et ajustement de la récupération des images MinIO.
- **Tests & Qualité** : Amélioration de la fiabilité des tests (isolation des variables d'environnement, suppression des avertissements de compatibilité Django) et ajout d'utilitaires de test.
- **Backend & Core** : Implémentation du suivi (tracking) des événements de connexion/déconnexion et ajout d'utilitaires pour la gestion des URLs et de l'état.
- **Corrections** : Résolution de problèmes de routage pour l'export statique et nettoyage des URIs de redirection Keycloak.

### Autres changements
- Mise à jour des traductions (i18n) et suppression de langues inutilisées dans le frontend.
