# Synthèse d'activité : gristgouv (du 13 mars 2026 au 9 mai 2026)

## Résumé de l'activité
L'activité récente de l'organisation gristgouv s'est concentrée sur l'amélioration de l'expérience utilisateur et l'ajout de nouvelles fonctionnalités, notamment pour les formulaires intra-administration et l'apprentissage de l'outil Grist. L'image Docker a été mise à jour avec la dernière version de Grist, et des améliorations significatives ont été apportées à la sécurité et à l'accessibilité de l'application principale. Ces évolutions permettent aux utilisateurs de bénéficier d'une plateforme plus robuste, sécurisée et facile à utiliser.

## Sécurité
Des améliorations significatives ont été apportées à la sécurité du dépôt [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) avec l'implémentation de DOMPurify pour la sanitisation du contenu HTML et la prévention des attaques XSS. Le dépôt [grist-core](/repos/gristlabs/grist-core) a également implémenté un flux OAuth avec gestion des consentements et des autorisations.

## Autres changements notables
Le dépôt [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) a migré son interface de développement vers Vue.js, ce qui représente un changement technique majeur. Le dépôt [grist-core](/repos/gristlabs/grist-core) a refondu sa structure OIDC en préparation de l'implémentation du flux de consentement et de gestion des autorisations, et a ajouté un backend de stockage externe basé sur le système de fichiers pour les tests.

## Dépôts les plus actifs
- [widgets-config](/repos/gristgouv/widgets-config) : Ajout d'un nouveau widget pour les formulaires intra-administration.
- [gristlabs-widgets](/repos/gristlabs/gristlabs-widgets) : Amélioration du widget calendrier et mise à jour des environnements de développement.
- [grist-mooc](/repos/gristgouv/grist-mooc) : Mise à jour des contenus de formation pour faciliter l'apprentissage de Grist.
- [grist-docker-image](/repos/gristgouv/grist-docker-image) : Mise à jour de l'image Docker avec la dernière version de Grist.
- [grist-cw-intra-form](/repos/gristgouv/grist-cw-intra-form) : Ajout d'un éditeur de texte enrichi et amélioration de la validation des formulaires.
- [grist-core](/repos/gristlabs/grist-core) : Ajout de raccourcis clavier, amélioration de l'accessibilité et implémentation d'un flux OAuth.
