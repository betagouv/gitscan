# Synthèse d'activité : betagouv-experimentations (du 13/05 au 26/05)

## Résumé de l'activité
L'activité de l'organisation est marquée par une phase intense de prototypage et de standardisation de l'infrastructure. De nombreux nouveaux projets sont lancés pour tester la création rapide d'applications web en utilisant des technologies modernes (React, Next.js, PostgreSQL) et le Design System Français (DSFR). 

L'accent est mis sur l'automatisation du déploiement et l'intégration de l'intelligence artificielle pour accélérer le développement. Des outils fonctionnels émergent, notamment un système de suivi de contacts pour l'équipe ASN dans [crm-asn](/repos/betagouv-experimentations/crm-asn) et une application de gestion de tâches dans [repo-test](/repos/betagouv-experimentations/repo-test).

## Sécurité
- Correction d'une vulnérabilité d'injection SQL de haute sévérité via la mise à jour de l'ORM dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Renforcement de la protection des applications par l'ajout d'en-têtes de sécurité dans [crm-asn](/repos/betagouv-experimentations/crm-asn).
- Implémentation d'une authentification basée sur l'appartenance à une organisation GitHub pour sécuriser l'accès aux logs dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy).

## Autres changements notables
- **Automatisation de l'infrastructure** : Déploiement massif et configuration de workflows CI/CD via Coolify sur l'ensemble des nouveaux dépôts ([test-jb4](/repos/betagouv-experimentations/test-jb4), [test-jb2](/repos/betagouv-experimentations/test-jb2), [test-jb1](/repos/betagouv-experimentations/test-jb1), [test-benoit](/repos/betagouv-experimentations/test-benoit), [simulation-doctorat](/repos/betagouv-experimentations/simulation-doctorat), [eval-metier-rag](/repos/betagouv-experimentations/eval-metier-rag), [26052026](/repos/betagouv-experimentations/26052026)).
- **Optimisation du template de prototypage** : Dans [template-proto](/repos/betagouv-experimentations/template-proto), ajout de l'auto-provisionnement de l'infrastructure, de l'automatisation des migrations de base de données et de l'intégration de capacités d'IA (Claude skills).
- **Observabilité** : Développement d'un proxy dédié à la récupération, l'analyse et la gestion des logs d'exécution dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'un outil de suivi des accompagnements et gestion des contacts.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Création d'un service de proxy pour la gestion sécurisée des logs.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Évolution du template de base incluant l'IA et l'automatisation infra.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Mise en place d'une application CRUD complète avec persistance de données.
- [test-jb3](/repos/betagouv-experimentations/test-jb3) : Maintenance de sécurité et ajustements de l'interface utilisateur.
