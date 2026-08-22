# Synthèse d'activité : IA-Generative (du DD/MM au DD/MM)

## Résumé de l'activité
L'activité de la période est marquée par une montée en puissance des capacités d'analyse de contenu et d'automatisation. L'intégration de systèmes RAG ([Stirling-PDF](/repos/IA-Generative/Stirling-PDF)) et de nouvelles fonctionnalités de génération de questions-réponses ([abrege](/repos/IA-Generative/abrege)) renforce l'intelligence des outils de traitement de documents. Parallèlement, l'extension des capacités de transcription ([ocr-api](/repos/IA-Generative/ocr-api), [mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions)) et l'amélioration de l'expérience utilisateur via des parcours d'onboarding ([IAssistant-Direct](/repos/IA-Generative/IAssistant-Direct)) ou des interfaces mobiles ([dictaphone](/repos/IA-Generative/dictaphone)) augmentent la valeur métier pour les utilisateurs finaux.

L'écosystème de l'automatisation s'enrichit également avec le développement de nouveaux nœuds n8n ([n8n-nodes-playwright-core](/repos/IA-Generative/n8n-nodes-playwright-core), [n8n-nodes-async-api](/repos/IA-Generative/n8n-nodes-async-api)) et une meilleure gestion des ressources distantes.

## Sécurité
- **Protection contre les injections** : Renforcement de la sécurité contre les injections de prompt (OWASP LLM01) ([owuiapps-agents](/repos/IA-Generative/owuiapps-agents)).
- **Authentification et accès** : Implémentation de l'authentification à deux facteurs (2FA/TOTP) ([myvault](/repos/IA-Generative/myvault)), amélioration de la gestion des jetons JWT/PKCE ([dictaphone](/repos/IA-Generative/dictaphone)) et support de la déconnexion fédérée Keycloak ([owuiapps-agents](/repos/IA-Generative/owuiapps-agents)).
- **Protection des données** : Mise en place de garde-fous anti-leak ([myvault](/repos/IA-Generative/myvault), [mycollections](/repos/IA-Generative/mycollections)), hachage des secrets ([myvault](/repos/IA-Generative/myvault)) et renforcement de la conformité via la documentation des données PII ([mirai-api](/repos/IA-Generative/mirai-api)).
- **Sécurisation des infrastructures** : Utilisation d'images Docker non-root ([device-management](/repos/IA-Generative/device-management)), intégration de `gitleaks` pour la détection de secrets ([claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway), [Archives-Mail-Thunderbird-Distribution](/repos/IA-Generative/Archives-Mail-Thunderbird-Distribution)) et protection contre les attaques SSRF et XSS ([mycollections](/repos/IA-Generative/mycollections), [myvault](/repos/IA-Generative/myvault)).

## Autres changements notables
- **Évolutions architecturales** : Migration majeure vers un modèle de microservices ([mcr](/repos/IA-Generative/mcr)), passage de la gestion des files d'attente de Kafka vers Redis ([kevent-ai](/repos/IA-Generative/kevent-ai)) et optimisation des processus de build via un modèle "in-cluster" ([mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions)).
- **Intégration de modèles et services** : Support opérationnel des modèles GLM-5.2 de Scaleway ([claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway)) et expansion de l'écosystème de nœuds n8n ([n8n-nodes-playwright-core](/repos/IA-Generative/n8n-nodes-playwright-core), [n8n-nodes-async-api](/repos/IA-Generative/n8n-nodes-async-api)).
- **Déploiement et Cloud** : Introduction de charts Helm pour faciliter le déploiement et préparation au déploiement cloud-native ([device-management](/repos/IA-Generative/device-management)).

## Dépôts les plus actifs
- [myvault](/repos/IA-Generative/myvault) : Travaux intensifs sur la sécurité, le chiffrement et la gestion des accès.
- [mycollections](/repos/IA-Generative/mycollections) : Amélioration de l'expérience playground et sécurisation des données.
- [mcr](/repos/IA-Generative/mcr) : Refonte profonde de l'architecture vers les microservices.
- [abrege](/repos/IA-Generative/abrege) : Ajout de fonctionnalités de scraping web et de génération de QA.
- [ocr-api](/repos/IA-Generative/ocr-api) : Extension des formats de fichiers et des capacités de transcription.
- [claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway) : Intégration des modèles Scaleway et stabilisation de l'API.
- [kevent-ai](/repos/IA-Generative/kevent-ai) : Migration vers Redis et optimisation de la gestion des tâches.
- [device-management](/repos/IA-Generative/device-management) : Nouveaux outils de monitoring et préparation au cloud-native.
