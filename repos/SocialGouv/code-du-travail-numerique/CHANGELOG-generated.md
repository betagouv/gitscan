## Changelog : code-du-travail-numerique (30 derniers jours, au 21 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la recherche, la correction de bugs et l'ajout de nouvelles fonctionnalités comme un quizz sur le code du travail et un support pour les modifications du SMIC dans les contributions. Des optimisations techniques ont également été apportées, notamment concernant l'instance Elasticsearch utilisée par l'application.

### Évolutions fonctionnelles
- **Recherche :** Amélioration de la pertinence des résultats de recherche, notamment pour les définitions et les outils, avec un ajustement des seuils de "fuzziness" et de "boost". [#7265](https://github.com/SocialGouv/code-du-travail-numerique/issues/7265), [#7266](https://github.com/SocialGouv/code-du-travail-numerique/issues/7266), [#7229](https://github.com/SocialGouv/code-du-travail-numerique/issues/7229), [#7217](https://github.com/SocialGouv/code-du-travail-numerique/issues/7217), [#7246](https://github.com/SocialGouv/code-du-travail-numerique/issues/7246)
- **Contributions :** Support du challenger pour les modifications du SMIC sur les contributions. [#7284](https://github.com/SocialGouv/code-du-travail-numerique/issues/7284)
- **Outils :** Ajout de la prise en compte de l'inaptitude non professionnelle pour le préavis de licenciement. [#7275](https://github.com/SocialGouv/code-du-travail-numerique/issues/7275)
- **Quizz :** Ajout d'un quizz sur le code du travail. [#7261](https://github.com/SocialGouv/code-du-travail-numerique/issues/7261)
- **Page "Quoi de neuf" :** Mise en avant de la page "Quoi de neuf". [#7249](https://github.com/SocialGouv/code-du-travail-numerique/issues/7249)
- **A/B Testing :** Mise en place d'un A/B testing sur les labels pour les contributions. [#7243](https://github.com/SocialGouv/code-du-travail-numerique/issues/7243)

### Évolutions techniques
- **Elasticsearch :** Migration vers une instance interne d'Elasticsearch pour améliorer la performance et la stabilité. [#7256](https://github.com/SocialGouv/code-du-travail-numerique/issues/7256)
- **Elasticsearch (Preprod) :** Correction de l'URL d'Elasticsearch pour l'environnement de préproduction et utilisation de l'instance interne.
- **Tests E2E :** Mise à jour des tests end-to-end (E2E). [#7267](https://github.com/SocialGouv/code-du-travail-numerique/issues/7267)
- **Liens morts :** Correction de liens morts suite à la migration vers le DSFR de legifrance. [#7271](https://github.com/SocialGouv/code-du-travail-numerique/issues/7271)

### Autres changements
- **Correction d'un bug :** Correction de l'ouverture incorrecte d'un accordéon dans la section des contributions. [#7278](https://github.com/SocialGouv/code-du-travail-numerique/issues/7278)
- **Logs :** Ajout de logs pour la connexion à Elasticsearch.
- **Navigation :** Sauvegarde du state de la recherche lors des navigations avant/arrière. [#7255](https://github.com/SocialGouv/code-du-travail-numerique/issues/7255)
- **Recherche :** Amélioration de la correspondance exacte pour les thèmes de pré-recherche. [#7247](https://github.com/SocialGouv/code-du-travail-numerique/issues/7247)
