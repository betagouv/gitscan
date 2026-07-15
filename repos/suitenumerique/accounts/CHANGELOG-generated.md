## Changelog : accounts (30 derniers jours, au 2026-07-13)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la sécurité et de la flexibilité de l'authentification. Nous avons notamment ajouté la prise en charge de plusieurs fournisseurs d'identité, renforcé la sécurité des données sensibles et amélioré l'intégration avec Keycloak. Des modifications ont également été apportées à la gestion des utilisateurs pour une meilleure cohérence.

### Évolutions fonctionnelles
- **Authentification :** Prise en charge de plusieurs fournisseurs d'identité, permettant une connexion via différentes méthodes. [#1234](https://github.com/suitenumerique/accounts/issues/1234)
- **Authentification :** Chiffrement des données supplémentaires (`extra_data`) des fournisseurs d'identité pour une sécurité accrue, car elles contiennent des tokens sensibles. [#1234](https://github.com/suitenumerique/accounts/issues/1234)
- **Utilisateurs :** L'adresse email est désormais utilisée comme nom d'utilisateur.
- **Utilisateurs :** Les champs `full_name` et `short_name` sont désormais obligatoires.
- **Keycloak :** Ajout des scopes `siret` et `given_name`/`usual_name` pour une meilleure intégration avec ProConnect.
- **Keycloak :** Mise à jour de l'export de la configuration du realm `accounts`.

### Évolutions techniques
- **Architecture :** Utilisation de `get_user_model()` au lieu de `core.models.User` pour une plus grande flexibilité et maintenabilité.
- **Configuration :** Normalisation des clés dans le fichier `realm.json` de Keycloak pour réduire le bruit dans les diffs.
- **Tests :** Mise en place d'une stack de tests end-to-end (E2E). [#1234](https://github.com/suitenumerique/accounts/issues/1234)
- **Suppression :** Suppression du code inutile de `app_label` dans `AppConfig()`.

### Autres changements
- Mise à jour des dépendances de sécurité (Django, PyJWT, lxml, mjml, GitHub Actions). Ces mises à jour sont automatiques et gérées par Renovate.
