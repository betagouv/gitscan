## Changelog : plusfraichemaville-site (30 derniers jours, au 20 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'expérience utilisateur, notamment en repensant le parcours de création de projet et en ajoutant de nouvelles fonctionnalités de suivi des données. Des optimisations techniques ont également été apportées pour améliorer la performance et la sécurité de la plateforme.

### Évolutions fonctionnelles
- **Création de projet :** Refonte complète du flux de création de projet avec un formulaire étape par étape [#484](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/484), incluant un bouton d'annulation [#2d54ec06](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/2d54ec06) et une gestion améliorée des onglets [#65d6e48a](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/65d6e48a). Un avertissement est affiché si l'utilisateur quitte le formulaire en cours de création [#05829414](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/05829414).
- **Page d'accueil :** Nouvelle page d'accueil [#487](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/487).
- **Suivi des données :** Ajout du suivi des vues de projets dans l'annuaire [#39fb221a](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/39fb221a) et des informations sur les aides cliquées pour chaque projet utilisateur [#7bbba9ab](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/7bbba9ab).
- **Fiche diagnostic :** Enregistrement des fiches diagnostics vues par chaque utilisateur [#f339fd92](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/f339fd92).
- **Redirection :** Correction d'une redirection vers la page de connexion lorsque l'utilisateur n'est pas connecté [#0e65d4aa](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/0e65d4aa) et suppression de la redirection après la création d'un projet si l'utilisateur n'en a pas [#fe17bdb6](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/fe17bdb6).
- **Page "Mes projets" :** Amélioration de la responsivité de la page "Mes projets" [#485](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/485).

### Évolutions techniques
- **Sentry :** Migration vers une nouvelle configuration de Sentry pour une meilleure gestion des erreurs [#480](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/480) et correction de problèmes liés à la migration [#481](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/481).
- **Sécurité :** Mise à jour des dépendances pour corriger des vulnérabilités de sécurité [#479](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/479).
- **Outils :** Passage à pnpm pour la gestion des dépendances [#844e687a](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/844e687a).
- **Tailwind CSS :** Mise à jour de Tailwind CSS et suppression de code Sass inutilisé [#fd078cd3](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/fd078cd3).

### Autres changements
- Amélioration des logs pour les erreurs 404 dans Sentry [#a0e34341](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/a0e34341).
- Correction de typos [#45568df8](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/45568df8).
- Suppression de librairies inutilisées [#c7c8535e](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/c7c8535e).
- Ajout de métriques KR2.1 [#483](https://github.com/incubateur-ademe/plusfraichemaville-site/pulls/483).
- Correction pour éviter d'afficher des erreurs Cartagene incorrectes [#dc3c5506](https://github.com/incubateur-ademe/plusfraichemaville-site/commit/dc3c5506).
