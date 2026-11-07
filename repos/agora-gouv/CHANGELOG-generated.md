# Synthèse d'activité : agora-gouv (du 10/07 au 27/08)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de l'expérience utilisateur et la robustesse de l'infrastructure. Les utilisateurs bénéficieront d'une meilleure clarté des informations (notamment sur l'identité des auteurs des réponses) et de fonctionnalités de partage plus fluides sur l'application mobile [agora-app](/repos/agora-gouv/agora-app). 

En parallèle, les outils d'administration ont été enrichis pour permettre une modération plus précise et une gestion de contenu facilitée [agora-back](/repos/agora-gouv/agora-back) [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi).

## Sécurité
- Renforcement de la sécurité réseau via le filtrage par adresse IP sur l'instance Metabase [agora-metabase-scalingo](/repos/agora-gouv/agora-metabase-scalingo).
- Automatisation de la gestion des certificats SSL (via Sectigo et le protocole ACME) pour sécuriser les échanges sur l'application, le backend et le frontend [agora-app](/repos/agora-gouv/agora-app) [agora-back](/repos/agora-gouv/agora-back) [agora-front](/repos/agora-gouv/agora-front).

## Autres changements notables
- Migration majeure de la plateforme de gestion de contenu vers Strapi V5 [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi).
- Optimisation des performances et de la stabilité via l'ajustement des configurations Nginx et de la mémoire Node.js [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi).
- Refonte de l'algorithme de calcul des tendances [agora-back](/repos/agora-gouv/agora-back).
- Mise en conformité de l'interface mobile avec le Design System Français (DSFR) [agora-app](/repos/agora-gouv/agora-app).
- Simplification de l'infrastructure de gestion des certificats SSL en migrant la configuration vers l'application Nuxt [agora-front](/repos/agora-gouv/agora-front).

## Dépôts les plus actifs
- [agora-back](/repos/agora-gouv/agora-back) : Évolutions majeures sur la modération, la gestion des contenus et les algorithmes de tendances.
- [agora-app](/repos/agora-gouv/agora-app) : Améliorations de l'expérience utilisateur mobile et mise en conformité visuelle.
- [agora-cms-strapi](/repos/agora-gouv/agora-cms-strapi) : Migration technologique vers Strapi V5 et optimisations de performance.
- [agora-front](/repos/agora-gouv/agora-front) : Améliorations de l'interface web et simplification de la gestion des certificats.
