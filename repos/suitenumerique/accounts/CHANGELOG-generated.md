## Changelog : accounts (30 derniers jours, au 01/10/2026)

### Résumé
Ce mois a été marqué par le passage en version 0.1.0. L'expérience utilisateur a été enrichie par l'ajout de nouvelles pages (profil, connexion intermédiaire) et d'éléments d'interface plus intuitifs. Parallèlement, des efforts importants ont été consacrés à la sécurisation du système d'authentification et à l'amélioration de la surveillance des événements de connexion.

### Évolutions fonctionnelles
- **Interface utilisateur** : Ajout d'une page d'accueil pour le profil utilisateur et d'un menu utilisateur dans le pied de page.
- **Parcours de connexion** : Introduction d'une page de connexion intermédiaire pour fluidifier l'expérience.
- **Internationalisation** : Mise à jour des chaînes traduites et suppression des langues inutilisées.

### Évolutions techniques
- **Sécurité et Authentification** :
    - Mise en œuvre des meilleures pratiques de sécurité RFC 9700.
    - Amélioration de la gestion des déconnexions : support du "RP-initiated logout" et synchronisation de la déconnexion avec le fournisseur d'identité (IdP) amont.
    - Optimisations OIDC : gestion des requêtes POST pour la déconnexion, transfert du `login_hint` et génération de `sub` personnalisés.
    - Correction des URIs de redirection pour Keycloak.
- **Observabilité et Core** :
    - Mise en place du suivi (tracking) des événements d'authentification Django et des événements OIDC (connexion/déconnexion).
    - Ajout d'utilitaires de gestion pour les états (state) et les URLs.
- **Infrastructure et Déploiement** :
    - Mise à jour de la configuration Helm (ajout de labels et de jobs de nettoyage).
    - Migration de MinIO vers `pgsty/silo`.
    - Mise à jour des environnements de développement (Python, UV, Node.js).
- **Tests** :
    - Amélioration de la fiabilité des tests par l'isolation des variables d'environnement et la suppression des avertissements de compatibilité Django.

### Autres changements
- Mise à jour de la documentation Helm.
