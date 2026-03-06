## Changelog : egapro (30 derniers jours)

### Résumé
Les dernières mises à jour d'EgaPro se concentrent sur l'amélioration de la sécurité, de la qualité du code et de l'expérience utilisateur. De nouvelles fonctionnalités ont été ajoutées, notamment la gestion des entreprises et du profil utilisateur, ainsi que l'intégration d'une API externe (Weez). Des corrections de bugs et des améliorations de l'infrastructure ont également été apportées pour assurer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- Ajout de pages légales : mentions légales, données personnelles, cookies, accessibilité et plan du site. [#2883](https://github.com/SocialGouv/egapro/issues/2883)
- Ajout d'une page d'aide et de ressources avec une navigation sommaire. [#2875](https://github.com/SocialGouv/egapro/issues/2875)
- Ajout d'une page FAQ avec des sections accordéon. [#2876](https://github.com/SocialGouv/egapro/issues/2876)
- Intégration de l'API Weez. [#2872](https://github.com/SocialGouv/egapro/issues/2872)
- Ajout de la fonctionnalité "Mes déclarations". [#2852](https://github.com/SocialGouv/egapro/issues/2852)
- Ajout de la fonctionnalité "Mes entreprises". [#2850](https://github.com/SocialGouv/egapro/issues/2850)
- Ajout de la fonctionnalité "Mon profil". [#2839](https://github.com/SocialGouv/egapro/issues/2839)
- Ajout d'une page de connexion. [#2823](https://github.com/SocialGouv/egapro/issues/2823)
- Mise en place de la page d'accueil avec son header et footer. [#2822](https://github.com/SocialGouv/egapro/issues/2822)
- Création des pages d'erreurs 404 et 500. [#2832](https://github.com/SocialGouv/egapro/issues/2832)
- Mise à jour du label CSE. [#2882](https://github.com/SocialGouv/egapro/issues/2882)
- Liaison des cartes d'indicateurs à travail-emploi.gouv.fr. [#2881](https://github.com/SocialGouv/egapro/issues/2881)
- Amélioration des retours sur les pages d'erreurs. [#2880](https://github.com/SocialGouv/egapro/issues/2880)

### Évolutions techniques
- Mise en place de Sentry pour la gestion des erreurs et des sourcemaps. [#2889](https://github.com/SocialGouv/egapro/issues/2889)
- Refactoring : extraction d'un composant Breadcrumb partagé pour éviter les duplications. [#2885](https://github.com/SocialGouv/egapro/issues/2885)
- Amélioration de la configuration de CLAUDE et application sur la codebase existante. [#2863](https://github.com/SocialGouv/egapro/issues/2863)
- Utilisation de `next/image` pour les images et mise à jour des guidelines associées. [#2877](https://github.com/SocialGouv/egapro/issues/2877)
- Ajout de tests E2E pour la page de connexion. [#2849](https://github.com/SocialGouv/egapro/issues/2849)
- Ajout de la configuration Vitest pour les tests avec DSFR. [#2794](https://github.com/SocialGouv/egapro/issues/2794)
- Optimisation du temps de build Docker via du caching. [#2795](https://github.com/SocialGouv/egapro/issues/2795)
- Ajout de jobs CI pour l'analyse statique du code (CLAUDE, RGAA, Lighthouse). [#2874](https://github.com/SocialGouv/egapro/issues/2874), [#2886](https://github.com/SocialGouv/egapro/issues/2886), [#2818](https://github.com/SocialGouv/egapro/issues/2818)
- Mise à jour de la configuration de l'action Sonar. [#2886](https://github.com/SocialGouv/egapro/issues/2886)
- Ajout de conditions dans les actions CLAUDE. [#2870](https://github.com/SocialGouv/egapro/issues/2870)
- Ajout de tests unitaires et E2E.
- Mise à jour de la configuration de Drizzle. [#2819](https://github.com/SocialGouv/egapro/issues/2819)

### Autres changements
- Mise à jour du fichier `.gitignore`. [#2887](https://github.com/SocialGouv/egapro/issues/2887)
- Mise à jour de la documentation (README). [#2849](https://github.com/SocialGouv/egapro/issues/2849)
- Correction de bugs liés à l'authentification Proconnect.
- Nettoyage du code et amélioration de la lisibilité.
- Correction de problèmes liés aux tests E2E. [#2915](https://github.com/SocialGouv/egapro/issues/2915)
