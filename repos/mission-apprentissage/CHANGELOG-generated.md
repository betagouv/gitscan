# Synthèse d'activité : mission-apprentissage (du 22 juin au 22 juillet 2026)

## Résumé de l'activité
La période a été marquée par des améliorations significatives de l'infrastructure, avec des migrations de serveurs et une rotation des secrets SOPS pour renforcer la sécurité. Plusieurs dépôts ont bénéficié d'évolutions fonctionnelles, notamment [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) avec l'intégration d'un nouveau modèle d'apprentissage, [tableaudebord-lab](/repos/mission-apprentissage/tableaudebord-lab) avec l'ajout d'un classificateur de contacts, et [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas) avec l'ajout de filtres et l'intégration de nouvelles données. Des améliorations de l'API et de la gestion des données ont également été apportées à [lba-github-mcp](/repos/mission-apprentissage/lba-github-mcp) et [api-apprentissage](/repos/mission-apprentissage/api-apprentissage).

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de la sécurité :
- Rotation des secrets SOPS dans [mongodb](/repos/mission-apprentissage/mongodb), [labonnealternance](/repos/mission-apprentissage/labonnealternance), [bal](/repos/mission-apprentissage/bal) et [api-apprentissage](/repos/mission-apprentissage/api-apprentissage).
- Suppression des sous-modules `.infra/authorizations` et `.infra/inventories` dans [mongodb](/repos/mission-apprentissage/mongodb), [bal](/repos/mission-apprentissage/bal) et [api-apprentissage](/repos/mission-apprentissage/api-apprentissage) pour simplifier la gestion et renforcer la sécurité.

## Autres changements notables
- Migration de nombreux serveurs de production et de recette dans plusieurs dépôts ([bal](/repos/mission-apprentissage/bal), [api-apprentissage](/repos/mission-apprentissage/api-apprentissage), [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas), [infra](/repos/mission-apprentissage/infra)).
- Migration de la gestion des secrets d'Ansible Vault vers SOPS dans [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab).
- Mise à jour de Mongoose vers la version 9 et réécriture du plugin `diffHistory` dans [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage).
- Ajout de Sentry pour la surveillance des erreurs dans [infra](/repos/mission-apprentissage/infra).

## Dépôts les plus actifs
- [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) : Amélioration du modèle de classification et refonte de la gestion des secrets.
- [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas) : Ajout de nouvelles fonctionnalités d'intégration de données et d'amélioration de l'outil de Machine Learning.
- [bal](/repos/mission-apprentissage/bal) : Amélioration de l'ingestion de données DECA, gestion des identifiants et migrations d'infrastructure.
- [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Refonte de l'affichage des erreurs, ajout de l'export des offres d'emploi et rotation des secrets.
- [api-apprentissage](/repos/mission-apprentissage/api-apprentissage) : Amélioration de la stabilité, de la performance et de la documentation de l'API.
