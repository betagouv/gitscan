## Changelog : nosgestesclimat-app (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la stabilité de l'application, notamment en corrigeant des erreurs de déploiement et des tests défaillants. Des améliorations significatives ont été apportées à la gestion des simulations, avec la possibilité de les supprimer depuis l'espace personnel et une meilleure gestion des cookies et de la sécurité. Une refonte de l'architecture vers une approche monorepo a également été initiée.

### Évolutions fonctionnelles
- Possibilité de supprimer une simulation depuis l'espace personnel de l'utilisateur [#1747](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1747).
- Ajout d'une bannière JVA [#1748](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1748).
- Ajout d'un bouton "Je ne sais pas" pour les questions du simulateur (en test AB) [#1737](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1737).
- Amélioration de l'affichage des nombres sur les pages d'actions [#1724](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1724).
- Nouvelle page de résultats [#1696](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1696).
- Amélioration du formulaire de consentement aux cookies avec plus de détails sur les cookies utilisés [#1708](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1708).
- Utilisation d'un nouveau calendrier sur la page de demande de démonstration [#1711](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1711).
- Mise à jour de la terminologie : remplacement de "Groupes" par "Tests collectifs" [#1712](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1712).
- Correction de l'affichage des questions dans la section "services" [#1717](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1717).
- Correction d'un bug empêchant la mise à jour des simulations terminées [#461](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/461).
- Amélioration de la réconciliation des simulations anonymes lors de la connexion [#457](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/457).

### Évolutions techniques
- Refactorisation de l'architecture vers une approche monorepo [#1745](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1745).
- Mise en place de devcontainers pour un environnement de développement cohérent [#1751](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1751).
- Amélioration du déploiement sur Scalingo et correction des problèmes associés.
- Mise à jour de Prisma vers la version 7.0.
- Amélioration de la gestion des cookies et ajout de l'attribut `SameSite=Strict` pour renforcer la sécurité.
- Refactorisation du code pour utiliser des composants serveur (Server Components).
- Amélioration de la configuration de Sentry pour une meilleure gestion des erreurs.
- Optimisation de la gestion des dépendances et du build.
- Migration de certains fichiers de configuration vers la racine du projet.

### Autres changements
- Correction d'une erreur de configuration `tsconfigrootdir` [#1757](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1757).
- Ajout de documentation sur l'installation du projet [#1733](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1733).
- Amélioration du contraste de l'interface utilisateur dans l'IDE.
- Suppression de fichiers inutiles (yarnrc, .pnpm-store).
- Ajout de suivi (tracking) pour la page `/fin` et amélioration du suivi général.
- Corrections de typos et ajouts de traductions manquantes.
- Amélioration de la gestion des tests E2E et correction de tests défaillants.
- Mise à jour de la documentation README.
- Correction d'un bug d'affichage de la bannière [#1749](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1749).
- Ajout d'un favicon.
- Amélioration de l'accessibilité de l'application [#1703](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1703).
