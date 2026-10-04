## Changelog : drive (30 derniers jours, au 1er octobre 2026)

### Résumé
Ce mois-ci, le projet a franchi une étape majeure avec l'introduction d'un système de gestion des restrictions beaucoup plus granulaire, permettant un contrôle précis sur l'accès aux dossiers et fichiers. Le processus de téléchargement a été renforcé pour plus de fiabilité, et l'interface utilisateur a été affinée pour améliorer la navigation et le rendu des documents.

### Évolutions fonctionnelles
- **Nouveau système de restrictions** : possibilité d'activer ou désactiver des restrictions sur des éléments, de cibler des dossiers spécifiques et de masquer les éléments restreints des résultats de recherche et des exports.
- **Fiabilisation des téléchargements** : le système réserve désormais l'espace de stockage nécessaire avant de valider un upload et communique la taille des fichiers pour une gestion plus robuste.
- **Amélioration de l'interface** : correction de la vue "Récents" qui ne se mettait pas à jour correctement, meilleure gestion des langues de navigateur et amélioration du rendu des fichiers PDF.
- **Sécurité accrue** : mise en place de limitations de débit (rate limiting) sur la création d'éléments et renforcement des droits d'upload à la racine.

### Évolutions techniques
- **Optimisation des performances** : accélération de la recherche de hiérarchie (ancêtres) et implémentation d'un pool de connexions pour la base de données PostgreSQL.
- **Infrastructure et DevOps** : remplacement de MinIO par RustFS pour le stockage d'objets en local et mise à jour des configurations Docker et Helm.
- **Refactoring** : migration vers la bibliothèque de composants UI officielle (`@gouvfr-lasuite/ui-components`) et restructuration de la logique de gestion des permissions pour plus de modularité.
- **Qualité et tests** : renforcement de la couverture des tests de bout en bout (E2E), notamment sur la corbeille et les réservations d'upload, et amélioration des tests de charge.

### Autres changements
- **Documentation** : mise à jour de la documentation technique, notamment sur les paramètres de permissions et les exemples de serveurs de ressources.
- **Nettoyage** : suppression de variables d'environnement inutilisées et simplification de certains flux du backend.
