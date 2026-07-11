# Synthèse d'activité : etalab-ia (du 16 mai 2026 au 1er juillet 2026)

## Résumé de l'activité
L'organisation etalab-ia a connu une période d'activité soutenue, marquée par des avancées significatives sur plusieurs fronts. Le développement de l'API [whisperx-openai-api](/repos/etalab-ia/whisperx-openai-api) a permis de créer une solution performante pour la transcription audio, compatible avec l'API OpenAI.  Des efforts importants ont été consacrés à l'amélioration de la plateforme RAG (Retrieval-Augmented Generation) avec des mises à jour notables sur [ragtime](/repos/etalab-ia/ragtime) et [rag-facile](/repos/etalab-ia/rag-facile), incluant l'ajout de fonctionnalités d'authentification, d'évaluation de la qualité des réponses et d'intégration de l'IA Inspect.  Enfin, les projets [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) et [OpenGateRAG](/repos/etalab-ia/OpenGateRAG) ont progressé en termes de stabilité, de sécurité et d'intégration.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction de vulnérabilités dans [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) (CVE-2026-11940 et CVE-2026-55200).
- Ajout d'un hook pre-commit gitleaks dans [eval-transcript](/repos/etalab-ia/eval-transcript) pour prévenir les fuites de secrets.

## Autres changements notables
- Changement de nom du projet [rag-facile](/repos/etalab-ia/rag-facile) vers [ragtime](/repos/etalab-ia/ragtime).
- Migration de la base de données [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) vers une architecture serverless pour une meilleure scalabilité.
- Refonte de l'architecture interne de [rag-facile](/repos/etalab-ia/rag-facile) pour une meilleure modularité.
- Unification de la documentation OpenAPI de [OpenGateRAG](/repos/etalab-ia/OpenGateRAG) avec [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).

## Dépôts les plus actifs
- [whisperx-openai-api](/repos/etalab-ia/whisperx-openai-api) : Développement initial d'une API de transcription audio compatible avec OpenAI.
- [rag-facile](/repos/etalab-ia/rag-facile) : Amélioration significative de la plateforme RAG avec ajout d'authentification, d'évaluation de la qualité et d'intégration d'IA.
- [ragtime](/repos/etalab-ia/ragtime) : Refonte et ajout d'une interface en ligne de commande pour la gestion des collections.
- [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) : Amélioration de la sécurité, de l'authentification et de l'API.
- [mediatech](/repos/etalab-ia/mediatech) : Intégration de nouveaux jeux de données et optimisation du traitement des données.
- [eval-transcript](/repos/etalab-ia/eval-transcript) : Ajout de nouveaux fournisseurs de transcription et d'un moteur de scoring pour l'évaluation de la qualité.
