# Synthèse d'activité : IA-Generative (du 01/10 au 31/10)

## Résumé de l'activité
L'organisation IA-Generative a connu une période d'activité intense, marquée par une montée en puissance des capacités d'intelligence artificielle et une amélioration majeure de l'expérience utilisateur. L'introduction d'assistants de recherche avancés dans [mycollections](/repos/IA-Generative/mycollections), de fonctionnalités multimodales (voix, vision, image) dans [Muffin](/repos/IA-Generative/Muffin) et d'une interface interactive "Bulle + IA" dans [IAssistant-Direct](/repos/IA-Generative/IAssistant-Direct) transforme radicalement la manière dont les utilisateurs interagissent avec leurs données.

Parallèlement, l'écosystème s'enrichit d'outils de productivité de plus en plus intégrés, comme le nouveau projet [mille-feuille](/repos/IA-Generative/mille-feuille) ou les extensions pour LibreOffice ([iassistant-libreoffice](/repos/IA-Generative/iassistant-libreoffice) et [dig-dig-doc](/repos/IA-Generative/dig-dig-doc)). Ces évolutions visent à rendre l'IA plus accessible, plus intuitive et capable de s'insérer naturellement dans les flux de travail existants.

## Sécurité
- **Renforcement de l'authentification** : Mise en place de la double authentification (2FA/TOTP) dans [myvault](/repos/IA-Generative/myvault) et [keycloak-jar-test](/repos/IA-Generative/keycloak-jar-test), et généralisation de l'usage des jetons (refresh tokens, API keys) et du SSO Keycloak dans [toolmesh](/repos/IA-Generative/toolmesh), [ocr](/repos/IA-Generative/ocr), [ocr-api](/repos/IA-Generative/ocr-api), [mcr](/repos/IA-Generative/mcr) et [abrege](/repos/IA-Generative/abrege).
- **Protection des données et des accès** : Implémentation de garde-fous contre les injections de prompts dans [owuiapps-agents](/repos/IA-Generative/owuiapps-agents), de mécanismes anti-fuite et de chiffrement des données sensibles dans [myvault](/repos/IA-Generative/myvault), [iassistant-libreoffice](/repos/IA-Generative/iassistant-libreoffice) et [Muffin](/repos/IA-Generative/Muffin).
- **Sécurisation des infrastructures** : Durcissement des conteneurs (passage en mode non-root) dans [ocr](/repos/IA-Generative/ocr), [ocr-api](/repos/IA-Generative/ocr-api), [abrege](/repos/IA-Generative/abrege) et [GatewAI](/repos/IA-Generative/GatewAI), ainsi que la correction de vulnérabilités critiques dans [owuiapps-agents](/repos/IA-Generative/owuiapps-agents) et [ocr-api](/repos/IA-Generative/ocr-api).

## Autres changements notables
- **Évolutions architecturales** : Migration vers des architectures en microservices ([mcr](/repos/IA-Generative/mcr), [Muffin](/repos/IA-Generative/Muffin)), passage de Kafka à Redis pour la gestion des files d'attente ([kevent-ai](/repos/IA-Generative/kevent-ai)) et optimisation majeure de la latence des API ([translate-rt](/repos/IA-Generative/translate-rt)).
- **Adoption de nouveaux standards** : Intégration massive du protocole MCP (Model Context Protocol) pour permettre aux outils de communiquer entre eux ([toolmesh](/repos/IA-Generative/toolmesh), [mycollections](/repos/IA-Generative/mycollections), [mille-feuille](/repos/IA-Generative/mille-feuille), [dig-dig-doc](/repos/IA-Generative/dig-dig-doc) et [Muffin](/repos/IA-Generative/Muffin)).
- **Automatisation et déploiement** : Modernisation des pipelines CI/CD et des stratégies de déploiement (Docker, Helm, ArgoCD) à travers l'ensemble des dépôts, notamment [translate-rt](/repos/IA-Generative/translate-rt), [n8n-nodes-s3-presigner](/repos/IA-Generative/n8n-nodes-s3-presigner) et [GatewAI](/repos/IA-Generative/GatewAI).

## Dépôts les plus actifs
- [mycollections](/repos/IA-Generative/mycollections) : Transformation majeure avec l'arrivée des assistants de recherche et l'intégration de nouvelles sources de données (Google Drive, Résana).
- [ocr](/repos/IA-Generative/ocr) et [ocr-api](/repos/IA-Generative/ocr-api) : Améliorations significatives de l'interface utilisateur, des SDK et de la sécurité.
- [myvault](/repos/IA-Generative/myvault) : Renforcement massif de la sécurité et ajout de l'authentification à deux facteurs.
- [GatewAI](/repos/IA-Generative/GatewAI) : Introduction du streaming en temps réel via WebSocket et gestion avancée des quotas.
- [iassistant-libreoffice](/repos/IA-Generative/iassistant-libreoffice) : Internationalisation complète et sécurisation accrue des données locales.
- [abrege](/repos/IA-Generative/abrege) : Nouvelles capacités d'analyse sémantique et modernisation de l'interface utilisateur.
