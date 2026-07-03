# Synthèse d'activité : IA-Generative (du 22/06 au 29/06)

## Résumé de l'activité
L'organisation IA-Generative a connu une semaine riche en activités, axée sur l'amélioration de la sécurité, de la robustesse et de l'expérience utilisateur de ses différents projets. Plusieurs dépôts ont bénéficié de correctifs de sécurité importants, notamment [myvault](/repos/IA-Generative/myvault) et [device-management](/repos/IA-Generative/device-management).  Des avancées significatives ont été réalisées dans l'intégration de l'IA, avec l'ajout de fonctionnalités RAG dans [Stirling-PDF](/repos/IA-Generative/Stirling-PDF) et l'amélioration de l'API [mirai-api](/repos/IA-Generative/mirai-api). L'accent a également été mis sur l'automatisation et l'amélioration des processus de développement, avec des mises à jour de CI/CD et l'intégration d'outils d'observabilité.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations significatives en matière de sécurité :

- [myvault](/repos/IA-Generative/myvault) : Ajout de l'authentification à deux facteurs (2FA), limitation du débit, renforcement de la gestion des secrets M2M, et correction de vulnérabilités.
- [device-management](/repos/IA-Generative/device-management) : Correction de vulnérabilités suite à un audit de sécurité, renforcement de la gestion des secrets et suppression de composants non sécurisés.
- [abrege](/repos/IA-Generative/abrege) : Correction d'une vulnérabilité de sécurité.
- [Archives-Mail-Thunderbird-Distribution](/repos/IA-Generative/Archives-Mail-Thunderbird-Distribution) : Renforcement de la sécurité du dépôt avec un `.gitignore` plus restrictif et l'intégration de `gitleaks`.
- [owuiapps-agents](/repos/IA-Generative/owuiapps-agents) : Implémentation d'une garde anti-prompt-injection et de limitations de débit.

## Autres changements notables
Plusieurs évolutions techniques majeures ont été apportées :

- **Infrastructure :** Passage à Redis pour la gestion des files d'attente dans [kevent-ai](/repos/IA-Generative/kevent-ai).
- **Architecture :** Refactorisation de l'architecture de [mcr](/repos/IA-Generative/mcr) vers une approche basée sur les "use cases" et migration vers une approche asynchrone pour la diarisation.
- **Intégration :** Intégration de Grafana avec SSO Keycloak dans [device-management](/repos/IA-Generative/device-management).
- **Développement :** Amélioration des processus de CI/CD dans [abrege](/repos/IA-Generative/abrege) et [Archives-Mail-Thunderbird-Distribution](/repos/IA-Generative/Archives-Mail-Thunderbird-Distribution).

## Dépôts les plus actifs
- [myvault](/repos/IA-Generative/myvault) : Améliorations majeures de la sécurité et ajout de l'authentification à deux facteurs.
- [device-management](/repos/IA-Generative/device-management) : Renforcement de la sécurité et amélioration de l'observabilité.
- [Stirling-PDF](/repos/IA-Generative/Stirling-PDF) : Intégration de fonctionnalités RAG et optimisation des performances.
- [mcr](/repos/IA-Generative/mcr) : Refactorisation de l'architecture et amélioration de la gestion de la diarisation.
- [mirai-mesreunions](/repos/IA-Generative/mirai-mesreunions) : Ajout de l'importation de vidéos YouTube et amélioration de la gestion des fichiers MCR.
