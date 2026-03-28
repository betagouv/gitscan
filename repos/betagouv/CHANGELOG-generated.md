# Synthèse d'activité : betagouv (derniers 7 jours)

## Résumé de l'activité
L'activité de betagouv sur les 7 derniers jours a été très riche, touchant un grand nombre de dépôts. On observe une forte concentration sur l'amélioration de l'expérience utilisateur, avec des refontes d'interface (diagbruit.beta.gouv.fr, espace-membre-next), l'ajout de nouvelles fonctionnalités (Aidants_Connect, api-subventions-asso, anssi-portail), et des corrections de bugs pour une meilleure stabilité. La sécurité est également un point d'attention, avec l'ajout de l'authentification à deux facteurs (gestion-des-subventions-locales) et des mises à jour de dépendances pour corriger des vulnérabilités (dsfr-assets, anssi-recommandations-cyber-data). Plusieurs dépôts ont bénéficié de mises à jour techniques importantes, comme des refactorings d'architecture (api-subventions-asso, resultats-Elections-FPT) et l'intégration de nouveaux outils (PostHog sur france-chaleur-urbaine).

## Sécurité
Plusieurs dépôts ont bénéficié de mises à jour de sécurité :
- **anssi-recommandations-cyber-data** : Mise à jour de dépendances vulnérables (deepeval, protobuf).
- **gestion-des-subventions-locales** : Ajout de l'authentification à deux facteurs (OTP) et protection contre les attaques par force brute.
- **dsfr-assets** : Mise à jour vers la version 1.14.3 pour corriger des failles de sécurité.
- **euphrosyne-digilab** : Mise à jour des dépendances.
- **grist-budget-agriculture** : Ajout d'un scan antivirus ClamAV pour les fichiers uploadés.

## Autres changements notables
- **resultats-Elections-FPT** : Migration vers Vue.js et mise en place d'une CI/CD.
- **api-subventions-asso** : Refactoring majeur de l'architecture avec l'introduction de patterns Mapper, Port et Adapter.
- **ComparIA** : Ajout de nouveaux modèles de langage (Mistral Small 4, GPT-5.4, Gemini 3.1 Flash Lite, etc.) et implémentation d'un filtre anti-spam.
- **diagbruit.beta.gouv.fr** : Refonte de l'interface utilisateur et ajout de nouvelles fonctionnalités.
- **a-just** : Mise à jour de l'extracteur de données pour la collecte 2026.
- **france-chaleur-urbaine** : Intégration de PostHog pour le suivi analytics et l'autocapture.
- **dsfr-form-builder** : Ajout d'un site de documentation et de démonstration.

## Dépôts les plus actifs
- **Aidants_Connect** : Ajout de nouvelles fonctionnalités pour les conseillers numériques et les aidants.
- **ComparIA** : Ajout de nouveaux modèles de langage et amélioration de la réactivité.
- **a-just** : Corrections et améliorations pour la collecte de données 2026.
- **api-subventions-asso** : Refactoring majeur et ajout de nouvelles fonctionnalités.
- **diagbruit.beta.gouv.fr** : Refonte de l'interface utilisateur et ajout de nouvelles fonctionnalités.
- **france-chaleur-urbaine** : Ajout de nouveaux modes de chauffage et amélioration de l'interface utilisateur.
- **gestion-des-subventions-locales** : Amélioration de la sécurité et ajout de nouvelles fonctionnalités.
- **euphrosyne** : Amélioration de l'interface utilisateur et intégration du DSFR.
- **grist-budget-agriculture** : Amélioration du traitement des informations budgétaires.
