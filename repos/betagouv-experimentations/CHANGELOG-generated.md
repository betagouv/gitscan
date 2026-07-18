# Synthèse d'activité : betagouv-experimentations (du 13 mai au 22 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur le lancement de nombreux nouveaux prototypes, avec une forte utilisation de Coolify pour la configuration et le déploiement. Plusieurs projets ont progressé dans la création d'applications web pour l'administration, notamment un CRM pour l'équipe ASN de la DINUM ([crm-asn](/repos/betagouv-experimentations/crm-asn)), une application de liste de tâches ([repo-test](/repos/betagouv-experimentations/repo-test)) et des prototypes visant à simplifier la création d'applications avec des outils modernes comme React, Next.js et PostgreSQL ([test-jb1](/repos/betagouv-experimentations/test-jb1), [test-jb2](/repos/betagouv-experimentations/test-jb2), [test-jb4](/repos/betagouv-experimentations/test-jb4)).  L'accent est mis sur l'utilisation du Design System Français (DSFR) et l'exploration de l'IA pour faciliter le développement.

## Sécurité
Une correction de vulnérabilité SQL injection a été appliquée dans [test-jb3](/repos/betagouv-experimentations/test-jb3) en mettant à jour les librairies `drizzle-orm` et `drizzle-kit`.  Des headers de sécurité ont également été ajoutés à [crm-asn](/repos/betagouv-experimentations/crm-asn) pour renforcer la protection de l'application.

## Autres changements notables
Le proxy de logs Coolify ([coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy)) a bénéficié d'améliorations significatives, notamment l'ajout d'un endpoint pour la récupération des logs, l'intégration avec GitHub via un webhook et une meilleure gestion des erreurs. Le projet [template-proto](/repos/betagouv-experimentations/template-proto) a intégré l'auto-provisionnement Coolify et se prépare à l'utilisation des compétences d'IA d'Etalab.

## Dépôts les plus actifs
*   [crm-asn](/repos/betagouv-experimentations/crm-asn) : Développement d'une application de suivi des contacts pour l'équipe ASN de la DINUM, avec des fonctionnalités de base et des améliorations de sécurité.
*   [test-jb1](/repos/betagouv-experimentations/test-jb1) : Initialisation d'un prototype visant à simplifier la création d'applications web.
*   [test-jb2](/repos/betagouv-experimentations/test-jb2) : Lancement initial d'un prototype utilisant Claude Code et le DSFR.
*   [repo-test](/repos/betagouv-experimentations/repo-test) : Développement d'une application de liste de tâches avec des fonctionnalités CRUD et persistance des données.
*   [coolify-logs-proxy](/repos/betagouv-experimentations/coolify-logs-proxy) : Amélioration du proxy de logs Coolify avec de nouvelles fonctionnalités et une meilleure gestion des erreurs.
