## Changelog : eval-transcript (30 derniers jours, au 30 mai 2026)

### Résumé
Ce mois-ci, le projet eval-transcript a connu une expansion significative de ses capacités de transcription. De nouveaux fournisseurs de services de transcription ont été intégrés (Albert, Scaleway Voxtral, Hugging Face Parakeet, oMLX) et des améliorations ont été apportées à la gestion des fichiers, à la configuration et à la robustesse du système. L'ajout d'un système de manifest permet une synchronisation plus efficace des benchmarks.

### Évolutions fonctionnelles
- Ajout du support pour le service de transcription Albert via une API. [#5](https://github.com/etalab-ia/eval-transcript/pull/5)
- Intégration du fournisseur Scaleway Voxtral pour la transcription audio. [#6](https://github.com/etalab-ia/eval-transcript/pull/6)
- Ajout d'un adaptateur pour le service de transcription oMLX, avec gestion des erreurs améliorée et option de sortie texte par défaut. [#1](https://github.com/etalab-ia/eval-transcript/pull/1) et [#7](https://github.com/etalab-ia/eval-transcript/pull/7)
- Intégration du service Hugging Face Parakeet avec une gestion plus robuste des sorties. [#8](https://github.com/etalab-ia/eval-transcript/pull/8)
- Possibilité de sauvegarder les transcriptions au format oMLX. [#2](https://github.com/etalab-ia/eval-transcript/pull/2)
- Implémentation d'un système de manifest pour synchroniser les benchmarks. [#3](https://github.com/etalab-ia/eval-transcript/pull/3)

### Évolutions techniques
- Refactoring du code pour extraire des fonctions d'aide pour la gestion des sorties de transcription, améliorant la lisibilité et la maintenabilité. [#7](https://github.com/etalab-ia/eval-transcript/pull/7)
- Utilisation de `python-dotenv` pour la gestion de la configuration locale, facilitant le développement et les tests. [#5](https://github.com/etalab-ia/eval-transcript/pull/5)
- Amélioration de la robustesse de la découverte des fichiers manifest. [#3](https://github.com/etalab-ia/eval-transcript/pull/3)
- Renforcement de la gestion des réponses API des services Albert et Hugging Face. [#5](https://github.com/etalab-ia/eval-transcript/pull/5) et [#8](https://github.com/etalab-ia/eval-transcript/pull/8)

### Autres changements
- Ajout d'une licence MIT au projet. [#9](https://github.com/etalab-ia/eval-transcript/pull/9)
- Documentation ajoutée pour l'exemple de configuration de l'environnement. [#6](https://github.com/etalab-ia/eval-transcript/pull/6)
- Initialisation de l'espace de travail du benchmark de transcription uv. [#20](https://github.com/etalab-ia/eval-transcript/commit/fa6ac950b589f9468854426892394a9639a87696)
- Simplification de l'affichage des sorties de transcription. [#7](https://github.com/etalab-ia/eval-transcript/pull/7)
