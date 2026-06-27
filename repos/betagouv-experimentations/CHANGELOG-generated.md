# Synthèse d'activité : betagouv-experimentations (du 13 mai au 22 mai 2026)

## Résumé de l'activité
La période a été marquée par une forte activité de lancement de nouveaux prototypes, avec une majorité de dépôts initialisés et configurés avec Coolify. Plusieurs projets ont progressé vers des premières versions fonctionnelles, notamment [crm-asn](/repos/betagouv-experimentations/crm-asn) et [repo-test](/repos/betagouv-experimentations/repo-test), qui proposent déjà des applications concrètes de suivi de contacts et de gestion de tâches.  L'accent est mis sur l'utilisation d'outils modernes comme Next.js, React, TypeScript, PostgreSQL et le Design System Français, ainsi que sur l'intégration de l'IA via Claude Code.

## Sécurité
Une correction de vulnérabilité SQL injection a été appliquée dans [test-jb3](/repos/betagouv-experimentations/test-jb3), renforçant la sécurité de l'application. De plus, [crm-asn](/repos/betagouv-experimentations/crm-asn) a bénéficié de l'ajout d'headers de sécurité pour une meilleure protection.

## Autres changements notables
Le projet [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) a connu des avancées significatives avec l'ajout de fonctionnalités pour la récupération des logs, l'authentification via GitHub et l'intégration avec les webhooks GitHub.  [template-proto](/repos/betagouv-experimentations/template-proto) a intégré l'auto-provisionnement Coolify et prépare l'intégration des compétences d'IA d'Etalab.

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'une application de suivi des contacts pour l'équipe ASN de la DINUM, avec ajout de fonctionnalités et améliorations de sécurité.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Implémentation d'une application de liste de tâches complète avec fonctionnalités CRUD et persistance des données.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Développement d'un proxy pour les logs Coolify avec ajout de fonctionnalités d'authentification et d'intégration avec GitHub.
- [test-jb2](/repos/betagouv-experimentations/test-jb2) et [test-jb4](/repos/betagouv-experimentations/test-jb4) : Initialisation de nouveaux projets prototypes avec configuration de l'environnement et du workflow CI/CD.
