# Synthèse d'activité : gristgouv (du 23 mai 2026 au 26 juin 2026)

## Résumé de l'activité
L'organisation gristgouv a connu une activité soutenue ce mois-ci, axée sur l'amélioration de la sécurité, l'expérience utilisateur et l'accessibilité de la plateforme Grist. L'ajout d'un nouveau widget de formulaire intra-administration via [widgets-config](/repos/gristgouv/widgets-config) permet aux agents de l'État de créer des formulaires directement dans Grist. Des améliorations significatives ont été apportées à la sécurité de l'image Docker via [grist-docker-image](/repos/gristgouv/grist-docker-image) avec l'intégration d'un scanner de vulnérabilités. L'offre de formation continue de s'enrichir avec la mise à jour des exercices du MOOC via [grist-mooc](/repos/gristgouv/grist-mooc).

## Sécurité
L'image Docker de Grist a bénéficié d'une amélioration significative de la sécurité grâce à l'intégration de Trivy pour l'analyse des vulnérabilités et la génération de rapports. [grist-docker-image](/repos/gristgouv/grist-docker-image)

## Autres changements notables
- L'image Docker a été mise à jour vers la version 1.7.15 via [grist-docker-image](/repos/gristgouv/grist-docker-image).
- L'intégration du workflow GVISOR a été améliorée pour une construction plus robuste de l'image Docker via [grist-docker-image](/repos/gristgouv/grist-docker-image).
- Des tests automatisés ont été ajoutés au projet [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) pour améliorer la qualité du code.
- Des améliorations de la traduction en hongrois et en italien ont été apportées à [grist-core](/repos/gristgouv/grist-core).

## Dépôts les plus actifs
- [grist-docker-image](/repos/gristgouv/grist-docker-image) : Amélioration significative de la sécurité et de la robustesse de l'image Docker.
- [gristlabs-widgets](/repos/gristgouv/gristlabs-widgets) : Amélioration de la lisibilité et de la robustesse des widgets.
- [grist-mooc](/repos/gristgouv/grist-mooc) : Mise à jour du contenu de formation pour faciliter l'apprentissage de Grist.
- [widgets-config](/repos/gristgouv/widgets-config) : Ajout d'un nouveau widget pour les formulaires intra-administration.
