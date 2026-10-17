# Synthèse d'activité : agora-gouv (du 20/08 au 23/09)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de l'expérience utilisateur et la modernisation des infrastructures. Les utilisateurs bénéficieront d'une interface plus intuitive et conforme aux standards de design (DSFR) dans [agora-app](/repos/agora-gouv/agora-app) et [agora-front](/repos/agora-gouv/agora-front), ainsi que de nouvelles fonctionnalités de partage et de visibilité des auteurs de contributions.

Parallèlement, des efforts importants ont été déployés pour renforcer la fiabilité du système, notamment via l'automatisation de la gestion des certificats de sécurité et la migration vers de nouvelles versions technologiques pour le contenu, impactant directement la stabilité de [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) et [agora-back](/repos/agora-gouv/agora-back).

## Sécurité
- Automatisation de la gestion des certificats SSL via le protocole ACME (Sectigo) pour sécuriser les échanges sur [agora-back](/repos/agora-gouv/agora-back) et [agora-app](/repos/agora-gouv/agora-app).
- Simplification et sécurisation de la gestion des certificats SSL au sein de l'application [agora-front](/repos/agora-gouv/agora-front).
- Renforcement de la sécurité de l'accès à l'instance Metabase par l'ajout d'un filtrage par adresse IP via NGINX dans [agora-metabase-scalingo](/repos/agora-gouv/agora-metabase-scalingo).

## Autres changements notables
- Migration majeure de la plateforme de gestion de contenu vers Strapi V5 dans [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi).
- Optimisation des performances et de la stabilité du serveur (mémoire Node.js, configurations Nginx) dans [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi).
- Refonte de l'algorithme de calcul des tendances (versions V3 et V4) dans [agora-back](/repos/agora-gouv/agora-back).
- Amélioration de la gestion du cache Redis et des processus de nettoyage dans [agora-back](/repos/agora-gouv/agora-back).

## Dépôts les plus actifs
- [agora-back](/repos/agora-gouv/agora-back) : Évolutions majeures des fonctionnalités d'administration, de l'API et des algorithmes de tendances.
- [agora-app](/repos/agora-gouv/agora-app) : Améliorations de l'expérience mobile, du partage de contenu et de la conformité au design system.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Migration technologique majeure et optimisation des performances de l'infrastructure de contenu.
