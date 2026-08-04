## Changelog : accounts (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur le renforcement de la gestion des identités et de la sécurité. Le système supporte désormais plusieurs fournisseurs d'identité et propose des mécanismes de protection accrus pour les données sensibles. Les capacités du serveur d'autorisation ont également été étendues pour offrir plus de flexibilité et de précision dans la gestion des accès.

### Évolutions fonctionnelles
- **Gestion des identités** : support de plusieurs fournisseurs d'identité et gestion améliorée des flux de connexion via les réseaux sociaux (Social Auth).
- **Sécurité** : 
    - Chiffrement des données sensibles (`extra_data`) des fournisseurs d'identité.
    - Sécurisation de la procédure de déconnexion (passage en méthode POST uniquement).
- **Serveur d'autorisation (OIDC)** : 
    - Ajout de la revendication (`claim`) `guest`.
    - Possibilité de personnaliser et configurer le serveur d'autorisation.
    - Amélioration de la résilience de l'endpoint d'introspection avec un mécanisme de repli (fallback) vers les backends PSA.
- **Scopes ProConnect** : ajout des périmètres `siret`, `given_name` et `usual_name`.

### Évolutions techniques
- **Base de données** : adoption des UUID Version 7 pour les clés primaires afin d'optimiser les performances et l'indexation.
- **Gestion du cache** : refonte de l'invalidation du cache pour les backends PSA.
- **Keycloak** : mise à jour et normalisation de la configuration du royaume (`realm.json`).
- **Tests** : 
    - Amélioration de la couverture de tests, notamment sur la gestion des erreurs d'introspection.
    - Optimisation de la configuration par défaut des tests Django.
- **Refactoring** : nettoyage de configurations inutiles (`app_label`).

### Autres changements
- **Documentation** : mise à jour de la documentation concernant les périmètres (scopes) et les revendications (claims) supportés.
- **CI/CD** : stabilisation de l'environnement Node.js pour les processus de traduction (Crowdin) et uniformisation des arguments de version.
