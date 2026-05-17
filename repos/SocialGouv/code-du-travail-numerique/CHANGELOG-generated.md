## Changelog : code-du-travail-numerique (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la recherche, la correction de bugs et l'ajout de nouvelles fonctionnalités comme un quizz sur le code du travail. Des efforts ont également été faits pour la conformité RGPD et la surveillance des erreurs via Sentry. Une migration vers une instance interne d'Elasticsearch a été initiée pour améliorer la performance et la stabilité.

### Évolutions fonctionnelles
- Ajout d'un quizz sur le code du travail pour une meilleure compréhension des droits et obligations. [#7261](https://github.com/SocialGouv/code-du-travail-numerique/issues/7261)
- Amélioration de la recherche :
    - Sauvegarde de l'état de la recherche lors des navigations avant/arrière. [#7255](https://github.com/SocialGouv/code-du-travail-numerique/issues/7255)
    - Ajustement du "boost" (importance) des outils dans les résultats de recherche. [#7266](https://github.com/SocialGouv/code-du-travail-numerique/issues/7266)
    - Correction de la recherche exacte pour les thèmes de pré-recherche. [#7247](https://github.com/SocialGouv/code-du-travail-numerique/issues/7247)
- Mise en avant de la page "Quoi de neuf" pour une meilleure visibilité des nouveautés. [#7249](https://github.com/SocialGouv/code-du-travail-numerique/issues/7249)
- Amélioration de la conformité RGPD :
    - Ajout d'un avertissement lors de la saisie de données personnelles dans les commentaires. [#7244](https://github.com/SocialGouv/code-du-travail-numerique/issues/7244)
    - Mise à jour du bandeau cookie pour une meilleure information des utilisateurs. [#7248](https://github.com/SocialGouv/code-du-travail-numerique/issues/7248)
- Correction de liens morts dans les conventions collectives suite à la migration vers le DSFR de legifrance. [#7271](https://github.com/SocialGouv/code-du-travail-numerique/issues/7271)
- Correction d'un bug empêchant l'ouverture correcte des accordéons dans la section "contribution". [#7278](https://github.com/SocialGouv/code-du-travail-numerique/issues/7278)
- Ajout de l'inaptitude non professionnelle pour le calcul du préavis de licenciement. [#7275](https://github.com/SocialGouv/code-du-travail-numerique/issues/7275)
- Suppression d'une question inutile sur la date de sortie dans le formulaire d'indemnité de licenciement (3239). [#7236](https://github.com/SocialGouv/code-du-travail-numerique/issues/7236)
- Amélioration de la cohérence du message dans la description du formulaire d'indemnité de licenciement. [#7237](https://github.com/SocialGouv/code-du-travail-numerique/issues/7237)

### Évolutions techniques
- Migration vers une instance interne d'Elasticsearch pour améliorer la performance et la stabilité de la recherche. [#7256](https://github.com/SocialGouv/code-du-travail-numerique/issues/7256)
- Correction des erreurs remontées par Sentry pour une meilleure surveillance de l'application. [#7225](https://github.com/SocialGouv/code-du-travail-numerique/issues/7225)
- Mise en place d'un A/B Testing sur les labels pour les contributions afin d'optimiser la recherche. [#7243](https://github.com/SocialGouv/code-du-travail-numerique/issues/7243)
- Mise à jour des tests E2E pour assurer la qualité de l'application. [#7267](https://github.com/SocialGouv/code-du-travail-numerique/issues/7267)
