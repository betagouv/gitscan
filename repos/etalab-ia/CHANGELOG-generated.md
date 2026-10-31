# Synthèse d'activité : etalab-ia (du 25/10 au 31/10)

## Résumé de l'activité
L'activité récente de l'organisation est marquée par une montée en puissance de l'écosystème RAG (Retrieval-Augmented Generation) et des capacités d'agents autonomes. La plateforme [ragtime](/repos/etalab-ia/ragtime) (issue de la refonte de rag-facile) a franchi un cap majeur avec l'ajout de l'authentification, de la persistance des conversations et de l'évaluation de la qualité des réponses. Parallèlement, les capacités d'agents de [letta](/repos/etalab-ia/letta) et [letta-code](/repos/etalab-ia/letta-code) s'enrichissent avec le support de nouveaux modèles (Anthropic, Gemini, Kimi) et de nouveaux outils de planification.

L'automatisation des données pour le secteur public est également une priorité, avec la mise en place de pipelines d'ingestion automatisés via [mediatech](/repos/etalab-ia/mediatech) et [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api), garantissant une meilleure fraîcheur des informations. Enfin, l'accessibilité et l'intégration des outils sont renforcées par les évolutions du [chat-widget](/repos/etalab-ia/chat-widget) et de [albert-code](/repos/etalab-ia/albert-code).

## Sécurité
- Renforcement de l'isolation des environnements et de la gestion sécurisée des identifiants dans [just-code](/repos/etalab-ia/just-code).
- Intégration des recommandations de sécurité de l'ANSSI et de la DINUM pour accompagner l'usage de l'IA dans [skills](/repos/etalab-ia/skills).
- Mise en place de protections contre les abus (abuse caps) et durcissement de la sécurité de l'iframe pour le [chat-widget](/repos/etalab-ia/chat-widget).
- Intégration de scans de sécurité automatisés (Gitleaks, CVE Lite) dans les pipelines de [eval-transcript](/repos/etalab-ia/eval-transcript) et [chat-widget](/repos/etalab-ia/chat-widget).

## Autres changements notables
- Refonte architecturale majeure vers une "Clean Architecture" pour [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) et migration vers une architecture serverless pour [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api).
- Renommage du projet [rag-facile](/repos/etalab-ia/rag-facile) en [ragtime](/repos/etalab-ia/ragtime).
- Unification des API et de la documentation entre [OpenGateRAG](/repos/etalab-ia/OpenGateRAG) et [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).

## Dépôts les plus actifs
- [ragtime](/repos/etalab-ia/ragtime) : Refonte complète incluant l'authentification, la gestion de collections et l'intégration du thème DSFR.
- [lettabot](/repos/etalab-ia/lettabot) : Expansion multi-plateforme (Slack, Discord, Telegram) et nouveau système de configuration via YAML.
- [letta](/repos/etalab-ia/letta) : Évolution des capacités d'agents (mode listener, appels d'outils parallèles) et support étendu des modèles.
- [chat-widget](/repos/etalab-ia/chat-widget) : Sortie de la version 0.2.0 avec de nouvelles méthodes d'intégration via Web Components.
- [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) : Amélioration de la gestion des clés, du rate limiting et de l'observabilité avec Langfuse.
