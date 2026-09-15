## Changelog : fondation (30 derniers jours, au 14/09/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur la fiabilité du système d'ingestion de données (Lolfi) et l'amélioration de l'accessibilité de l'interface. Les outils de gestion des agendas et des documents ont été simplifiés pour offrir une expérience de sélection plus fluide, tandis que de nouveaux mécanismes d'alerte garantissent une meilleure réactivité en cas d'anomalie technique.

### Évolutions fonctionnelles
- **Gestion des agendas et documents** : 
    - Amélioration de la sélection de fichiers (actions groupées, sélection globale et sélection via tableau) [#642](https://github.com/betagouv/fondation/issues/642), [#626](https://github.com/betagouv/fondation/issues/626), [#580](https://github.com/betagouv/fondation/issues/580).
    - Automatisation de l'invalidation des rapports officiels lors de modifications de dates, de fichiers ou de résultats [#633](https://github.com/betagouv/fondation/issues/633), [#627](https://github.com/betagouv/fondation/issues/627), [#603](https://github.com/betagouv/fondation/issues/603), [#601](https://github.com/betagouv/fondation/issues/601).
    - Amélioration de la génération de documents (intégration des polices et en-têtes) [#588](https://github.com/betagouv/fondation/issues/588) et correction du téléchargement des pièces jointes [#583](https://github.com/betagouv/fondation/issues/583).
- **Fiabilité et alertes** : 
    - Mise en place de notifications pour les échecs, les interruptions ou les anomalies lors de l'ingestion Lolfi [#623](https://github.com/betagouv/fondation/issues/623), [#620](https://github.com/betagouv/fondation/issues/620), [#609](https://github.com/betagouv/fondation/issues/609), [#608](https://github.com/betagouv/fondation/issues/608), [#607](https://github.com/betagouv/fondation/issues/607), [#604](https://github.com/betagouv/fondation/issues/604).
- **Expérience utilisateur et Accessibilité** : 
    - Refonte de l'affichage des alertes via des composants "toasts" accessibles [#582](https://github.com/betagouv/fondation/issues/582).
    - Amélioration de l'accessibilité globale (modales partagées, étiquetage des éditeurs de texte pour les lecteurs d'écran, page de déclaration d'accessibilité) [#579](https://github.com/betagouv/fondation/issues/579), [#587](https://github.com/betagouv/fondation/issues/587), [#630](https://github.com/betagouv/fondation/issues/630).
    - Corrections ergonomiques sur la typographie, le placement des éléments et les écrans de transparence [#590](https://github.com/betagouv/fondation/issues/590), [#589](https://github.com/betagouv/fondation/issues/589), [#592](https://github.com/betagouv/fondation/issues/592), [#600](https://github.com/betagouv/fondation/issues/600).
- **Nouvelles fonctionnalités** : 
    - Activation de la fonctionnalité "Je donne mon avis" [#644](https://github.com/betagouv/fondation/issues/644).
    - Ajout d'une vue pour lister les magistrats n'ayant pas encore d'évaluation [#572](https://github.com/betagouv/fondation/issues/572).

### Évolutions techniques
- **Architecture et API** : 
    - Synchronisation régulière des clients OpenAPI [#645](https://github.com/betagouv/fondation/issues/645), [#634](https://github.com/betagouv/fondation/issues/634).
    - Refactorisation de la synchronisation des sessions Lolfi pour plus de robustesse [#611](https://github.com/betagouv/fondation/issues/611).
- **Qualité et Observabilité** : 
    - Intégration de la mesure de couverture pour les suites de tests unitaires et E2E [#628](https://github.com/betagouv/fondation/issues/628).
    - Ajout du suivi analytique via Matomo [#635](https://github.com/betagouv/fondation/issues/635).
- **Infrastructure** : 
    - Optimisation du déploiement des assets documentaires sur Scalingo [#593](https://github.com/betagouv/fondation/issues/593).

### Autres changements
- **Documentation** : Mise à jour et unification des commandes de configuration dans le README [#571](https://github.com/betagouv/fondation/issues/571).
