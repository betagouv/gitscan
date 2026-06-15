## Changelog : mcr (30 derniers jours, au 12 juin 2026)

### Résumé
Cette période a été marquée par des améliorations significatives de la robustesse et de la flexibilité de l'application MCR. Des corrections de bugs ont été apportées pour gérer les erreurs de transcription et les problèmes d'état des livrables. De nouvelles fonctionnalités ont été implémentées pour améliorer la gestion des notes, l'intégration avec des outils externes comme Google Drive et l'ajout de capacités de débogage. L'architecture interne a été refactorisée pour une meilleure maintenabilité et extensibilité.

### Évolutions fonctionnelles
- Ajout d'un bouton de téléchargement audio pour les utilisateurs [#757](https://github.com/IA-Generative/mcr/issues/757).
- Possibilité de relancer la génération de livrables en cas d'échec [#720](https://github.com/IA-Generative/mcr/issues/720).
- Ajout de la possibilité d'utiliser des notes personnalisées dans les sections du rapport [#727](https://github.com/IA-Generative/mcr/issues/727).
- Amélioration de la gestion des participants et des notes dans les transcriptions, notamment pour éviter la perte d'informations entre les segments audio [#746](https://github.com/IA-Generative/mcr/issues/746), [#697](https://github.com/IA-Generative/mcr/issues/697).
- Ajout d'une page de maintenance pour signaler les interruptions de service [#799](https://github.com/IA-Generative/mcr/issues/799).
- Intégration avec Google Drive pour visualiser les transcriptions et les rapports [#687](https://github.com/IA-Generative/mcr/issues/687), [#437](https://github.com/IA-Generative/mcr/issues/437).
- Ajout d'un outil de débogage pour faciliter le diagnostic des problèmes [#792](https://github.com/IA-Generative/mcr/issues/792).
- Amélioration des suggestions de prompts personnalisés [#710](https://github.com/IA-Generative/mcr/issues/710).

### Évolutions techniques
- Refactorisation de l'architecture pour séparer les couches de domaine, d'infrastructure et de présentation, améliorant la modularité et la testabilité [#810](https://github.com/IA-Generative/mcr/issues/810).
- Migration vers une architecture basée sur des cas d'utilisation (use cases) pour une meilleure organisation du code [#820](https://github.com/IA-Generative/mcr/issues/820), [#770](https://github.com/IA-Generative/mcr/issues/770).
- Ajout d'un linter pour faire respecter les règles d'architecture et de style de code [#814](https://github.com/IA-Generative/mcr/issues/814).
- Amélioration de la gestion des erreurs et des exceptions, notamment pour les tâches Celery et les appels API.
- Mise à jour des dépendances et correction de problèmes liés à la configuration de l'environnement local [#834](https://github.com/IA-Generative/mcr/issues/834).
- Suppression de code obsolète et de fonctionnalités non utilisées [#773](https://github.com/IA-Generative/mcr/issues/773), [#689](https://github.com/IA-Generative/mcr/issues/689).
- Amélioration de la journalisation (logging) pour faciliter le débogage et la surveillance.
- Ajout de tests unitaires et d'intégration pour garantir la qualité du code.

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les modifications de l'architecture [#760](https://github.com/IA-Generative/mcr/issues/760).
- Mise à jour de la configuration Slack pour inclure les nouveaux membres de l'équipe [#834](https://github.com/IA-Generative/mcr/issues/834).
- Correction de fautes de frappe et amélioration de la lisibilité du code [#785](https://github.com/IA-Generative/mcr/issues/785).
- Suppression de la limite de longueur des commentaires de feedback [#835](https://github.com/IA-Generative/mcr/issues/835).
