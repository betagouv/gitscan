## Changelog : infomedicament (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les améliorations se sont concentrées sur l'optimisation des performances du site, notamment en améliorant la mise en cache des données et en optimisant la génération du sitemap. Une nouvelle structure de menu a été implémentée et des améliorations ont été apportées à l'importation et à la gestion des données PBDM.

### Évolutions fonctionnelles
- **Nouveau menu :** Mise en place d'un nouveau menu dans l'en-tête et le pied de page du site. [#239](https://github.com/betagouv/infomedicament/pull/239)
- **Ajout des classes cliniques :** Intégration des classes cliniques avec pathos. [#212](https://github.com/betagouv/infomedicament/issues/212)
- **Sitemap :** Ajout d'un sitemap.xml pour améliorer le référencement du site, avec une intégration de test associée.
- **Pages statiques :** Les pages "alpha_lists" et "glossaire" sont maintenant générées statiquement pour de meilleures performances.

### Évolutions techniques
- **Performances (Cache) :** Mise en cache des requêtes statiques à la base de données avec `unstable_cache` pour réduire la charge lors de la génération statique des pages (SSG).
- **Performances (Sitemap) :** Génération statique du sitemap au moment de la construction (build time) avec une revalidation ISR (Incremental Static Regeneration) toutes les 24 heures.
- **Performances (Header) :** Optimisation de la récupération des données ATC dans l'en-tête pour alléger le chargement des pages.
- **Refactoring :** Déplacement de la récupération des données pour les "alpha_lists" vers des composants serveur.
- **Build :** Optimisation de la taille de l'image de l'application en supprimant les artefacts inutiles (.next/cache).
- **Proxy :** Amélioration de la gestion du proxy pour éviter de limiter les requêtes RSC (React Server Components) et de préchargement.
- **Rate Limit :** Ajustement du limiteur de débit (rate limit) du proxy en staging.

### Autres changements
- **Scripts :** Ajout de scripts pour l'importation des données PBDM et la construction des tables PostgreSQL dérivées.
- **Devcontainer :** Ajout du script d'importation PBDM au setup du devcontainer.
- **Configuration :** Ajout d'une configuration pour ignorer le dossier `.next/server` lors de la construction.
- **Corrections :** Résolution de collisions de clés dans le cache `unstable_cache` entre différentes fonctions.
- **Corrections :** Rétrogradation de l'utilisation de `unstable_cache` pour `getNoticeRcpLastUpdated` suite à des problèmes.
