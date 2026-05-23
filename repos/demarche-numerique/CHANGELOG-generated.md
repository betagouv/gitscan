# Synthèse d'activité : demarche-numerique (du 17/03 au 27/03)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) avec des optimisations de performance, une migration technique vers des technologies plus maintenables (ERB, Sidekiq) et des corrections de bugs impactant l'expérience utilisateur, notamment dans la gestion des pièces justificatives et l'affichage des avis.  Parallèlement, le proxy [ds_proxy](/repos/demarche-numerique/ds_proxy) a bénéficié d'améliorations pour faciliter son utilisation et sa maintenance, notamment en simplifiant la construction des images Docker et en améliorant la gestion des mots de passe.

## Sécurité
- Correction de vulnérabilités potentielles et gestion des identifiants/données sensibles sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- Migration de composants Haml vers ERB sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) pour une meilleure maintenabilité.
- Utilisation de Sidekiq pour la gestion des tâches asynchrones sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr), améliorant la réactivité.
- Refonte du processus de construction des images Docker sur [ds_proxy](/repos/demarche-numerique/ds_proxy) pour simplifier la création d'images à partir de packages.
- Migration de l'adaptateur d'établissement vers l'API Entreprise v4 sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Améliorations significatives de la plateforme, incluant des optimisations de performance, des corrections de bugs et des migrations techniques.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Améliorations de la gestion des mots de passe et simplification du processus de construction des images Docker.
