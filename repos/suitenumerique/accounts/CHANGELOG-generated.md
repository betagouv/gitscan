## Changelog : accounts (30 derniers jours, au 27 juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'authentification et de la gestion des utilisateurs, notamment avec l'ajout de la prise en charge de multiples fournisseurs d'identité et la configuration avancée du serveur d'autorisation OIDC. Des corrections de sécurité et des améliorations de la robustesse ont également été apportées.

### Évolutions fonctionnelles
- Prise en charge de plusieurs fournisseurs d'identité pour l'authentification [#2345](https://github.com/suitenumerique/accounts/issues/2345).
- L'adresse email est désormais utilisée comme nom d'utilisateur.
- Ajout d'un claim "guest" pour le serveur d'autorisation OIDC.
- La vue de déconnexion nécessite désormais une requête POST pour plus de sécurité.
- Gestion améliorée des vues de connexion Social Auth nécessitant des requêtes POST.
- Possibilité de récupérer des informations supplémentaires (scopes `given_name`, `usual_name` et `siret`) depuis Keycloak/ProConnect.

### Évolutions techniques
- Configuration et personnalisation du serveur d'autorisation OIDC.
- L'endpoint d'introspection peut désormais retomber sur les backends PSA.
- Chiffrement des données supplémentaires des fournisseurs d'identité (contenant des tokens) pour renforcer la sécurité.
- Utilisation de `get_user_model()` au lieu de `core.models.User` pour une meilleure flexibilité.
- Ajout de `pytest.mark.django_db` par défaut pour les tests.
- Suppression d'un `app_label` inutile dans la configuration des applications.
- Mise à jour de la configuration du realm Keycloak.
- Configuration explicite de Node.js pour les workflows CrowdIn.
- Rétour à Node.js 22.x pour `i18next-parser` afin de corriger des problèmes de CI.

### Autres changements
- Correction de la référence au dépôt `docs` dans le changelog.
- Documentation des scopes et claims supportés.
- Mises à jour de sécurité des dépendances : Django, PyJWT, lxml, mjml, GitHub Actions et pytest.
- Normalisation des clés dans le fichier `realm.json` de Keycloak pour réduire le bruit dans les diffs.
- Les champs `full_name` et `short_name` des utilisateurs ne sont plus autorisés à être nuls.
