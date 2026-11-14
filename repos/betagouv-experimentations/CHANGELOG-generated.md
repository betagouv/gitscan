# Synthèse d'activité : betagouv-experimentations (du 15/05 au 22/05/2026)

## Résumé de l'activité
L'activité de l'organisation est marquée par une phase intense d'initialisation de nouveaux prototypes, visant à standardiser la création de services web administratifs. La majorité des nouveaux projets adoptent une stack technologique commune (Next.js, DSFR, PostgreSQL) et s'appuient sur une infrastructure automatisée via Coolify pour accélérer le déploiement.

Parallèlement, des outils spécifiques progressent, notamment un outil de gestion de contacts pour l'équipe ASN ([crm-asn](/repos/betagouv-experimentations/crm-asn)) et des améliorations sur la gestion des logs et de l'infrastructure ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)).

## Sécurité
- Correction d'une vulnérabilité d'injection SQL critique dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Renforcement de la sécurité applicative avec l'ajout d'en-têtes de protection dans [crm-asn](/repos/betagouv-experimentations/crm-asn).
- Implémentation d'une authentification basée sur l'appartenance à une organisation GitHub dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy).

## Autres changements notables
- **Automatisation de l'infrastructure** : Mise en place de l'auto-provisionnement de Coolify et de l'automatisation des migrations de base de données dans [template-proto](/repos/betagouv-experimentations/template-proto).
- **Intégration de l'IA** : Optimisation de l'usage des capacités de Claude pour le prototypage et le cadrage dans [template-proto](/repos/betagouv-experimentations/template-proto) et [repo-test](/repos/betagouv-experimentations/repo-test).
- **Observabilité** : Amélioration de la récupération des logs et de la gestion des erreurs dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement des fonctionnalités de suivi de contacts et de gestion d'interactions.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Évolutions sur l'automatisation du déploiement et l'intégration de l'IA.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Amélioration de la robustesse du proxy de logs et de l'authentification.
- [test-jb3](/repos/betagouv-experimentations/test-jb3) : Maintenance de sécurité et ajustements de l'interface utilisateur.
