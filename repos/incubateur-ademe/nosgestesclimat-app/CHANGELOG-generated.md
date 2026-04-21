## Changelog : nosgestesclimat-app (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'infrastructure de déploiement, la correction de bugs et l'ajout de nouvelles fonctionnalités pour améliorer l'expérience utilisateur. Une migration vers une architecture monorepo a été initiée pour faciliter le développement et la maintenance du projet. Des améliorations de la gestion des cookies et du suivi ont également été apportées.

### Évolutions fonctionnelles
- Possibilité de supprimer une simulation depuis l'espace personnel de l'utilisateur. [#1747](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1747)
- Ajout d'une bannière JVA (Justice Verte et Agriculture). [#1748](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1748)
- Implémentation d'un bouton "Je ne sais pas" pour certaines questions, dans le cadre d'un test A/B. [#1737](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1737)
- Ajout d'une nouvelle question sur la consommation d'électricité avec un interrupteur. [#1701](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1701)
- Amélioration de l'affichage des nombres sur les pages d'actions. [#1724](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1724)
- Nouvelle page de résultats. [#1696](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1696)
- Amélioration de la gestion des groupes (renommés "Tests collectifs"). [#1712](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1712)
- Utilisation d'un nouveau calendrier sur la page de demande de démonstration. [#1711](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1711)
- Correction de l'affichage des questions "manquantes" et "brutes manquantes". [#1716](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1716)
- Ajout de la possibilité de partager les données via un iframe. [#1732](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1732)

### Évolutions techniques
- Migration vers une architecture monorepo pour faciliter la gestion des dépendances et le développement. [#1745](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1745)
- Amélioration du pipeline CI/CD pour les déploiements.
- Mise à jour de Prisma vers la version 7.0.
- Refactor de la gestion des cookies et du suivi pour améliorer la conformité et la performance. [#1669](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1669)
- Amélioration de la configuration de Sentry pour une meilleure gestion des erreurs.
- Conversion de certains composants en composants serveur pour optimiser les performances.
- Mise en place de devcontainers pour faciliter le développement local. [#1751](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1751)
- Ajout de tests E2E pour garantir la qualité du code.
- Correction de problèmes de déploiement sur Scalingo et en CI.
- Amélioration de la configuration de Next.js.
- Suppression de dépendances inutilisées.

### Autres changements
- Documentation sur l'installation du projet mise à jour. [#1733](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1733)
- Corrections d'accessibilité. [#1703](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1703)
- Amélioration du contraste de l'interface utilisateur dans l'IDE.
- Mise à jour des traductions et correction de typos.
- Ajout de commentaires et documentation dans le code.
- Suppression de fichiers inutiles.
- Amélioration de la gestion des releases Sentry.
- Ajout de tracking pour la page /fin.
- Ajout d'un favicon.
- Correction de l'affichage de la bannière en fonction des règles. [#1749](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1749)
