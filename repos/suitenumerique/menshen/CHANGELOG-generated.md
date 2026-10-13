## Changelog : menshen (30 derniers jours, au 02/10/2026)

### Résumé
Les récentes évolutions se concentrent sur le renforcement de la sécurité (chiffrement des secrets et nouveaux algorithmes de hachage), l'amélioration de la robustesse de l'API lors de l'introspection de jetons et une simplification de la bibliothèque client pour une meilleure expérience développeur.

### Évolutions fonctionnelles
- **Amélioration de l'introspection** : support des champs email vides et des jetons d'accès opaques dans les réponses d'introspection.
- **Gestion des secrets clients** : support des caractères spéciaux (séquences de pourcentage) et ajout d'une option de configuration (`use_special_chars`) pour contrôler la complexité de génération des secrets.
- **Environnement de test** : ajout d'une variante "proconnect" dans le playground pour faciliter les démonstrations.

### Évolutions techniques
- **Sécurité renforcée** : 
    - Adoption d'Argon2 comme algorithme de hachage de mot de passe par défaut.
    - Mise en place du chiffrement pour les secrets clients des fournisseurs de services (SP).
    - Restauration de la liste des hacheurs de mots de passe.
- **Optimisation des performances** : réduction des appels inutiles à la base de données lors de la gestion des identifiants des fournisseurs de services.
- **Refactorisation du client** : simplification et clarification des noms de classes (ex: `MenshenClient` devient `TokenExchangeClient`, `MenshenConfiguration` devient `Configuration`).
- **Infrastructure et Build** : 
    - Migration vers le système de build `uv`.
    - Correction du workflow de publication des paquets sur PyPI.

### Autres changements
- **Documentation** : ajout de la documentation concernant les actions disponibles via les services `lasuite`.
- **Maintenance** : nettoyage de l'interface d'administration (suppression de propriétés inconnues) et correction des données de test (fixtures) du playground.
