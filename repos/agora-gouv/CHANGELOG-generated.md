# Synthèse d'activité : agora-gouv (du 20/08 au 27/08/2026)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de l'expérience utilisateur et la consolidation de l'infrastructure technique. Les évolutions majeures concernent l'optimisation des fonctionnalités de partage et de modération, ainsi que l'amélioration de la visibilité des contenus (affichage des auteurs, clusters de mots) pour enrichir l'interaction des citoyens sur [agora-back](/repos/agora-gouv/agora-back) et [agora-app](/repos/agora-gouv/agora-app).

Parallèlement, un effort important a été déployé pour automatiser et sécuriser la gestion des certificats SSL à travers l'ensemble de l'écosystème, garantissant une meilleure stabilité du service. Ces travaux renforcent la fiabilité de la plateforme pour les utilisateurs finaux tout en simplifiant la maintenance technique pour les équipes.

## Sécurité
- Automatisation de la gestion des certificats via le protocole ACME (Sectigo) pour sécuriser les échanges sur [agora-back](/repos/agora-gouv/agora-back) et [agora-app](/repos/agora-gouv/agora-app).
- Simplification et sécurisation de la gestion des certificats SSL au sein de [agora-front](/repos/agora-gouv/agora-front).

## Autres changements notables
- Migration majeure de la plateforme de gestion de contenu vers Strapi V5 dans [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi).
- Refonte de l'algorithme de calcul des tendances (V3 et V4) dans [agora-back](/repos/agora-gouv/agora-back) pour une meilleure pertinence des données.
- Optimisations de performance et de gestion de la mémoire sur [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) et [agora-back](/repos/agora-gouv/agora-back).

## Dépôts les plus actifs
- [agora-back](/repos/agora-gouv/agora-back) : Développement intensif de nouvelles fonctionnalités d'administration, de modération et d'optimisation algorithmique.
- [agora-app](/repos/agora-gouv/agora-app) : Amélioration de l'expérience mobile, du partage de contenu et de la conformité au Design System FR.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Migration vers une nouvelle version majeure et optimisations de l'infrastructure de contenu.
