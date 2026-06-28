## Changelog : dossierfacile-backend (30 derniers jours, au 26 juin 2026)

### Résumé
Ce changelog présente les évolutions récentes du backend de DossierFacile.fr. Les améliorations portent principalement sur l'expérience utilisateur dans le back-office, la gestion des droits d'accès, l'optimisation des performances de recherche et l'ajout de nouvelles fonctionnalités pour la gestion des taxes foncières et des propriétaires.

### Évolutions fonctionnelles
- Ajout d'un endpoint de vérification d'email et suppression d'utilisateur, ainsi qu'un endpoint de test pour simuler un rejet par un opérateur. [#1260](https://github.com/MTES-MCT/dossierfacile-backend/issues/1260)
- Possibilité de télécharger des documents pour DFC avec des limites de débit personnalisées. [#1252](https://github.com/MTES-MCT/dossierfacile-backend/issues/1252)
- Amélioration de la gestion des taxes foncières avec l'ajout de règles Docia pour les catégories RESIDENCY et OWNER. [#1262](https://github.com/MTES-MCT/dossierfacile-backend/issues/1262)
- Support de plusieurs propriétaires pour le nom de la taxe foncière. [#1263](https://github.com/MTES-MCT/dossierfacile-backend/issues/1263)
- Ajout d'un premier fichier `agents.md` pour la documentation des agents. [#1253](https://github.com/MTES-MCT/dossierfacile-backend/issues/1253)
- Mise à jour du label de la taxe dans le back-office. [#1248](https://github.com/MTES-MCT/dossierfacile-backend/issues/1248)
- Ajout d'un log lors de la suppression d'un fichier dans le back-office. [#1240](https://github.com/MTES-MCT/dossierfacile-backend/issues/1240)

### Évolutions techniques
- Optimisation de la requête pour la récupération paginée des tenants à archiver.
- Correction d'un problème de concurrence pouvant entraîner la création de plusieurs tenants simultanément. [#1257](https://github.com/MTES-MCT/dossierfacile-backend/issues/1257)
- Refonte de la transaction pour la tâche d'archivage des tenants. [#1255](https://github.com/MTES-MCT/dossierfacile-backend/issues/1255)
- Amélioration de la vue matérialisée `latest_operator` pour une création plus efficace. [#1251](https://github.com/MTES-MCT/dossierfacile-backend/issues/1251)
- Ajout d'index sur la colonne `email` (en minuscules) de la table `user_account` pour optimiser les recherches. [#1256](https://github.com/MTES-MCT/dossierfacile-backend/issues/1256)
- Optimisation des recherches de tenants et de propriétaires.
- Amélioration de la dissociation de la jointure tenant/principal dans le back-office. [#1249](https://github.com/MTES-MCT/dossierfacile-backend/issues/1249)
- Vérification des permissions d'accès des opérateurs lors d'actions sur les tenants, les partages d'appartements et les fichiers. [#1254](https://github.com/MTES-MCT/dossierfacile-backend/issues/1254)
- Correction d'un bug empêchant les utilisateurs de se déconnecter du back-office. [#1256](https://github.com/MTES-MCT/dossierfacile-backend/issues/1256)

### Autres changements
- Bump de version à v3.5.11.
- Corrections et revue de code diverses.
