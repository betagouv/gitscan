# Synthèse d'activité : IA-Generative (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité de la semaine a été marquée par un effort massif de sécurisation des plateformes et d'intégration de capacités d'intelligence artificielle avancées. Les utilisateurs bénéficient de nouvelles fonctionnalités de génération de questions-réponses et de recherche documentaire (RAG) dans [abrege](/repos/IA-Generative/abrege) et [Stirling-PDF](/repos/IA-Generative/Stirling-PDF). Parallèlement, l'expérience utilisateur est enrichie par de nouveaux outils de gestion de tâches, de partage collaboratif et d'assistants d'onboarding, notamment dans [drive](/repos/IA-Generative/drive), [IAssistant-Direct](/repos/IA-Generative/IAssistant-Direct) et [dictaphone](/repos/IA-Generative/dictaphone).

## Sécurité
- Protection contre les injections de prompt et les fuites de données ([owuiapps-agents](/repos/IA-Generative/owuiapps-agents)).
- Authentification renforcée (2FA/TOTP, SSO Keycloak, gestion des jetons JWT/PKCE) ([myvault](/repos/IA-Generative/myvault), [owuiapps-agents](/repos/IA-Generative/owuiapps-agents), [dictaphone](/repos/IA-Generative/dictaphone)).
- Sécurisation des accès et des flux (limitation de débit, protection contre les attaques SSRF/CORS, validation de signatures WOPI) ([myvault](/repos/IA-Generative/myvault), [mycollections](/repos/IA-Generative/mycollections), [drive](/repos/IA-Generative/drive)).
- Durcissement de l'infrastructure et des conteneurs ([ocr-api](/repos/IA-Generative/ocr-api), [device-management](/repos/IA-Generative/device-management)).
- Intégration de la détection de secrets (gitleaks) dans les pipelines ([claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway), [Archives-Mail-Thunderbird-Distribution](/repos/IA-Generative/Archives-Mail-Thunderbird-Distribution)).

## Autres changements notables
- Migrations architecturales majeures (passage aux microservices et remplacement de Kafka par Redis pour la gestion des files d'attente) ([mcr](/repos/IA-Generative/mcr), [kevent-ai](/repos/IA-Generative/kevent-ai)).
- Optimisation des processus de build et de déploiement (adoption de BuildKit, utilisation de Helm et préparation au déploiement cloud-native) ([mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions), [device-management](/repos/IA-Generative/device-management), [claim-controller](/repos/IA-Generative/claim-controller)).
- Intégration de nouveaux modèles d'IA, notamment les modèles GLM-5.2 de Scaleway ([claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway)).

## Dépôts les plus actifs
- [myvault](/repos/IA-Generative/myvault) : Focus intensif sur la sécurité, le chiffrement et l'authentification.
- [mycollections](/repos/IA-Generative/mycollections) : Évolutions de l'interface utilisateur et renforcement de l'isolation des données.
- [mcr](/repos/IA-Generative/mcr) : Refactorisation majeure vers une architecture microservices.
- [drive](/repos/IA-Generative/drive) : Amélioration des fonctionnalités de partage collaboratif et de la sécurité WOPI.
- [abrege](/repos/IA-Generative/abrege) : Ajout de capacités de scraping web et de génération de QA.
- [kevent-ai](/repos/IA-Generative/kevent-ai) : Migration de l'infrastructure de gestion des files d'attente vers Redis.
