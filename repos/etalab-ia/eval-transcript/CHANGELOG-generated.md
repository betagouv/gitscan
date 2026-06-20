## Changelog : eval-transcript (30 derniers jours, au 2026-06-19)

### Résumé
Ce mois-ci, le projet eval-transcript a connu une évolution significative, axée sur l'amélioration des capacités d'évaluation et de benchmark des modèles de transcription audio. De nouveaux fournisseurs de transcription ont été intégrés (Scaleway Voxtral, Albert, ElevenLabs), ainsi que des outils pour l'évaluation de la qualité des transcriptions, notamment via l'utilisation de LLM (Large Language Models) pour juger de la gravité sémantique des erreurs. L'infrastructure CI/CD a également été renforcée et documentée.

### Évolutions fonctionnelles
- Ajout de la possibilité de pousser les transcriptions locales vers Hugging Face Hub via la nouvelle sous-commande `results push` [#43](https://github.com/etalab-ia/eval-transcript/pull/43).
- Intégration du fournisseur de transcription Scaleway Voxtral, incluant la suppression de la traduction inutile et l'alignement avec les fichiers source de vérité [#20](https://github.com/etalab-ia/eval-transcript/pull/20), [#3](https://github.com/etalab-ia/eval-transcript/pull/3).
- Ajout du fournisseur de transcription Albert [#5](https://github.com/etalab-ia/eval-transcript/pull/5).
- Intégration du fournisseur de transcription ElevenLabs, avec gestion des timeouts [#24](https://github.com/etalab-ia/eval-transcript/pull/24).
- Implémentation d'un moteur de scoring pour évaluer la qualité des transcriptions, incluant des rapports détaillés et l'alignement des erreurs [#10](https://github.com/etalab-ia/eval-transcript/pull/10), [#12](https://github.com/etalab-ia/eval-transcript/pull/12), [#13](https://github.com/etalab-ia/eval-transcript/pull/13), [#14](https://github.com/etalab-ia/eval-transcript/pull/14), [#15](https://github.com/etalab-ia/eval-transcript/pull/15).
- Utilisation de LLM (Large Language Models) pour évaluer la gravité sémantique des erreurs de transcription [#35](https://github.com/etalab-ia/eval-transcript/pull/35), [#37](https://github.com/etalab-ia/eval-transcript/pull/37), [#38](https://github.com/etalab-ia/eval-transcript/pull/38).
- Ajout de recettes de benchmark pour WhisperX et Kyutai (MLX) [#9](https://github.com/etalab-ia/eval-transcript/pull/9).
- Possibilité de sauvegarder les transcriptions obtenues [#2](https://github.com/etalab-ia/eval-transcript/pull/2).
- Ajout d'un adaptateur pour le modèle oMLX [#1](https://github.com/etalab-ia/eval-transcript/pull/1).

### Évolutions techniques
- Refactor de la logique de jugement pour améliorer la conception et la gestion des erreurs [#40](https://github.com/etalab-ia/eval-transcript/pull/40), [#41](https://github.com/etalab-ia/eval-transcript/pull/41).
- Amélioration de la robustesse de la gestion des erreurs et des réponses des APIs (Hugging Face, ElevenLabs) [#34](https://github.com/etalab-ia/eval-transcript/pull/34).
- Suppression de l'étape ffprobe et du check de durée pour Voxtral dans les workflows CI [#39](https://github.com/etalab-ia/eval-transcript/pull/39), [#40](https://github.com/etalab-ia/eval-transcript/pull/40).
- Documentation des workflows CI et de l'utilisation des datasets Hugging Face [#42](https://github.com/etalab-ia/eval-transcript/pull/42).
- Ajout d'un hook pre-commit gitleaks pour la sécurité [#17](https://github.com/etalab-ia/eval-transcript/pull/17).
- Utilisation de `python-dotenv` pour la configuration locale [#8](https://github.com/etalab-ia/eval-transcript/pull/8).

### Autres changements
- Mise à jour de la documentation pour clarifier les prérequis et l'utilisation de l'environnement [#17](https://github.com/etalab-ia/eval-transcript/pull/17).
- Renommage de "source truth" en "ground truth" pour une terminologie plus standard [#33](https://github.com/etalab-ia/eval-transcript/pull/33).
- Ajout d'une licence MIT au projet [#9](https://github.com/etalab-ia/eval-transcript/pull/9).
- Nettoyage et simplification du code, notamment dans la gestion des sorties de transcription [#7](https://github.com/etalab-ia/eval-transcript/pull/7).
