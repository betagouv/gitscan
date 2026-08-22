# Synthèse d'activité : betagouv-experimentations (du 19/05 au 26/05)

## Résumé de l'activité
L'activité de l'organisation est marquée par une phase intense de lancement de nouveaux prototypes. De nombreux projets sont initialisés en utilisant une stack technologique standardisée (Next.js, React, PostgreSQL, Drizzle ORM et le Design System Français) afin de faciliter la création rapide de services web pour l'administration.

Parallèlement, des avancées fonctionnelles significatives ont été réalisées, notamment avec le développement d'un outil de suivi de contacts pour l'équipe ASN ([crm-asn](/repos/betagouv-experimentations/crm-asn)) et l'amélioration des outils de gestion et de récupération des logs de déploiement ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)).

## Sécurité
- Correction d'une vulnérabilité d'injection SQL de haute sévérité via la mise à jour de l'ORM dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Renforcement de la protection des applications par l'ajout d'en-têtes de sécurité dans [crm-asn](/repos/betagouv-experimentations/crm-asn).
- Amélioration de l'authentification dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) via l'intégration de l'appartenance à une organisation GitHub.

## Autres changements notables
- Automatisation poussée de l'infrastructure avec l'intégration de l'auto-provisionnement Coolify, la gestion automatique des migrations de base de données et la mise en place de tests de fumée dans [template-proto](/repos/betagouv-experimentations/template-proto).
- Optimisation de l'intégration des capacités d'intelligence artificielle (via Claude) dans [template-proto](/repos/betagouv-experimentations/template-proto) et [repo-test](/repos/betagouv-experimentations/repo-test).
- Généralisation de l'utilisation de workflows CI/CD pour le déploiement automatisé sur l'ensemble des nouveaux dépôts ([test-jb4](/repos/betagouv-experimentations/test-jb4), [test-jb2](/repos/betagouv-experimentations/test-jb2), [test-benoit](/repos/betagouv-experimentations/test-benoit), etc.).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'un outil de suivi des accompagnements et des contacts pour l'équipe ASN.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Amélioration des fonctionnalités de récupération, d'analyse et de gestion des logs de déploiement.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Optimisation de l'automatisation du déploiement et des capacités d'IA.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Mise en place d'une application complète de gestion de tâches (CRUD).
