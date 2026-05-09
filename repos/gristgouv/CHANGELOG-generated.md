# Synthèse d'activité : gristgouv (du 13 mars 2026 au 9 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation gristgouv s'est concentrée sur l'amélioration continue de l'application Grist et de son écosystème. Des efforts significatifs ont été déployés pour enrichir l'offre de widgets, notamment avec l'ajout d'un widget de formulaire intra-administration via [widgets-config](/repos/gristgouv/widgets-config) et l'amélioration du widget calendrier dans [gristlabs-widgets](/repos/gristlabs-widgets).  Le projet [grist-mooc](/repos/grist-mooc) a été mis à jour avec de nouveaux contenus pédagogiques, facilitant l'apprentissage de l'outil. Enfin, l'image Docker [grist-docker-image](/repos/grist-docker-image) a été mise à jour avec la dernière version de Grist, simplifiant le déploiement et la mise à jour pour les utilisateurs.

## Sécurité
Des améliorations de sécurité ont été apportées au dépôt [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) avec l'implémentation de DOMPurify pour la sanitisation du contenu HTML et la prévention des attaques XSS. De plus, le dépôt [grist-core](/repos/gristgouv/grist-core) a bénéficié d'une refactorisation des types `ISandbox` et d'une amélioration de la gestion des sessions pour renforcer la sécurité et la robustesse.

## Autres changements notables
Le dépôt [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) a subi une migration complète de son interface vers Vue.js, modernisant ainsi sa base de code.  [grist-core](/repos/gristgouv/grist-core) a vu l'ajout d'un point de terminaison pour lister les enregistrements et des améliorations significatives de la gestion des autorisations, de l'interface de gestion des applications OAuth et de la recherche dans les documents.

## Dépôts les plus actifs
- [grist-core](/repos/gristgouv/grist-core) : Ce dépôt a connu une activité intense avec des améliorations de la sécurité, de nouvelles fonctionnalités et des refactorisations importantes.
- [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) : Ce dépôt a été marqué par une migration technologique majeure et des améliorations de la sécurité et de l'expérience utilisateur.
- [gristlabs-widgets](/repos/gristlabs-widgets) : Ce dépôt s'est concentré sur l'amélioration de l'expérience utilisateur et la mise à jour des dépendances.
- [grist-docker-image](/repos/gristgouv/grist-docker-image) : Ce dépôt a permis de diffuser rapidement la dernière version de Grist aux utilisateurs via une image Docker mise à jour.
