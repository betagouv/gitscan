## Changelog : code-du-travail-numerique (30 derniers jours, au 5 mai 2026)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en termes de recherche, avec notamment une meilleure gestion de l'historique de navigation et un ajustement du système de boost des résultats. De nouvelles fonctionnalités ont été ajoutées, comme un quizz sur le code du travail et une mise en avant de la page "Quoi de neuf". Des corrections ont également été apportées pour améliorer la stabilité et la conformité du site, notamment concernant les liens brisés, les erreurs remontées par Sentry et la gestion des données personnelles (RGPD).

### Évolutions fonctionnelles
- Ajout d'un quizz sur le code du travail, permettant aux utilisateurs de tester leurs connaissances. ([#7261](https://github.com/SocialGouv/code-du-travail-numerique/issues/7261))
- Mise en avant de la page "Quoi de neuf" pour une meilleure visibilité des nouveautés. ([#7249](https://github.com/SocialGouv/code-du-travail-numerique/issues/7249))
- Amélioration de la recherche : sauvegarde de l'état de la recherche lors des navigations avant/arrière. ([#7255](https://github.com/SocialGouv/code-du-travail-numerique/issues/7255))
- Correction de liens morts dans les conventions collectives suite à la migration vers le DSFR de legifrance. ([#7271](https://github.com/SocialGouv/code-du-travail-numerique/issues/7271))
- Ajout d'un warning lors de la saisie de données personnelles dans les commentaires, pour renforcer la conformité RGPD. ([#7244](https://github.com/SocialGouv/code-du-travail-numerique/issues/7244))
- Mise à jour du bandeau cookie pour améliorer l'information sur l'utilisation des cookies. ([#7248](https://github.com/SocialGouv/code-du-travail-numerique/issues/7248))
- Suppression d'une question inutile sur la date de sortie dans le formulaire d'indemnité de licenciement (3239). ([#7236](https://github.com/SocialGouv/code-du-travail-numerique/issues/7236))

### Évolutions techniques
- Migration vers une instance interne d'Elasticsearch (ES) pour améliorer la performance et la stabilité de la recherche. ([#7256](https://github.com/SocialGouv/code-du-travail-numerique/issues/7256))
- Amélioration de la requête Elasticsearch pour mieux booster les contributions. ([#7229](https://github.com/SocialGouv/code-du-travail-numerique/issues/7229), [#7217](https://github.com/SocialGouv/code-du-travail-numerique/issues/7217), [#7246](https://github.com/SocialGouv/code-du-travail-numerique/issues/7246))
- Correction de l'URL Elasticsearch pour l'environnement de pré-production.
- Ajout de logs pour faciliter le débogage des problèmes de connexion à Elasticsearch.
- Correction de plusieurs erreurs remontées par Sentry pour améliorer la stabilité de l'application. ([#7225](https://github.com/SocialGouv/code-du-travail-numerique/issues/7225))
- Amélioration de la cohérence des messages dans le formulaire d'indemnité de licenciement. ([#7237](https://github.com/SocialGouv/code-du-travail-numerique/issues/7237))

### Autres changements
- Mise en place d'un A/B testing sur les labels des contributions pour optimiser la recherche. ([#7243](https://github.com/SocialGouv/code-du-travail-numerique/issues/7243))
- Correction d'un problème d'exact match pour la recherche thématique. ([#7247](https://github.com/SocialGouv/code-du-travail-numerique/issues/7247))
