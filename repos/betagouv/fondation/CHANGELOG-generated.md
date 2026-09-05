## Changelog : fondation (30 derniers jours, au 04/09/2026)

### Résumé
Cette période a été marquée par une amélioration significative de la fiabilité de l'ingestion des données et de l'accessibilité de l'interface. Les utilisateurs bénéficient de fonctionnalités enrichies pour la gestion des documents et un suivi plus précis des évaluations des magistrats.

### Évolutions fonctionnelles
- **Gestion des documents et des ordres du jour** : 
    - Amélioration de la préparation des ordres du jour via la sélection directe de fichiers dans les tableaux [#580](https://github.com/betagouv/fondation/issues/580).
    - Intégration automatique des polices et des en-têtes dans les documents générés [#588](https://github.com/betagouv/fondation/issues/588).
    - Automatisation de l'invalidation des rapports officiels lors de modifications de l'agenda (changement de date ou suppression de fichier) [#601](https://github.com/betagouv/fondation/issues/601) [#603](https://github.com/betagouv/fondation/issues/603).
    - Ajout de colonnes de statut pour les documents et possibilité de taguer les fichiers liés à une proposition [#560](https://github.com/betagouv/fondation/issues/560) [#562](https://github.com/betagouv/fondation/issues/562).
    - Correction du téléchargement des pièces jointes pour récupérer le fichier réel plutôt que la page de l'application [#583](https://github.com/betagouv/fondation/issues/583).
- **Suivi métier et évaluations** : 
    - Ajout de la possibilité de lister les magistrats dont l'évaluation est manquante [#572](https://github.com/betagouv/fondation/issues/572) et intégration d'un indicateur spécifique sur les dossiers de nomination [#551](https://github.com/betagouv/fondation/issues/551).
    - Correction de l'affectation des fiches de juridiction, désormais rattachées au magistrat plutôt qu'à la session [#591](https://github.com/betagouv/fondation/issues/591).
- **Expérience utilisateur et accessibilité** : 
    - Refonte des composants modaux et des notifications (passage aux "toasts") pour une meilleure accessibilité [#579](https://github.com/betagouv/fondation/issues/579) [#582](https://github.com/betagouv/fondation/issues/582).
    - Améliorations diverses suite aux revues UX (écrans de transparence, typographie, positionnement des validations) [#592](https://github.com/betagouv/fondation/issues/592) [#600](https://github.com/betagouv/fondation/issues/600) [#590](https://github.com/betagouv/fondation/issues/590) [#589](https://github.com/betagouv/fondation/issues/589).
    - Optimisation de l'accessibilité pour les lecteurs d'écran (étiquetage de l'éditeur de texte riche) [#587](https://github.com/betagouv/fondation/issues/587).

### Évolutions techniques
- **Fiabilité de l'ingestion de données (Lolfi)** : 
    - Renforcement de la surveillance de l'ingestion avec de nouvelles alertes en cas d'arrêt ou d'échec de l'import [#609](https://github.com/betagouv/fondation/issues/609) [#608](https://github.com/betagouv/fondation/issues/608).
    - Amélioration de la détection des scripts de relais divergents [#612](https://github.com/betagouv/fondation/issues/612) et résolution des blocages de jobs d'ingestion [#604](https://github.com/betagouv/fondation/issues/604).
    - Découplage de la synchronisation des sessions Lolfi du cycle de traitement des fichiers pour plus de robustesse [#611](https://github.com/betagouv/fondation/issues/611).
- **Infrastructure et CI/CD** : 
    - Optimisation du déploiement des assets documentaires sur Scalingo [#593](https://github.com/betagouv/fondation/issues/593).
    - Synchronisation automatique des clients OpenAPI [#585](https://github.com/betagouv/fondation/issues/585).
    - Amélioration de la gestion des échecs de génération de documents via Gotenberg [#573](https://github.com/betagouv/fondation/issues/573).

### Autres changements
- **Documentation** : Mise à jour du README et unification des commandes de configuration du projet [#571](https://github.com/betagouv/fondation/issues/571).
- **Développement** : Amélioration de l'environnement de test et de Storybook [#569](https://github.com/betagouv/fondation/issues/569) [#557](https://github.com/betagouv/fondation/issues/557).
