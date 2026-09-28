## Changelog : menshen (30 derniers jours, au 23 septembre 2026)

### Résumé
Les récentes évolutions se concentrent sur le renforcement de la sécurité et la robustesse de l'API. Le serveur supporte désormais mieux les différents types de jetons et propose des mécanismes de chiffrement pour les secrets. Le client a également été simplifié pour offrir une meilleure expérience de développement.

### Évolutions fonctionnelles
- **Amélioration de l'introspection des jetons** : support étendu des types de jetons (bearer ou MAC), des jetons d'accès opaques et gestion des réponses contenant des champs email vides.
- **Gestion sécurisée des secrets** : support des secrets clients contenant des séquences de caractères spéciaux (%) et ajout d'une option de configuration pour contrôler la complexité de leur génération.
- **Protection des données** : ajout du support du chiffrement pour les secrets clients des fournisseurs de services (SP).

### Évolutions techniques
- **Sécurité** : adoption d'Argon2 comme algorithme de hachage de mot de passe par défaut.
- **Performance** : optimisation de l'enregistrement des identifiants des fournisseurs de services en évitant des appels inutiles à la base de données.
- **Refactorisation du client** : simplification de l'API client via le renommage de classes pour plus de clarté (ex: `MenshenClient` devient `TokenExchangeClient`) et migration vers le système de build `uv`.
- **CI/CD** : correction du workflow de publication des paquets sur PyPI.

### Autres changements
- **Documentation** : ajout de la documentation concernant les actions disponibles pour les services de la suite.
- **Environnement de test** : amélioration du playground avec la correction des données de test (fixtures) et le support de l'envoi de contenu encodé en formulaire.
- **Maintenance** : correction de problèmes de linting suite aux mises à jour de version.
