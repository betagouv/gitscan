## Changelog : mcr (30 derniers jours, au 01 Juillet 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la robustesse et de la performance du système, notamment au niveau de la transcription et de la gestion des tâches asynchrones. De nouvelles fonctionnalités ont été ajoutées, comme la possibilité de télécharger les fichiers audio et de générer des rapports directement vers Google Drive. L'architecture a également été revue pour adopter une approche plus orientée "use cases", améliorant ainsi la maintenabilité et l'évolutivité du code.

### Évolutions fonctionnelles
- Ajout de la possibilité de télécharger les fichiers audio pour l'utilisateur ([#757](https://github.com/IA-Generative/mcr/issues/757)).
- Intégration de la génération de rapports directement vers Google Drive ([#367](https://github.com/IA-Generative/mcr/issues/367)).
- Amélioration de la gestion des erreurs et des cas limites lors de la transcription, notamment pour les réunions supprimées ([#807](https://github.com/IA-Generative/mcr/issues/807)).
- Possibilité d'utiliser le modèle de langage GPTOSS pour la transcription ([#761](https://github.com/IA-Generative/mcr/issues/761)).
- Correction d'un problème de phase inversée dans le downmix stéréo, améliorant la qualité audio ([#862](https://github.com/IA-Generative/mcr/issues/862)).
- Amélioration de la gestion des URL de webinaires pour une meilleure compatibilité ([#863](https://github.com/IA-Generative/mcr/issues/863)).
- Ajout d'une page de maintenance pour informer les utilisateurs en cas de problèmes. ([#798](https://github.com/IA-Generative/mcr/issues/798))

### Évolutions techniques
- Refactorisation importante de l'architecture pour adopter une approche basée sur les "use cases", améliorant la modularité et la testabilité du code.
- Suppression de la machine à états (state machine) pour la gestion des réunions, simplifiant ainsi le code et réduisant sa complexité ([#861](https://github.com/IA-Generative/mcr/issues/861)).
- Migration vers une approche asynchrone pour la diarisation, améliorant la réactivité du système ([#898](https://github.com/IA-Generative/mcr/issues/898)).
- Amélioration de la gestion des timeouts pour les appels HTTP, augmentant la robustesse du système.
- Ajout de pre-commit hooks pour la linting, le formatage et la détection de secrets, améliorant la qualité du code et la sécurité ([#874](https://github.com/IA-Generative/mcr/issues/874)).
- Mise en place d'une meilleure observability avec Sentry, incluant des rapports d'erreurs plus détaillés et une gestion des erreurs améliorée ([#793](https://github.com/IA-Generative/mcr/issues/793)).
- Utilisation de `httpx` au lieu de `fastapi` pour les requêtes HTTP, améliorant potentiellement les performances et la flexibilité.
- Passage à une organisation de code basée sur Git Trunk, simplifiant le workflow de développement ([#796](https://github.com/IA-Generative/mcr/issues/796)).

### Autres changements
- Mise à jour de la documentation pour refléter les nouvelles fonctionnalités et les changements d'architecture ([#760](https://github.com/IA-Generative/mcr/issues/760)).
- Amélioration de la configuration et de la gestion des secrets via 1Password.
- Suppression de code mort et nettoyage général du code.
- Mise à jour des dépendances et des configurations pour améliorer la sécurité et la stabilité.
- Ajout d'une skill de débogage pour faciliter le diagnostic des problèmes en production. ([#839](https://github.com/IA-Generative/mcr/issues/839))
- Amélioration des tests unitaires et d'intégration pour garantir la qualité du code.
