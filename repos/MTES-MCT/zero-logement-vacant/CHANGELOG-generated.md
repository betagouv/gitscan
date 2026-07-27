## Changelog : zero-logement-vacant (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de la sécurité et de l'authentification, avec une migration vers un nouveau système d'authentification (Better Auth). Des corrections de bugs et des optimisations ont également été apportées, notamment au niveau de la gestion des filtres, de l'export des données et de la synchronisation des utilisateurs Cerema. Enfin, des outils de diagnostic et de réparation des données ont été ajoutés.

### Évolutions fonctionnelles
- Correction d'un bug empêchant l'affichage correct des marqueurs de bâtiments sur la carte. [#1921](https://github.com/MTES-MCT/zero-logement-vacant/issues/1921)
- Amélioration de la gestion des filtres intercommunaux pour les logements en groupe. [#1870](https://github.com/MTES-MCT/zero-logement-vacant/issues/1870)
- Correction de l'export de l'étiquette énergétique des logements. [#1818](https://github.com/MTES-MCT/zero-logement-vacant/issues/1818)
- Correction d'un problème de doublons d'utilisateurs LOVAC Cerema lors du suivi analytique. [#1888](https://github.com/MTES-MCT/zero-logement-vacant/issues/1888)
- Amélioration de la visibilité des périmètres sur la carte, avec la possibilité de les afficher ou de les masquer. [#1884](https://github.com/MTES-MCT/zero-logement-vacant/issues/1884)
- Ajout d'un chargement paresseux du formulaire d'inscription Livestorm pour optimiser les performances. [#1924](https://github.com/MTES-MCT/zero-logement-vacant/issues/1924)

### Évolutions techniques
- **Authentification :** Migration vers un nouveau système d'authentification (Better Auth) pour renforcer la sécurité et améliorer l'expérience utilisateur. Cela inclut la gestion des sessions, la synchronisation des utilisateurs, la gestion des accès et la protection contre les attaques.
- **Performance :** Compression des réponses de l'API pour réduire la taille des données transférées et améliorer les temps de chargement. [#1925](https://github.com/MTES-MCT/zero-logement-vacant/issues/1925)
- **Infrastructure :** Ajout d'un paramètre pour configurer le type de base de données (flavor) via Terraform. [#1916](https://github.com/MTES-MCT/zero-logement-vacant/issues/1916)
- **Tests :** Mise à jour des dépendances de test (Cypress, Playwright, Jest).
- **Outils :** Création d'un outil de diagnostic et de réparation des données (ZLV repair harness) avec une interface en ligne de commande (CLI).
- **Mises à jour :** Mise à jour de Metabase et du pilote DuckDB. [#1921](https://github.com/MTES-MCT/zero-logement-vacant/issues/1921)

### Autres changements
- Documentation : Mise à jour de la documentation concernant la configuration de Clever Cloud et le nouveau système d'authentification.
- Correction de plusieurs problèmes de style et de formatage du code.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de tests unitaires et d'intégration pour améliorer la couverture du code.
- Mise à jour des dépendances npm et yarn.
- Amélioration de la conformité RGAA pour l'accessibilité. [#1893](https://github.com/MTES-MCT/zero-logement-vacant/issues/1893)
