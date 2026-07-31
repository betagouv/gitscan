## Changelog : agreste (30 derniers jours, au 30 juillet 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la recherche, notamment l'ajout de filtres, la pagination des résultats et une meilleure présentation des taxonomies. Des corrections de bugs et des améliorations de la sécurité ont également été apportées, ainsi que des optimisations pour les tests et le déploiement. Un effort important a été réalisé pour améliorer la robustesse et la maintenabilité du code.

### Évolutions fonctionnelles
- **Recherche :** Ajout de filtres pour affiner les résultats de recherche ([#43](https://github.com/betagouv/agreste/pull/43), [#46](https://github.com/betagouv/agreste/pull/46)).
- **Recherche :** Pagination des résultats de recherche pour une meilleure expérience utilisateur ([#54](https://github.com/betagouv/agreste/pull/54)).
- **Recherche :** Affichage de la requête de recherche actuelle dans la barre de recherche ([#59](https://github.com/betagouv/agreste/pull/59)).
- **Recherche :** Affichage de la hiérarchie des taxonomies dans la barre latérale de recherche ([#45](https://github.com/betagouv/agreste/pull/45)).
- **Recherche :** Possibilité de sélectionner plusieurs valeurs dans les facettes de recherche ([#43](https://github.com/betagouv/agreste/pull/43)).
- **Bloc "Publications récentes" :** Ajout d'une option pour filtrer le lien "Voir toutes les publications" ([#61](https://github.com/betagouv/agreste/pull/61)).
- **Pages d'erreur :** Correction des erreurs 404 et 500 et affichage du design système (DSFR) sur ces pages.
- **Notifications :** Ajout d'un système de notifications avec configuration et affichage dans l'interface d'administration ([#555](https://github.com/betagouv/agreste/pull/555), [#554](https://github.com/betagouv/agreste/pull/554), [#553](https://github.com/betagouv/agreste/pull/553)).
- **Iframe :** Gestion conditionnelle des pages lors du chargement en iframe ([#551](https://github.com/betagouv/agreste/pull/551)).

### Évolutions techniques
- **Tests :** Ajout de tests Playwright avec comparaison visuelle pour l'interface utilisateur ([#58](https://github.com/betagouv/agreste/pull/58)).
- **Tests :** Amélioration de la couverture de tests et refactoring pour utiliser des factories ([#39](https://github.com/betagouv/agreste/pull/39), [#27](https://github.com/betagouv/agreste/pull/27)).
- **CI/CD :** Mise en place d'un workflow GitHub Actions pour la création de releases ([#18](https://github.com/betagouv/agreste/pull/18), [#21](https://github.com/betagouv/agreste/pull/21)).
- **Déploiement :** Mise à jour des dépendances et support uniquement des dernières versions de Python et PostgreSQL ([#58](https://github.com/betagouv/agreste/pull/58)).
- **Architecture :** Refactorisation du code pour améliorer la réutilisation et la maintenabilité, notamment dans le module de recherche.
- **Sécurité :** Validation des entrées `year` et `authorId` pour renforcer la sécurité ([#47](https://github.com/betagouv/agreste/pull/47)).
- **Documentation :** Mise à jour de la documentation et ajout de commentaires pour faciliter la compréhension du code.

### Autres changements
- Mise à jour de la documentation pour ProConnect après la packagification ([#547](https://github.com/betagouv/agreste/pull/547)).
- Correction de bugs mineurs et améliorations de la lisibilité du code.
- Mise à jour des dépendances (tarteaucitronjs).
- Amélioration de la gestion des traductions et correction de problèmes liés à l'i18n ([#35](https://github.com/betagouv/agreste/pull/35)).
- Ajout de scripts de diagnostic pour le serveur (utilisation de la mémoire, latence).
- Correction d'un bug lié à l'affichage des couleurs des tags sélectionnés.
- Mise à jour du README avec des instructions de mise à niveau et de publication.
