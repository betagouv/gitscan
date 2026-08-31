## Changelog : menshen (30 derniers jours, au 25 août 2026)

### Résumé
Les récentes évolutions se sont concentrées sur la stabilisation de l'environnement de développement et l'optimisation des processus d'automatisation (CI/CD). Le projet a également bénéficié d'un nettoyage du code interne pour supprimer des composants d'authentification inutilisés.

### Évolutions techniques
- **Authentification** : Suppression du backend d'authentification OIDC non utilisé.
- **CI/CD & Infrastructure** :
    - Amélioration de la stabilité des builds via le verrouillage des versions (semver) des GitHub Actions liées à Docker.
    - Optimisation du job `gitlint` par l'utilisation de `uvx` et la suppression de la dépendance `requests`.
