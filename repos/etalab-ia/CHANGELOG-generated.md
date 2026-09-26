# Synthèse d'activité : etalab-ia (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité de l'organisation a été marquée par une montée en puissance significative des capacités d'agents et des systèmes de RAG (Retrieval-Augmented Generation). Les projets [letta](/repos/etalab-ia/letta) et [letta-code](/repos/etalab-ia/letta-code) ont considérablement enrichi leurs fonctionnalités (planification, mémoire, sous-agents) et leur support de modèles, tandis que l'écosystème d'évaluation s'est consolidé avec le lancement de [eval-ocr-htr](/repos/etalab-ia/eval-ocr-htr) et l'amélioration de l'exportation des résultats vers Hugging Face pour [evalap](/repos/etalab-ia/evalap) et [eval-transcript](/repos/etalab-ia/eval-transcript).

Parallèlement, l'automatisation des flux de données s'est intensifiée, notamment via le pipeline reliant [mediatech](/repos/etalab-ia/mediatech) à l'API Albert grâce à [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api), facilitant ainsi l'accès à des données légales de haute qualité pour les applications d'IA.

## Sécurité
- Renforcement de la protection des données par l'intégration de contrôles automatiques contre les fuites de secrets (via Gitleaks) dans [just-code](/repos/etalab-ia/just-code) et [eval-transcript](/repos/etalab-ia/eval-transcript).
- Mise en place de mécanismes de vérification d'attestation pour garantir l'intégrité des composants dans [just-code](/repos/etalab-ia/just-code).
- Amélioration de la gestion de la sécurité des clés API et de l'authentification dans [ragtime](/repos/etalab-ia/ragtime) et [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).

## Autres changements notables
- **Refonte logicielle majeure** : [just-code](/repos/etalab-ia/just-code) a migré vers un développement intégral en Go, offrant un binaire unique, un support Windows et des environnements d'exécution plus modernes (Lima, macOS).
- **Évolution architecturale** : [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) adopte une "Clean Architecture" et intègre Langfuse pour une meilleure observabilité, tandis que [ragtime](/repos/etalab-ia/ragtime) (anciennement [rag-facile](/repos/etalab-ia/rag-facile)) a bénéficié d'une refonte pour une meilleure modularité et l'ajout de l'authentification via Supabase.
- **Industrialisation des données** : Migration de la base de données vers une architecture serverless pour [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) et automatisation des mises à jour quotidiennes des dictionnaires dans [albert-data-collections](/repos/etalab-ia/albert-data-collections).
- **Optimisation de l'infrastructure** : Amélioration des performances de déploiement pour [whisperx-openai-api](/repos/etalab-ia/whisperx-openai-api) (support GPU H200) et [marker-serve](/repos/etalab-ia/marker-serve) (optimisation Docker).

## Dépôts les plus actifs
- [letta](/repos/etalab-ia/letta) : Évolutions majeures sur la gestion des conversations, les capacités d'agents et l'optimisation des prompts.
- [lettabot](/repos/etalab-ia/lettabot) : Extension de l'intégration multi-plateformes (Slack, Discord, Telegram) et refonte du système de configuration.
- [just-code](/repos/etalab-ia/just-code) : Transition vers le langage Go et élargissement de la compatibilité système (Windows, macOS).
- [ragtime](/repos/etalab-ia/ragtime) : Refonte complète de l'architecture, ajout d'une interface CLI et intégration de Supabase.
- [eval-transcript](/repos/etalab-ia/eval-transcript) : Ajout de nouveaux fournisseurs de transcription et implémentation d'un moteur de scoring par LLM.
