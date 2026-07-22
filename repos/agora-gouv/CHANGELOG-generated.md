# Synthèse d'activité : agora-gouv (du 02/07 au 16/07)

## Résumé de l'activité
L'activité récente de l'organisation agora-gouv s'est concentrée sur l'amélioration de la plateforme, tant sur le front-end que sur le back-end et l'application mobile. Des efforts importants ont été déployés pour optimiser l'expérience utilisateur, notamment en corrigeant des bugs liés au partage de contenu, aux liens profonds et à l'affichage. La migration vers Strapi V5 dans [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) représente une évolution technique majeure, visant à améliorer la stabilité et les performances du CMS. L'automatisation de la gestion des certificats via ACME dans [agora-back](/repos/agora-gouv/agora-back) renforce la sécurité de la plateforme.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de sécurité :
- Ajout de certificats Sectigo dans [agora-app](/repos/agora-gouv/agora-app) pour améliorer la sécurité et la compatibilité.
- Implémentation de l'automatisation Sectigo via ACME pour la gestion des certificats dans [agora-back](/repos/agora-gouv/agora-back).

## Autres changements notables
- Migration de la plateforme [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) vers Strapi V5, une mise à jour majeure de la plateforme CMS.
- Refonte de l'algorithme de calcul des tendances dans [agora-back](/repos/agora-gouv/agora-back) (V3 et V4).
- Simplification du flush du cache Redis dans [agora-back](/repos/agora-gouv/agora-back) pour une suppression plus fiable des données.

## Dépôts les plus actifs
- [agora-front](/repos/agora-gouv/agora-front) : Amélioration de l'interface utilisateur, corrections de bugs d'affichage et de liens profonds.
- [agora-back](/repos/agora-gouv/agora-back) : Amélioration de la gestion des consultations, optimisation des performances et ajout de fonctionnalités d'administration.
- [agora-app](/repos/agora-gouv/agora-app) : Corrections de bugs liés au partage de contenu, aux liens profonds et à l'alignement avec le Design System FR.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Migration vers Strapi V5 et ajout de nouvelles fonctionnalités pour la gestion du contenu.
