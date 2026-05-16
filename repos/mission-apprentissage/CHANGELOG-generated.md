# Synthèse d'activité : mission-apprentissage (du 16/04 au 16/05/2026)

## Résumé de l'activité
L'organisation mission-apprentissage a connu une période d'activité soutenue, marquée par des améliorations significatives sur plusieurs de ses plateformes.  Les efforts se sont concentrés sur l'amélioration de l'expérience utilisateur, notamment sur [labonnealternance](/repos/mission-apprentissage/labonnealternance) avec l'ajout de nouvelles fonctionnalités pour les recruteurs et l'optimisation du SEO, et sur [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas) avec l'ajout de nouvelles pages et fonctionnalités d'onboarding. La sécurité a également été renforcée avec la migration de la gestion des secrets vers SOPS sur [infra](/repos/mission-apprentissage/infra) et [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas).  Des améliorations techniques ont été apportées à l'infrastructure, aux bases de données et aux processus de développement pour une meilleure performance et maintenabilité.

## Sécurité
Plusieurs changements ont été apportés pour améliorer la sécurité :
- Migration de la gestion des secrets d'Ansible Vault vers SOPS sur [infra](/repos/mission-apprentissage/infra) et [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas).
- Mise à jour des images Docker de Nginx et ModSecurity-CRS sur [infra](/repos/mission-apprentissage/infra) pour bénéficier des dernières corrections de sécurité.
- Épinglage de `handlebars` et `form-data` sur [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas) pour corriger des CVE critiques.
- Migration de l'outil de scan de secrets de Talisman vers Gitleaks sur [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas).

## Autres changements notables
- Refactorisation et amélioration de la gestion des secrets avec SOPS sur plusieurs dépôts ([infra](/repos/mission-apprentissage/infra), [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab)).
- Mise à jour de Mongoose vers la version 9 et réécriture du plugin `diffHistory` sur [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage).
- Amélioration de la synchronisation avec Elasticsearch sur [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage).
- Remplacement de Mailhog par Mailpit pour les tests SMTP sur [voeux-affelnet](/repos/mission-apprentissage/voeux-affelnet).
- Ajout de la configuration d'une autorité de certification pour l'authentification des membres d'une grappe MongoDB sur [mongodb](/repos/mission-apprentissage/mongodb).

## Dépôts les plus actifs
- [labonnealternance](/repos/mission-apprentissage/labonnealternance) : Ajout de nouvelles fonctionnalités pour les recruteurs, amélioration du SEO et implémentation de l'export de données vers France Travail.
- [flux-retour-cfas](/repos/mission-apprentissage/flux-retour-cfas) : Ajout de nouvelles pages d'atterrissage, d'une fonctionnalité d'onboarding et amélioration de la collaboration ML/OFA.
- [labonnealternance-lab](/repos/mission-apprentissage/labonnealternance-lab) : Intégration d'un nouveau modèle d'apprentissage et migration de la gestion des secrets vers SOPS.
- [catalogue-apprentissage](/repos/mission-apprentissage/catalogue-apprentissage) : Corrections d'affichage et de synchronisation avec Elasticsearch, ainsi qu'une mise à jour majeure de Mongoose.
- [infra](/repos/mission-apprentissage/infra) : Amélioration de la sécurité avec la migration vers SOPS et mises à jour de sécurité pour Nginx et ModSecurity.
