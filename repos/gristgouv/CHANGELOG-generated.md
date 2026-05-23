# Synthèse d'activité : gristgouv (du 13 mars 2026 au 9 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation gristgouv s'est concentrée sur l'amélioration continue de la plateforme Grist, tant au niveau de l'application principale que de ses outils associés. Des efforts significatifs ont été déployés pour enrichir l'expérience utilisateur avec de nouvelles fonctionnalités comme l'intégration de formulaires intra-administration ([widgets-config](/repos/gristgouv/widgets-config)) et un éditeur de texte enrichi ([grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form)).  La sécurité a également été renforcée, notamment dans [grist-core](/repos/gristgouv/grist-core), et des améliorations ont été apportées à l'administration et à l'API de Grist. L'offre de formation ([grist-mooc](/repos/gristgouv/grist-mooc)) a été mise à jour avec de nouveaux exercices.

## Sécurité
Plusieurs améliorations de sécurité ont été implémentées :
- Correction d'une vulnérabilité de gestion des origines opaques pour les requêtes CORS dans [grist-core](/repos/gristgouv/grist-core).
- Implémentation de DOMPurify pour la sanitisation du contenu HTML et la prévention des attaques XSS dans [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form).

## Autres changements notables
- Migration complète de l'interface de développement vers Vue.js dans [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form).
- Mise à jour de l'image Docker pour intégrer la dernière version de Grist (v1.7.13) dans [grist-docker-image](/repos/gristgouv/grist-docker-image).
- Amélioration de la gestion des sessions pour éviter la pollution avec les clés API dans [grist-core](/repos/gristgouv/grist-core).

## Dépôts les plus actifs
- [grist-core](/repos/gristgouv/grist-core) : Améliorations significatives de l'application Grist, incluant la sécurité, l'administration, l'API et la recherche.
- [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) : Refonte de l'interface utilisateur et renforcement de la sécurité du formulaire intra.
- [grist-mooc](/repos/gristgouv/grist-mooc) : Mise à jour du contenu de formation pour faciliter l'apprentissage de Grist.
- [gristlabs-widgets](/repos/gristlabs/gristlabs-widgets) : Amélioration du widget calendrier et mise à jour des environnements de développement.
