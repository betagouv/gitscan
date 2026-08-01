# Synthèse d'activité : betagouv-experimentations (du 13 mai au 26 mai 2026)

## Résumé de l'activité
L'organisation a connu une période d'intense activité de lancement de nouveaux projets et de développement initial. Plusieurs prototypes ont été initialisés, notamment avec l'utilisation de Coolify pour le déploiement et l'intégration du Design System Français (DSFR).  Un projet, `crm-asn`, a déjà progressé vers une application fonctionnelle de suivi de contacts pour l'équipe ASN de la DINUM, incluant des améliorations de sécurité.  D'autres projets, comme `coolify-logs-proxy`, ont vu des fonctionnalités importantes ajoutées, améliorant la gestion des logs et l'intégration avec GitHub. L'accent est mis sur la création rapide de services web pour l'administration, souvent en s'appuyant sur l'IA et des outils modernes.

## Sécurité
- Correction d'une vulnérabilité SQL injection de haute sévérité dans [test-jb3](/repos/betagouv-experimentations/test-jb3).
- Ajout d'headers de sécurité pour renforcer la protection de l'application dans [crm-asn](/repos/betagouv-experimentations/crm-asn).

## Autres changements notables
- Intégration de l'auto-provisionnement Coolify dans [template-proto](/repos/betagouv-experimentations/template-proto) pour simplifier le déploiement.
- Refonte de la configuration de l'environnement de développement et passage à un fichier `package-lock.json` pour des builds reproductibles dans [template-proto](/repos/betagouv-experimentations/template-proto).
- Développement d'un proxy pour les logs Coolify avec authentification via GitHub dans [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy).

## Dépôts les plus actifs
- [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'une application de suivi des contacts pour l'équipe ASN, avec ajout de fonctionnalités et d'améliorations de sécurité.
- [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Ajout de fonctionnalités pour la récupération des logs Coolify et l'intégration avec GitHub.
- [template-proto](/repos/betagouv-experimentations/template-proto) : Préparation à l'utilisation des skills d'IA d'Etalab et amélioration de la configuration du projet.
- [test-jb2](/repos/betagouv-experimentations/test-jb2) : Initialisation d'un prototype avec Next.js, React, TypeScript, PostgreSQL, Drizzle ORM, Zod et @codegouvfr/react-dsfr.
- [test-jb3](/repos/betagouv-experimentations/test-jb3) : Correction d'une vulnérabilité de sécurité et amélioration de la documentation.
