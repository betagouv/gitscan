## Changelog : ami-notifications-api (30 derniers jours, au 18 août 2026)

### Résumé
Ce mois-ci, l'application a franchi une étape importante avec l'introduction d'un nouveau module de "Services" et d'un outil de gestion renforcé pour les administrateurs. L'expérience utilisateur a également été fluidifiée, notamment via une refonte de l'écran d'accueil et une gestion plus intuitive de l'authentification.

### Évolutions fonctionnelles
- **Nouveau module "Services"** : ajout d'un menu dédié, de pages de détails avec rendu Markdown et d'un système de déploiement progressif via des feature flags [#943](https://github.com/numerique-gouv/ami-notifications-api/issues/943).
- **Administration renforcée** : nouveaux outils pour les agents permettant de gérer (ajouter, modifier, supprimer, lister) les services avec un suivi des modifications (audit logs) [#1054](https://github.com/numerique-gouv/ami-notifications-api/issues/1054).
- **Amélioration des suivis (Followups)** : ajout de pages de détails et amélioration de l'affichage des informations partenaires [#266](https://github.com/numerique-gouv/ami-notifications-api/issues/266).
- **Expérience utilisateur (UX)** :
    - Refonte de l'écran de démarrage (mise en page, titres et liens d'aide) [#1098](https://github.com/numerique-gouv/ami-notifications-api/issues/1098).
    - Affichage de promotions automatiques sur la page d'accueil liées aux vacances scolaires [#1001](https://github.com/numerique-gouv/ami-notifications-api/issues/1001).
    - Optimisation du flux d'authentification (nouvelle page de connexion et meilleure gestion des erreurs FranceConnect) [#1152](https://github.com/numerique-gouv/ami-notifications-api/issues/1152).
    - Ajout de bannières informatives sur les pages d'édition [#769](https://github.com/numerique-gouv/ami-notifications-api/issues/769).
    - Corrections diverses : boutons de préférences, initialisation des dates et corrections de textes [#1107](https://github.com/numerique-gouv/ami-notifications-api/issues/1107), [#1076](https://github.com/numerique-gouv/ami-notifications-api/issues/1076), [#1170](https://github.com/numerique-gouv/ami-notifications-api/issues/1170), [#1157](https://github.com/numerique-gouv/ami-notifications-api/issues/1157).
- **Partenariat** : intégration du partenaire "RDV SP" [#1130](https://github.com/numerique-gouv/ami-notifications-api/issues/1130).

### Évolutions techniques
- **Sécurité et API** : mise en place de la limitation de débit (rate limiting) pour les clés d'accès et ajout d'un endpoint de vérification [#1096](https://github.com/numerique-gouv/ami-notifications-api/issues/1096). Finalisation de la migration des champs de notification vers l'API v2 [#1005](https://github.com/numerique-gouv/ami-notifications-api/issues/1005).
- **Infrastructure et Build** : optimisation du build avec Vite pour le proxying des URLs Django et simplification de la gestion des variables d'environnement [#1138](https://github.com/numerique-gouv/ami-notifications-api/issues/1138), [#1095](https://github.com/numerique-gouv/ami-notifications-api/issues/1095).
- **CI/CD et Qualité** : ajout d'une action GitHub pour les tests système [#10](https://github.com/numerique-gouv/ami-notifications-api/issues/10) et d'une vérification des messages de commit en pré-commit [#157](https://github.com/numerique-gouv/ami-notifications-api/issues/157).
- **Refactoring** : optimisation des composants frontend (modales, navigation et gestion des URLs de services) [#979](https://github.com/numerique-gouv/ami-notifications-api/issues/979), [#950](https://github.com/numerique-gouv/ami-notifications-api/issues/950), [#1063](https://github.com/numerique-gouv/ami-notifications-api/issues/1063).
- **Tests** : amélioration de la gestion des secrets de test et suppression de tests obsolètes [#1154](https://github.com/numerique-gouv/ami-notifications-api/issues/1154), [#1165](https://github.com/numerique-gouv/ami-notifications-api/issues/1165).

### Autres changements
- **Nettoyage** : suppression d'icônes et de code inutilisés [#445](https://github.com/numerique-gouv/ami-notifications-api/issues/445), [#266](https://github.com/numerique-gouv/ami-notifications-api/issues/266).
- **Standardisation** : passage à l'attribut de langue français et utilisation des apostrophes typographiques [#1118](https://github.com/numerique-gouv/ami-notifications-api/issues/1118), [#1161](https://github.com/numerique-gouv/ami-notifications-api/issues/1161).
- **Documentation** : affinement du schéma de l'API [#876](https://github.com/numerique-gouv/ami-notifications-api/issues/876).
