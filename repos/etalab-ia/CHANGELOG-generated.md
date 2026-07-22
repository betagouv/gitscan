# Synthèse d'activité : etalab-ia (du 16 mai 2026 au 16 juillet 2026)

## Résumé de l'activité
L'organisation etalab-ia a connu une période d'activité soutenue, marquée par des avancées significatives sur plusieurs fronts. Les projets se sont concentrés sur l'amélioration de l'infrastructure et des outils existants, notamment OpenGateLLM, ragtime et mediatech, avec un accent sur la robustesse, la sécurité et l'expérience utilisateur. L'intégration de nouvelles fonctionnalités, comme l'export vers Hugging Face Hub (evalap, mediatech-to-albert-api) et l'ajout de compétences (dragster, letta-code), témoigne d'une volonté d'enrichir l'offre et de répondre aux besoins des utilisateurs. Plusieurs projets ont également bénéficié d'une refonte architecturale pour une meilleure maintenabilité et scalabilité.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations en matière de sécurité :
- Correction de vulnérabilités dans OpenGateLLM ([OpenGateLLM](/repos/etalab-ia/OpenGateLLM)).
- Ajout d'un hook pre-commit gitleaks pour améliorer la sécurité dans eval-transcript ([eval-transcript](/repos/etalab-ia/eval-transcript)).
- Renforcement de la sécurité avec une deny-list dans albert-code ([albert-code](/repos/etalab-ia/albert-code)).

## Autres changements notables
- **Refactorings architecturaux :** OpenGateLLM et ragtime ont subi des refactorings importants pour améliorer la structure du code et la maintenabilité.
- **Migration d'infrastructure :** mediatech-to-albert-api a migré sa base de données vers une architecture serverless pour une meilleure scalabilité.
- **Suppression de fonctionnalités :** La fonctionnalité RAG a été supprimée d'OpenGateLLM ([OpenGateLLM](/repos/etalab-ia/OpenGateLLM)).
- **Changement de nom :** Le projet rag-facile a été renommé ragtime ([ragtime](/repos/etalab-ia/ragtime)).

## Dépôts les plus actifs
- [whisperx-openai-api](/repos/etalab-ia/whisperx-openai-api) : Développement initial rapide d'une API pour la transcription audio, compatible avec OpenAI.
- [ragtime](/repos/etalab-ia/ragtime) : Refonte et ajout de fonctionnalités pour la gestion de collections de documents.
- [skills](/repos/etalab-ia/skills) : Amélioration de la synchronisation avec datagouv et refactoring pour la sécurité.
- [mediatech](/repos/etalab-ia/mediatech) : Intégration de nouveaux jeux de données et optimisation du traitement des données.
- [letta-code](/repos/etalab-ia/letta-code) : Ajout de support pour de nouveaux modèles d'IA et amélioration de la gestion des agents.
- [OpenGateLLM](/repos/etalab-ia/OpenGateLLM) : Refactoring de l'architecture, corrections de bugs et améliorations de la sécurité.
- [BlockNote](/repos/etalab-ia/BlockNote) : Corrections de bugs et améliorations de l'expérience utilisateur.
