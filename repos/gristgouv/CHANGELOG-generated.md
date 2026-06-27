# Synthèse d'activité : gristgouv (du 23 mai au 23 juin 2026)

## Résumé de l'activité
L'organisation gristgouv a connu une période d'activité soutenue, marquée par des améliorations significatives de l'expérience utilisateur et de la sécurité. L'ajout d'un nouveau widget de formulaire intra-administration via [widgets-config](/repos/gristgouv/widgets-config) permet aux agents de l'État de créer des formulaires directement dans Grist. Des efforts importants ont été consacrés à l'amélioration de l'accessibilité et de l'internationalisation de Grist via [grist-core](/repos/gristgouv/grist-core), avec l'ajout de traductions et l'amélioration du support des lecteurs d'écran. La sécurité a également été renforcée avec l'intégration d'un scanner de vulnérabilités dans l'image Docker via [grist-docker-image](/repos/gristgouv/grist-docker-image).

## Sécurité
- Intégration de Trivy pour l'analyse des vulnérabilités de l'image Docker et génération d'un rapport JSON des vulnérabilités détectées dans [grist-docker-image](/repos/gristgouv/grist-docker-image).

## Autres changements notables
- Amélioration de la gestion des locales (langues) pour une meilleure internationalisation dans [grist-core](/repos/gristgouv/grist-core).
- Ajout d'une nouvelle build utilisant une version plus récente de gvisor dans [grist-docker-image](/repos/gristgouv/grist-docker-image).
- Ajout d'un workflow CI avec des tests "smoke tests" utilisant Vitest dans [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form).

## Dépôts les plus actifs
- [grist-core](/repos/gristgouv/grist-core) : Améliorations majeures de l'accessibilité, de l'expérience utilisateur et de l'internationalisation.
- [grist-docker-image](/repos/gristgouv/grist-docker-image) : Renforcement de la sécurité avec l'intégration d'un scanner de vulnérabilités et mise à jour de Grist.
- [widgets-config](/repos/gristgouv/widgets-config) : Ajout d'un nouveau widget pour les formulaires intra-administration.
- [gristlabs-widgets](/repos/gristgouv/gristlabs-widgets) : Amélioration de la lisibilité et de la robustesse des widgets.
- [grist-mooc](/repos/gristgouv/grist-mooc) : Mise à jour des contenus de formation.
