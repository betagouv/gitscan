# Synthèse d'activité : agora-gouv (du 26 juin au 10 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation agora-gouv s'est concentrée sur l'amélioration de la plateforme, tant sur le plan fonctionnel qu'en termes de performance et de sécurité. Des efforts importants ont été déployés pour moderniser l'infrastructure avec la migration vers Strapi V5 ([agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi)) et automatiser la gestion des certificats SSL ([agora-back](/repos/agora-gouv/agora-back)). L'expérience utilisateur a également été améliorée, notamment au niveau de l'application mobile ([agora-app](/repos/agora-gouv/agora-app)) et de l'interface web ([agora-front](/repos/agora-gouv/agora-front)), avec des corrections de bugs et des ajustements de design.

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité :
- Ajout de certificats Sectigo pour la validation de domaine ([agora-front](/repos/agora-gouv/agora-front), [agora-app](/repos/agora-gouv/agora-app)).
- Automatisation du renouvellement des certificats SSL via ACME ([agora-back](/repos/agora-gouv/agora-back)).

## Autres changements notables
- Migration de la plateforme CMS vers Strapi V5 ([agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi)).
- Amélioration de la gestion du cache et de l'algorithme de tendances ([agora-back](/repos/agora-gouv/agora-back)).
- Ajustements de la configuration Nginx pour améliorer la stabilité et les performances ([agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi)).

## Dépôts les plus actifs
- [agora-back](/repos/agora-gouv/agora-back) : Amélioration de la gestion du cache, de l'algorithme de tendances et intégration de Strapi V5.
- [agora-front](/repos/agora-gouv/agora-front) : Corrections de bugs d'affichage et d'interaction, ajustements de design et gestion des liens profonds.
- [agora-app](/repos/agora-gouv/agora-app) : Corrections de bugs liés au partage de contenu, aux liens profonds et à l'affichage, alignement avec le Design System FR.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Migration vers Strapi V5 et améliorations de la stabilité et des performances.
