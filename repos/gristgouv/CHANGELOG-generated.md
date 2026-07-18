# Synthèse d'activité : gristgouv (du 23 mai au 26 juin 2026)

## Résumé de l'activité
L'activité récente de l'organisation gristgouv s'est concentrée sur l'amélioration de la sécurité, l'enrichissement de l'offre de formation et l'amélioration de l'expérience utilisateur. L'ajout d'un nouveau widget de formulaire intra-administration via [widgets-config](/repos/gristgouv/widgets-config) permet aux agents de l'État de créer plus facilement des formulaires. Des améliorations significatives de la sécurité ont été apportées à l'image Docker via [grist-docker-image](/repos/gristgouv/grist-docker-image) avec l'intégration d'un scanner de vulnérabilités. Enfin, le contenu de formation a été mis à jour via [grist-mooc](/repos/gristgouv/grist-mooc) et des tests automatisés ont été ajoutés à [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) pour améliorer la qualité du code.

## Sécurité
- L'image Docker a été renforcée en sécurité avec l'intégration de Trivy pour l'analyse des vulnérabilités via [grist-docker-image](/repos/gristgouv/grist-docker-image). Un rapport JSON des vulnérabilités détectées est désormais disponible.
- Amélioration de l'environnement de construction avec GVISOR via [grist-docker-image](/repos/gristgouv/grist-docker-image) pour une meilleure abstraction et robustesse.

## Autres changements notables
- Mise à jour de l'image Grist vers la version 1.7.15 via [grist-docker-image](/repos/gristgouv/grist-docker-image).
- Ajout d'une première suite de tests automatisés (smoke tests) pour le formulaire intra via [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form).

## Dépôts les plus actifs
- [grist-docker-image](/repos/gristgouv/grist-docker-image) : Amélioration significative de la sécurité et de la robustesse de l'image Docker.
- [widgets-config](/repos/gristgouv/widgets-config) : Ajout d'un nouveau widget pour les formulaires intra-administration.
- [gristlabs-widgets](/repos/gristgouv/gristlabs-widgets) : Amélioration de la lisibilité et de la robustesse des widgets, notamment en gérant mieux l'affichage des erreurs.
- [grist-mooc](/repos/gristgouv/grist-mooc) : Mise à jour du contenu de formation avec de nouveaux exercices et instructions.
