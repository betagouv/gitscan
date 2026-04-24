## Changelog : benefriches (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur dans la création de projets urbains, notamment en ajoutant des étapes de saisie plus précises concernant les bâtiments (réutilisation, construction, démolition, dépenses). Des améliorations ont également été apportées à la robustesse de l'application, avec des corrections de bugs et des optimisations de l'infrastructure. Enfin, des améliorations de la documentation et des tests ont été réalisées.

### Évolutions fonctionnelles
- Ajout d'un endpoint API pour calculer le coût de l'inaction sur une friche [#fae2976](https://github.com/incubateur-ademe/benefriches/commit/fae2976).
- Amélioration de l'affichage des coûts évités si le total est nul [#a35f75a](https://github.com/incubateur-ademe/benefriches/commit/a35f75a).
- Correction du comportement de la répartition des surfaces des bâtiments lors de la réutilisation quand celle-ci tombe à zéro [#b3978ee](https://github.com/incubateur-ademe/benefriches/commit/b3978ee).
- Correction du calcul de `futureOperator` pour éviter d'utiliser des données obsolètes [#41f6581](https://github.com/incubateur-ademe/benefriches/commit/41f6581).
- Correction de la navigation inverse pour les dépenses liées aux projets urbains [#001266c](https://github.com/incubateur-ademe/benefriches/commit/001266c).
- Ajout d'étapes pour la saisie des dépenses de construction/rénovation dans les projets urbains [#128ba36](https://github.com/incubateur-ademe/benefriches/commit/128ba36), [#3bda97d](https://github.com/incubateur-ademe/benefriches/commit/3bda97d).
- Ajout de pictogrammes et de couleurs spécifiques pour les types de zones urbaines [#7149476](https://github.com/incubateur-ademe/benefriches/commit/7149476).
- Ajout d'étapes pour la saisie des informations sur la réutilisation et la nouvelle construction des bâtiments dans les projets urbains [#26dcf3d](https://github.com/incubateur-ademe/benefriches/commit/26dcf3d).
- Ajout d'une étape pour la saisie des informations sur la démolition des bâtiments dans les projets urbains [#0400633](https://github.com/incubateur-ademe/benefriches/commit/0400633).
- Ajout d'une étape pour la saisie des informations sur les acteurs du développement des bâtiments dans les projets urbains [#415b055](https://github.com/incubateur-ademe/benefriches/commit/415b055).
- Ajout d'une étape pour la saisie des usages des bâtiments existants et nouveaux [#b56e047](https://github.com/incubateur-ademe/benefriches/commit/b56e047).
- Amélioration de l'interface utilisateur pour la sélection des modèles de projets et des cas d'utilisation [#3e6f100](https://github.com/incubateur-ademe/benefriches/commit/3e6f100).
- Ajout d'une filigrane "démo" sur les exports PDF pour les projets créés en mode express [#384f1a3](https://github.com/incubateur-ademe/benefriches/commit/384f1a3).
- Amélioration de l'affichage des instructions et des avertissements dans les formulaires de création de sites en mode démo [#dae82dc](https://github.com/incubateur-ademe/benefriches/commit/dae82dc).
- Ajout de la possibilité de basculer entre les thèmes clair et sombre [#9ddd4f7](https://github.com/incubateur-ademe/benefriches/commit/9ddd4f7).

### Évolutions techniques
- Ajout de la documentation Swagger pour les endpoints publics de l'API [#3b74413](https://github.com/incubateur-ademe/benefriches/commit/3b74413).
- Refactorisation de la gestion des surfaces pour utiliser un schéma commun [#89f956b](https://github.com/incubateur-ademe/benefriches/commit/89f956b).
- Standardisation des variables d'environnement pour les feature flags avec le préfixe `WEBAPP_FF_` [#f067c7f](https://github.com/incubateur-ademe/benefriches/commit/f067c7f).
- Mise à jour des dépendances mineures et majeures de l'API et du web [#7f4ecd4](https://github.com/incubateur-ademe/benefriches/commit/7f4ecd4), [#34b80d3](https://github.com/incubateur-ademe/benefriches/commit/34b80d3), [#397c36b](https://github.com/incubateur-ademe/benefriches/commit/397c36b), [#047c413](https://github.com/incubateur-ademe/benefriches/commit/047c413), [#e26e38e](https://github.com/incubateur-ademe/benefriches/commit/e26e38e).
- Amélioration de la configuration CI/CD pour une meilleure gestion des secrets et des tests [#ff0410b](https://github.com/incubateur-ademe/benefriches/commit/ff0410b), [#a0a4ea8](https://github.com/incubateur-ademe/benefriches/commit/a0a4ea8), [#af1dfc4](https://github.com/incubateur-ademe/benefriches/commit/af1dfc4), [#f12d312](https://github.com/incubateur-ademe/benefriches/commit/f12d312), [#72568ac](https://github.com/incubateur-ademe/benefriches/commit/72568ac), [#df6d7fc](https://github.com/incubateur-ademe/benefriches/commit/df6d7fc), [#1b7a7ab](https://github.com/incubateur-ademe/benefriches/commit/1b7a7ab).
- Ajout de contrôles de concurrence pour éviter les conflits lors du déploiement [#6f7b69d](https://github.com/incubateur-ademe/benefriches/commit/6f7b69d).
- Utilisation de cookies sécurisés pour une meilleure sécurité [#09f4dc8](https://github.com/incubateur-ademe/benefriches/commit/09f4dc8), [#de3c7df](https://github.com/incubateur-ademe/benefriches/commit/de3c7df), [#035dd2c](https://github.com/incubateur-ademe/benefriches/commit/035dd2c).
- Amélioration de la journalisation avec l'utilisation d'un logger injectable [#927a293](https://github.com/incubateur-ademe/benefriches/commit/927a293).

### Autres changements
- Correction de bugs mineurs dans les tests E2E et les formulaires [#34d81cb](https://github.com/incubateur-ademe/benefriches/commit/34d81cb), [#595b1aa](https://github.com/incubateur-ademe/benefriches/commit/595b1aa), [#be56201](https://github.com/incubateur-ademe/benefriches/commit/be56201), [#fc9e358](https://github.com/incubateur-ademe/benefriches/commit/fc9e358), [#30a50a0](https://github.com/incubateur-ademe/benefriches/commit/30a50a0).
- Mise à jour de la documentation pour les tests E2E [#93dc95c](https://github.com/incubateur-ademe/benefriches/commit/93dc95c).
- Nettoyage du code et suppression de fichiers inutilisés [#4988082](https://github.com/incubateur-ademe/benefriches/commit/4988082), [#d39831f](https://github.com/incubateur-ademe/benefriches/commit/d39831f), [#86ae657](https://github.com/incubateur-ademe/benefriches/commit/86ae657).
- Correction d'erreurs de typage dans les tests [#f8ff36a](https://github.com/incubateur-ademe/benefriches/commit/f8ff36a).
- Correction de l'ordre des imports dans le code web [#0c0b5a9](https://github.com/incubateur-ademe/benefriches/commit/0c0b5a9), [#890c5df](https://github.com/incubateur-ademe/benefriches/commit/890c5df).
