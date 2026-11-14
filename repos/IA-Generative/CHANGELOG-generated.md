# Synthèse d'activité : IA-Generative (du 01/10 au 30/10)

## Résumé de l'activité
L'organisation IA-Generative connaît une phase d'expansion majeure, marquée par l'intégration massive de capacités multimodales (voix, vision, image) et le déploiement d'assistants de recherche intelligents. Les utilisateurs bénéficient de nouveaux outils de productivité, comme des assistants de recherche guidés dans [mycollections](/repos/IA-Generative/mycollections) ou des capacités de génération de documents via IA dans [dig-dig-doc](/repos/IA-Generative/dig-dig-doc).

Parallèlement, l'écosystème se structure autour de standards émergents comme le protocole MCP et une automatisation accrue via des nœuds n8n spécialisés. Ces évolutions visent à offrir des expériences plus fluides, plus intelligentes et mieux intégrées aux flux de travail professionnels.

## Sécurité
- **Protection contre les attaques IA** : Renforcement de la défense contre les injections de prompt dans [owuiapps-agents](/repos/IA-Generative/owuiapps-agents) et mise en place de gardes-fous pour les actions critiques des agents dans [agent-skills](/repos/IA-Generative/agent-skills).
- **Gestion des identités et accès** : Généralisation de l'authentification à deux facteurs (2FA/TOTP) et gestion fine des niveaux de sécurité eIDAS dans [myvault](/repos/IA-Generative/myvault), [toolmesh](/repos/IA-Generative/toolmesh) et [keycloak-jar-test](/repos/IA-Generative/keycloak-jar-test).
- **Confidentialité et protection des données** : Migration des secrets vers des coffres-forts natifs dans [iassistant-libreoffice](/repos/IA-Generative/iassistant-libreoffice), chiffrement des données sensibles dans [Muffin](/repos/IA-Generative/Muffin) et protection contre les fuites d'informations dans [myvault](/repos/IA-Generative/myvault).
- **Durcissement des infrastructures** : Passage à une exécution en mode "non-root" pour les conteneurs dans [abrege](/repos/IA-Generative/abrege) et [ocr-api](/repos/IA-Generative/ocr-api), et intégration de scans de sécurité (gitleaks) dans [claude-code-scaleway](/repos/IA-Generative/claude-code-scaleway).

## Autres changements notables
- **Adoption du protocole MCP** : Intégration massive du *Model Context Protocol* pour l'interopérabilité des outils et des agents dans [toolmesh](/repos/IA-Generative/toolmesh), [mycollections](/repos/IA-Generative/mycollections), [mille-feuille](/repos/IA-Generative/mille-feuille), [dig-dig-doc](/repos/IA-Generative/dig-dig-doc) et [Muffin](/repos/IA-Generative/Muffin).
- **Évolutions architecturales** : Migration vers des architectures en micro-services dans [mcr](/repos/IA-Generative/mcr) et [Muffin](/repos/IA-Generative/Muffin), et remplacement de Kafka par Redis pour la gestion des files d'attente dans [kevent-ai](/repos/IA-Generative/kevent-ai).
- **Optimisations de performance** : Introduction du streaming WebSocket en temps réel dans [GatewAI](/repos/IA-Generative/GatewAI) et parallélisation des processus de transcription et de traduction dans [translate-rt](/repos/IA-Generative/translate-rt).

## Dépôts les plus actifs
- [mycollections](/repos/IA-Generative/mycollections) : Transformation majeure avec l'introduction d'assistants de recherche et l'intégration de nouvelles sources de données (Résana, Google Drive).
- [Muffin](/repos/IA-Generative/Muffin) : Évolution vers une plateforme multimodale (voix, image, vision) et passage en micro-services.
- [GatewAI](/repos/IA-Generative/GatewAI) : Avancées significatives sur le streaming temps réel et la gestion des quotas de tokens.
- [myvault](/repos/IA-Generative/myvault) : Travaux intensifs sur la sécurité, le chiffrement des données et l'authentification 2FA.
- [agent-skills](/repos/IA-Generative/agent-skills) : Restructuration profonde de l'organisation des compétences et simplification du processus d'installation.
- [ocr](/repos/IA-Generative/ocr) et [ocr-api](/repos/IA-Generative/ocr-api) : Évolutions majeures de l'interface utilisateur, des SDK et du durcissement de la sécurité.
