## Changelog : euphrosyne (30 derniers jours, au 27 août 2026)

### Résumé
Les interventions récentes ont principalement porté sur la résolution d'un problème d'accès lié à l'authentification ORCID et sur la stabilisation des outils de vérification de la qualité du code.

### Évolutions fonctionnelles
- Correction d'une régression empêchant la connexion via le fournisseur ORCID [#1988](https://github.com/betagouv/euphrosyne/pull/1988).

### Évolutions techniques
- Rectification de la méthode de soumission de l'authentification ORCID (passage en POST) pour rétablir le service.
- Résolution d'erreurs liées à l'outil de vérification de code `pylint-django`.
