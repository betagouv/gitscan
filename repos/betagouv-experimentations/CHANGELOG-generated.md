# Synthèse d'activité : betagouv-experimentations (du 13/05 au 26/05)

## Résumé de l'activité
L'activité de l'organisation est marquée par une forte dynamique de lancement de nouveaux prototypes et l'industrialisation des processus de mise en production. Une grande partie des dépôts ([test-jb4](/repos/betagouv-experimentations/test-jb4), [test-jb2](/repos/betagouv-experimentations/test-jb2), [test-benoit](/repos/betagouv-experimentations/test-benoit), [simulation-doctorat](/repos/betagouv-experimentations/simulation-doctorat), [eval-metier-rag](/repos/betagouv-experimentations/eval-metier-rag), [26052026](/repos/betagouv-experimentations/26052026)) ont été initialisés en utilisant un socle technologique standardisé (Next.js, React, DSFR) et un déploiement automatisé via Coolify.

Parallèlement, des outils fonctionnels progressent significativement, notamment un outil de suivi de contacts ([crm-asn](/repos/betagouv-experimentations/crm-asn)), une application de gestion de tâches ([repo-test](/repos/betagouv-experimentations/repo-test)) et un proxy dédié à la gestion des logs ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)).

## Sécurité
- Correction d'une vulnérabilité SQL injection de haute sévérité via la mise à jour de l'ORM ([test-jb3](/repos/betagouv-experimentations/test-jb3)).
- Renforcement de la protection des applications par l'ajout d'en-têtes de sécurité ([crm-asn](/repos/betagouv-experimentations/crm-asn)).
- Mise en place d'une authentification basée sur l'appartenance à une organisation GitHub pour sécuriser l'accès aux logs ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)).

## Autres changements notables
- Optimisation du workflow de prototypage avec l'intégration de l'auto-provisionnement Coolify, l'automatisation des migrations de base de données et une meilleure exploitation des capacités d'IA ([template-proto](/repos/betagouv-experimentations/template-proto)).
- Évolution structurelle du projet de suivi de contacts, qui a été renommé et stabilisé ([crm-asn](/repos/betagouv-experimentations/crm-asn)).
- Développement de fonctionnalités avancées pour la gestion des logs, incluant la prise en charge des logs structurés et la gestion des webhooks GitHub ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'un outil de suivi des accompagnements pour l'équipe ASN.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Amélioration du template de base et de l'usage de l'IA.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Création d'un proxy pour la récupération et l'analyse des logs de déploiement.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Implémentation d'une application CRUD complète avec persistance de données.
