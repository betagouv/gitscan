# Synthèse d'activité : MTES-MCT (du 25/07 au 05/08)

## Résumé de l'activité
L'activité de l'organisation a été particulièrement intense, marquée par une volonté de modernisation des outils et une amélioration significative de l'expérience utilisateur. Les efforts se sont concentrés sur la mise en conformité avec les standards de design (DSFR) pour des applications comme [mobilic](/repos/MTES-MCT/mobilic) ou [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles), ainsi que sur l'ajout de fonctionnalités métier clés, telles que la gestion des haies pour [envergo](/repos/MTES-MCT/envergo) ou les demandes de détachement pour [mobilic](/repos/MTES-MCT/mobilic).

Parallèlement, une montée en version technologique majeure a été opérée sur plusieurs projets, notamment via la migration vers de nouveaux frameworks (AdonisJS 7, React 18) et la mise à jour de l'environnement de formation R (version 4.6). Ces évolutions garantissent une meilleure pérennité et performance des services pour les utilisateurs finaux et les agents de l'État.

## Sécurité
- Mise en œuvre de l'authentification multi-facteurs (MFA) pour [trackdechets](/repos/MTES-MCT/trackdechets).
- Migration vers Better Auth pour renforcer la gestion des utilisateurs dans [zero-logement-vacant](/repos/MTES-MCT/zero-logement-vacant).
- Renforcement des contrôles d'accès via Keycloak et sécurisation des routes pour [potentiel](/repos/MTES-MCT/potentiel).
- Mise en place d'une authentification par token pour l'API d'[ecobalyse-runner](/repos/MTES-MCT/ecobalyse-runner) et d'[ecobalyse](/repos/MTES-MCT/ecobalyse).
- Support de plusieurs clés API pour une gestion plus fine des accès dans [mon-devis-sans-oublis-backend-ocr](/repos/MTES-MCT/mon-devis-sans-oublis-backend-ocr).
- Sécurisation de la transmission des logs via le protocole SSL pour [dossierfacile-backend](/repos/MTES-MCT/dossierfacile-backend).

## Autres changements notables
- **Modernisation des frameworks et langages** : Migrations vers AdonisJS 7 pour [vizeau](/repos/MTES-MCT/vizeau), React 18 pour [partaj](/repos/MTES-MCT/partaj), et passage à R 4.6 pour l'ensemble des modules du [parcours-r](/repos/MTES-MCT/parcours-r).
- **Refontes d'interface et UX** : Refonte complète de la page de résultats pour [otelo](/repos/MTES-MCT/otelo) et de la page d'accueil pour [sparte](/repos/MTES-MCT/sparte).
- **Évolutions infrastructurelles et DevOps** : Automatisation des déploiements Android pour [monitor-field](/repos/MTES-MCT/monitor-field), intégration de Sentry pour la surveillance d'erreurs dans [envergo](/repos/MTES-MCT/envergo) et [prelevements-deau-web](/repos/MTES-MCT/prelevements-deau-web), et mise en place de "Review Apps" sur Scalingo pour [mobilic](/repos/MTES-MCT/mobilic).
- **Restructuration de données** : Fusion des dépôts data et front-end pour [ecobalyse](/repos/MTES-MCT/ecobalyse).

## Dépôts les plus actifs
- [mobilic](/repos/MTES-MCT/mobilic) : Évolutions majeures sur le cycle de vie des salariés et mise en conformité visuelle DSFR.
- [envergo](/repos/MTES-MCT/envergo) : Améliorations importantes sur la gestion des haies et des dossiers multi-départementaux.
- [otelo](/repos/MTES-MCT/otelo) : Refonte de l'interface de résultats et ajout d'un mode tutoriel pour les utilisateurs.
- [ecobalyse](/repos/MTES-MCT/ecobalyse) : Extension de la modélisation environnementale et refonte de l'architecture.
- [monitorenv](/repos/MTES-MCT/monitorenv) : Refonte de la gestion des zones réglementaires et du suivi de mission.
- [resorption-bidonvilles](/repos/MTES-MCT/resorption-bidonvilles) : Amélioration de l'accessibilité et intégration d'une nouvelle phase de diagnostic technique.
