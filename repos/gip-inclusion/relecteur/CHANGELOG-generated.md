## Changelog : relecteur (30 derniers jours, au 20/10/2026)

### Résumé
Ce mois-ci, le projet a franchi une étape importante avec l'intégration de la revue de code directement dans les pipelines CI (via GitHub Actions), permettant des résumés automatiques en français. L'outil est devenu beaucoup plus robuste face aux contraintes des modèles d'IA (gestion des limites de débit et des interruptions) et offre désormais des capacités avancées pour générer automatiquement des cas de test à partir de l'historique du projet.

### Évolutions fonctionnelles
- **Intégration CI/CD** : Possibilité d'exécuter des revues de Pull Requests directement dans la CI via une GitHub Action, avec génération de résumés en français.
- **Configuration enrichie** : 
    - Sélection précise des fichiers à réviser via le fichier `.relecteur/config.toml`.
    - Choix du modèle d'IA et du "juge" directement dans la configuration du dépôt (support de l'API Anthropic).
    - Utilisation des clés d'API et des paramètres spécifiques au dépôt évalué (via `.env`).
- **Reporting amélioré** : Ajout de métriques de performance détaillées, incluant le temps moyen et le nombre de tokens consommés par revue.
- **Génération de cas d'évaluation** : 
    - Capacité de créer automatiquement des cas de test à partir de l'historique du dépôt ou des commentaires de revue existants.
    - Possibilité de lier les corrections suggérées aux cas de test créés.

### Évolutions techniques
- **Résilience accrue** : 
    - Amélioration de la gestion des limites de débit (rate limits) et des timeouts : le système peut désormais reprendre une revue là où elle s'était arrêtée après une pause automatique.
    - Meilleure gestion des erreurs de service (classification des erreurs 503 comme erreurs de fournisseur).
- **Optimisation du moteur d'évaluation** :
    - Introduction d'un "DefectFinder" et utilisation de probabilités pour améliorer la précision du jugement des défauts.
    - Amélioration du traitement des grandes Pull Requests en les segmentant par groupes de fichiers.
    - Refonte du système de scoring pour une meilleure gestion des cas de "silence" (quand l'IA ne détecte rien).
- **Refactoring** : Nettoyage des interfaces publiques, renommage des classes de statut pour plus de clarté et renforcement de l'immutabilité des constantes du moteur.

### Autres changements
- **Documentation** : Mise à jour des guides concernant la gestion des grandes Pull Requests et les prérequis de version Git.
- **Tests et Qualité** : Amélioration de la fiabilité des tests en remplaçant les sorties simulées par des enregistrements de runs réels.
- **Maintenance** : Arrêt du suivi des artefacts de build.
