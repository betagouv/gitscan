## Changelog : Muffin (30 derniers jours, au 23 octobre 2026)

### Résumé
Ce mois a marqué une évolution majeure de Muffin, passant d'un outil de consultation à une plateforme de gestion documentaire active. Les nouveautés se concentrent sur la capacité de l'IA à proposer des modifications de documents ("documents vivants"), une refonte complète du moteur de recherche pour plus de précision, et une interface utilisateur considérablement simplifiée grâce à des assistants de configuration guidés.

### Évolutions fonctionnelles
- **Gestion des documents et édition :**
    - Introduction des "documents vivants" permettant de gérer des révisions, des verrous d'édition et des propositions de modifications par l'IA.
    - Amélioration de l'importation : gestion des fichiers ZIP volumineux par lots et extraction progressive des PDF longs avec suivi de la progression.
    - Détection automatique des doublons lors de l'ajout de fichiers ou d'URL.
- **Expérience de Chat et Agent :**
    - L'assistant peut désormais poser des questions interactives (choix multiples ou texte libre) pour affiner les recherches [#344](https://github.com/IA-Generative/Muffin/issues/344).
    - Suggestion de questions de démarrage basées sur les paires question-réponse stockées.
    - L'agent peut désormais aider l'utilisateur sur l'utilisation de l'application via un guide utilisateur intégré.
- **Organisation et Collections :**
    - Mise en place d'une hiérarchie de sous-collections avec héritage automatique des droits d'accès.
    - Possibilité d'effectuer des recherches transversales sur l'ensemble d'une arborescence de collections.
- **Interface Utilisateur (Frontend) :**
    - Nouveau système de configuration guidé (wizard) pour paramétrer les collections plus facilement.
    - Amélioration de la visualisation des sources : encadrement précis des passages cités dans les documents et les captures d'écran.
- **Administration :**
    - Mise en place d'un suivi de la consommation des appels LLM pour les administrateurs.

### Évolutions techniques
- **Moteur de recherche :** Remplacement de Meilisearch par une recherche hybride via **Qdrant** (combinant recherche dense et BM25) pour une meilleure pertinence des résultats [#355](https://github.com/IA-Generative/Muffin/issues/355).
- **Optimisation de l'indexation :**
    - Nouvelle stratégie de découpage (chunking) par LLM par défaut.
    - Optimisation du traitement des documents longs par échantillonnage intelligent des pages, réduisant ainsi les coûts et le temps de traitement [#373](https://github.com/IA-Generative/Muffin/issues/373).
    - Estimation en temps réel du coût en appels LLM lors de la configuration des collections [#375](https://github.com/IA-Generative/Muffin/issues/375).
- **Architecture et Pipeline :**
    - Refactorisation du worker pour séparer les étapes d'extraction, d'enrichissement et d'importation.
    - Implémentation de logs de tâches structurés permettant un suivi en direct de l'avancement des processus.
- **Infrastructure :**
    - Mise à jour des charts Helm et ajustement des ressources pour les pods Qdrant.

### Autres changements
- **Documentation :** Mise à jour complète de la documentation concernant la recherche Qdrant, les procédures de sauvegarde et les paramètres de configuration des collections.
- **Design :** Modernisation de la page d'accueil et ajout d'animations pour illustrer le fonctionnement de la plateforme.
