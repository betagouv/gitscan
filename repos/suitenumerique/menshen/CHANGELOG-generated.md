## Changelog : menshen (30 derniers jours, au 02/10/2026)

### Résumé
Les récentes évolutions se concentrent sur le renforcement de la sécurité (chiffrement des secrets, nouveau hacheur de mots de passe) et l'amélioration de la robustesse de l'API, notamment pour l'introspection des jetons. L'expérience développeur est également optimisée grâce à une refonte du client et des améliorations de l'environnement de démonstration (Playground).

### Évolutions fonctionnelles
- **Amélioration de l'introspection des jetons** : prise en charge des champs email vides et des jetons d'accès opaques dans les réponses.
- **Gestion des secrets clients** : support des séquences de caractères spéciaux (pourcentage) et ajout d'une option de configuration pour contrôler la complexité des caractères générés.
- **Amélioration du Playground** : ajout d'une variante "ProConnect" et correction des données de démonstration (fixtures).

### Évolutions techniques
- **Sécurité renforcée** : adoption d'Argon2 comme hacheur de mots de passe par défaut et implémentation du chiffrement pour les secrets clients des fournisseurs de services (SP).
- **Optimisation des performances** : réduction des appels de sauvegarde inutiles lors de la gestion des identifiants de fournisseur de services.
- **Refonte du client** : simplification et clarification des noms de classes (`TokenExchangeClient`, `TokenType`, `Configuration`) et migration vers le système de build `uv`.
- **Maintenance backend** : correction de la gestion des types de jetons échangés, restauration de la liste des hacheurs de mots de passe et nettoyage de l'interface d'administration.
- **CI/CD** : correction du workflow de publication des paquets sur PyPI.

### Autres changements
- **Documentation** : ajout de la documentation concernant les actions disponibles depuis les services de la suite.
