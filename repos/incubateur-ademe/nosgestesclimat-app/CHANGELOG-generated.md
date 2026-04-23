## Changelog : nosgestesclimat-app (30 derniers jours, au 22 avril 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de stabilité, de performance et d'expérience utilisateur. Une refonte architecturale vers une structure de monorepo a été initiée, ouvrant la voie à une meilleure organisation du code et à une plus grande flexibilité. Des corrections de bugs et des améliorations de l'interface utilisateur ont également été apportées, notamment concernant la gestion des simulations, l'affichage des bannières et la traduction.

### Évolutions fonctionnelles
- Possibilité de supprimer une simulation depuis l'espace personnel de l'utilisateur. [#1747](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1747)
- Ajout d'une bannière JVA (Justice Verte et Agriculture). [#1748](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1748)
- Ajout d'un bouton "Je ne sais pas" pour certaines questions, dans le cadre d'un test A/B. [#1737](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1737)
- Amélioration de l'affichage des règles de la bannière. [#1749](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1749)
- Nouvelle page de résultats en cours de développement. [#1696](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1696)
- Mise à jour du calendrier sur la page de demande de démonstration. [#1711](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1711)
- Correction de l'affichage des questions "manquantes" et "brutes manquantes". [#1716](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1716)
- Ajout d'un interrupteur pour la question de consommation d'électricité. [#1701](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1701)
- Traduction de nouveaux textes et correction de typos. [#1715](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1715), [#1714](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1714), [#1710](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1710), [#1703](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1703)
- Modification du terme "Groupes" en "Tests collectifs". [#1712](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1712)

### Évolutions techniques
- Refonte de l'architecture vers une structure de monorepo. [#1745](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1745)
- Mise en place de devcontainers pour faciliter le développement. [#1751](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1751)
- Amélioration des workflows CI/CD et des configurations ESLint. [#1765](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1765)
- Mise à jour de Prisma vers la version 7.0.
- Refactor de la gestion du tracking et des cookies. [#1669](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1669)
- Conversion de certains composants en composants serveur.
- Amélioration de la gestion des URL et des proxies.
- Correction de problèmes de déploiement sur Scalingo et GitHub Actions.
- Correction de bugs liés aux tests E2E et aux tests unitaires.
- Mise à jour des dépendances.

### Autres changements
- Documentation sur l'installation du projet ajoutée. [#1733](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1733)
- Amélioration du contraste de l'interface utilisateur dans l'IDE.
- Suppression de fichiers inutiles.
- Ajout de commentaires et de logs pour faciliter le débogage.
- Correction de la configuration de Sentry pour une meilleure remontée d'erreurs.
- Ajout d'un favicon.
- Suppression de la cache des composants Banner.
- Ouverture des liens dans la bannière dans un nouvel onglet.
- Correction de l'opérateur `!=` dans les conditions des funfacts. [#1755](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1755)
- Ajout de la gestion des erreurs lors de la migration de la base de données.
- Amélioration du tracking sur la page `/fin`.
- Ajout d'un bouton pour partager les données dans un iframe.
- Correction de l'affichage de la page `/fin` sur Safari.
- Correction de l'affichage des nombres sur les pages d'actions.
- Suppression du footer dans les tests.
- Correction de l'affichage de l'alerte en mode mobile horizontal.
- Ajout d'un `aria-label` manquant.
- Suppression de la partition des cookies.
- Ajout d'une politique SameSite Strict pour les cookies non sécurisés.
- Suppression de la configuration `prestart` et `poststart`.
- Suppression des buildpacks personnalisés pour le déploiement.
- Amélioration de la configuration de Storybook.
- Ajout de la gestion des releases Sentry.
- Ajout de la gestion des logs.
- Suppression de l'option `partitioned` pour les cookies.
- Ajout d'un bouton "Je ne sais pas" pour certaines questions.
- Ajout de la gestion des erreurs lors de la migration de la base de données.
- Ajout d'un favicon.
- Suppression de la cache des composants Banner.
- Ouverture des liens dans la bannière dans un nouvel onglet.
- Correction de l'opérateur `!=` dans les conditions des funfacts.
- Ajout de la gestion des erreurs lors de la migration de la base de données.
- Ajout d'un favicon.
- Suppression de la cache des composants Banner.
- Ouverture des liens dans la bannière dans un nouvel onglet.
- Correction de l'opérateur `!=` dans les conditions des funfacts.
