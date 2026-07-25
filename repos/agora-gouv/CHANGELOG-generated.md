# Synthèse d'activité : agora-gouv (du 24/06 au 24/07)

## Résumé de l'activité
L'activité récente de l'organisation agora-gouv s'est concentrée sur l'amélioration de la plateforme, tant sur le front-end que sur le back-end et l'application mobile. Des efforts significatifs ont été déployés pour optimiser les performances et la stabilité, notamment avec la migration de [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) vers Strapi V5 et l'automatisation de la gestion des certificats via ACME dans [agora-back](/repos/agora-gouv/agora-back). L'expérience utilisateur a également été améliorée grâce à des corrections et des ajustements sur [agora-front](/repos/agora-gouv/agora-front) et [agora-app](/repos/agora-gouv/agora-app), notamment au niveau du partage de contenu et des liens profonds.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de la sécurité :
- Ajout de certificats Sectigo pour améliorer la sécurité dans [agora-app](/repos/agora-gouv/agora-app).
- Implémentation de l'automatisation Sectigo via ACME pour la gestion des certificats dans [agora-back](/repos/agora-gouv/agora-back).
- Correction des certificats SHA256 et des fingerprints dans [agora-front](/repos/agora-gouv/agora-front).

## Autres changements notables
- Migration de [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) vers Strapi V5, une mise à jour majeure de la plateforme.
- Refonte de l'algorithme de calcul des tendances (V3 et V4) dans [agora-back](/repos/agora-gouv/agora-back).
- Simplification du flush du cache Redis dans [agora-back](/repos/agora-gouv/agora-back) pour une meilleure gestion du cache.

## Dépôts les plus actifs
- [agora-back](/repos/agora-gouv/agora-back) : Amélioration de la gestion des consultations, de la sélection des questions et des fonctionnalités d'administration.
- [agora-front](/repos/agora-gouv/agora-front) : Ajustements de design, corrections de bugs et amélioration de l'expérience utilisateur.
- [agora-app](/repos/agora-gouv/agora-app) : Corrections de bugs liés au partage de contenu, aux liens profonds et à l'affichage, ainsi qu'alignement avec le Design System FR.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Migration vers Strapi V5 et ajout de nouvelles fonctionnalités pour la gestion du contenu.
