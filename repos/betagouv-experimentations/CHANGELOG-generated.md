# Synthèse d'activité : betagouv-experimentations (du 15/05 au 22/05)

## Résumé de l'activité
L'organisation connaît une phase intense de lancement de prototypes, visant à accélérer la création de services web administratifs. L'utilisation de l'IA et du Design System Français (DSFR) est au cœur de ces expérimentations, tandis que l'infrastructure de déploiement est largement automatisée via Coolify pour permettre une mise en production rapide.

Des outils spécifiques voient également leurs fonctionnalités s'étoffer, notamment un outil de suivi des contacts pour l'équipe ASN ([crm-asn](/repos/betagouv-experimentations/crm-asn)) et un proxy dédié à la gestion des logs ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)).

## Sécurité
- Correction d'une vulnérabilité d'injection SQL critique via la mise à jour de l'ORM dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Renforcement de la protection des applications par l'ajout d'en-têtes de sécurité dans [crm-asn](/repos/betagouv-experimentations/crm-asn).
- Sécurisation de l'accès au proxy de logs via une authentification basée sur l'appartenance à une organisation GitHub dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy).

## Autres changements notables
- **Automatisation de l'infrastructure** : Généralisation de l'usage de Coolify pour le provisionnement et le déploiement continu sur la quasi-totalité des nouveaux projets ([test-jb4](/repos/betagouv-experimentations/test-jb4), [test-jb2](/repos/betagouv-experimentations/test-jb2), [simulation-doctorat](/repos/betagouv-experimentations/simulation-doctorat)).
- **Optimisation de l'IA et des workflows** : Amélioration de l'usage des capacités d'IA (Claude) et automatisation des migrations de base de données dans [template-proto](/repos/betagouv-experimentations/template-proto).
- **Amélioration de l'observabilité** : Développement de fonctionnalités de récupération de logs d'exécution et de prise en charge des logs structurés dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'un outil de suivi des interactions et des contacts.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Création d'un outil de gestion et de récupération des logs de déploiement.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Évolution du template de prototypage avec intégration d'IA et d'automatisation.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Implémentation d'une application de gestion de tâches complète avec persistance de données.
