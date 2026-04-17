## Changelog : nosgestesclimat-app (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, l'application a bénéficié d'améliorations significatives en termes de déploiement, de stabilité et d'expérience utilisateur. Une refonte architecturale vers une structure monorepo a été initiée, et des corrections ont été apportées pour améliorer la fiabilité des tests et des déploiements. Des améliorations de l'interface utilisateur et des corrections de bugs ont également été déployées, notamment concernant la gestion des simulations, les bannières d'information et l'accessibilité.

### Évolutions fonctionnelles
- Possibilité de supprimer une simulation depuis l'espace personnel de l'utilisateur. [#1747](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1747)
- Ajout d'une bannière JVA (Justice Verte et Alimentaire). [#1748](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1748)
- Ajout d'un bouton "Je ne sais pas" pour les questions du simulateur, faisant l'objet d'un test A/B. [#1737](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1737)
- Amélioration de la gestion des simulations anonymes lors de la connexion. [#457](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/457)
- Nouvelle page de résultats pour le simulateur. [#1696](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1696)
- Amélioration de l'affichage des nombres sur les pages d'actions. [#1724](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1724)
- Mise à jour du calendrier sur la page de demande de démonstration. [#1711](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1711)
- Ajout d'une nouvelle question sur la consommation d'électricité avec un switch. [#1701](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1701)
- Correction de l'affichage des règles de la bannière. [#1749](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1749)
- Correction de l'affichage des questions de type "services" dans le simulateur. [#1717](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1717)

### Évolutions techniques
- Refonte de l'architecture vers une structure monorepo. [#1745](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1745)
- Mise en place de devcontainers pour faciliter le développement. [#1751](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1751)
- Amélioration du processus de déploiement sur Scalingo et GitHub Actions.
- Mise à jour de Prisma vers la version 7.0.
- Refactorisation du code pour améliorer la maintenabilité et la performance.
- Amélioration de la gestion des cookies et de la sécurité (SameSite).
- Mise en place d'un système de traçabilité plus robuste avec Sentry.
- Optimisation des dépendances et des builds.
- Migration de certains composants vers des composants serveur.

### Autres changements
- Corrections de bugs et améliorations de l'accessibilité. [#1703](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1703)
- Documentation sur l'installation du projet mise à jour. [#1733](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1733)
- Amélioration de la configuration de l'IDE (VS Code).
- Corrections de typos et mises à jour de traductions.
- Suppression de code inutilisé.
- Ajout de tests E2E et corrections de tests existants.
- Mise à jour de la documentation README.
- Amélioration du tracking et de l'analyse des données.
- Ajout de commentaires et de documentation au code.
