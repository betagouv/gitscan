# Synthèse d'activité : agora-gouv (du 26 juin au 10 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation agora-gouv s'est concentrée sur l'amélioration de la plateforme, tant sur le plan fonctionnel qu'en termes de performance et de sécurité. Des efforts importants ont été déployés pour migrer vers des versions plus récentes de technologies clés comme Strapi V5, et pour optimiser la gestion du cache et des performances globales. L'expérience utilisateur a également été améliorée, notamment sur l'application mobile et le site web, avec des corrections de bugs, des ajustements de design et l'ajout de nouvelles fonctionnalités comme l'identification de l'auteur des réponses.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations en matière de sécurité :
- Ajout de certificats Sectigo pour la validation de domaine dans [agora-front](/repos/agora-gouv/agora-front) et [agora-app](/repos/agora-gouv/agora-app).
- Automatisation du renouvellement des certificats SSL via ACME dans [agora-back](/repos/agora-gouv/agora-back).

## Autres changements notables
- Migration de la plateforme Strapi vers la version 5 dans [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) et adaptation de [agora-back](/repos/agora-gouv/agora-back).
- Amélioration significative de la gestion du cache dans [agora-back](/repos/agora-gouv/agora-back), avec des ajustements pour le cache de cluster de mots et les thèmes hebdomadaires.
- Refonte de l'algorithme de calcul des tendances dans [agora-back](/repos/agora-gouv/agora-back) avec l'introduction d'une nouvelle formule (V3 et V4).

## Dépôts les plus actifs
- [agora-back](/repos/agora-gouv/agora-back) : Amélioration de la gestion du cache, migration vers Strapi V5 et ajout de nouvelles fonctionnalités d'administration.
- [agora-front](/repos/agora-gouv/agora-front) : Corrections de bugs et améliorations de l'interface utilisateur, notamment au niveau des liens profonds et de l'affichage.
- [agora-app](/repos/agora-gouv/agora-app) : Corrections de bugs liés au partage de contenu, aux liens profonds et à l'alignement avec le Design System FR.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Migration vers Strapi V5 et ajout de nouvelles fonctionnalités comme l'identification de l'auteur des réponses et les clusters de mots pour la semaine libre.
