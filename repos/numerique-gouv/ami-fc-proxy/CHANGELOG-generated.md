## Changelog : ami-fc-proxy (30 derniers jours, au 26 mai 2026)

### Résumé
Ce changelog décrit les améliorations apportées au proxy FranceConnect au cours du dernier mois. Les principaux changements concernent l'implémentation du support pour l'API FranceConnect Identity (ami-fi), notamment la gestion des endpoints d'autorisation, de token, d'information utilisateur et de déconnexion. Des corrections ont également été apportées pour assurer la compatibilité avec les déploiements sur Scalingo.

### Évolutions fonctionnelles
- Implémentation du proxy pour l'endpoint de déconnexion FranceConnect Identity ([#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)).
- Implémentation du proxy pour l'endpoint d'information utilisateur FranceConnect Identity ([#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)).
- Implémentation du proxy pour l'endpoint de token FranceConnect Identity ([#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)).
- Implémentation du proxy pour l'endpoint d'autorisation FranceConnect Identity ([#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)).
- L'URL de callback d'autorisation est maintenant configurée pour mapper le code et l'origine de la requête ([#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)).

### Évolutions techniques
- Utilisation de `FileStore` pour le stockage des fichiers ([#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)).
- Amélioration de la gestion des données POST pour l'endpoint de token FranceConnect Identity, en utilisant l'encodage URL et en envoyant les données correctement ([#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)).
- Ajout d'une gestion des exceptions pour l'endpoint de token FranceConnect Identity ([#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)).
- Corrections pour assurer la compatibilité des déploiements sur Scalingo, notamment la suppression du buildpack Heroku uv ([#2](https://github.com/numerique-gouv/ami-fc-proxy/pull/2)).

### Autres changements
- Stockage de l'origine de la requête dans l'endpoint `authorize-request` ([#708](https://github.com/numerique-gouv/ami-fc-proxy/pull/708)).
