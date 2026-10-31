# Synthèse d'activité : agora-gouv (du 02/07 au 23/09)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de l'expérience utilisateur et la stabilisation des infrastructures. Les évolutions majeures incluent une meilleure fluidité du partage de contenu sur mobile [agora-app](/repos/agora-gouv/agora-app), une interface plus intuitive [agora-front](/repos/agora-gouv/agora-front) et des outils d'administration renforcés pour la gestion des contenus et des questions [agora-back](/repos/agora-gouv/agora-back) et [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi).

Ces changements visent à rendre la plateforme plus robuste, plus facile à modérer et plus conforme aux standards de design officiels, tout en optimisant la gestion technique des certificats de sécurité.

## Sécurité
- Sécurisation de l'accès à l'instance Metabase via un filtrage par adresse IP [agora-metabase-scalingo](/repos/agora-gouv/agora-metabase-scalingo).
- Automatisation et amélioration de la gestion des certificats SSL (via ACME et Sectigo) pour garantir la continuité de service [agora-front](/repos/agora-gouv/agora-front), [agora-back](/repos/agora-gouv/agora-back) et [agora-app](/repos/agora-gouv/agora-app).

## Autres changements notables
- Migration majeure de la plateforme de gestion de contenu vers Strapi V5 [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi).
- Refonte technique de l'algorithme de calcul des tendances [agora-back](/repos/agora-gouv/agora-back).
- Optimisations d'infrastructure et de performance, notamment sur la gestion de la mémoire Node.js, la configuration Nginx et le cache Redis [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) et [agora-back](/repos/agora-gouv/agora-back).
- Alignement de l'interface de l'application mobile avec le Design System Français (DSFR) [agora-app](/repos/agora-gouv/agora-app).

## Dépôts les plus actifs
- [agora-back](/repos/agora-gouv/agora-back) : Évolutions majeures sur les fonctionnalités d'administration, l'API et les algorithmes de tendances.
- [agora-app](/repos/agora-gouv/agora-app) : Améliorations de l'expérience utilisateur mobile et de la conformité visuelle.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Travaux de migration de version majeure et d'optimisation des performances serveur.
