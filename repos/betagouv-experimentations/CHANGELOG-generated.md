# Synthèse d'activité : betagouv-experimentations (du 15/05 au 22/05)

## Résumé de l'activité
L'activité de l'organisation est marquée par une forte dynamique de prototypage, avec le lancement de nombreux nouveaux services visant à standardiser la création d'applications web pour l'administration ([test-jb4](/repos/betagouv-experimentations/test-jb4), [test-jb2](/repos/betagouv-experimentations/test-jb2), [test-benoit](/repos/betagouv-experimentations/test-benoit), [simulation-doctorat](/repos/betagouv-experimentations/simulation-doctorat)). Ces projets s'appuient sur un socle technologique récurrent (Next.js, PostgreSQL, DSFR) et une infrastructure de déploiement automatisée via Coolify.

Parallèlement, l'organisation fait progresser des outils opérationnels et d'infrastructure, notamment avec le développement d'un outil de suivi de contacts pour l'équipe ASN ([crm-asn](/repos/betagouv-experimentations/crm-asn)) et l'amélioration des capacités de monitoring et de gestion des logs ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)).

## Sécurité
- Correction d'une vulnérabilité d'injection SQL de haute sévérité via la mise à jour de l'ORM dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Renforcement de la protection des applications par l'ajout d'en-têtes de sécurité dans [crm-asn](/repos/betagouv-experimentations/crm-asn).
- Amélioration de l'authentification des accès via l'appartenance à une organisation GitHub dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy).

## Autres changements notables
- **Automatisation de l'infrastructure** : Mise en place de l'auto-provisionnement de Coolify et de l'automatisation des migrations de base de données dans [template-proto](/repos/betagouv-experimentations/template-proto).
- **Intégration de l'IA** : Intégration de capacités d'intelligence artificielle (skills Claude) dans les workflows de build et de configuration pour [template-proto](/repos/betagouv-experimentations/template-proto) et [repo-test](/repos/betagouv-experimentations/repo-test).
- **Évolution du monitoring** : Amélioration du proxy de logs pour supporter l'analyse de logs structurés et la gestion automatique du nettoyage des ressources via des webhooks GitHub ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement des fonctionnalités de suivi de contacts et sécurisation de l'application.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Ajout de fonctionnalités de monitoring, d'authentification et de gestion de webhooks.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Automatisation du déploiement et intégration de capacités d'IA.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Implémentation d'une application de gestion de tâches complète avec persistance de données.
- [test-jb3](/repos/betagouv-experimentations/test-jb3) : Mise à jour de sécurité critique et ajustements de l'interface utilisateur.
