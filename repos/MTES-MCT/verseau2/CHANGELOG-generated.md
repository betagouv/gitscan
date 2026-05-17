## Changelog : verseau2 (30 derniers jours, au 13 mai 2026)

### Résumé
Ce changelog présente les améliorations apportées à Verseau2 au cours du dernier mois. Les principales évolutions concernent l'ajout de nouvelles colonnes pour le bilan, l'amélioration de la gestion des erreurs et des rapports, ainsi que des optimisations de la configuration pour le déploiement en environnement Docker. Des corrections de bugs et des améliorations de la documentation ont également été réalisées.

### Évolutions fonctionnelles
- Ajout de nouvelles colonnes au bilan, répondant aux besoins de l'évolution [#72](https://github.com/MTES-MCT/verseau2/issues/72).
- Les rapports sont désormais envoyés même en cas d'erreur [#76](https://github.com/MTES-MCT/verseau2/issues/76).
- Correction d'un bug concernant la liste des ouvrages RMC [#69](https://github.com/MTES-MCT/verseau2/issues/69).
- Mise à jour du titre de l'application et ajout de la gestion de l'environnement [#74](https://github.com/MTES-MCT/verseau2/issues/74).
- Correction d'un problème de redirection de l'URL `https://www.saineau.beta.gouv.fr/verseau` [#80](https://github.com/MTES-MCT/verseau2/issues/80).
- Correction d'un bug lié au trim des adresses email dans les requêtes [#70](https://github.com/MTES-MCT/verseau2/issues/70).
- Correction d'un bug recette [#71](https://github.com/MTES-MCT/verseau2/issues/71).

### Évolutions techniques
- Amélioration de la structure des types et des signatures dans le backend [#81](https://github.com/MTES-MCT/verseau2/issues/81).
- Fix des règles ESLint et amélioration de la gestion des erreurs dans le backend [#75](https://github.com/MTES-MCT/verseau2/issues/75).
- Ajout de la configuration du serveur pour Docker, facilitant le déploiement et l'exécution de l'application.
- Ajout de la configuration pour le reverse proxy [#73](https://github.com/MTES-MCT/verseau2/issues/73).
- Amélioration de la gestion des requêtes pour les API REST MASA.
- Ajout de paths manquants.
- Amélioration du formatage des requêtes SQL dans les logs.
- Limitation de la longueur des paramètres dans les logs de requête.

### Autres changements
- Désactivation temporaire de la synchronisation de la base de données [#78](https://github.com/MTES-MCT/verseau2/issues/78).
- Amélioration de la documentation et des commandes dans le fichier `AGENTS.md`.
