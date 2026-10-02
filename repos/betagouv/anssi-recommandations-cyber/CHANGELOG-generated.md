## Changelog : anssi-recommandations-cyber (30 derniers jours, au 24/09/2026)

### Résumé
Ce mois-ci, les efforts se sont concentrés sur l'amélioration de la précision des réponses fournies par l'intelligence artificielle et sur la robustesse du système. L'application est désormais capable de mieux contextualiser les informations pour enrichir les paragraphes et dispose d'un système de surveillance renforcé pour détecter et identifier précisément les erreurs techniques lors des échanges avec le modèle d'IA.

### Évolutions fonctionnelles
- **Amélioration de l'enrichissement documentaire** : mise en place d'une stratégie de recherche par pages adjacentes et meilleure priorisation des preuves issues des guides pour des réponses plus pertinentes.
- **Optimisation du formatage** : stabilisation du rendu des listes Markdown dans les réponses générées par l'IA.

### Évolutions techniques
- **Observabilité et gestion des erreurs** : 
    - Implémentation d'un bus d'événements pour centraliser la gestion des erreurs.
    - Intégration de Sentry pour la remontée automatique des incidents.
    - Distinction précise des erreurs de communication selon l'étape du processus (reformulation, reclassement ou génération de texte).
- **Optimisation du traitement IA** : 
    - Amélioration de la gestion du contexte documentaire pour éviter le partage de segments de texte (chunks) entre les paragraphes enrichis.
    - Garantie d'un contexte documentaire unique par paragraphe.
- **Refactoring** : extraction de méthodes explicites pour les appels au LLM afin d'améliorer la maintenabilité du code.

### Autres changements
- **Documentation** : 
    - Création d'un nouveau dossier de documentation centralisé.
    - Ajout de schémas d'architecture détaillés (modèle C4 en PlantUML).
    - Documentation des conventions d'écriture des tests.
- **Sécurité** : résolution de plusieurs vulnérabilités via la mise à jour de dépendances critiques (pip, nanoid, idna).
- **Développement** : introduction de nouvelles conventions pour les agents de développement (skills TDD et Git).
