## Changelog : Muffin (30 derniers jours, au 28 octobre 2026)

### Résumé
Ce mois a été marqué par une montée en puissance majeure de l'intelligence de traitement documentaire. Muffin améliore considérablement sa capacité à comprendre les documents complexes (tableaux, mises en page scannées, documents très longs) et rend l'interaction avec l'agent plus fluide et transparente. L'expérience utilisateur est enrichie par des outils de visualisation de données (graphiques) et un suivi précis de la consommation des ressources.

### Évolutions fonctionnelles
- **Agent conversationnel et UX** :
  - Amélioration de la précision des citations avec vérification par ID et ancrage visuel dans les documents [#402](https://github.com/IA-Generative/Muffin/issues/402).
  - Support du streaming des réponses pour une lecture en temps réel pendant la génération.
  - Interaction améliorée : l'agent peut poser des questions de clarification à l'utilisateur ou proposer des questions de démarrage [#344](https://github.com/IA-Generative/Muffin/issues/344).
  - Capacité de l'agent à proposer des modifications de documents (format Markdown).
- **Analyse de données et Tableurs** :
  - Génération et affichage de graphiques directement dans les réponses de l'agent [#434](https://github.com/IA-Generative/Muffin/issues/434).
  - Ajout d'un onglet "Données" pour consulter les informations extraites des documents tabulaires [#431](https://github.com/IA-Generative/Muffin/issues/431).
  - Possibilité d'interroger les données tabulaires via des requêtes SQL avec correction d'erreur automatique [#433](https://github.com/IA-Generative/Muffin/issues/433).
- **Gestion documentaire et Collections** :
  - Introduction des "documents vivants" permettant de gérer des révisions et un historique de modifications.
  - Mise en place d'une hiérarchie de sous-collections pour une meilleure organisation.
  - Assistant de configuration guidé pour la création de collections avec estimation du coût des paramètres avant validation [#375](https://github.com/IA-Generative/Muffin/issues/375).
- **Monitoring et Usage** :
  - Nouvelle page de suivi affichant la consommation en temps réel (CPU, mémoire, temps) et l'impact énergétique des tâches.
  - Logs de tâches structurés et suivis en direct pour une meilleure visibilité sur les processus en cours.

### Évolutions techniques
- **Recherche et Indexation** :
  - Migration du moteur de recherche vers Qdrant pour supporter la recherche hybride (dense + BM25) [#355](https://github.com/IA-Generative/Muffin/issues/355).
  - Nouvelle stratégie de découpage (chunking) par LLM devenue la méthode par défaut.
  - Optimisation du traitement des documents longs par échantillonnage de pages et traitement par plages pour réduire les coûts et le temps de calcul [#373](https://github.com/IA-Generative/Muffin/issues/373).
- **OCR et Vision** :
  - Déploiement de nouveaux services (pods) spécialisés pour l'analyse de mise en page (layout) et la reconnaissance de tableaux complexes [#406](https://github.com/IA-Generative/Muffin/issues/406), [#410](https://github.com/IA-Generative/Muffin/issues/410).
  - Amélioration de la lecture des documents scannés via l'intégration de modèles PP-OCRv5 et PP-DocLayoutV3.
- **Architecture et Ingestion** :
  - Refonte du pipeline de traitement : séparation des tâches en microservices spécialisés (extraction, enrichissement, import).
  - Optimisation de l'ingestion des tableurs via un flux de fichiers Parquet par feuille et utilisation de DuckDB pour les requêtes [#431](https://github.com/IA-Generative/Muffin/issues/431).
  - Amélioration de l'importation de fichiers ZIP volumineux via un traitement par lots (batching) pour optimiser la mémoire.

### Autres changements
- Mise à jour de la documentation technique concernant Qdrant, la gestion des sous-collections et les paramètres de configuration.
