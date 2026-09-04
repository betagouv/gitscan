## Changelog : pitchou (30 derniers jours, au 27 août 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de la gestion des espèces protégées et de leurs impacts, tant au niveau de l'interface utilisateur que de la fiabilité des données. Les capacités d'administration ont été renforcées pour faciliter les revues annuelles et la gestion des dossiers, tandis que la génération de documents a été simplifiée et sécurisée.

### Évolutions fonctionnelles
- **Gestion des espèces et impacts** : Amélioration de l'interface utilisateur pour les espèces impactées et ajout de liens directs vers le référentiel des types d'impact.
- **Suivi des anomalies** : Harmonisation de l'affichage des anomalies entre les logs de synchronisation et l'onglet projet pour une meilleure cohérence.
- **Gestion documentaire** : 
    - Possibilité de générer plusieurs fichiers simultanément [#678](https://github.com/betagouv/pitchou/issues/678).
    - Clarification des libellés dans les modèles de documents [#677](https://github.com/betagouv/pitchou/issues/677).
    - Correction permettant la génération de documents même sans espèces listées [#676](https://github.com/betagouv/pitchou/issues/676).
- **Administration et dossiers** :
    - Ajout de catégories d'activités [#688](https://github.com/betagouv/pitchou/issues/688).
    - Possibilité d'assigner des "followers" à un dossier [#671](https://github.com/betagouv/pitchou/issues/671).
    - Suivi de la source explicite des dossiers [#679](https://github.com/betagouv/pitchou/issues/679).
    - Nouvel outil permettant aux administrateurs de télécharger les données des dossiers pour les revues annuelles [#684](https://github.com/betagouv/pitchou/issues/684).
    - Possibilité de créer et mettre à jour des dossiers depuis l'extérieur de la DN [#669](https://github.com/betagouv/pitchou/issues/669).
    - Possibilité de déclencher manuellement la synchronisation DN [#687](https://github.com/betagouv/pitchou/issues/687).
- **Corrections** : Rectification de l'affichage de la zone cadastral sur la carte du projet [#674](https://github.com/betagouv/pitchou/issues/674).

### Évolutions techniques
- **Fiabilisation des données** : Migration du référentiel des types d'impact vers la base de données (au lieu d'un fichier externe) pour plus de robustesse [#670](https://github.com/betagouv/pitchou/issues/670) et [#691](https://github.com/betagouv/pitchou/issues/691).
- **Automatisation** : Peuplement automatique de la base de données avec les données des espèces impactées lors de la création de nouveaux fichiers [#683](https://github.com/betagouv/pitchou/issues/683).
- **Refactoring** : Renommage de la phase de recevabilité pour plus de clarté [#690](https://github.com/betagouv/pitchou/issues/690).
- **Observabilité** : Ajout d'un déclencheur de test Sentry pour l'administration [#675](https://github.com/betagouv/pitchou/issues/675).

### Autres changements
- **Documentation** : Ajout d'une ADR (Architecture Decision Record) détaillant la structuration des espèces protégées en base de données.
- **Maintenance du code** : 
    - Mise en place d'un changelog interne [#686](https://github.com/betagouv/pitchou/issues/686).
    - Suppression des outils d'import obsolètes [#682](https://github.com/betagouv/pitchou/issues/682).
    - Application d'une règle de limitation de taille des fichiers (200 lignes) pour améliorer la lisibilité [#680](https://github.com/betagouv/pitchou/issues/680).
