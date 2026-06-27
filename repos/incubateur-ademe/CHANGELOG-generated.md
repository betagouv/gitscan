# Synthèse d'activité : incubateur-ademe (du 16 mai 2026 au 16 juin 2026)

## Résumé de l'activité
L'activité récente de l'incubateur-ademe s'est concentrée sur l'amélioration et la maintenance de ses outils et plateformes existants. Plusieurs dépôts ont bénéficié de mises à jour de sécurité, de corrections de bugs et d'optimisations de performance. Des efforts significatifs ont été déployés pour améliorer l'expérience utilisateur, notamment avec l'ajout de nouvelles fonctionnalités et l'amélioration de l'accessibilité. On note également des migrations vers de nouvelles versions de technologies clés, comme la mise à niveau de Rust dans [vaultwarden](/repos/incubateur-ademe/vaultwarden) et de Node.js dans [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions). L'intégration de nouveaux services et l'amélioration de l'interopérabilité entre les outils sont également des thèmes récurrents, comme l'intégration de PostHog dans [nosgestesclimat-site-nextjs](/repos/incubateur-ademe/nosgestesclimat-site-nextjs) et l'authentification FGP dans [grafana](/repos/incubateur-ademe/grafana).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Correction de vulnérabilités d'open redirect dans [dashlord](/repos/incubateur-ademe/dashlord).
- Amélioration de la sécurité en bloquant des potentielles injections SQL et des IDOR dans [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions).
- Ajout d'un scan de secrets avec Talisman dans [benefriches](/repos/incubateur-ademe/benefriches).
- Ajout d'un throttleur pour la sécurité de l'API dans [benefriches](/repos/incubateur-ademe/benefriches).

## Autres changements notables
- Migration vers Airflow v3 dans [quefairedemesobjets](/repos/incubateur-ademe/quefairedemesobjets) pour une meilleure gestion des données.
- Refonte de l'interface utilisateur de [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) et de [bandit-manchot](/repos/incubateur-ademe/bandit-manchot).
- Migration complète vers TypeScript dans [dsfr-override](/repos/incubateur-ademe/dsfr-override) pour une meilleure maintenabilité.
- Mise à niveau de n8n vers la version 2 dans [n8n-scalingo](/repos/incubateur-ademe/n8n-scalingo).
- Refonte de l'authentification et de l'architecture dans [tacct-legacy-nextjs](/repos/incubateur-ademe/tacct-legacy-nextjs).

## Dépôts les plus actifs
- [territoires-en-transitions](/repos/incubateur-ademe/territoires-en-transitions) : Améliorations significatives de la gestion des audits de labellisation, de l'import de plans d'action et refactorisation technique.
- [plusfraichemaville-site](/repos/incubateur-ademe/plusfraichemaville-site) : Ajout d'une page sur les risques pour la santé liés aux îlots de chaleur urbains et amélioration de la gestion des aides financières.
- [nosgestesclimat-site-nextjs](/repos/incubateur-ademe/nosgestesclimat-site-nextjs) : Amélioration de l'expérience utilisateur avec l'ajout d'un bloc d'actions concrètes et de nouvelles fonctionnalités.
- [benefriches](/repos/incubateur-ademe/benefriches) : Ajout de la documentation sur les impacts évités et refonte de l'onglet de comparaison des impacts.
- [quefairedemesobjets](/repos/incubateur-ademe/quefairedemesobjets) : Amélioration de la robustesse et de la gestion des données avec la migration vers Airflow v3.
