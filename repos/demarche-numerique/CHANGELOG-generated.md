# Synthèse d'activité : demarche-numerique (du 29/06 au 29/07)

## Résumé de l'activité
La période a été marquée par des améliorations significatives sur la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr), axées sur l'expérience utilisateur avec notamment une gestion améliorée des pièces justificatives, la personnalisation des dossiers et l'intégration de nouvelles données comme le quotient familial et les données ARS.  Parallèlement, des efforts importants ont été réalisés pour moderniser l'infrastructure avec la finalisation de la migration vers Rails 8 et l'optimisation des performances via l'utilisation de DataLoaders. Le proxy [ds_proxy](/repos/demarche-numerique/ds_proxy) a également bénéficié d'améliorations de configuration et de stabilité.

## Sécurité
- Ajout d'une validation de la présence d'un token API pour certaines fonctionnalités sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Renforcement de la sécurité de l'application [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- Finalisation de la migration vers Rails 8 sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Refactorisation du code et amélioration du pipeline CI/CD sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) pour une meilleure maintenabilité.
- Ajout de la prise en charge de S3 et Swift avec détection automatique du type de stockage sur [ds_proxy](/repos/demarche-numerique/ds_proxy).
- Suppression du header `content-md5` altéré par le proxy [ds_proxy](/repos/demarche-numerique/ds_proxy).

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Amélioration de l'expérience utilisateur et modernisation de l'infrastructure avec la migration vers Rails 8.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Amélioration de la flexibilité de la configuration et de la stabilité du proxy.
