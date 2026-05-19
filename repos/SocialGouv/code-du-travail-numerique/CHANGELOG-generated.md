## Changelog : code-du-travail-numerique (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la recherche, la correction de bugs et l'ajout de nouvelles fonctionnalités comme un quizz sur le code du travail. Des améliorations ont également été apportées à la gestion des données personnelles (RGPD) et à la robustesse de l'application grâce à la correction d'erreurs remontées par Sentry. Une migration vers une instance interne d'Elasticsearch a été initiée.

### Évolutions fonctionnelles
- Ajout d'un quizz sur le code du travail pour une meilleure compréhension des règles. [#7261](https://github.com/SocialGouv/code-du-travail-numerique/issues/7261)
- Amélioration de la recherche : sauvegarde de l'état de la recherche lors des navigations avant/arrière. [#7255](https://github.com/SocialGouv/code-du-travail-numerique/issues/7255)
- Mise en avant de la page "Quoi de neuf" pour une meilleure visibilité des nouveautés. [#7249](https://github.com/SocialGouv/code-du-travail-numerique/issues/7249)
- Ajout d'un avertissement lors de la saisie de données personnelles dans les commentaires pour renforcer la conformité RGPD. [#7244](https://github.com/SocialGouv/code-du-travail-numerique/issues/7244)
- Mise à jour du bandeau cookie pour une meilleure information des utilisateurs concernant le RGPD. [#7248](https://github.com/SocialGouv/code-du-travail-numerique/issues/7248)
- Correction d'un bug empêchant l'ouverture correcte d'un accordéon dans la section "contribution". [#7278](https://github.com/SocialGouv/code-du-travail-numerique/issues/7278)
- Ajout de l'inaptitude non professionnelle pour le calcul du préavis de licenciement. [#7275](https://github.com/SocialGouv/code-du-travail-numerique/issues/7275)
- Suppression de la question sur la date de sortie pour le motif de licenciement 3239 dans le simulateur d'indemnités de licenciement. [#7236](https://github.com/SocialGouv/code-du-travail-numerique/issues/7236)
- Correction de liens morts dans les conventions collectives suite à la migration vers le DSFR de Légifrance. [#7271](https://github.com/SocialGouv/code-du-travail-numerique/issues/7271)

### Évolutions techniques
- Migration vers une instance interne d'Elasticsearch pour une meilleure performance et contrôle. [#7256](https://github.com/SocialGouv/code-du-travail-numerique/issues/7256)
- Amélioration de la recherche : ajustement du "boost" pour les outils afin d'améliorer la pertinence des résultats. [#7266](https://github.com/SocialGouv/code-du-travail-numerique/issues/7266)
- Amélioration de la recherche : mise à jour de la requête Elasticsearch pour améliorer le "boost" des contributions. [#7229](https://github.com/SocialGouv/code-du-travail-numerique/issues/7229) et [#7217](https://github.com/SocialGouv/code-du-travail-numerique/issues/7217) [#7246](https://github.com/SocialGouv/code-du-travail-numerique/issues/7246)
- Correction d'erreurs remontées par Sentry pour améliorer la stabilité de l'application. [#7225](https://github.com/SocialGouv/code-du-travail-numerique/issues/7225)
- Mise à jour des tests E2E pour assurer la qualité du code. [#7267](https://github.com/SocialGouv/code-du-travail-numerique/issues/7267)

### Autres changements
- Ajout de logs pour faciliter le débogage de la connexion à Elasticsearch.
- Correction de l'URL d'Elasticsearch pour l'environnement de pré-production.
- Implémentation d'un A/B testing sur les labels de recherche pour les contributions. [#7243](https://github.com/SocialGouv/code-du-travail-numerique/issues/7243)
