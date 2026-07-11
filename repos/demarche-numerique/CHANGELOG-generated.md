# Synthèse d'activité : demarche-numerique (du 27/06 au 10/07)

## Résumé de l'activité
La période a été marquée par des améliorations significatives de la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr), axées sur la performance, la sécurité et l'expérience utilisateur. Des optimisations ont été apportées à la gestion des pièces jointes, des attestations et des exports de données. Parallèlement, le proxy [ds_proxy](/repos/demarche-numerique/ds_proxy) a été enrichi avec la prise en charge de nouveaux types de stockage (S3 et Swift) et une configuration plus flexible. La migration vers Rails 8 sur la plateforme principale est également un changement majeur pour l'avenir.

## Sécurité
- Renforcement de la sécurité de la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) avec la correction de vulnérabilités potentielles et la migration vers l'authentification à deux facteurs ProConnect.
- Suppression du header `content-md5` altéré par le proxy [ds_proxy](/repos/demarche-numerique/ds_proxy) pour une meilleure intégrité des données.

## Autres changements notables
- Migration de la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) vers Rails 8, une mise à jour majeure du framework.
- Configuration du mode proxy S3 sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) pour optimiser l'accès au stockage objet.
- Refactorisation de la configuration S3 dans [ds_proxy](/repos/demarche-numerique/ds_proxy) pour une meilleure organisation.

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Améliorations majeures de la plateforme, incluant la gestion des pièces jointes, des attestations, des exports et la migration vers Rails 8.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Ajout de la prise en charge de S3 et Swift, corrections de bugs et optimisations de la configuration.
