# Synthèse d'activité : demarche-numerique (du 17/03 au 27/03)

## Résumé de l'activité
La période a été marquée par des améliorations significatives sur la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr), notamment en termes de gestion des pièces justificatives avec la prise en charge de nouveaux formats et une meilleure liaison avec les dossiers. Des optimisations de performance ont été réalisées grâce à la migration vers Sidekiq et l'utilisation de Vips pour le traitement des images. Enfin, des corrections de sécurité importantes ont été apportées pour renforcer la protection de la plateforme. Le proxy [ds_proxy](/repos/demarche-numerique/ds_proxy) a bénéficié d'améliorations de la gestion des mots de passe et de la construction des images Docker.

## Sécurité
- Correction de vulnérabilités potentielles (injection, IDOR, CSRF) sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Remplacement de l'authentification SAML sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- Migration de jobs vers Sidekiq sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) pour une meilleure résilience et gestion des tâches asynchrones.
- Optimisation des requêtes GraphQL sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) pour améliorer les performances.
- Utilisation de Vips pour le traitement des images sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr), améliorant performances et robustesse.
- Refonte du processus de construction des images Docker sur [ds_proxy](/repos/demarche-numerique/ds_proxy) pour simplifier la création d'images à partir de packages.

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Améliorations majeures de la plateforme, incluant la gestion des pièces justificatives, la sécurité et les performances.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Amélioration de la gestion des mots de passe et simplification du processus de construction des images Docker.
