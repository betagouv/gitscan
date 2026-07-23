## Changelog : anssi-portail (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la performance du site via le rendu côté serveur (SSR) pour de nombreuses pages, incluant les guides, les financements, et le catalogue. Des corrections de SEO ont également été apportées, notamment pour les sitemaps et les liens canoniques. Des améliorations de l'expérience utilisateur ont été implémentées, notamment pour le parcours de sécurisation et la page NIS2.

### Évolutions fonctionnelles
- Implémentation du rendu côté serveur (SSR) pour de nombreuses pages : guides, financements, associations, collectivités, test de maturité, sessions de groupe, pages NIS2, etc. [#1234](https://github.com/betagouv/anssi-portail/issues/1234)
- Amélioration du parcours de sécurisation : affichage de la progression, des badges de complétion, et des mesures par module.
- Ajout de la possibilité de féliciter l'utilisateur à la fin du parcours de sécurisation.
- Amélioration de l'affichage des cartes de modules dans le parcours de sécurisation.
- Ajout d'un lien dans la note informative de la page NIS2.
- Correction de l'affichage des liens dans le footer.
- Mise à jour des mesures du module Cyberdépart.
- Ajout des pages des contacts régionaux dans le sitemap.
- Ajout des pages ressources et services dans le sitemap.
- Ajout des pages guides et financements dans le sitemap.

### Évolutions techniques
- Migration vers Svelte 5 pour le composant Guide.
- Refonte de l'architecture pour supporter le rendu côté serveur (SSR).
- Utilisation d'un seul runtime Svelte pour améliorer la performance.
- Mutualisation des versions de dépendances.
- Amélioration de la gestion des erreurs 403.
- Mise à jour de plusieurs dépendances pour corriger des failles de sécurité (axios, brace-expansion, dompurify, uuid, etc.).
- Ajout de tests Playwright pour l'authentification.
- Ajout d'un Nix Shell pour le développement en local.
- Renforcement de la sécurité du CI/CD (désactivation des identifiants git, secrets explicites).
- Ajout de la validation de configuration avec `zizmor`.
- Utilisation de uuid v7 pour générer des clés primaires.

### Autres changements
- Ajout de métadonnées Open Graph et Twitter pour le SEO.
- Amélioration de la hiérarchie des titres sur plusieurs pages pour le SEO.
- Correction de l'indentation des secrets dans les fichiers YAML de déploiement.
- Ajout de commentaires et de documentation pour améliorer la maintenabilité du code.
- Suppression de code inutile et de styles obsolètes.
- Correction de bugs mineurs et amélioration de la qualité du code.
- Ajout d'un pixel de suivi et gestion du consentement.
- Ajout de la campagne Matomo à l'origine des demandes d'aide.
- Uniformisation des noms des propriétés des composants Svelte.
