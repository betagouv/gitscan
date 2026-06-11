## Changelog : eval-transcript (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, le projet eval-transcript a connu une évolution significative avec l'ajout de plusieurs nouveaux fournisseurs de transcription (Albert, Scaleway Voxtral, ElevenLabs, Kyutai, Cohere), ainsi que des améliorations importantes dans les capacités de scoring et de reporting des transcriptions. Des corrections et des refactorings ont également été effectués pour améliorer la robustesse et la maintenabilité du code.

### Évolutions fonctionnelles
- Ajout de la prise en charge du fournisseur de transcription Albert via API. [#5](https://github.com/etalab-ia/eval-transcript/pull/5)
- Ajout de la prise en charge du fournisseur de transcription Scaleway Voxtral. [#6](https://github.com/etalab-ia/eval-transcript/pull/6)
- Ajout de la prise en charge du fournisseur de transcription ElevenLabs, avec la possibilité de configurer un délai d'expiration. [#19](https://github.com/etalab-ia/eval-transcript/pull/19), [#24](https://github.com/etalab-ia/eval-transcript/pull/24)
- Remplacement du fournisseur Parakeet par Kyutai STT comme modèle de référence local. [#22](https://github.com/etalab-ia/eval-transcript/pull/22)
- Ajout de la prise en charge du fournisseur de transcription Cohere, incluant des tests de validation et de la documentation. [#21](https://github.com/etalab-ia/eval-transcript/pull/21)
- Implémentation de rapports de scoring, incluant des alignements et les erreurs les plus fréquentes. [#13](https://github.com/etalab-ia/eval-transcript/pull/13), [#14](https://github.com/etalab-ia/eval-transcript/pull/14), [#15](https://github.com/etalab-ia/eval-transcript/pull/15)
- Ajout de commandes CLI pour le scoring des transcriptions. [#11](https://github.com/etalab-ia/eval-transcript/pull/11)
- Possibilité de sauvegarder les transcriptions au format texte. [#2](https://github.com/etalab-ia/eval-transcript/pull/2)
- Ajout d'un mécanisme de synchronisation de manifestes pour les benchmarks. [#3](https://github.com/etalab-ia/eval-transcript/pull/3)
- Normalisation des nombres pour une meilleure évaluation. [#18](https://github.com/etalab-ia/eval-transcript/pull/18), [#20](https://github.com/etalab-ia/eval-transcript/pull/20)

### Évolutions techniques
- Refactoring de l'extraction des helpers de sortie de transcription pour une meilleure organisation du code. [#7](https://github.com/etalab-ia/eval-transcript/pull/7)
- Ajout d'un hook pre-commit gitleaks pour la détection de secrets. [#17](https://github.com/etalab-ia/eval-transcript/pull/17)
- Amélioration de la robustesse de la gestion des réponses API pour Hugging Face et Scaleway. [#8](https://github.com/etalab-ia/eval-transcript/pull/8), [#12](https://github.com/etalab-ia/eval-transcript/pull/12)
- Utilisation de `python-dotenv` pour la configuration locale. [#5](https://github.com/etalab-ia/eval-transcript/pull/5)
- Ajout d'une gestion du timeout pour les commandes `transcribe` en ligne de commande. [#18](https://github.com/etalab-ia/eval-transcript/pull/18)

### Autres changements
- Ajout d'une licence MIT au projet. [#9](https://github.com/etalab-ia/eval-transcript/pull/9)
- Mise à jour de la documentation pour inclure des exemples de configuration de l'environnement.
- Corrections mineures et améliorations de la robustesse du code.
