# Synthèse d'activité : gristgouv (du 13 mars 2026 au 9 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation gristgouv s'est concentrée sur l'amélioration de l'expérience utilisateur et l'ajout de nouvelles fonctionnalités à la plateforme Grist. L'ajout d'un widget de formulaire intra-administration ([widgets-config](/repos/gristgouv/widgets-config)) permet aux agents de l'État de créer des formulaires directement dans Grist. Des améliorations significatives ont également été apportées à l'application Grist elle-même ([grist-core](/repos/gristlabs/grist-core)), notamment en matière de configuration, d'OAuth, de recherche et de sécurité. Enfin, des efforts ont été déployés pour enrichir le contenu de formation ([grist-mooc](/repos/gristgouv/grist-mooc)) et maintenir l'image Docker à jour ([grist-docker-image](/repos/gristgouv/grist-docker-image)).

## Sécurité
Des améliorations de sécurité ont été apportées au projet [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) avec l'implémentation de DOMPurify pour la sanitisation du contenu HTML et la prévention des attaques XSS. Des améliorations de la sécurité de la gestion des sessions ont également été implémentées dans [grist-core](/repos/gristlabs/grist-core).

## Autres changements notables
Une migration importante vers Vue.js a été effectuée dans [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) pour l'interface de développement.  [grist-core](/repos/gristlabs/grist-core) a bénéficié d'une mise à jour majeure de Pyodide (de 0.23.4 à 0.28.1) et d'une correction d'un problème de socket Docker.

## Dépôts les plus actifs
- [grist-core](/repos/gristlabs/grist-core) : Améliorations majeures de l'application Grist, incluant la configuration, l'OAuth, l'API et la recherche.
- [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) : Refonte de l'interface utilisateur et renforcement de la sécurité du formulaire intra-administration.
- [widgets-config](/repos/gristgouv/widgets-config) : Ajout d'un nouveau widget pour les formulaires intra-administration.
- [grist-mooc](/repos/gristgouv/grist-mooc) : Mise à jour du contenu de formation pour faciliter l'apprentissage de Grist.
