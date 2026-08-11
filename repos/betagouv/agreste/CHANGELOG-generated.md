## Changelog : agreste (30 derniers jours, au 10 août 2026)

### Résumé
Ce mois-ci, l'expérience de recherche a été considérablement enrichie avec des filtres plus intuitifs, une meilleure gestion de la pagination et une interface plus ergonomique. Le système de notifications a été entièrement modernisé pour offrir plus de flexibilité, tandis que la stabilité technique du projet a été renforcée par l'introduction de tests automatisés de bout en bout et une mise à jour des technologies de base (Python et PostgreSQL).

### Évolutions fonctionnelles

**Recherche et filtrage**
- Amélioration de l'ergonomie de recherche : ajout de compteurs dans les filtres (et suppression automatique des filtres vides) [#65](https://github.com/betagouv/agreste/pull/65).
- Interface de recherche enrichie : introduction de filtres repliables [#46](https://github.com/betagouv/agreste/pull/46), affichage de la hiérarchie des taxonomies dans la barre latérale [#45](https://github.com/betagouv/agreste/pull/45) et ajout de métadonnées dans les résultats [#48](https://github.com/betagouv/agreste/pull/48).
- Navigation optimisée : ajout de la pagination en haut et en bas de page [#54](https://github.com/betagouv/agreste/pull/54), possibilité de sélectionner plusieurs valeurs dans les facettes [#43](https://github.com/betagouv/agreste/pull/43) et affichage de la requête actuelle dans la barre de recherche [#59](https://github.com/betagouv/agreste/pull/59).
- Corrections de confort : suppression du saut automatique vers les résultats de recherche [#64](https://github.com/betagouv/agreste/pull/64) et réinitialisation de la page lors du changement de filtre [#54](https://github.com/betagouv/agreste/pull/54).

**Interface utilisateur et blocs de contenu**
- Correction des pages d'erreur (404 et 500) pour garantir un rendu conforme au design système (DSFR).
- Correction d'un problème d'affichage (overflow) pour les noms de fichiers longs dans les tuiles de téléchargement [#40](https://github.com/betagouv/agreste/pull/40).
- Évolution du bloc "Publications récentes" : ajout d'une option simple pour afficher ou masquer le lien "Voir tout".
- Correction de l'affichage des couleurs des tags sélectionnés.

### Évolutions techniques

**Infrastructure et CI/CD**
- Mise à jour des environnements : passage aux dernières versions de Python et PostgreSQL [#58](https://github.com/betagouv/agreste/pull/58).
- Qualité logicielle : mise en place de tests de bout en bout (E2E) avec Playwright, incluant des tests de régression visuelle.
- Optimisation de la CI : les tests sont désormais exécutés uniquement sur les Pull Requests pour accélérer les cycles de développement.
- Réorganisation de la structure des tests pour une meilleure maintenance.

**Architecture et Refactoring**
- Refonte majeure du système de notifications : séparation de la logique, ajout de logs et amélioration de la configuration.
- Amélioration de la gestion des versions du logiciel pour une source de vérité unique.

### Autres changements
- **Documentation** : mise à jour du README incluant les instructions de mise à jour et de déploiement.
- **Internationalisation (i18n)** : amélioration de la gestion des traductions et indépendance accrue vis-à-vis du dépôt `sites_conformes`.
