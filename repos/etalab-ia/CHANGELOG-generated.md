# Synthèse d'activité : etalab-ia (du 23/09 au 30/09)

## Résumé de l'activité
L'activité de l'organisation est marquée par une montée en maturité des outils de RAG (Retrieval-Augmented Generation) et des frameworks d'agents, avec notamment le lancement de l'outil de benchmark [eval-ocr-htr](/repos/etalab-ia/eval-ocr-htr). Les efforts se sont concentrés sur la robustesse des infrastructures (authentification, persistance des données via Supabase), l'élargissement du support des modèles de pointe (Anthropic, Gemini, Qwen) et le renforcement des capacités d'évaluation de la qualité des réponses. 

Ces évolutions visent à fournir des solutions prêtes pour une utilisation en production, tout en intégrant des standards de sécurité et de conformité essentiels pour les agents publics. L'écosystème s'enrichit également de nouveaux pipelines automatisés pour la gestion des données légales et de l'amélioration de l'observabilité des modèles.

## Sécurité
- Intégration des guides de sécurité de l'ANSSI et de la DINUM pour accompagner l'usage de l'IA dans le secteur public ([skills](/repos/etalab-ia/skills)).
- Renforcement de l'isolation par défaut, du scan de secrets et du contrôle des montages pour les environnements d'exécution ([just-code](/repos/etalab-ia/just-code)).
- Mise en place de vérifications de vulnérabilités des dépendances en pré-push ([parcours-rag](/repos/etalab-ia/parcours-rag)).

## Autres changements notables
- Refonte majeure de l'architecture de [rag-facile](/repos/etalab-ia/rag-facile) (devenu [ragtime](/repos/etalab-ia/ragtime)) incluant l'authentification et la persistance des conversations via Supabase.
- Migration vers une "Clean Architecture" et intégration de l'observabilité avec Langfuse pour [OpenGateLLM](/repos/etalab-ia/OpenGateLLM).
- Évolution vers une architecture multi-runtimes (agent-vm, macOS) et portage massif de composants en Go pour [just-code](/repos/etalab-ia/just-code).
- Migration de la base de données vers une architecture serverless pour [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api).
- Passage à la version majeure 2.0.0 de [chartsgouv](/repos/etalab-ia/chartsgouv) pour la mise en conformité avec le Design Système de l'État (DSFR 6.1).
- Initialisation et stabilisation de [OpenGateRAG](/repos/etalab-ia/OpenGateRAG) avec mise en place de pipelines CI/CD et de tests de bout en bout.

## Dépôts les plus actifs
- [lettabot](/repos/etalab-ia/lettabot) : Extension massive des intégrations (Slack, Discord, Telegram) et refonte du système de configuration.
- [ragtime](/repos/etalab-ia/ragtime) : Transformation profonde de la plateforme de gestion de collections et de l'interface utilisateur.
- [letta](/repos/etalab-ia/letta) et [letta-code](/repos/etalab-ia/letta-code) : Évolutions rapides du support de modèles et des capacités des agents.
- [just-code](/repos/etalab-ia/just-code) : Avancées techniques majeures sur la sécurité, l'isolation et le support multi-plateforme.
