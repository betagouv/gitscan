## Changelog : histologe (30 derniers jours, au 16 octobre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration du cycle de vie des signalements (clôture, orientation) et sur l'enrichissement des outils de suivi géographique grâce à un nouvel historique des adresses. Des efforts significatifs ont également été portés sur la sécurité (audit des logs, renforcement de la double authentification) et sur l'optimisation des performances de recherche et des tableaux de bord statistiques.

### Évolutions fonctionnelles

**Gestion des signalements et dossiers**
- Amélioration du processus de clôture : ajout d'une validation par étapes [#6352](https://github.com/MTES-MCT/histologe/issues/6352), ajustement des options de clôture [#6436](https://github.com/MTES-MCT/histologe/issues/6436) et repositionnement des champs dans le formulaire [#6362](https://github.com/MTES-MCT/histologe/issues/6362).
- Évolution des motifs de clôture et du calcul du taux de résolution [#6370](https://github.com/MTES-MCT/histologe/issues/6370).
- Ajout d'un onglet "Orientation" dans les dossiers du Back Office [#6406](https://github.com/MTES-MCT/histologe/issues/6406).
- Paramétrage enrichi pour les affectations automatiques [#6386](https://github.com/MTES-MCT/histologe/issues/6386).

**Gestion des adresses et géolocalisation**
- Mise en place de l'historique des adresses avec vues liste et carte [#6416](https://github.com/MTES-MCT/histologe/issues/6416), [#6310](https://github.com/MTES-MCT/histologe/issues/6310) et fonctionnalité d'export [#6353](https://github.com/MTES-MCT/histologe/issues/6353).
- Amélioration de la recherche d'adresse par code postal et ville via une liste de résultats [#6420](https://github.com/MTES-MCT/histologe/issues/6420).
- Limitation des suggestions d'adresses au territoire de l'utilisateur lors de l'import d'arrêtés [#6410](https://github.com/MTES-MCT/histologe/issues/6410).

**Interface et Expérience Utilisateur**
- Mise à jour des tableaux de bord statistiques (Metabase) pour les RT [#6435](https://github.com/MTES-MCT/histologe/issues/6435).
- Augmentation du nombre de recherches sauvegardées possibles dans les listes de signalements [#6369](https://github.com/MTES-MCT/histologe/issues/6369).
- Renforcement de la sécurité via l'extension de la double authentification (2FA) sur le Front Office [#6390](https://github.com/MTES-MCT/histologe/issues/6390).
- Améliorations visuelles : allègement du header/footer [#6422](https://github.com/MTES-MCT/histologe/issues/6422) et ajout du bouton lien au format DSFR dans l'éditeur TinyMCE [#6383](https://github.com/MTES-MCT/histologe/issues/6383).

### Évolutions techniques

**Architecture et API**
- Refactorisation du code : déplacement de méthodes de plusieurs repositories vers des services de requête dédiés (Query Services) [#6378](https://github.com/MTES-MCT/histologe/issues/6378).
- Optimisation de l'API : mise en place de vues distinctes (résumé vs détail) pour les listes de signalements [#6357](https://github.com/MTES-MCT/histologe/issues/6357).
- Création d'une commande pour l'archivage des signalements [#6365](https://github.com/MTES-MCT/histologe/issues/6365).
- Ajout d'une page de test pour l'API de Document IA [#6431](https://github.com/MTES-MCT/histologe/issues/6431).

**Infrastructure et Performance**
- Optimisation des requêtes SQL lors de l'utilisation des filtres par zone [#6356](https://github.com/MTES-MCT/histologe/issues/6356).
- Mise à jour de l'infrastructure Metabase (intégration PostgreSQL et mise à jour MySQL) [#6345](https://github.com/MTES-MCT/histologe/issues/6345).
- Optimisation des déploiements Scalingo avec l'installation du package `rev` [#6373](https://github.com/MTES-MCT/histologe/issues/6373).

**Sécurité et Audit**
- Sécurisation des logs : suppression des noms de fichiers et des UUID exploitables pour limiter les risques d'audit [#6344](https://github.com/MTES-MCT/histologe/issues/6344).
- Nettoyage des logs de suivi des appels API [#6459](https://github.com/MTES-MCT/histologe/issues/6459).

### Autres changements
- Corrections diverses d'interface (CSS mobile, hauteur des champs de texte, menus contextuels) et mise à jour des composants et versions des packages JS [#6487](https://github.com/MTES-MCT/histologe/issues/6487).
