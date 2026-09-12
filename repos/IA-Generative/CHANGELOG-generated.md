# Synthèse d'activité : IA-Generative (du 20/08 au 27/08)

## Résumé de l'activité
L'activité de l'organisation a été dominée par un double objectif : la sécurisation accrue des services et l'enrichissement des capacités d'intelligence artificielle. Les développements ont permis de renforcer la protection contre les attaques (injections de prompts, fuites de données) et de déployer des mécanismes d'authentification robustes (2FA, SSO). 

En parallèle, l'écosystème s'est enrichi de nouvelles fonctionnalités d'IA (RAG, génération de questions-réponses, intégration des modèles Scaleway) et de l'expansion de l'offre d'automatisation via n8n. Enfin, une cohérence visuelle a été renforcée à travers l'adoption de la nouvelle mascotte Mirai sur plusieurs interfaces.

## Sécurité
- **Protection contre les attaques LLM et fuites de données** : Mise en place de garde-fous contre les injections de prompts (OWASP LLM01) et de mécanismes anti-leak ([owuiapps-agents](/repos/IA-Generative/owuiapps-agents), [myvault](/repos/IA-Generative/myvault), [mycollections](/repos/IA-Generative/mycollections)).
- **Renforcement de l'authentification** : Introduction de l'authentification à deux facteurs (2FA/TOTP), gestion fine des niveaux de sécurité eIDAS et support SSO ([myvault](/repos/IA-Generative/myvault), [keycloak-jar-test](/repos/IA-Generative/keycloak-jar-test), [owuiapps-agents](/repos/IA-Generative/owuiapps-agents), [dictaphone](/repos/IA-Generative/dictaphone)).
- **Sécurisation des échanges et des infrastructures** : Durcissement des conteneurs, vérification systématique des signatures WOPI, protection contre les attaques SSRF/CORS et sécurisation des jetons de session ([drive](/repos/IA-Generative/drive), [mycollections](/repos/IA-Generative/mycollections), [ocr-api](/repos/IA-Generative/ocr-api), [device-management](/repos/IA-Generative/device-management)).

## Autres changements notables
- **Évolutions architecturales majeures** : Migration vers un modèle de microservices ([mcr](/repos/IA-Generative/mcr)) et changement d'infrastructure de files d'attente de Kafka vers Redis ([kevent-ai](/repos/IA-Generative/kevent-ai)).
- **Modernisation DevOps et CI/CD** : Optimisation des pipelines de déploiement, intégration de Helm et passage à BuildKit rootless pour les processus de construction en cluster ([ocr-api](/repos/IA-Generative/ocr-api), [mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions), [device-management](/repos/IA-Generative/device-management), [claim-controller](/repos/IA-Generative/claim-controller)).

## Dépôts les plus actifs
- [myvault](/repos/IA-Generative/myvault) : Travaux intensifs sur la sécurité, le chiffrement des données et l'authentification 2FA.
- [mycollections](/repos/IA-Generative/mycollections) : Améliorations de l'interface utilisateur, du playground IA et de la sécurité des accès.
- [drive](/repos/IA-Generative/drive) : Évolutions sur le partage collaboratif et le renforcement de la sécurité des intégrations WOPI.
- [abrege](/repos/IA-Generative/abrege) : Ajout de fonctionnalités de scraping web et de génération de questions-réponses.
- [mcr](/repos/IA-Generative/mcr) : Refactorisation majeure vers les microservices et amélioration de l'expérience d'import de fichiers.
- [n8n-nodes-async-api](/repos/IA-Generative/n8n-nodes-async-api) : Développement des premiers nœuds dédiés aux services IA BRIO.
