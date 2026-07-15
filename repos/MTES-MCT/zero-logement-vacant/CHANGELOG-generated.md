## Changelog : zero-logement-vacant (30 derniers jours, au 08 juillet 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations de la qualité du code, des corrections de bugs et l'ajout de nouvelles fonctionnalités, notamment concernant la gestion des utilisateurs, l'export de données et l'intégration de données externes. Des efforts importants ont été consacrés à la refactorisation du code et à l'amélioration des tests.

### Évolutions fonctionnelles
- Amélioration de la gestion des utilisateurs : correction du filtrage des périmètres multi-structures et prise en compte des établissements. [#1870](https://github.com/MTES-MCT/zero-logement-vacant/issues/1870)
- Correction de l'export des données : l'étiquette DPE (Diagnostic de Performance Énergétique) est maintenant correctement exportée. [#1818](https://github.com/MTES-MCT/zero-logement-vacant/issues/1818)
- Ajout de la possibilité d'éditer les propriétaires dont l'adresse BAN (Bureau d'Aide au Numérotage) a un score nul. [#1881](https://github.com/MTES-MCT/zero-logement-vacant/issues/1881)
- Ajout d'un contrôle de plein écran à la carte des logements. [#1872](https://github.com/MTES-MCT/zero-logement-vacant/issues/1872)
- Amélioration de la gestion des utilisateurs CEREMA LOVAC : déduplication des utilisateurs non enregistrés par adresse e-mail. [#1888](https://github.com/MTES-MCT/zero-logement-vacant/issues/1888)
- Ajout d'une fonctionnalité permettant de lister les consommateurs CEREMA Portail DF LOVAC non enregistrés. [#1846](https://github.com/MTES-MCT/zero-logement-vacant/issues/1846)
- Correction de l'affichage du libellé de l'année de vacance (remplacement de "inconsistancy2022" par "2023"). [#1875](https://github.com/MTES-MCT/zero-logement-vacant/issues/1875)
- Correction de la couleur des icônes de filtre de logement (utilisation de la couleur "bleu-france"). [#1876](https://github.com/MTES-MCT/zero-logement-vacant/issues/1876)
- Modification des libellés de ressources pour une meilleure clarté. [#1878](https://github.com/MTES-MCT/zero-logement-vacant/issues/1878)

### Évolutions techniques
- Refactorisation importante du code de validation, migration vers `validatorNext` pour une meilleure performance et maintenabilité.
- Mise en place d'un système de cache pour les données de référence afin d'améliorer les performances. [#1852](https://github.com/MTES-MCT/zero-logement-vacant/issues/1852)
- Migration des outils de linting et de formattage vers `oxlint` et `oxfmt`. [#1852](https://github.com/MTES-MCT/zero-logement-vacant/issues/1852)
- Amélioration de la gestion des tests, notamment pour l'export des données et les API.
- Refactorisation de l'architecture pour utiliser des factories plus robustes et modulaires.
- Déploiement du frontend avec Terraform. [#1882](https://github.com/MTES-MCT/zero-logement-vacant/issues/1882)
- Correction de problèmes liés à la gestion du cycle de vie des images MapLibre. [#1863](https://github.com/MTES-MCT/zero-logement-vacant/issues/1863)

### Autres changements
- Ajout de documentation pour la nouvelle fonctionnalité de réparation (repair harness).
- Mise à jour des dépendances (sans impact majeur sur l'utilisateur).
- Amélioration de la configuration du CI/CD.
- Correction de problèmes mineurs de style et de formatage du code.
- Ajout de seeds pour l'environnement de démonstration.
- Correction de bugs liés au filtre intercommunal DDT. [#1867](https://github.com/MTES-MCT/zero-logement-vacant/issues/1867)
- Amélioration du dashboard d'analyse. [#1868](https://github.com/MTES-MCT/zero-logement-vacant/issues/1868)
- Correction de l'affichage du fallback "Pas d'information" pour le type de propriétaire. [#1882](https://github.com/MTES-MCT/zero-logement-vacant/issues/1882)
