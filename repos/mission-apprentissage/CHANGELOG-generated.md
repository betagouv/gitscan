# Synthèse d'activité : mission-apprentissage (du 24/04 au 08/07/2026)

## Résumé de l'activité
L'organisation "mission-apprentissage" a connu une période d'activité soutenue, marquée par des améliorations significatives de l'infrastructure, de la sécurité et des fonctionnalités de ses différents services.  Plusieurs migrations de serveurs ont été réalisées pour améliorer la stabilité et la performance. Des efforts importants ont été consacrés à l'automatisation des tâches (skills pour GitHub), à l'amélioration de l'expérience utilisateur (refonte de l'interface de labonnealternance, correction de bugs) et au renforcement de la sécurité (configuration d'une autorité de certification, rotation de secrets). L'ajout de Sentry pour la supervision des erreurs est une avancée notable pour la gestion des incidents.

## Sécurité
Plusieurs changements ont été apportés pour renforcer la sécurité :

- Configuration d'une autorité de certification pour l'authentification des membres d'un cluster MongoDB [mongodb](/repos/mission-apprentissage/mongodb).
- Rotation du secret SOPS pour renforcer la sécurité dans [infra](/repos/mission-apprentissage/infra) et [labonnealternance](/repos/mission-apprentissage/labonnealternance).
- Mise en place d'une auto-révocation des clés API inutilisées dans [bal](/repos/mission-apprentissage/bal).

## Autres changements notables
- Migrations de serveurs pour plusieurs projets : [labonnealternance](/repos/mission-apprentissage/labonnealternance), [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas), [bal](/repos/mission-apprentissage/bal), [api-apprentissage](/repos/mission-apprentissage/api-apprentissage), [infra](/repos/mission-apprentissage/infra).
- Suppression de sous-modules obsolètes dans [bal](/repos/mission-apprentissage/bal), [api-apprentissage](/repos/mission-apprentissage/api-apprentissage) et [infra](/repos/mission-apprentissage/infra) pour simplifier l'infrastructure.
- Intégration de Sentry pour la supervision des erreurs [infra](/repos/mission-apprentissage/infra).
- Migration de la gestion des secrets d'Ansible Vault vers SOPS dans [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab).
- Unification du logging avec Pino dans [labonnealternance](/repos/mission-apprentissage/labonnealternance).

## Dépôts les plus actifs
- [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Refonte de l'interface utilisateur, correction de bugs et migration des serveurs.
- [mna-skills](/repos/mission-apprentissage/mna-skills) : Développement initial des skills pour l'automatisation des tâches GitHub.
- [infra](/repos/mission-apprentissage/infra) : Migrations de serveurs, ajout de Sentry et améliorations de la sécurité.
- [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) : Amélioration du modèle de classification, migration de la gestion des secrets et corrections de bugs.
- [bal](/repos/mission-apprentissage/bal) : Importation des données Akto, correction de bugs et migration des serveurs.
