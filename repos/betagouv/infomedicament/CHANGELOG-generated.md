## Changelog : infomedicament (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'optimisation des performances du site, notamment en améliorant la mise en cache des données et en optimisant la génération du sitemap. Une nouvelle structure de menu a été implémentée et des améliorations ont été apportées à l'importation des données PDBM.

### Évolutions fonctionnelles
- Ajout des classes cliniques avec pathos [#212](https://github.com/betagouv/infomedicament/issues/212).
- Nouvelle structure de menu pour l'en-tête et le pied de page.
- Ajout d'un sitemap.xml avec un test d'intégration.
- Préchargement désactivé pour les interactions afin d'optimiser les performances.

### Évolutions techniques
- Amélioration des performances du sitemap : génération statique au moment de la construction avec une revalidation ISR de 24 heures.
- Mise en cache statique des requêtes de base de données pour réduire la charge pendant la génération de sites statiques (SSG).
- Correction d'une collision de clés dans le cache `unstable_cache` entre `getSubstanceSpecialitesCIS` et `getSubstanceAllSpecialites`.
- Refactorisation du code pour déplacer la récupération des données vers des composants serveur pour `alpha_lists`.
- Utilisation de `generateStaticParams` pour la SSG de `alpha_lists` et `glossaire`.
- Optimisation de l'en-tête : remplacement de `getAtc` par `getAtcMenuItems` plus léger.
- Utilisation de `Sec-Fetch-Dest` pour ignorer les requêtes RSC et de préchargement du proxy pour éviter les limitations de débit.
- Suppression des artefacts `.next/cache` pour réduire la taille de l'image de l'application.
- Ajout de `.next/server` à `slugignore` pour éviter des problèmes lors de la construction.

### Autres changements
- Ajout de scripts pour l'importation des données PDBM, incluant des commandes npm post-import pour les tables PostgreSQL dérivées et une configuration pour le devcontainer et Scalingo.
- Réintroduction d'une limite de 200 requêtes par minute sur le proxy.
- Augmentation temporaire de la limite de débit du proxy à 1000 requêtes par minute en environnement de staging.
