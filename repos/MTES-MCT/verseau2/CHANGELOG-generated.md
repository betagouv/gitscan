## Changelog : verseau2 (30 derniers jours, au 13 mai 2026)

### Résumé
Cette version apporte des améliorations significatives à l'application, notamment l'ajout de nouvelles colonnes au bilan, une meilleure gestion des erreurs lors de l'envoi de rapports, et des corrections pour la redirection de l'URL et la gestion des adresses email. Des optimisations ont également été apportées à la structure du code backend et à la documentation.

### Évolutions fonctionnelles
- Ajout de nouvelles colonnes au bilan, répondant aux besoins exprimés dans l'issue [#72](https://github.com/MTES-MCT/verseau2/issues/72).
- Les rapports sont désormais envoyés même en cas d'erreur, améliorant la fiabilité du système [#76](https://github.com/MTES-MCT/verseau2/issues/76).
- Correction d'un problème de redirection de l'URL `https://www.saineau.beta.gouv.fr/verseau` vers une URL reconstruite par Nginx [#80](https://github.com/MTES-MCT/verseau2/issues/80).
- Mise à jour du titre de l'application et ajout de la gestion de l'environnement [#74](https://github.com/MTES-MCT/verseau2/issues/74).
- Correction de la liste des ouvrages RMC [#69](https://github.com/MTES-MCT/verseau2/issues/69).
- Correction d'un bug lié au trim des adresses email dans les requêtes [#70](https://github.com/MTES-MCT/verseau2/issues/70).
- Ajout de la configuration du serveur pour Docker [#73](https://github.com/MTES-MCT/verseau2/issues/73).
- Correction d'un correctif recette [#71](https://github.com/MTES-MCT/verseau2/issues/71).

### Évolutions techniques
- Amélioration de la structure des types et des sélections dans le backend [#81](https://github.com/MTES-MCT/verseau2/issues/81).
- Refactoring de la gestion des requêtes pour les API REST MASA.
- Amélioration du formatage des requêtes SQL dans les logs.
- Limitation de la longueur des paramètres dans les logs de requête pour une meilleure lisibilité.
- Fix des règles ESLint et gestion des erreurs dans le backend [#75](https://github.com/MTES-MCT/verseau2/issues/75).
- Ajout de paths manquants.

### Autres changements
- Désactivation temporaire de la synchronisation de la base de données [#78](https://github.com/MTES-MCT/verseau2/issues/78).
- Amélioration de la documentation et des commandes dans le fichier `AGENTS.md`.
