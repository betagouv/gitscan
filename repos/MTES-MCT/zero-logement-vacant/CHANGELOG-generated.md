## Changelog : zero-logement-vacant (30 derniers jours, au 21 juillet 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de la sécurité et de l'authentification, avec la migration vers un nouveau système d'authentification (Better Auth). Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées, notamment au niveau de la gestion des filtres, de la cartographie et de l'export de données. Des outils de diagnostic et de réparation des données ont été ajoutés.

### Évolutions fonctionnelles
- Correction de l'affichage des marqueurs de bâtiments sur la carte ([#1873](https://github.com/MTES-MCT/zero-logement-vacant/issues/1873)).
- Amélioration de la gestion des filtres intercommunaux pour les structures DDT ([#1867](https://github.com/MTES-MCT/zero-logement-vacant/issues/1867)).
- Possibilité de rendre le champ "date de naissance" optionnel lors de l'édition des propriétaires ([#1861](https://github.com/MTES-MCT/zero-logement-vacant/issues/1861)).
- Amélioration du rendu du tableau de bord d'analyse ([#1868](https://github.com/MTES-MCT/zero-logement-vacant/issues/1868)).
- Correction du libellé de l'année de vacance 2023 ([#1875](https://github.com/MTES-MCT/zero-logement-vacant/issues/1875)).
- Correction de la couleur des icônes de filtre pour utiliser la palette de couleurs "bleu-france" ([#1876](https://github.com/MTES-MCT/zero-logement-vacant/issues/1876)).
- Ajout d'un contrôle de plein écran à la carte des logements ([#1872](https://github.com/MTES-MCT/zero-logement-vacant/issues/1872)).
- Ajout d'un affichage des consommateurs LOVAC non enregistrés ([#1846](https://github.com/MTES-MCT/zero-logement-vacant/issues/1846)).
- Amélioration de l'affichage des périmètres sur la carte, avec possibilité de les masquer ou de les afficher en rouge ([#1884](https://github.com/MTES-MCT/zero-logement-vacant/issues/1884)).

### Évolutions techniques
- Migration vers un nouveau système d'authentification (Better Auth) pour renforcer la sécurité et améliorer l'expérience utilisateur. Cela inclut la gestion des sessions, la synchronisation des utilisateurs Cerema et la gestion des accès.
- Mise à jour des versions de Metabase et du pilote DuckDB pour corriger des vulnérabilités et améliorer la stabilité.
- Refactorisation du code d'authentification pour une meilleure maintenabilité et une plus grande sécurité.
- Ajout d'un outil de diagnostic et de réparation des données (ZLV repair harness) avec une interface en ligne de commande.
- Amélioration de la gestion des tests, notamment avec l'ajout de tests E2E avec Playwright.
- Mise en place d'un système de déploiement avec Terraform.
- Amélioration de la gestion des erreurs et des logs.
- Ajout de types pour améliorer la sécurité du code.

### Autres changements
- Mise à jour de la documentation pour refléter les changements apportés au système d'authentification et à l'outil de diagnostic.
- Correction de problèmes de formatage et de style dans le code.
- Ajout de commentaires et de documentation pour améliorer la lisibilité du code.
- Mise à jour des dépendances.
- Ajout d'une documentation pour l'implémentation du repair harness.
- Ajout d'une méthodologie de test RGAA pour l'accessibilité.
- Correction de la configuration du cron sur Clever Cloud.
