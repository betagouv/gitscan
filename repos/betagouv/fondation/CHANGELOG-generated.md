## Changelog : fondation (30 derniers jours, au 18 septembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur la fiabilité du suivi des données (LOLFI) grâce à un nouveau système d'alertes, l'optimisation de la gestion des documents et des agendas, ainsi qu'un effort significatif sur l'accessibilité et l'ergonomie de l'interface utilisateur.

### Évolutions fonctionnelles
- **Gestion des documents et agendas** : 
    - Amélioration de la sélection de fichiers (actions groupées, sélection totale et via tableau) [#626, #580, #642].
    - Automatisation de l'invalidation des rapports officiels lors de modifications (dates, fichiers ou résultats) [#601, #603, #627, #633].
    - Amélioration de la génération documentaire avec l'intégration automatique des polices et des en-têtes [#588].
    - Correction du téléchargement des pièces jointes [#583].
- **Fiabilité et alertes** : Mise en place d'un système d'alertes renforcé pour le suivi des processus LOLFI (échecs d'importation, arrêts d'ingestion, données incomplètes ou scripts divergents) [#604, #607, #608, #609, #612, #620, #623].
- **Accessibilité et interface** : 
    - Amélioration de l'accessibilité via l'utilisation de notifications ("toasts") et de fenêtres modales conformes [#579, #582].
    - Optimisation de la navigation entre les rapports des membres [#647] et de l'affichage des sessions (barre de session fixe et header rework) [#650, #651].
    - Amélioration de l'accessibilité du riche texte pour les lecteurs d'écran [#587].
- **Nouvelle fonctionnalité** : Activation de la fonctionnalité "Je donne mon avis" [#644].

### Évolutions techniques
- **Architecture et Refactoring** : 
    - Découplage de la synchronisation des sessions LOLFI pour améliorer la robustesse [#611].
    - Restructuration des énumérations (un fichier par concept) pour une meilleure maintenance [#648].
- **Qualité et Observabilité** : 
    - Ajout de la mesure de couverture pour les suites de tests unitaires et E2E [#628].
    - Intégration de Matomo pour le suivi analytique [#635].
    - Automatisation de la synchronisation des clients OpenAPI [#645, #634, #585].
- **Infrastructure** : Déploiement des ressources (assets) documentaires sur Scalingo [#593].

### Autres changements
- **Gestion des dépendances** : Fixation de la version de la bibliothèque Zod pour assurer la compatibilité avec NestJS [#646].
