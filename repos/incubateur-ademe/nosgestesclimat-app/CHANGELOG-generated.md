## Changelog : nosgestesclimat-app (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de déploiement, de stabilité et d'expérience utilisateur. Une refonte de l'architecture vers une structure monorepo a été initiée, ouvrant la voie à une meilleure organisation du code et à des développements plus efficaces. Des corrections de bugs ont été apportées pour améliorer la fiabilité de l'application, notamment concernant les tests, les cookies et l'affichage des données. Enfin, de nouvelles fonctionnalités et des améliorations ont été déployées pour affiner le parcours utilisateur, comme la suppression de simulations et l'ajout de bannières d'information.

### Évolutions fonctionnelles
- Possibilité de supprimer une simulation depuis l'espace personnel [#1747](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1747).
- Ajout d'une bannière JVA (Justice Verte et Agriculture) [#1748](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1748).
- Implémentation d'un bouton "Je ne sais pas" pour certaines questions, en phase de test A/B [#1737](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1737).
- Ajout d'un nouveau switch pour la question sur la consommation d'électricité [#1701](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1701).
- Amélioration de l'affichage des nombres sur les pages d'actions après filtrage [#1724](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1724).
- Création d'une nouvelle page de résultats [#1696](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1696).
- Correction de l'affichage des questions "manquantes" et "brutes" [#1716](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1716).
- Suppression de l'affichage du footer dans les tests [#1721](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1721).
- Masquage de l'alerte lorsque l'utilisateur tourne son mobile horizontalement [#1720](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1720).

### Évolutions techniques
- Refonte de l'architecture vers une structure monorepo [#1745](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1745) et [#1759](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1759).
- Amélioration de la configuration de CI/CD et des configurations ESLint [#1765](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1765).
- Mise en place de devcontainers pour faciliter le développement local [#1751](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1751).
- Correction de problèmes liés au déploiement sur Scalingo et les environnements de préproduction.
- Amélioration de la gestion des cookies et de la sécurité (SameSite Strict).
- Mise à jour de la version de Prisma à v7.0.
- Refactorisation du code pour améliorer la performance et la maintenabilité.
- Amélioration du suivi (tracking) et de la gestion des erreurs avec Sentry.
- Optimisation de la configuration de Next.js.

### Autres changements
- Ajout de traductions [#1769](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1769).
- Documentation sur l'installation du projet mise à jour [#1733](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1733).
- Correction de la condition pour l'opérateur `!=` dans les funfacts [#1755](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1755).
- Amélioration du contraste de l'interface utilisateur dans l'IDE.
- Suppression de fichiers inutiles (yarnrc, .pnpm-store).
- Ajout de commentaires et d'informations dans le code.
- Mise à jour des dépendances.
- Amélioration de la gestion des logs et des erreurs.
- Correction de problèmes liés aux tests E2E et aux tests unitaires.
- Ajout d'un favicon.
- Correction de l'affichage de la bannière selon les règles [NGC-3240](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1749).
- Correction de l'affichage de la page /fin sur Safari et dans les intégrations iframe.
- Ajout d'informations à la liste des questions.
- Correction de l'affichage des services dans les questions.
