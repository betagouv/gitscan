## Changelog : verseau2 (30 derniers jours, au 20 mai 2026)

### Résumé
Ce mois-ci, Verseau2 a bénéficié d'améliorations significatives en termes de fonctionnalités d'export de données, de gestion des bilans et de configuration pour les déploiements. Des corrections de bugs et des améliorations de la qualité du code ont également été apportées, ainsi que des ajustements pour faciliter le déploiement et la configuration de l'application.

### Évolutions fonctionnelles
- Ajout de l'export CSV pour les données, permettant aux utilisateurs de récupérer facilement les informations au format tableur.  [#82](https://github.com/MTES-MCT/verseau2/issues/82)
- Ajout de nouvelles colonnes au bilan, enrichissant les informations disponibles pour l'analyse. [#72](https://github.com/MTES-MCT/verseau2/issues/72)
- Gestion des dates de début et de fin pour les bilans, offrant plus de flexibilité dans la génération des rapports. [#84](https://github.com/MTES-MCT/verseau2/issues/84)
- Les rapports sont désormais envoyés même en cas d'erreur, assurant une meilleure traçabilité des opérations. [#76](https://github.com/MTES-MCT/verseau2/issues/76)
- Mise à jour du titre de l'application et ajout de la gestion de l'environnement (développement, production, etc.). [#74](https://github.com/MTES-MCT/verseau2/issues/74)
- Correction d'un problème de redirection de l'URL `https://www.saineau.beta.gouv.fr/verseau`. [#80](https://github.com/MTES-MCT/verseau2/issues/80)

### Évolutions techniques
- Ajout de la gestion CORS pour permettre les déploiements frontend/backend sur des domaines différents. [#83](https://github.com/MTES-MCT/verseau2/issues/83)
- Amélioration de la structure des types et des services dans le backend pour une meilleure maintenabilité. [#81](https://github.com/MTES-MCT/verseau2/issues/81)
- Correction des règles ESLint et amélioration de la gestion des erreurs dans le backend. [#75](https://github.com/MTES-MCT/verseau2/issues/75)
- Ajout de la configuration pour le reverse proxy (Nginx), facilitant le déploiement de l'application. [#73](https://github.com/MTES-MCT/verseau2/issues/73)
- Amélioration de la gestion des requêtes pour les API REST MASA. [#85](https://github.com/MTES-MCT/verseau2/issues/85)
- Ajout de paths manquants pour les API REST MASA. [#86](https://github.com/MTES-MCT/verseau2/issues/86)
- Trim des adresses email dans les requêtes pour éviter les problèmes de formatage. [#70](https://github.com/MTES-MCT/verseau2/issues/70)

### Autres changements
- Mise à jour de la dépendance `axios` vers la version 1.16. [#66](https://github.com/MTES-MCT/verseau2/issues/66)
- Amélioration de la documentation et des commandes dans le fichier `AGENTS.md`. [#87](https://github.com/MTES-MCT/verseau2/issues/87)
- Désactivation temporaire de la synchronisation de la base de données. [#78](https://github.com/MTES-MCT/verseau2/issues/78)
- Ajout de la configuration du serveur pour Docker. [#77](https://github.com/MTES-MCT/verseau2/issues/77)
- Correction d'un correctif de recette. [#71](https://github.com/MTES-MCT/verseau2/issues/71)
