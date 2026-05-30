# Synthèse d'activité : mission-apprentissage (du 15/05 au 29/05/2026)

## Résumé de l'activité
L'organisation "mission-apprentissage" a connu une période d'activité soutenue, marquée par des améliorations significatives sur plusieurs de ses projets clés. Les efforts se sont concentrés sur l'amélioration de la sécurité (notamment avec la migration vers SOPS pour la gestion des secrets), l'optimisation des performances (comme pour le job d'enrichissement de [bal](/repos/mission-apprentissage/bal)) et l'ajout de nouvelles fonctionnalités pour les utilisateurs.  Des améliorations importantes ont été apportées à [labonnealternance](/repos/mission-apprentissage/labonnealternance) avec la migration vers GitHub Issues et la suppression de l'API v1 obsolète, ainsi qu'à [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas) avec l'ajout de nouvelles pages d'atterrissage et l'activation de la version 2 de la collaboration.

## Sécurité
Plusieurs dépôts ont bénéficié d'améliorations de la sécurité :

*   Correction d'une vulnérabilité critique affectant la gestion des fragments TCP (Dirty Frag et Fragnesia) dans [infra](/repos/mission-apprentissage/infra).
*   Migration d'Ansible Vault vers SOPS pour une gestion des secrets plus sécurisée dans [infra](/repos/mission-apprentissage/infra) et [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas).
*   Protection des routes "admin" et "france-travail" dans [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas).

## Autres changements notables
*   Migration vers GitHub Issues en remplacement de Jira dans [labonnealternance](/repos/mission-apprentissage/labonnealternance).
*   Suppression de Swagger et de l'API v1 obsolète dans [labonnealternance](/repos/mission-apprentissage/labonnealternance).
*   Refactorisation et amélioration de la gestion des secrets avec SOPS dans [infra](/repos/mission-apprentissage/infra) et [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab).
*   Mise à jour de Mongoose vers la version 9 et réécriture du plugin `diffHistory` dans [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage).

## Dépôts les plus actifs
*   [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Améliorations majeures de l'application, incluant la migration vers GitHub Issues et la suppression de l'API v1.
*   [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas) : Ajout de nouvelles fonctionnalités pour faciliter l'inscription et l'information, ainsi que des améliorations de la sécurité.
*   [infra](/repos/mission-apprentissage/infra) : Améliorations significatives de la sécurité et de la gestion des secrets.
*   [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) : Intégration d'un nouveau modèle d'apprentissage et amélioration du processus de CI/CD.
*   [bal](/repos/mission-apprentissage/bal) : Optimisation des performances et correction de bugs pour la boîte aux lettres d'apprentissage.
