## Changelog : anssi-portail (30 derniers jours, au 17 juillet 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la migration vers le rendu côté serveur (SSR) pour améliorer la performance et l'accessibilité du portail. De nombreuses pages ont été rendues côté serveur, incluant les pages NIS2, financements, guides, et le catalogue. Des améliorations SEO ont également été apportées, notamment l'ajout de balises canoniques, de sitemaps et de robots.txt. Des corrections et améliorations ont été apportées au parcours de sécurisation, notamment l'affichage des modules et le suivi de la progression.

### Évolutions fonctionnelles
- **Parcours de sécurisation :** Amélioration de l'affichage des modules, affichage de la progression, et gestion du parcours complet pour les utilisateurs connectés.
- **Pages NIS2, Financements, Guides et Catalogue :** Ces pages sont désormais rendues côté serveur, améliorant ainsi la performance et l'accessibilité.
- **Amélioration de l'affichage des mesures :** Affichage du nombre de mesures par module et de la progression globale.
- **Page d'aide :** Ajout d'un lien vers la campagne Matomo pour l'origine des demandes d'aide.
- **Associations :** Page des associations rendue côté serveur.

### Évolutions techniques
- **Migration vers SSR :**  Implémentation du rendu côté serveur pour de nombreuses pages, incluant l'utilisation de composants Svelte et l'optimisation de l'enrichissement des données.
- **Refonte de l'architecture :**  Abstraction de la logique d'enrichissement, séparation des composants client et serveur, et mutualisation des composants.
- **Optimisations de performance :** Préchargement des données et des assets pour améliorer la vitesse de chargement des pages.
- **Sécurité :** Mise à jour de plusieurs dépendances pour corriger des vulnérabilités (uuid, DomPurify, Multer). Ajout d'outils de validation de la configuration (zizmor).
- **CI/CD :** Amélioration de la configuration du CI/CD, notamment avec l'ajout de secrets explicites et la configuration de Renovate.
- **Dépendances :** Mise à jour de plusieurs dépendances (vitest, papaparse, prettier-plugin-svelte, etc.).
- **Configuration :** Ajout d'un Nix Shell pour faciliter le développement en local.

### Autres changements
- **SEO :** Ajout de balises canoniques, de sitemaps et de robots.txt pour améliorer le référencement.
- **Documentation :** Mise à jour du README.
- **Nettoyage de code :** Suppression de code inutile et amélioration de la lisibilité du code.
- **Correction de bugs :** Correction de plusieurs bugs mineurs, notamment liés à l'affichage des liens et des titres.
- **Amélioration de l'UI :** Utilisation des composants DSFR pour une meilleure cohérence visuelle.
