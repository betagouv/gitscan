# Synthèse d'activité : betagouv-experimentations (du 13 mai au 26 mai 2026)

## Résumé de l'activité
L'organisation betagouv-experimentations a connu une période d'activité intense, marquée par le lancement de nombreux nouveaux prototypes et l'avancement de projets existants. Plusieurs dépôts ont été initialisés, configurés avec Coolify et le Design System Français (DSFR), témoignant d'une volonté de standardiser et d'accélérer le développement d'applications web pour l'administration.  Un focus particulier a été mis sur l'intégration d'IA, notamment avec Claude Code, et sur la sécurisation des applications, comme illustré par les corrections de vulnérabilités dans [test-jb3](/repos/betagouv-experimentations/test-jb3). L'application de suivi des contacts pour l'équipe ASN de la DINUM ([test-cadrer-20260521](/repos/betagouv-experimentations/test-cadrer-20260521) et [crm-asn](/repos/betagouv-experimentations/crm-asn)) représente une avancée concrète en termes de fonctionnalités.

## Sécurité
- Correction d'une vulnérabilité SQL injection de haute sévérité dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Ajout d'en-têtes de sécurité pour renforcer la protection de l'application [crm-asn](/repos/betagouv-experimentations/crm-asn).

## Autres changements notables
- Intégration de l'auto-provisionnement Coolify dans [template-proto](/repos/betagouv-experimentations/template-proto) pour simplifier le déploiement.
- Refonte de la configuration de l'environnement de développement et amélioration de la capture de l'URL de la base de données Coolify dans [template-proto](/repos/betagouv-experimentations/template-proto).
- Développement d'un proxy pour les logs Coolify ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)) avec authentification GitHub et gestion des erreurs.

## Dépôts les plus actifs
- [test-cadrer-20260521](/repos/betagouv-experimentations/test-cadrer-20260521) : Création d'une application de suivi des contacts pour l'équipe ASN de la DINUM.
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement initial du CRM-ASN, incluant la création de contacts et l'ajout de fonctionnalités de sécurité.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Préparation à l'utilisation des compétences d'IA d'Etalab et amélioration de la configuration.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Développement d'un proxy pour les logs Coolify avec authentification et gestion des erreurs.
- [test-jb3](/repos/betagouv-experimentations/test-jb3) : Correction d'une vulnérabilité de sécurité et améliorations de la documentation.
