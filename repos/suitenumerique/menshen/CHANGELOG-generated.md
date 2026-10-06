## Changelog : menshen (30 derniers jours, au 02 octobre 2026)

### Résumé
Les récentes évolutions se concentrent sur le renforcement de la sécurité (chiffrement et hachage), l'amélioration de la robustesse de l'API lors de l'introspection de jetons et une simplification de l'utilisation de la bibliothèque client pour les développeurs.

### Évolutions fonctionnelles
- **Flexibilité de l'API** : prise en charge des champs email vides et des types de jetons d'accès opaques lors des réponses d'introspection.
- **Gestion des secrets clients** : ajout d'une option de configuration pour l'utilisation de caractères spéciaux et support des séquences de pourcentage dans les secrets.
- **Environnement de test** : enrichissement du playground avec une nouvelle variante "proconnect" et correction des données de démonstration.

### Évolutions techniques
- **Sécurité renforcée** : 
    - Adoption d'Argon2 comme algorithme de hachage de mot de passe par défaut.
    - Mise en place du chiffrement pour les secrets clients des fournisseurs de services (SP).
    - Restauration de la gestion de la liste des hachages de mots de passe.
- **Refactoring du client** : simplification et clarification des noms de classes pour une meilleure ergonomie (ex: `TokenExchangeClient` au lieu de `MenshenClient`).
- **Optimisation et maintenance** : 
    - Réduction des appels inutiles à la base de données lors de la sauvegarde des identifiants de service.
    - Nettoyage de l'interface d'administration Django.
- **Infrastructure et Build** : 
    - Migration vers le système de build `uv`.
    - Correction du workflow de publication des paquets sur PyPI.

### Autres changements
- **Documentation** : ajout de la documentation relative aux actions disponibles depuis les services de la suite.
