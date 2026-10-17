# Synthèse d'activité : etalab-ia (dernière période)

## Résumé de l'activité
L'activité récente de l'organisation se concentre sur la maturation des outils de recherche documentaire (RAG) et l'enrichissement des capacités des agents intelligents. Les développements, notamment via [ragtime](/repos/etalab-ia/ragtime) et [mediatech](/repos/etalab-ia/mediatech), permettent une exploitation plus performante et automatisée des données publiques pour les applications d'IA.

L'accent est également mis sur la fiabilité et la conformité, avec des avancées notables dans l'évaluation automatisée des modèles ([evalap](/repos/etalab-ia/evalap), [eval-transcript](/repos/etalab-ia/eval-transcript)) et l'intégration de standards de sécurité publique ([skills](/repos/etalab-ia/skills)). Ces évolutions renforcent la robustesse et l'accessibilité des solutions pour les agents de l'État et les développeurs.

## Sécurité
- Intégration des guides de sécurité de l'ANSSI et de la DINUM pour accompagner l'usage de l'IA dans le secteur public ([skills](/repos/etalab-ia/skills)).
- Renforcement de l'isolation par défaut, du scan de secrets et de la gestion sécurisée des identifiants ([just-code](/repos/etalab-ia/just-code)).
- Mise en place de vérifications de vulnérabilités des dépendances en pré-push ([parcours-rag](/repos/etalab-ia/parcours-rag)).

## Autres changements notables
- **Évolutions architecturales et infrastructurelles** : Migration vers une "Clean Architecture" pour [OpenGateLLM](/repos/etalab-ia/OpenGateLLM), passage à une architecture serverless pour [mediatech-to-albert-api](/repos/etalab-ia/mediatech-to-albert-api) et refonte modulaire de [ragtime](/repos/etalab-ia/ragtime).
- **Évolutions identitaires et de versioning** : Passage à la version 2.0.0 de [chartsgouv](/repos/etalab-ia/chartsgouv) et changement de nom du projet [rag-facile](/repos/etalab-ia/rag-facile) en [ragtime](/repos/etalab-ia/ragtime).
- **Développement et performance** : Portage massif de composants en Go pour [just-code](/repos/etalab-ia/just-code) et optimisation des images Docker pour [marker-serve](/repos/etalab-ia/marker-serve).
- **Lancement** : Mise à disposition de la version initiale de l'outil de benchmark OCR/manuscrit ([eval-ocr-htr](/repos/etalab-ia/eval-ocr-htr)).

## Dépôts les plus actifs
- [ragtime](/repos/etalab-ia/ragtime) : Refonte majeure de l'architecture, ajout de l'authentification et changement de nom.
- [lettabot](/repos/etalab-ia/lettabot) : Expansion massive des plateformes supportées (Slack, Discord, Telegram) et refonte du système de configuration.
- [letta](/repos/etalab-ia/letta) et [letta-code](/repos/etalab-ia/letta-code) : Support de nouveaux modèles de pointe (Anthropic, Gemini) et nouveaux outils pour les agents (mémoire, planification).
- [evalap](/repos/etalab-ia/evalap) et [eval-transcript](/repos/etalab-ia/eval-transcript) : Automatisation de l'export des résultats vers Hugging Face et nouveaux moteurs de scoring par LLM.
- [just-code](/repos/etalab-ia/just-code) : Diversification des environnements d'exécution (Windows, macOS) et renforcement de la sécurité.
