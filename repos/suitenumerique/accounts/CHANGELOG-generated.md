## Changelog : accounts (30 derniers jours, au 28 juillet 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la sécurité, l'authentification et la configuration des fournisseurs d'identité (Keycloak notamment). Des correctifs ont été apportés pour supporter plusieurs fournisseurs d'identité et améliorer la robustesse de l'authentification, ainsi que des optimisations pour l'intégration avec Keycloak. Des changements techniques ont également été effectués pour améliorer la sécurité et la gestion des clés primaires.

### Évolutions fonctionnelles
- Ajout de la prise en charge de plusieurs fournisseurs d'identité pour l'authentification. [#1234](https://github.com/suitenumerique/accounts/issues/1234)
- Configuration et personnalisation de l'autorisation server (OIDC Provider).
- Ajout d'un claim "guest" pour l'OIDC Provider.
- Amélioration de la gestion des erreurs lors de l'introspection de l'OIDC Provider, avec un fallback vers les backends PSA.
- Le logout est désormais accessible uniquement via une requête POST, renforçant la sécurité.
- Prise en charge des vues de connexion de Social Auth nécessitant des requêtes POST.
- Chiffrement des données supplémentaires (`extra_data`) des fournisseurs d'identité, car elles contiennent des tokens sensibles.
- Ajout des scopes `given_name` et `usual_name` pour ProConnect dans Keycloak.

### Évolutions techniques
- Utilisation de UUID version 7 pour les clés primaires des modèles, améliorant la sécurité et la performance.
- Refonte des tests pour l'invalidation du cache des backends PSA.
- Ajout de `pytest.mark.django_db` par défaut pour les tests.
- Mise à jour de la version de Node.js utilisée pour les workflows CrowdIn (retour à la version 22.x).
- Suppression du code inutile de `app_label` dans `AppConfig()`.
- Mise à jour des dépendances de sécurité : Django, PyJWT, lxml, pytest, mjml et GitHub Actions.

### Autres changements
- Mise à jour de l'export du realm Keycloak (`realm.json`) pour une meilleure lisibilité.
- Correction de la référence au dépôt `docs` dans le changelog.
- Normalisation des clés dans le fichier `realm.json` de Keycloak pour réduire le bruit dans les diffs.
- Documentation des scopes et claims supportés.
