# Synthèse d'activité : demarche-numerique (du 28/02 au 27/03/2026)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de l'expérience utilisateur de la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) avec des ajouts de fonctionnalités comme le filtrage par code postal, le préremplissage de la date de naissance via France Connect et un bouton dédié aux professionnels ("ProConnect").  Des efforts ont également été faits pour améliorer la robustesse et la performance de l'infrastructure, notamment via la migration de tâches vers Sidekiq et l'optimisation de l'API géographique. Enfin, [ds_proxy](/repos/demarche-numerique/ds_proxy) a bénéficié d'améliorations pour faciliter son utilisation et sa maintenance.

## Sécurité
Aucun changement lié à la sécurité n'a été signalé durant cette période.

## Autres changements notables
- Migration de tâches de fond vers Sidekiq sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) pour une meilleure gestion des erreurs et des retentatives.
- Optimisation des performances de l'API géographique via la mise en cache sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Refonte du processus de construction des images Docker sur [ds_proxy](/repos/demarche-numerique/ds_proxy) pour simplifier la création d'images.
- Migration de composants Haml vers ERB sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) pour une meilleure intégration.

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Amélioration significative de l'expérience utilisateur avec de nouvelles fonctionnalités et optimisations de performance.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Amélioration de la gestion des mots de passe et simplification du processus de construction des images Docker.
