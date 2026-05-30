# Synthèse d'activité : betagouv-experimentations (du 13 mai 2026 au 22 mai 2026)

## Résumé de l'activité
La période a été marquée par une forte activité de lancement de nouveaux projets et de développement initial de prototypes. Plusieurs dépôts ont été initialisés avec une configuration Coolify pour faciliter le déploiement et l'hébergement.  On observe une tendance à l'utilisation de technologies modernes comme Next.js, React, TypeScript, PostgreSQL et le Design System Français (DSFR).  Le projet [test-cadrer-20260521](/repos/betagouv-experimentations/test-cadrer-20260521) et [crm-asn](/repos/betagouv-experimentations/crm-asn) se démarquent par la création d'applications fonctionnelles, notamment un CRM pour l'équipe ASN de la DINUM.  Une attention particulière a été portée à la sécurité, avec une correction de vulnérabilité SQL injection dans [test-jb3](/repos/betagouv-experimentations/test-jb3).

## Sécurité
- Correction d'une vulnérabilité SQL injection de haute sévérité dans [test-jb3](/repos/betagouv-experimentations/test-jb3) via une mise à jour de `drizzle-orm` et `drizzle-kit`.
- Ajout d'en-têtes de sécurité dans [test-cadrer-20260521](/repos/betagouv-experimentations/test-cadrer-20260521) pour renforcer la protection de l'application.

## Autres changements notables
- Intégration de l'auto-provisionnement Coolify dans [template-proto](/repos/betagouv-experimentations/template-proto) pour simplifier le déploiement.
- Refonte de la configuration de l'environnement de développement et amélioration de la capture d'URL de base de données dans [template-proto](/repos/betagouv-experimentations/template-proto).
- Développement d'un proxy de logs Coolify ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)) avec authentification GitHub et gestion des erreurs.

## Dépôts les plus actifs
- [test-cadrer-20260521](/repos/betagouv-experimentations/test-cadrer-20260521) : Développement d'une application de suivi des contacts pour l'équipe ASN, avec ajout de fonctionnalités et amélioration de la sécurité.
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Création d'un CRM pour l'équipe ASN, incluant la gestion des contacts et l'affichage de la date de création.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Amélioration de l'infrastructure et préparation à l'intégration de compétences d'IA.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Développement d'un proxy pour les logs Coolify avec authentification et gestion des erreurs.
