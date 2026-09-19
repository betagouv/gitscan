# Synthèse d'activité : agora-gouv (du 02/07 au 27/08/2026)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de l'expérience utilisateur et la consolidation de l'infrastructure technique. Les utilisateurs bénéficieront d'une interface plus claire, de fonctionnalités de partage enrichies sur mobile et d'une meilleure visibilité sur l'origine des contributions. 

Parallèlement, des outils de modération plus précis et une automatisation de la gestion des certificats de sécurité renforcent la fiabilité et la capacité de pilotage de la plateforme. Ces évolutions visent à rendre l'engagement citoyen plus fluide tout en garantissant une stabilité accrue du système.

## Sécurité
- Automatisation de la gestion des certificats SSL via le protocole ACME (Sectigo) pour garantir la continuité et la sécurité des connexions ([agora-back](/repos/agora-gouv/agora-back), [agora-app](/repos/agora-gouv/agora-app)).
- Simplification et sécurisation de la gestion des certificats au niveau de l'infrastructure web ([agora-front](/repos/agora-gouv/agora-front)).

## Autres changements notables
- Migration majeure du système de gestion de contenu vers Strapi V5 ([agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi)).
- Refonte de l'algorithme de calcul des tendances pour optimiser la mise en avant des sujets ([agora-back](/repos/agora-gouv/agora-back)).
- Optimisations de performance et de stabilité, incluant des ajustements de la mémoire Node.js, de la configuration des serveurs Nginx et de la gestion du cache Redis ([agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi), [agora-back](/repos/agora-gouv/agora-back)).
- Mise en conformité de l'interface mobile avec le Design System de l'État (DSFR) ([agora-app](/repos/agora-gouv/agora-app)).

## Dépôts les plus actifs
- [agora-back](/repos/agora-gouv/agora-back) : Développement intensif de nouvelles fonctionnalités métier, d'outils d'administration et de la logique algorithmique.
- [agora-app](/repos/agora-gouv/agora-app) : Amélioration de l'expérience utilisateur mobile, de la navigation et de la conformité visuelle.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Travaux de fond sur la migration technologique et l'optimisation des performances du CMS.
