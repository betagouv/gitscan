## Changelog : conversations (30 derniers jours)

### Résumé
Ce mois-ci, l'équipe a apporté des améliorations significatives à l'expérience utilisateur, notamment en ajoutant un mode sombre persistant, en optimisant l'affichage du markdown en streaming et en permettant de désactiver la recherche internet automatique. Des corrections de bugs ont également été implémentées pour améliorer la stabilité et la compatibilité, en particulier concernant le rendu des fichiers PDF et le mode sombre. Des améliorations techniques ont été apportées pour la maintenance et la performance du code.

### Évolutions fonctionnelles
- Possibilité de désactiver la recherche internet automatique pour l'utilisateur. [#4545083](https://github.com/suitenumerique/conversations/commit/4545083)
- Ajout d'un mode sombre persistant, conservant le thème choisi par l'utilisateur. [#ff9e833](https://github.com/suitenumerique/conversations/commit/ff9e833)
- Amélioration de l'intégration de l'API Find avec le sous-utilisateur et le tag. [#3106d5f](https://github.com/suitenumerique/conversations/commit/3106d5f)
- Implémentation de FindRagBackend pour une meilleure gestion de la recherche. [#23fa1d6](https://github.com/suitenumerique/conversations/commit/23fa1d6)
- Correction du rendu des formules mathématiques et des carrousels dans différentes langues. [#09dceb5](https://github.com/suitenumerique/conversations/commit/09dceb5)
- Amélioration de l'interface utilisateur avec la mise à jour du kit UI et correction de la police Marianne. [#082937e](https://github.com/suitenumerique/conversations/commit/082937e)
- Correction de l'affichage des messages dans le mode sombre. [#2b81234](https://github.com/suitenumerique/conversations/commit/2b81234)
- Amélioration de l'expérience avec les fichiers PDF grâce à un parseur adaptatif (extraction de texte / OCR). [#3bbe7fb](https://github.com/suitenumerique/conversations/commit/3bbe7fb)

### Évolutions techniques
- Refactorisation du service AIAgentService pour une meilleure lisibilité et maintenabilité. [#ba712af](https://github.com/suitenumerique/conversations/commit/ba712af)
- Optimisation du rendu du markdown en streaming grâce à la division en blocs. [#af6facf](https://github.com/suitenumerique/conversations/commit/af6facf)
- Migration de ESLint vers la version 9 avec une configuration plate. [#9935335](https://github.com/suitenumerique/conversations/commit/9935335)
- Utilisation de `uv` au lieu de `pip` pour Crowdin. [#e925bff](https://github.com/suitenumerique/conversations/commit/e925bff)
- Correction de l'ordre de liveness et readiness pour le déploiement backend avec Helm. [#e60c938](https://github.com/suitenumerique/conversations/commit/e60c938)
- Refactorisation des parseurs de documents. [#1c573ad](https://github.com/suitenumerique/conversations/commit/1c573ad)
- Optimisation de la taille du bundle de surlignage de la syntaxe. [#23964cb](https://github.com/suitenumerique/conversations/commit/23964cb)

### Autres changements
- Correction du type MIME pour les fichiers PPTX. [#1088d88](https://github.com/suitenumerique/conversations/commit/1088d88)
- Ignorer la casse lors du retour à l'adresse e-mail dans OIDC. [#3c3eaf3](https://github.com/suitenumerique/conversations/commit/3c3eaf3)
- Mise à jour des dépendances : django-pydantic-field, pypdf, pillow, pydantic-ai, django. [#8feed1e, #61f86e1, #224e6f8, #54d2d3e]
- Mise à jour des chaînes traduites. [#a919d9a]
- Bump de la release à la version 0.0.13. [#9506df3]
- Correction du casting des IDs de collection vers les types attendus par l'API. [#c87c734]
- Monture du fichier de configuration JSON LLM dans les jobs Helm. [#fd372e1]
- Gestion de la suppression des collections temporaires. [#88bdcc2]
