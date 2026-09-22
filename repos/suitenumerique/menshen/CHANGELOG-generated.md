## Changelog : menshen (30 derniers jours, au 21 septembre 2026)

### Résumé
Ce mois-ci, menshen a franchi une étape importante avec le passage à la version 0.3.0. Les efforts se sont concentrés sur le renforcement de la sécurité (chiffrement des secrets et nouveaux standards de hachage) et sur la clarification de l'interface de programmation (SDK client) pour rendre l'intégration plus intuitive pour les développeurs.

### Évolutions fonctionnelles
- **Sécurité des secrets :** Amélioration de la gestion des secrets clients, incluant désormais le support des séquences de pourcentage et le chiffrement des secrets des fournisseurs de services (SP).
- **Gestion des jetons :** Support étendu des types de jetons introspectés (bearer ou MAC).
- **Outil de test (Playground) :** Amélioration de l'expérience de test permettant l'envoi de contenus encodés en formulaire.

### Évolutions techniques
- **Sécurité renforcée :** Adoption d'Argon2 comme algorithme de hachage par défaut pour les mots de passe.
- **Refactoring du client :** Simplification de l'API du client pour une meilleure clarté (renommage de `MenshenClient` en `TokenExchangeClient` et simplification des autres classes de configuration).
- **Optimisation des performances :** Réduction des appels inutiles à la base de données lors de la gestion des identifiants des fournisseurs de services.
- **Infrastructure et CI/CD :** 
    - Migration vers le système de build `uv` pour le client.
    - Optimisation des workflows GitHub Actions (publication PyPI, gestion des versions Docker et amélioration du linting).
- **Nettoyage de l'architecture :** Suppression de l'ancien backend d'authentification OIDC et mise à jour des choix de types de jetons échangés.

### Autres changements
- **Documentation :** Ajout de la documentation concernant les actions disponibles depuis les services de la suite.
- **Maintenance :** Correction des fixtures de démonstration dans le playground et résolution de problèmes de linting suite aux mises à jour de version.
