# Synthèse d'activité : IA-Generative (du 15/10 au 22/10)

## Résumé de l'activité
L'organisation a franchi une étape majeure vers l'intelligence artificielle agentique avec le lancement d'assistants de recherche [mycollections](/repos/IA-Generative/mycollections), de capacités de génération de documents assistée [mille-feuille](/repos/IA-Generative/mille-feuille) [dig-dig-doc](/repos/IA-Generative/dig-dig-doc) et l'intégration de modèles Scaleway [claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway). Ces évolutions visent à rendre l'IA plus autonome, capable de raisonner et de produire des documents structurés de manière fluide.

L'expérience utilisateur est également au cœur des priorités avec la modernisation des interfaces via le design system DSFR [owuiapps-agents](/repos/IA-Generative/owuiapps-agents) [mille-feuille](/repos/IA-Generative/mille-feuille) et l'introduction de la "Bulle + IA" [IAssistant-Direct](/repos/IA-Generative/IAssistant-Direct) pour une interaction directe sur le web. L'adoption du protocole MCP [mycollections](/repos/IA-Generative/mycollections) [mille-feuille](/repos/IA-Generative/mille-feuille) [dig-dig-doc](/repos/IA-Generative/dig-dig-doc) assure une interopérabilité accrue entre les différents outils de l'écosystème.

## Sécurité
- **Authentification et accès** : Généralisation de l'usage de Keycloak pour le SSO [toolmesh](/repos/IA-Generative/toolmesh) [mille-feuille](/repos/IA-Generative/mille-feuille) [mcr](/repos/IA-Generative/mcr), mise en place de l'authentification à deux facteurs (2FA/TOTP) [myvault](/repos/IA-Generative/myvault) [keycloak-jar-test](/repos/IA-Generative/keycloak-jar-test) et sécurisation des flux via PKCE [dictaphone](/repos/IA-Generative/dictaphone) [IAssistant-Direct](/repos/IA-Generative/IAssistant-Direct).
- **Protection des modèles et des données** : Renforcement de la sécurité contre les injections de prompts [owuiapps-agents](/repos/IA-Generative/owuiapps-agents), mise en place de mécanismes anti-leak [myvault](/repos/IA-Generative/myvault) et chiffrement des données sensibles [myvault](/repos/IA-Generative/myvault).
- **Durcissement des infrastructures** : Application de politiques de conteneurs "non-root" [ocr](/repos/IA-Generative/ocr) [abrege](/repos/IA-Generative/abrege), renforcement du rate-limiting [ocr](/repos/IA-Generative/ocr) [ocr-api](/repos/IA-Generative/ocr-api) [myvault](/repos/IA-Generative/myvault) et sécurisation des échanges via des en-têtes HTTP et le masquage des détails d'erreurs API [owuiapps-agents](/repos/IA-Generative/owuiapps-agents).

## Autres changements notables
- **Évolutions architecturales** : Migration vers des architectures en microservices [mcr](/repos/IA-Generative/mcr), passage de Kafka à Redis pour la gestion des files d'attente [kevent-ai](/repos/IA-Generative/kevent-ai) et intégration de Meilisearch pour la recherche hybride [Muffin](/repos/IA-Generative/Muffin).
- **Standardisation** : Adoption massive du protocole MCP (Model Context Protocol) pour l'interopérabilité des agents et des outils [mycollections](/repos/IA-Generative/mycollections) [mille-feuille](/repos/IA-Generative/mille-feuille) [dig-dig-doc](/repos/IA-Generative/dig-dig-doc).
- **Infrastructure et CI/CD** : Modernisation des pipelines de déploiement [claim-controller](/repos/IA-Generative/claim-controller) et automatisation des environnements de prévisualisation pour les développeurs [mirai-api](/repos/IA-Generative/mirai-api).

## Dépôts les plus actifs
- [mycollections](/repos/IA-Generative/mycollections) : Développement majeur des assistants de recherche et refonte complète de l'expérience utilisateur.
- [ocr](/repos/IA-Generative/ocr) & [ocr-api](/repos/IA-Generative/ocr-api) : Extension des SDK et renforcement massif de la sécurité et de l'interface.
- [myvault](/repos/IA-Generative/myvault) : Focus intensif sur la sécurité (2FA, chiffrement) et la robustesse du système.
- [mille-feuille](/repos/IA-Generative/mille-feuille) & [dig-dig-doc](/repos/IA-Generative/dig-dig-doc) : Avancées sur la génération de documents assistée et l'interface de chat IA.
- [abrege](/repos/IA-Generative/abrege) : Ajout de capacités d'analyse sémantique et modernisation de l'interface utilisateur.
