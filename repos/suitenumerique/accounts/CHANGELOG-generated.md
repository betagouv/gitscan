## Changelog : accounts (30 derniers jours, au 24 septembre 2026)

### Résumé
Ce mois a été marqué par le passage à la version 0.1.0. L'expérience utilisateur s'enrichit avec l'arrivée de nouvelles pages (profil, connexion intermédiaire) et d'un menu utilisateur plus accessible. Le système d'authentification a été considérablement renforcé pour offrir une gestion de la déconnexion plus fluide et sécurisée, tout en améliorant la visibilité technique via un nouveau système de suivi des événements.

### Évolutions fonctionnelles
- **Amélioration de l'interface utilisateur** : ajout d'une page d'accueil pour le profil utilisateur, d'une page de connexion intermédiaire et d'un menu utilisateur dans le pied de page.
- **Gestion de la déconnexion** : support de la déconnexion initiée par l'application (RP-initiated logout), permettant de se déconnecter simultanément de l'application et du fournisseur d'identité (IdP) pour une sécurité accrue.

### Évolutions techniques
- **Authentification et OIDC** : 
    - Génération d'identifiants `sub` propres au système.
    - Support du paramètre `login_hint` vers les fournisseurs d'identité amont.
    - Configuration des niveaux d'assurance (ACR) pour le backend ProConnect.
    - Optimisation de la gestion des URI de redirection dans Keycloak.
- **Backend et Monitoring** : 
    - Mise en place du suivi (tracking) des événements de connexion, de déconnexion et des événements OIDC.
    - Ajout d'utilitaires pour la gestion des états (state) et des URLs.
- **Infrastructure et DevOps** : 
    - Mise à jour de l'environnement de développement (Python 3.14.7 et `uv`).
    - Ajustement des sources d'images pour MinIO.
    - Clarification des paramètres de déploiement concernant la mutabilité de `sub`.
- **Tests et Qualité** : 
    - Meilleure isolation des tests par rapport aux variables d'environnement.
    - Suppression des avertissements de dépréciation (Django 7.0) pour stabiliser les logs de test.
- **Frontend** : 
    - Correction des routes pour assurer le bon fonctionnement de l'export statique.
    - Verrouillage de la version Node.js pour garantir la stabilité des outils de traduction.

### Autres changements
- **Internationalisation** : mise à jour des chaînes de caractères traduites.
- **Nettoyage** : suppression des langues inutilisées dans le frontend.
