# Synthèse d'activité : etalab-ia (du 01/05 au 21/09)

## Résumé de l'activité
L'activité récente de l'organisation est dominée par l'expansion et la maturation de l'écosystème RAG (Retrieval-Augmented Generation) et des agents autonomes. Les développements ont permis d'enrichir les capacités de mémorisation et de planification des agents via [letta](/repos/etalab-ia/letta) et [letta-code](/repos/etalab-ia/letta-code), tout en améliorant les outils d'évaluation de la qualité des réponses avec [evalap](/repos/etalab-ia/evalap) et [eval-transcript](/repos/etalab-ia/eval-transcript).

Parallèlement, l'organisation a consolidé ses infrastructures de données et de services LLM, notamment avec l'automatisation des pipelines vers Hugging Face pour [mediatech](/repos/etalab-ia/mediatech) et l'unification des services [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) et [OpenGateRAG](/repos/etalab-ia/OpenGateRAG). Ces évolutions visent à offrir des outils plus robustes, scalables et prêts pour la production, comme en témoigne la préparation de [whisperx-openai-api](/repos/etalab-ia/whisperx-openai-api) pour les infrastructures GPU de pointe.

## Sécurité
- **Protection des données :** Implémentation de la détection automatique de secrets et de la vérification d'attestation pour garantir l'intégrité des composants dans [just-code](/repos/etalab-ia/just-code).
- **Gestion des accès :** Sécurisation de la saisie des clés API via une demande de mot de passe dans [ragtime](/repos/etalab-ia/ragtime) et intégration de l'authentification GitHub pour [albert-code](/repos/etalab-ia/albert-code).
- **Contrôles de conformité :** Ajout de vérifications de vulnérabilités des dépendances dans [parcours-rag](/repos/etalab-ia/parcours-rag) et [eval-transcript](/repos/etalab-ia/eval-transcript).

## Autres changements notables
- **Refontes architecturales et migrations :** Migration complète du projet [just-code](/repos/etalab-ia/just-code) vers le langage Go, adoption d'une "Clean Architecture" pour [OpenGateLLM](/repos/etalab-ia/OpenGateLLM), et passage à une architecture de base de données serverless pour [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api).
- **Rebranding et restructuration :** Transition du projet [rag-facile](/repos/etalab-ia/rag-facile) vers [ragtime](/repos/etalab-ia/ragtime), incluant une refonte modulaire de son architecture interne.
- **Optimisation de la production :** Préparation au déploiement haute performance pour [whisperx-openai-api](/repos/etalab-ia/whisperx-openai-api) (support GPU H200) et optimisation des processus de construction d'images Docker pour [marker-serve](/repos/etalab-ia/marker-serve) et [OpenGateRAG](/repos/etalab-ia/OpenGateRAG).

## Dépôts les plus actifs
- [lettabot](/repos/etalab-ia/lettabot) : Extension des intégrations (Slack, Discord, Telegram) et refonte du système de configuration.
- [letta](/repos/etalab-ia/letta) : Ajout de nouveaux modèles de pointe et de fonctionnalités avancées pour la gestion des agents.
- [just-code](/repos/etalab-ia/just-code) : Migration technologique vers Go et extension du support aux environnements Windows et macOS.
- [ragtime](/repos/etalab-ia/ragtime) : Rebranding et ajout d'une interface CLI pour la gestion des collections de documents.
- [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) : Amélioration de l'observabilité, de la gestion des quotas et de l'architecture logicielle.
