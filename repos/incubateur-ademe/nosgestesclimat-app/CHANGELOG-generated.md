## Changelog : nosgestesclimat-app (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur une refonte architecturale majeure vers une structure monorepo, améliorant la maintenabilité et la scalabilité du projet.  Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment concernant l'affichage des résultats, la gestion des cookies et l'accessibilité. Des améliorations de la gestion des erreurs et du suivi (tracking) ont également été implémentées.

### Évolutions fonctionnelles
- Possibilité de supprimer une simulation depuis l'espace personnel de l'utilisateur. [#1747](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1747)
- Ajout d'une bannière JVA (Justice Verte et Agriculture). [#1748](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1748)
- Ajout d'un bouton "Je ne sais pas" pour certaines questions, testé via un AB test. [#1737](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1737)
- Nouvelle page de résultats avec une refonte de l'affichage. [#1696](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1696)
- Correction de l'affichage des nombres sur les pages d'actions après filtrage. [#1724](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1724)
- Amélioration de l'accessibilité du site. [#1703](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1703)
- Ajout d'une nouvelle question sur la consommation d'électricité. [#1701](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1701)
- Correction de l'affichage de la bannière en fonction des règles. [#1749](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1749)
- Correction d'un bug empêchant l'affichage de la page `/fin` sur Safari et dans les intégrations iframe.

### Évolutions techniques
- Refonte de l'architecture vers une structure monorepo. [#1745](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1745)
- Mise en place de devcontainers pour faciliter le développement. [#1751](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1751)
- Amélioration des workflows CI/CD et configuration ESLint. [#1765](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1765)
- Mise à jour de Prisma vers la version 7.0.
- Refactorisation du code pour améliorer la performance et la maintenabilité.
- Amélioration de la gestion des cookies et du suivi (tracking). [#1669](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1669)
- Amélioration de la configuration de Sentry pour une meilleure gestion des erreurs.
- Conversion de certains composants en composants serveur.
- Correction de problèmes de déploiement sur Scalingo et GitHub Actions.
- Mise à jour des dépendances.

### Autres changements
- Documentation sur l'installation du projet ajoutée. [#1733](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1733)
- Ajout d'informations au schéma anonyme pour PostHog. [#459](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/459)
- Correction de la condition pour l'affichage des questions "missing" et "rawMissing". [#1716](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1716)
- Suppression du footer dans les tests. [#1721](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1721)
- Correction de l'affichage de l'alerte sur mobile en orientation paysage. [#1720](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1720)
- Suppression des balises hreflang si la page est uniquement en français. [#1719](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1719)
- Correction d'un bug empêchant la suppression de simulations. [#462](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/462)
- Correction de l'opérateur `!=` dans les conditions des funfacts. [#1755](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1755)
- Ajout de traductions. [#1769](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1769)
