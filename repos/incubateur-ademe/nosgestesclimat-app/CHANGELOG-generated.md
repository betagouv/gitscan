## Changelog : nosgestesclimat-app (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les développements se sont concentrés sur l'amélioration de l'infrastructure du projet avec une migration vers une architecture monorepo, des optimisations du déploiement et des corrections de bugs liés à la gestion des cookies et des tests. Des améliorations ont également été apportées à l'expérience utilisateur, notamment la suppression de simulations, l'ajout de bannières d'information et des corrections de suivi analytique.

### Évolutions fonctionnelles
- Suppression de la possibilité de supprimer une simulation depuis l'espace personnel [#1747](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1747).
- Ajout d'une bannière JVA (Justice Verte et Agriculture) [#1748](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1748).
- Ajout d'un bouton "Je ne sais pas" pour les questions du calculateur, avec un test A/B pour évaluer son impact [#1737](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1737).
- Ajout d'un nouveau commutateur pour la question de la consommation d'électricité [#1701](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1701).
- Correction de l'affichage de la bannière en fonction des règles définies [#1749](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1749).
- Amélioration du suivi analytique (Matomo) avec récupération sécurisée des données [#1770](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1770).
- Ajout d'un flag de fonctionnalité pour les actions [#1775](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1775).
- Correction de l'affichage des nombres filtrés sur les pages d'actions [#1724](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1724).

### Évolutions techniques
- Migration du projet vers une architecture monorepo [#1745](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1745).
- Refactorisation des workflows CI/CD et configuration ESLint [#1765](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1765).
- Mise en place de devcontainers pour faciliter le développement [#1751](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1751).
- Amélioration de la gestion des erreurs et des logs, notamment lors des sessions utilisateurs.
- Correction de problèmes de déploiement sur Scalingo et en environnement de préproduction.
- Mise à jour de Prisma vers la version 7.0.
- Optimisation de la gestion des cookies et ajout de la politique SameSite Strict pour la sécurité.
- Refactorisation du code pour utiliser des composants serveur.
- Amélioration de la configuration de Sentry pour une meilleure gestion des erreurs.
- Suppression des buildpacks personnalisés pour garantir le déploiement même en cas de problème avec les miroirs Ubuntu.
- Correction de la configuration de Next.js pour gérer correctement les origines.

### Autres changements
- Documentation sur l'installation du projet mise à jour [#1733](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1733).
- Ajout de traductions [#1769](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1769).
- Correction de l'opérateur `!=` dans les conditions des "funfacts" [#1755](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1755).
- Suppression de fichiers inutiles et amélioration de la lisibilité du code.
- Correction de problèmes liés aux tests E2E et aux tests unitaires.
- Amélioration du contraste de l'interface utilisateur dans l'IDE.
- Suppression des balises hreflang si la page est uniquement en français [#1719](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1719).
- Correction d'un bug empêchant l'affichage de la page `/fin` sur Safari.
- Correction de l'affichage des questions de services [#1717](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1717).
- Ajout d'informations au schéma anonyme pour Posthog [#459](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/459).
- Mise à jour du modèle de calcul vers la version 4.10.2 [#1722](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/1722) et [#463](https://github.com/incubateur-ademe/nosgestesclimat-app/issues/463).
