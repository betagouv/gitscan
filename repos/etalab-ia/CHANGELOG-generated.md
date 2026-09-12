# Synthèse d'activité : etalab-ia (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance de l'écosystème RAG (Retrieval-Augmented Generation) et des agents conversationnels. Les projets d'orchestration comme [ragtime](/repos/etalab-ia/ragtime) (issu de [rag-facile](/repos/etalab-ia/rag-facile)) et [letta](/repos/etalab-ia/letta) franchissent des étapes clés avec l'ajout de systèmes de compétences, une meilleure gestion de la mémoire et l'intégration de nouveaux modèles d'IA de pointe.

Parallèlement, l'organisation renforce ses capacités d'automatisation et d'évaluation. Les pipelines de données ([mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api)) et les outils de benchmark ([evalap](/repos/etalab-ia/evalap), [eval-transcript](/repos/etalab-ia/eval-transcript)) permettent désormais une intégration plus fluide et une diffusion automatisée des résultats vers des plateformes comme Hugging Face, offrant ainsi une meilleure visibilité sur la qualité des modèles déployés.

## Sécurité
- Amélioration des validations pour la fonctionnalité de sécurité du développement dans [skills](/repos/etalab-ia/skills).
- Sécurisation de la saisie des clés API dans [ragtime](/repos/etalab-ia/ragtime).
- Ajout d'un hook de sécurité Gitleaks pour la détection de secrets dans [eval-transcript](/repos/etalab-ia/eval-transcript).
- Mise en place de vérifications de vulnérabilités des dépendances en pré-push dans [parcours-rag](/repos/etalab-ia/parcours-rag).

## Autres changements notables
- **Architecture et Infrastructure :**
    - Migration vers une "Clean Architecture" pour isoler la logique métier dans [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
    - Refonte majeure de l'architecture de [rag-facile](/repos/etalab-ia/rag-facile) pour une meilleure modularité.
    - Migration de la base de données vers une architecture serverless pour [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api).
    - Unification de l'API et de la documentation entre [OpenGateRAG](/repos/etalab-ia/OpenGateRAG) et [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
- **Optimisations techniques :**
    - Support des GPU H200 pour [whisperx-openai-api](/repos/etalab-ia/whisperx-openai-api).
    - Optimisations de la gestion de la mémoire et de la concurrence dans [letta](/repos/etalab-ia/letta).
    - Optimisation de la construction des images Docker pour [marker-serve](/repos/etalab-ia/marker-serve).

## Dépôts les plus actifs
- [lettabot](/repos/etalab-ia/lettabot) : Extension massive des capacités d'intégration (Slack, Discord, Telegram) et refonte du système de configuration.
- [ragtime](/repos/etalab-ia/ragtime) : Transition majeure incluant une nouvelle interface CLI et une gestion de collections améliorée.
- [letta](/repos/etalab-ia/letta) : Évolution rapide du support des modèles (Anthropic, Gemini) et des capacités d'orchestration des agents.
- [evalap](/repos/etalab-ia/evalap) : Amélioration des capacités d'exportation et de visualisation des résultats d'évaluation vers Hugging Face.
- [mediatech](/repos/etalab-ia/mediatech) : Optimisation du traitement et de l'intégration de nouveaux jeux de données publics.
