# Synthèse d'activité : betagouv-experimentations (du 15/05 au 22/05)

## Résumé de l'activité
L'activité de l'organisation est marquée par une phase intense de lancement de nouveaux prototypes. La majorité des efforts se concentre sur l'initialisation de services web utilisant une stack technologique standardisée (Next.js, React, PostgreSQL, DSFR) et automatisée via Coolify. Cette approche permet de déployer rapidement des outils expérimentaux pour l'administration.

Parmi les avancées fonctionnelles majeures, on note le développement d'un outil de suivi des contacts pour l'équipe ASN dans [crm-asn](/repos/betagouv-experimentations/crm-asn) et la mise en place d'un proxy de gestion des logs dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy). L'organisation renforce également ses capacités de prototypage rapide en intégrant des capacités d'IA (Claude) directement dans ses workflows de développement.

## Sécurité
- Correction d'une vulnérabilité SQL injection de haute sévérité via la mise à jour de l'ORM dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Renforcement de la protection des applications par l'ajout d'en-têtes de sécurité dans [crm-asn](/repos/betagouv-experimentations/crm-asn).
- Amélioration de l'authentification dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) via l'intégration de l'appartenance à une organisation GitHub.

## Autres changements notables
- **Optimisation du prototypage et de l'IA** : Intégration de l'auto-provisionnement Coolify, automatisation des migrations de base de données et optimisation de l'usage des compétences de l'IA (Claude) dans [template-proto](/repos/betagouv-experimentations/template-proto).
- **Standardisation de l'infrastructure** : Déploiement massif de nouveaux environnements via des workflows CI/CD automatisés pour une série de nouveaux projets ([test-jb4](/repos/betagouv-experimentations/test-jb4), [test-jb2](/repos/betagouv-experimentations/test-jb2), [test-benoit](/repos/betagouv-experimentations/test-benoit), [simulation-doctorat](/repos/betagouv-experimentations/simulation-doctorat), etc.).
- **Gestion des logs** : Développement de fonctionnalités avancées de récupération de logs et de gestion des webhooks pour le nettoyage des ressources dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'une application de suivi des interactions et contacts pour l'équipe ASN.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Création d'un outil de proxy pour la gestion et la récupération des logs d'exécution.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Évolution du template de base avec automatisation DevOps et optimisation de l'IA.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Mise en place d'une application de gestion de tâches (CRUD) avec persistance de données.
- [test-jb3](/repos/betagouv-experimentations/test-jb3) : Maintenance corrective et mise à jour de sécurité.
