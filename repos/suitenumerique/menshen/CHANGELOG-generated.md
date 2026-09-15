## Changelog : menshen (30 derniers jours, au 01/09/2026)

### Résumé
Les récentes évolutions améliorent la flexibilité de l'introspection des jetons et l'utilisation de l'interface de test (playground), tout en renforçant la stabilité et l'efficacité des processus de déploiement automatisés.

### Évolutions fonctionnelles
- Prise en charge des types de jetons introspectés "bearer" ou "mac".
- Amélioration de l'outil de test (playground) permettant l'envoi de contenus encodés en formulaire (form-encoded).

### Évolutions techniques
- Suppression du backend d'authentification OIDC.
- Optimisation de la CI/CD : verrouillage des versions (semver) des actions GitHub liées à Docker et optimisation du job `gitlint` via l'utilisation de `uvx` et la suppression de la dépendance `requests`.

### Autres changements
- Correction de problèmes de linting suite aux mises à jour de dépendances.
