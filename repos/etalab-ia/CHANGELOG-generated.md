# Synthèse d'activité : etalab-ia (du 20/05 au 27/05)

## Résumé de l'activité
L'activité récente de l'organisation se concentre sur la maturation de l'écosystème RAG (Retrieval-Augmented Generation) et des agents intelligents. Les efforts ont permis de fluidifier le cycle de vie de la donnée, de l'ingestion automatisée avec [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) jusqu'à l'évaluation rigoureuse des performances via [evalap](/repos/etalab-ia/evalap) et [eval-transcript](/repos/etalab-ia/eval-transcript).

En parallèle, les outils de développement et d'interaction avec les LLM gagnent en robustesse et en fonctionnalités, notamment grâce aux évolutions de [letta](/repos/etalab-ia/letta) et [just-code](/repos/etalab-ia/just-code), qui introduisent des capacités de planification, de gestion de la mémoire et de sécurisation des environnements de travail.

## Sécurité
- Renforcement de la conformité et de la sécurité avec l'intégration des guides de l'ANSSI et de la DINUM dans [skills](/repos/etalab-ia/skills).
- Amélioration de la protection des données via la détection de secrets et un mode d'isolation complète dans [just-code](/repos/etalab-ia/just-code).
- Gestion avancée des clés API (révocation, filtrage) et contrôle de consommation renforcé (rate limiting) dans [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
- Mise en place de vérifications de vulnérabilités en pré-push et de hooks de sécurité (gitleaks) dans [parcours-rag](/repos/etalab-ia/parcours-rag) et [eval-transcript](/repos/etalab-ia/eval-transcript).

## Autres changements notables
- Refonte architecturale et renommage de la plateforme RAG, passant de [rag-facile](/repos/etalab-ia/rag-facile) à [ragtime](/repos/etalab-ia/ragtime).
- Migrations d'infrastructure majeures, incluant le passage vers une architecture serverless pour [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) et vers une "Clean Architecture" pour [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
- Passage à la version majeure 2.0.0 de [chartsgouv](/repos/etalab-ia/chartsgouv) pour une mise en conformité avec la version 6.1 du Design Système de l'État (DSFR).
- Optimisation des processus de déploiement et de construction d'images Docker pour [marker-serve](/repos/etalab-ia/marker-serve) et [OpenGateRAG](/repos/etalab-ia/OpenGateRAG).

## Dépôts les plus actifs
- [lettabot](/repos/etalab-ia/lettabot) : Extension massive des capacités d'intégration (Slack, Discord, Telegram) et refonte du système de configuration.
- [letta](/repos/etalab-ia/letta) : Ajout de nouveaux modèles (Anthropic, Gemini) et de fonctionnalités avancées de gestion de la mémoire et des agents.
- [rag-facile](/repos/etalab-ia/rag-facile) : Refonte complète de l'architecture interne et ajout de l'authentification via Supabase.
- [evalap](/repos/etalab-ia/evalap) : Amélioration de l'exportation des résultats vers Hugging Face et de l'interface utilisateur de visualisation.
