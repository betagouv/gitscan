# Synthèse d'activité : agora-gouv (du 01/07 au 28/07)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de l'expérience utilisateur et l'enrichissement des outils d'analyse et de modération. Les utilisateurs bénéficieront d'une navigation plus fluide sur mobile et web ([agora-front](/repos/agora-gouv/agora-front), [agora-app](/repos/agora-gouv/agora-app)), ainsi que de nouvelles capacités d'analyse de données, comme les clusters de mots pour les thématiques hebdomadaires ([agora-back](/repos/agora-gouv/agora-back), [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi)).

Parallèlement, des avancées significatives ont été réalisées pour renforcer la robustesse de la plateforme, notamment via l'automatisation de la gestion des certificats de sécurité et la modernisation de l'infrastructure de gestion de contenu ([agora-back](/repos/agora-gouv/agora-back), [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi)).

## Sécurité
- Automatisation de la gestion des certificats via le protocole ACME avec Sectigo ([agora-back](/repos/agora-gouv/agora-back), [agora-app](/repos/agora-gouv/agora-app)).
- Renforcement de la sécurité des liens profonds (deeplinks) et de la compatibilité mobile via l'utilisation de SHA256 et la mise à jour des configurations de certificats ([agora-front](/repos/agora-gouv/agora-front), [agora-app](/repos/agora-gouv/agora-app)).

## Autres changements notables
- Migration majeure de la plateforme de gestion de contenu vers Strapi V5 ([agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi)).
- Optimisation des performances serveurs (Nginx, mémoire Node.js) et simplification de la gestion du cache Redis ([agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi), [agora-back](/repos/agora-gouv/agora-back)).
- Refonte complète de l'algorithme de calcul des tendances ([agora-back](/repos/agora-gouv/agora-back)).

## Dépôts les plus actifs
- [agora-back](/repos/agora-gouv/agora-back) : Développement intensif de nouvelles fonctionnalités API, d'outils d'administration et de l'automatisation de la sécurité.
- [agora-app](/repos/agora-gouv/agora-app) : Amélioration de l'expérience utilisateur mobile, de la gestion des partages et de la conformité au Design System FR.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Migration technologique majeure et optimisation des performances de l'infrastructure.
- [agora-front](/repos/agora-gouv/agora-front) : Stabilisation de l'interface web et optimisation de la navigation mobile.
