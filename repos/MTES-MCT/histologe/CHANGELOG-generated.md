## Changelog : histologe (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'interface d'administration (Back Office), notamment via de nouveaux outils de visualisation cartographique et d'exportation pour l'historique des adresses. La gestion des dossiers et des signalements a été affinée pour offrir un suivi plus précis, tandis que la sécurité a été renforcée par l'extension de la double authentification et un meilleur contrôle des données sensibles dans les journaux système.

### Évolutions fonctionnelles
- **Gestion des dossiers et signalements (Back Office) :**
    - Ajout d'un onglet "Orientation" dans les dossiers [#6406](https://github.com/MTES-MCT/histologe/issues/6406).
    - Amélioration du processus de clôture des dossiers avec de nouveaux ajustements d'options [#6436](https://github.com/MTES-MCT/histologe/issues/6436) et une validation par étapes [#6352](https://github.com/MTES-MCT/histologe/issues/6352).
    - Ajout de paramètres pour les affectations automatiques [#6386](https://github.com/MTES-MCT/histologe/issues/6386).
    - Mise à jour des listes de motifs de clôture et calcul du taux de résolution [#6370](https://github.com/MTES-MCT/histologe/issues/6370).
- **Historique et recherche d'adresses :**
    - Nouvelles vues pour l'historique des adresses : vue liste [#6416](https://github.com/MTES-MCT/histologe/issues/6416) et vue carte [#6310](https://github.com/MTES-MCT/histologe/issues/6310).
    - Ajout d'une fonctionnalité d'exportation des adresses [#6353](https://github.com/MTES-MCT/histologe/issues/6353).
    - Amélioration de la recherche d'adresses (par code postal et ville) [#6420](https://github.com/MTES-MCT/histologe/issues/6420) et limitation des adresses proposées à l'import d'arrêtés au territoire concerné [#6410](https://github.com/MTES-MCT/histologe/issues/6410).
    - Augmentation du nombre de recherches sauvegardées possibles [#6369](https://github.com/MTES-MCT/histologe/issues/6369).
- **Expérience utilisateur (Front Office) :**
    - Renforcement de la sécurité par l'extension de la double authentification (MFA) [#6390](https://github.com/MTES-MCT/histologe/issues/6390).
    - Corrections d'interface : affichage des erreurs de validation [#6394](https://github.com/MTES-MCT/histologe/issues/6394), sélecteur de bâtiment sur mobile [#6522](https://github.com/MTES-MCT/histologe/issues/6522) et gestion du menu contextuel [#6493](https://github.com/MTES-MCT/histologe/issues/6493).
    - Obligation de validation de l'adresse pour les signalements [#6268](https://github.com/MTES-MCT/histologe/issues/6268).
- **Statistiques :**
    - Mise à jour des tableaux de bord statistiques via Metabase [#6435](https://github.com/MTES-MCT/histologe/issues/6435).

### Évolutions techniques
- **Architecture et API :**
    - Refactoring des méthodes de repository vers des services de requête dédiés pour une meilleure structure [#6378](https://github.com/MTES-MCT/histologe/issues/6378).
    - Mise en place de vues résumé et détaillée pour l'audit de l'API [#6357](https://github.com/MTES-MCT/histologe/issues/6357).
    - Nettoyage des logs de suivi des appels API [#6459](https://github.com/MTES-MCT/histologe/issues/6459).
- **Infrastructure et DevOps :**
    - Évolution de l'infrastructure Metabase avec l'intégration de PostgreSQL et mise à jour de MySQL [#6345](https://github.com/MTES-MCT/histologe/issues/6345).
    - Optimisation des déploiements Scalingo via l'installation du package `rev` [#6373](https://github.com/MTES-MCT/histologe/issues/6373).
- **Sécurité et Performance :**
    - Sécurisation des logs en supprimant les données sensibles (noms de fichiers et UUID exploitables) [#6344](https://github.com/MTES-MCT/histologe/issues/6344).
    - Optimisation des performances : requêtes de filtrage par zone [#6356](https://github.com/MTES-MCT/histologe/issues/6356) et résolution des problèmes d'engorgement des workers [#6327](https://github.com/MTES-MCT/histologe/issues/6327).

### Autres changements
- Amélioration du wording de l'interface [#6331](https://github.com/MTES-MCT/histologe/issues/6331).
- Nettoyage du code et suppression de commandes temporaires [#6355](https://github.com/MTES-MCT/histologe/issues/6355).
