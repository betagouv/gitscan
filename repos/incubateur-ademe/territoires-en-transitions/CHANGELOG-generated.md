## Changelog : territoires-en-transitions (30 derniers jours, au 07/10/2026)

### Résumé
Ce mois a été marqué par une avancée majeure dans l'automatisation des processus grâce à l'intégration de l'intelligence artificielle pour l'importation de plans d'action. La plateforme a également franchi une étape clé avec le déploiement des fonctionnalités liées à la démarche PCAET (pilotage et dépôt) et l'amélioration des outils d'aide à la décision (priorisation des leviers) pour les collectivités.

### Évolutions fonctionnelles
- **Démarche PCAET** : 
    - Mise en place d'un parcours complet de dépôt et d'instruction, incluant une nouvelle interface de pilotage et de suivi des étapes.
    - Ajout d'une page de démonstration interactive et d'une FAQ dédiée pour accompagner les utilisateurs.
    - Amélioration des notifications par email tout au long du cycle de vie du dossier.
- **Importation assistée par IA** : 
    - Capacité d'importer et de structurer automatiquement des plans d'action à partir de documents PDF ou Word via l'IA.
    - Extraction automatique de données clés : partenaires, financements, moyens humains, priorités et dates.
    - Introduction d'une étape de vérification humaine obligatoire pour valider les données extraites avant leur intégration.
- **Priorisation et Leviers** : 
    - Nouveaux outils de visualisation pour l'aide à la décision : matrice impact × mobilisation, treemap cliquable et histogrammes par catégorie.
    - Possibilité pour les collectivités de qualifier la pertinence de leurs leviers et de leurs catégories d'action.
- **Gestion des indicateurs et référentiels** : 
    - Transition vers le nouveau référentiel (CR) avec gestion des archives et des droits d'affichage.
    - Amélioration du calcul des scores indicatifs et gestion de la périodicité des indicateurs.
- **Gestion documentaire** : 
    - Amélioration du dépôt de preuves et des documents d'audit, avec support du téléchargement groupé (format ZIP).
    - Meilleure gestion de la confidentialité des fichiers.

### Évolutions techniques
- **Architecture et API** : 
    - Migration progressive de l'accès aux données de PostgREST vers tRPC pour une meilleure cohérence et fiabilité.
    - Refonte de la gestion des documents utilisant des jetons signés et le transport résumable pour plus de robustesse.
- **Intelligence Artificielle (LLM)** : 
    - Intégration de Vertex AI (Gemini) comme moteur principal, avec gestion fine des quotas par collectivité et optimisation du traitement des documents longs (chunking).
    - Mise en place d'un système de suivi et d'évaluation des performances de l'IA.
- **Infrastructure et Backend** : 
    - Migration vers Strapi 5.
    - Nettoyage de la stack technique : suppression de l'application "panier" et de ses dépendances obsolètes.
    - Optimisation des pipelines CI/CD pour accélérer les builds et améliorer la gestion du cache.

### Autres changements
- **Interface Utilisateur (UI)** : 
    - Création de nouveaux composants partagés (BetaLabel, ButtonGroup, Accordion) pour harmoniser le design.
    - Amélioration de l'accessibilité (navigation au clavier) et de la réactivité des composants.
- **Documentation** : 
    - Mise à jour importante des ADR (Architecture Decision Records) concernant le cycle de vie des données et la périodicité des indicateurs.
- **Nettoyage** : 
    - Suppression de code mort et de fonctionnalités non utilisées.
