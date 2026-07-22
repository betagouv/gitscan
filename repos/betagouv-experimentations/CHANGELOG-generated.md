# Synthèse d'activité : betagouv-experimentations (du 13 mai au 26 mai 2026)

## Résumé de l'activité
L'organisation a connu une période d'intense activité de lancement de nouveaux prototypes. Plusieurs projets ont été initialisés, bénéficiant d'une configuration rapide grâce à Coolify et à des workflows CI/CD automatisés.  On observe une forte tendance à l'utilisation de technologies modernes comme Next.js, React, TypeScript, PostgreSQL, et le Design System Français (DSFR).  Plusieurs projets se concentrent sur la création d'outils internes pour améliorer l'efficacité des équipes de la DINUM, notamment un CRM pour l'équipe ASN et des applications de suivi de contacts. Une attention particulière est portée à la sécurité, avec la correction d'une vulnérabilité SQL injection dans [test-jb3](/repos/betagouv-experimentations/test-jb3).

## Sécurité
- Correction d'une vulnérabilité SQL injection de haute sévérité dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Ajout d'en-têtes de sécurité pour renforcer la protection de l'application [crm-asn](/repos/betagouv-experimentations/crm-asn).

## Autres changements notables
- Intégration de l'auto-provisionnement de Coolify dans [template-proto](/repos/betagouv-experimentations/template-proto) pour simplifier le déploiement.
- Développement d'un proxy de logs Coolify [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) avec authentification et intégration GitHub.
- Renommage du projet [test-cadrer-20260521](/repos/betagouv-experimentations/test-cadrer-20260521) en [crm-asn](/repos/betagouv-experimentations/crm-asn).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'un CRM pour l'équipe ASN de la DINUM, incluant la gestion des contacts et des headers de sécurité.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Développement d'un proxy pour les logs Coolify avec authentification et intégration GitHub.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Préparation à l'intégration de compétences d'IA et amélioration de la configuration.
- [test-jb3](/repos/betagouv-experimentations/test-jb3) : Correction d'une vulnérabilité de sécurité et améliorations de la documentation.
- [repo-test](/repos/betagouv-experimentations/repo-test) : Ajout d'une application de liste de tâches complète avec CRUD et persistance des données.
