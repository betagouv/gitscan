# Synthèse d'activité : gristgouv (du 13 mars 2026 au 9 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation gristgouv s'est concentrée sur l'amélioration continue de la plateforme Grist, tant au niveau de l'application principale que de ses outils associés. Des efforts significatifs ont été déployés pour faciliter l'intégration de formulaires internes ([widgets-config](/repos/gristgouv/widgets-config), [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form)), améliorer l'expérience utilisateur avec de nouvelles fonctionnalités comme un widget calendrier adaptatif ([gristlabs-widgets](/repos/gristlabs-widgets)) et une recherche plus performante ([grist-core](/repos/gristgouv/grist-core)), et renforcer la sécurité de la plateforme ([grist-core](/repos/gristgouv/grist-core), [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form)). La documentation et les supports de formation ont également été mis à jour ([grist-mooc](/repos/gristgouv/grist-mooc)).

## Sécurité
Plusieurs améliorations de sécurité ont été apportées :

- Correction d'un problème de sécurité lié aux requêtes CORS dans [grist-core](/repos/gristgouv/grist-core).
- Implémentation de DOMPurify pour la sanitisation du contenu HTML et la prévention des attaques XSS dans [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form).

## Autres changements notables
- Migration de l'interface de développement de [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) vers Vue.js.
- Ajout d'un endpoint API pour la gestion des enregistrements dans [grist-core](/repos/gristgouv/grist-core).
- Mise à jour de l'image Docker de Grist vers la version 1.7.13 dans [grist-docker-image](/repos/gristgouv/grist-docker-image).

## Dépôts les plus actifs
- [grist-core](/repos/gristgouv/grist-core) : Améliorations significatives de l'application principale, incluant la gestion des applications OAuth, la recherche et la sécurité.
- [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) : Refonte de l'interface et renforcement de la sécurité pour l'intégration de formulaires.
- [gristlabs-widgets](/repos/gristlabs-widgets) : Amélioration de l'expérience utilisateur avec un widget calendrier adaptatif et ajout d'une fonctionnalité expérimentale.
- [grist-mooc](/repos/gristgouv/grist-mooc) : Mise à jour des supports de formation pour faciliter l'apprentissage de Grist.
