## Changelog : code-du-travail-numerique (30 derniers jours, au 30 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la recherche, l'ajout de nouvelles fonctionnalités comme un quizz sur le code du travail et la page "Quoi de neuf", ainsi que des corrections de bugs et des optimisations techniques, notamment concernant l'infrastructure de recherche et la gestion des erreurs.

### Évolutions fonctionnelles
- Ajout d'un quizz interactif pour tester ses connaissances sur le code du travail. ([#7261](https://github.com/SocialGouv/code-du-travail-numerique/issues/7261))
- Amélioration de la recherche : sauvegarde de l'état de la recherche lors des navigations avant/arrière. ([#7255](https://github.com/SocialGouv/code-du-travail-numerique/issues/7255))
- Mise en avant de la page "Quoi de neuf" pour une meilleure visibilité des nouveautés. ([#7249](https://github.com/SocialGouv/code-du-travail-numerique/issues/7249))
- Ajout d'une illustration du bulletin de paie sur la page du préavis de démission. ([#7210](https://github.com/SocialGouv/code-du-travail-numerique/issues/7210))
- Amélioration de la recherche pour une meilleure correspondance exacte des thèmes. ([#7247](https://github.com/SocialGouv/code-du-travail-numerique/issues/7247))
- Correction d'un problème de redirection automatique vers la convention collective après sauvegarde. ([#7203](https://github.com/SocialGouv/code-du-travail-numerique/issues/7203))
- Suppression d'une question inutile sur la date de sortie dans le simulateur d'indemnité de licenciement. ([#7236](https://github.com/SocialGouv/code-du-travail-numerique/issues/7236))

### Évolutions techniques
- Migration vers une instance interne du moteur de recherche Elasticsearch (ES) pour améliorer la performance et la stabilité. ([#7256](https://github.com/SocialGouv/code-du-travail-numerique/issues/7256))
- Amélioration de la pertinence des résultats de recherche en ajustant les requêtes Elasticsearch. ([#7229](https://github.com/SocialGouv/code-du-travail-numerique/issues/7229), [#7217](https://github.com/SocialGouv/code-du-travail-numerique/issues/7217), [#7246](https://github.com/SocialGouv/code-du-travail-numerique/issues/7246))
- Correction d'erreurs remontées par Sentry, l'outil de suivi des erreurs. ([#7225](https://github.com/SocialGouv/code-du-travail-numerique/issues/7225))
- Mise à jour des tests E2E pour utiliser Playwright au lieu de Cypress. ([#7212](https://github.com/SocialGouv/code-du-travail-numerique/issues/7212))
- Renommage des labels utilisés pour les contributions et autres pages pour une meilleure organisation. ([#7227](https://github.com/SocialGouv/code-du-travail-numerique/issues/7227))
- Ajout de données structurées JSON-LD et mise à jour du plan du site pour améliorer le référencement. ([#7224](https://github.com/SocialGouv/code-du-travail-numerique/issues/7224))

### Autres changements
- Mise à jour du bandeau cookie pour être conforme aux réglementations RGPD. ([#7248](https://github.com/SocialGouv/code-du-travail-numerique/issues/7248))
- Ajout d'un avertissement lors de la saisie de données personnelles dans les commentaires pour sensibiliser au RGPD. ([#7244](https://github.com/SocialGouv/code-du-travail-numerique/issues/7244))
- Corrections de tests E2E suite à l'ajout des actualités. ([#7220](https://github.com/SocialGouv/code-du-travail-numerique/issues/7220))
- Corrections d'affichage des résultats de recherche. ([#7219](https://github.com/SocialGouv/code-du-travail-numerique/issues/7219))
- Correction d'un problème de correspondance dans la recherche des définitions. ([#7206](https://github.com/SocialGouv/code-du-travail-numerique/issues/7206))
- Correction de bugs sur les titres, les marges et les liens de la page actualités. ([#7218](https://github.com/SocialGouv/code-du-travail-numerique/issues/7218))
- Correction de la gestion des liens d'ancre sans attribut `href` dans les fiches métiers. ([#7223](https://github.com/SocialGouv/code-du-travail-numerique/issues/7223))
