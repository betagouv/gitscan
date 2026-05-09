# Synthèse d'activité : incubateur-ademe (du 24 avril 2026 au 07 mai 2026)

## Résumé de l'activité
L'activité de l'incubateur-ademe au cours des dernières semaines a été marquée par des améliorations continues de ses outils et plateformes.  Plusieurs dépôts ont bénéficié de corrections de bugs et d'optimisations de performance, notamment [tacct](/repos/incubateur-ademe/tacct) et [stats-incubateur](/repos/incubateur-ademe/stats-incubateur).  Des fonctionnalités importantes ont été ajoutées à [plusfraisautravail](/repos/incubateur-ademe/plusfraisautravail) avec l'intégration d'alertes et de vigilances, et à [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles) avec l'ajout du mode embarquable et l'authentification à deux facteurs.  Des efforts significatifs ont également été déployés pour améliorer l'infrastructure et la sécurité, avec la migration vers OpenTofu pour [plusfraisautravail](/repos/incubateur-ademe/plusfraisautravail) et l'amélioration de l'authentification avec FGP pour [grafana](/repos/incubateur-ademe/grafana).

## Sécurité
- Mise en place d'une authentification consolidée via FGP (Federated Grafana Proxy) pour [grafana](/repos/incubateur-ademe/grafana).
- Amélioration de la sécurité avec Sentry et PostHog dans [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles).
- Mise à jour des dépendances pour corriger des vulnérabilités de sécurité dans [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site).

## Autres changements notables
- Migration vers OpenTofu pour la gestion de l'infrastructure de [plusfraisautravail](/repos/incubateur-ademe/plusfraisautravail).
- Refonte de l'architecture d'authentification avec SSO OAuth pour les tenants dans [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles).
- Passage à une structure de monorepo pour [nosgestesclimat-app](/repos/incubateur-ademe/nosgestesclimat-app).
- Mise à niveau de n8n vers la version 2 dans [n8n-scalingo](/repos/incubateur-ademe/n8n-scalingo).
- Refactorisation majeure du code client vers une architecture modulaire avec TypeScript dans [fine-grained-proxy](/repos/incubateur-ademe/fine-grained-proxy).

## Dépôts les plus actifs
- [plusfraisautravail](/repos/incubateur-ademe/plusfraisautravail) : Amélioration significative de l'application avec l'ajout d'alertes, de vigilances et une refonte de l'infrastructure.
- [roadmaps-faciles](/repos/incubateur-ademe/roadmaps-faciles) : Ajout de nombreuses nouvelles fonctionnalités, notamment le mode embarquable, l'authentification 2FA et la synchronisation avec Notion.
- [nosgestesclimat-site-nextjs](/repos/incubateur-ademe/nosgestesclimat-site-nextjs) : Amélioration de l'interface utilisateur et ajout de nouvelles fonctionnalités pour le suivi des actions et des résultats.
- [benefriches](/repos/incubateur-ademe/benefriches) : Ajout de visualisations et d'analyses pour les projets urbains, améliorant la compréhension de l'impact des friches.
- [tacct](/repos/incubateur-ademe/tacct) : Corrections de bugs et mises à jour des données pour une meilleure fiabilité et pertinence.
