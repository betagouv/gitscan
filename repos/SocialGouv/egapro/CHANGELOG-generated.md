## Changelog : egapro (30 derniers jours)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de l'expérience utilisateur, notamment avec l'ajout de nouvelles fonctionnalités comme la génération de PDF pour les déclarations, l'implémentation du parcours de second déclaration et l'ajout d'une page d'aide complète. Des améliorations techniques ont également été apportées pour la gestion des erreurs, les tests et l'infrastructure.

### Évolutions fonctionnelles
- Ajout de la génération et du téléchargement de la déclaration au format PDF. [#2904](https://github.com/SocialGouv/egapro/issues/2904) [#2910](https://github.com/SocialGouv/egapro/issues/2910)
- Implémentation du parcours de seconde déclaration (corrective action). [#2969](https://github.com/SocialGouv/egapro/issues/2969)
- Ajout d'une page de choix de parcours de conformité après la soumission d'une déclaration. [#2953](https://github.com/SocialGouv/egapro/issues/2953)
- Ajout d'une page d'avis du CSE avec les étapes de saisie et de confirmation. [#2906](https://github.com/SocialGouv/egapro/issues/2906)
- Ajout des pages légales : mentions légales, données personnelles, cookies, accessibilité, plan du site. [#2883](https://github.com/SocialGouv/egapro/issues/2883)
- Ajout d'une page FAQ avec des sections accordéon et une navigation par sommaire. [#2876](https://github.com/SocialGouv/egapro/issues/2876)
- Ajout d'une page d'aide et de ressources. [#2875](https://github.com/SocialGouv/egapro/issues/2875)
- Ajout des pages "Mon Espace", "Mes Entreprises" et "Mon Profil". [#2852](https://github.com/SocialGouv/egapro/issues/2852), [#2850](https://github.com/SocialGouv/egapro/issues/2850), [#2839](https://github.com/SocialGouv/egapro/issues/2839)
- Redirection de l'utilisateur vers la page "Mon Espace" après la connexion. [#2977](https://github.com/SocialGouv/egapro/issues/2977)
- Redirection des utilisateurs authentifiés. [#2988](https://github.com/SocialGouv/egapro/issues/2988)
- Correction d'un bug où l'utilisateur était redirigé vers la page d'accueil après la déconnexion. [#2993](https://github.com/SocialGouv/egapro/issues/2993)
- Auto-remplissage de la déclaration. [#2970](https://github.com/SocialGouv/egapro/issues/2970)

### Évolutions techniques
- Refonte de l'implémentation de la déclaration. [#2962](https://github.com/SocialGouv/egapro/issues/2962)
- Implémentation de l'API CSE avec un mock. [#2966](https://github.com/SocialGouv/egapro/issues/2966)
- Mise en place de Sentry pour la gestion des erreurs et l'envoi des sourcemaps. [#2889](https://github.com/SocialGouv/egapro/issues/2889)
- Ajout de tests E2E et amélioration de leur exécution dans la CI. [#2960](https://github.com/SocialGouv/egapro/issues/2960), [#2954](https://github.com/SocialGouv/egapro/issues/2954), [#2915](https://github.com/SocialGouv/egapro/issues/2915)
- Utilisation de Docker Compose pour les tests E2E. [#2960](https://github.com/SocialGouv/egapro/issues/2960)
- Amélioration de la configuration CI/CD avec des jobs pour l'analyse de code (CLAUDE, SonarQube, RGAA). [#2886](https://github.com/SocialGouv/egapro/issues/2886), [#2874](https://github.com/SocialGouv/egapro/issues/2874), [#2877](https://github.com/SocialGouv/egapro/issues/2877)
- Migration vers Drizzle ORM. [#2819](https://github.com/SocialGouv/egapro/issues/2819)
- Ajout de Vitest pour les tests avec DSFR. [#2794](https://github.com/SocialGouv/egapro/issues/2794)
- Nettoyage et simplification de la configuration. [#2782](https://github.com/SocialGouv/egapro/issues/2782)

### Autres changements
- Extraction du composant Breadcrumb partagé pour éviter les duplications. [#2885](https://github.com/SocialGouv/egapro/issues/2885)
- Ajout de liens vers travail-emploi.gouv.fr dans les cartes d'indicateurs. [#2881](https://github.com/SocialGouv/egapro/issues/2881)
- Correction de règles CSS pour une meilleure compatibilité avec DSFR. [#2961](https://github.com/SocialGouv/egapro/issues/2961)
- Mise à jour de la documentation README. [#2849](https://github.com/SocialGouv/egapro/issues/2849)
