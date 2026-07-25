# Synthèse d'activité : etalab-ia (du 16 mai 2026 au 23 juillet 2026)

## Résumé de l'activité
L'organisation etalab-ia a connu une période d'activité soutenue, marquée par des avancées significatives sur plusieurs projets. Les efforts se sont concentrés sur l'amélioration de l'infrastructure et des outils pour le traitement du langage naturel, notamment avec le développement de l'API [whisperx-openai-api](/repos/etalab-ia/whisperx-openai-api) pour la transcription audio, et l'évolution de la plateforme [rag-facile](/repos/etalab-ia/rag-facile) et [ragtime](/repos/etalab-ia/ragtime) pour la création d'applications RAG.  L'accent a également été mis sur l'amélioration de la qualité des données et leur accessibilité via [mediatech](/repos/etalab-ia/mediatech) et [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api). Plusieurs projets ont bénéficié d'améliorations de la sécurité, de la documentation et de l'expérience utilisateur.

## Sécurité
Plusieurs projets ont bénéficié d'améliorations de la sécurité :
- Correction de vulnérabilités dans [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) avec l'ignorance de certaines CVE et des refactorings des endpoints d'authentification.
- Ajout d'une vérification de vulnérabilités des dépendances en pré-push dans [parcours-rag](/repos/etalab-ia/parcours-rag).
- Ajout d'un hook pre-commit gitleaks pour renforcer la sécurité dans [OpenMockLLM](/repos/etalab-ia/OpenMockLLM).

## Autres changements notables
- Changement de nom du projet [rag-facile](/repos/etalab-ia/rag-facile) en [ragtime](/repos/etalab-ia/ragtime).
- Migration de la base de données de [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) vers une architecture serverless.
- Refonte de l'architecture interne de [rag-facile](/repos/etalab-ia/rag-facile) pour une meilleure modularité.
- Suppression de la fonctionnalité RAG dans [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
- Unification de la documentation OpenAPI de [OpenGateRAG](/repos/etalab-ia/OpenGateRAG) avec [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).

## Dépôts les plus actifs
- [rag-facile](/repos/etalab-ia/rag-facile) : Amélioration significative de la plateforme avec l'ajout d'authentification, d'intégration d'IA Inspect et d'un système de compétences.
- [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) : Refactoring majeur de l'architecture, corrections de bugs et améliorations de la sécurité.
- [mediatech](/repos/etalab-ia/mediatech) : Intégration de nouveaux jeux de données et optimisation du traitement des données.
- [ragtime](/repos/etalab-ia/ragtime) : Ajout d'une interface en ligne de commande pour la gestion des collections de documents et amélioration de la configuration initiale.
- [lettabot](/repos/etalab-ia/lettabot) : Amélioration de l'expérience utilisateur avec un assistant de configuration interactif et l'ajout de la prise en charge de Discord.
- [eval-transcript](/repos/etalab-ia/eval-transcript) : Ajout de nouveaux fournisseurs de transcription et développement d'un moteur de scoring pour évaluer la qualité des transcriptions.
