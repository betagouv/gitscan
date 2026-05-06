## Changelog : code-du-travail-numerique (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, le projet a connu des améliorations significatives en termes de recherche, avec des ajustements pour une meilleure pertinence des résultats et la gestion de l'historique de navigation. De nouvelles fonctionnalités ont été ajoutées, notamment un quizz sur le code du travail et une page listant les actualités. Des corrections ont également été apportées pour améliorer la stabilité et la qualité du code, ainsi que la gestion des liens et des tests.

### Évolutions fonctionnelles
- Ajout d'un quizz interactif sur le code du travail ([#7261](https://github.com/SocialGouv/code-du-travail-numerique/issues/7261)).
- Amélioration de la recherche : sauvegarde de l'état de la recherche lors des navigations avant/arrière ([#7255](https://github.com/SocialGouv/code-du-travail-numerique/issues/7255)).
- Ajout d'une page listant les actualités du code du travail ([#7205](https://github.com/SocialGouv/code-du-travail-numerique/issues/7205)).
- Mise en avant de la page "Quoi de neuf" ([#7249](https://github.com/SocialGouv/code-du-travail-numerique/issues/7249)).
- Ajout d'une illustration du bulletin de paie sur la page du préavis de démission ([#7210](https://github.com/SocialGouv/code-du-travail-numerique/issues/7210)).
- Correction de liens morts dans les conventions collectives suite à la migration vers le DSFR de legifrance ([#7271](https://github.com/SocialGouv/code-du-travail-numerique/issues/7271)).
- Suppression d'une question inutile sur la date de sortie dans le calculateur d'indemnité de licenciement ([#7236](https://github.com/SocialGouv/code-du-travail-numerique/issues/7236)).
- Ajout d'un avertissement RGPD lors de la saisie de données personnelles dans les commentaires ([#7244](https://github.com/SocialGouv/code-du-travail-numerique/issues/7244)).
- Mise à jour du bandeau cookie RGPD ([#7248](https://github.com/SocialGouv/code-du-travail-numerique/issues/7248)).

### Évolutions techniques
- Migration vers une instance interne d'Elasticsearch pour la production et la préproduction ([#7256](https://github.com/SocialGouv/code-du-travail-numerique/issues/7256)).
- Amélioration de la pertinence de la recherche en ajustant le "boost" des outils ([#7266](https://github.com/SocialGouv/code-du-travail-numerique/issues/7266)).
- Amélioration de la recherche pour une correspondance exacte des thèmes ([#7247](https://github.com/SocialGouv/code-du-travail-numerique/issues/7247)).
- Corrections de tests E2E suite à l'ajout des actualités ([#7220](https://github.com/SocialGouv/code-du-travail-numerique/issues/7220)).
- Mise en place d'un layout masonry grid pour l'affichage des résultats de recherche en horizontal ([#7215](https://github.com/SocialGouv/code-du-travail-numerique/issues/7215)).
- Migration des tests E2E de Cypress vers Playwright ([#7212](https://github.com/SocialGouv/code-du-travail-numerique/issues/7212)).
- Correction de bugs remontés par Sentry ([#7225](https://github.com/SocialGouv/code-du-travail-numerique/issues/7225)).
- Renommage des labels pour les contributions et autres pages ([#7227](https://github.com/SocialGouv/code-du-travail-numerique/issues/7227)).
- Ajout de JSON-LD et mise à jour du sitemap pour améliorer le référencement ([#7224](https://github.com/SocialGouv/code-du-travail-numerique/issues/7224)).
- Gestion des liens d'ancre sans `href` dans les fiches métiers ([#7223](https://github.com/SocialGouv/code-du-travail-numerique/issues/7223)).

### Autres changements
- Correction de problèmes d'affichage des résultats de recherche ([#7219](https://github.com/SocialGouv/code-du-travail-numerique/issues/7219)).
- Correction d'un "mismatch" dans la recherche des définitions ([#7206](https://github.com/SocialGouv/code-du-travail-numerique/issues/7206)).
- Amélioration de la cohérence des messages dans le calculateur d'indemnité de licenciement ([#7237](https://github.com/SocialGouv/code-du-travail-numerique/issues/7237)).
- Ajout d'un pattern pour la recherche d'IDCC et de SIRET ([#7216](https://github.com/SocialGouv/code-du-travail-numerique/issues/7216)).
