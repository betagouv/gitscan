# Synthèse d'activité : demarche-numerique (du 17/03 au 27/03)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de la sécurité et de la robustesse de la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr), notamment en renforçant l'authentification des super-admins et en corrigeant une vulnérabilité d'accès non autorisé. Des optimisations significatives ont également été apportées à l'API Entreprise pour améliorer ses performances et sa gestion des erreurs. Enfin, [ds_proxy](/repos/demarche-numerique/ds_proxy) a bénéficié d'améliorations pour faciliter son utilisation et sa maintenance.

## Sécurité
- Correction d'un accès non autorisé à des dossiers via un lien de réinitialisation incorrect sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Implémentation de mécanismes de protection contre les attaques XSS et correction de vulnérabilités liées à l'exportation de données sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Amélioration de la gestion des OTP pour les super-admins avec ré-authentification et restriction d'accès sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- Refonte de l'API Entreprise sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) avec l'utilisation de monades `Result` pour une meilleure gestion des erreurs.
- Migration de tâches de longue durée vers Sidekiq avec gestion des retries sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Refonte du processus de construction des images Docker sur [ds_proxy](/repos/demarche-numerique/ds_proxy) pour simplifier la création d'images à partir de packages.

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Amélioration significative de la sécurité, des performances et de la gestion des erreurs de la plateforme principale.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Amélioration de la gestion des mots de passe et simplification du processus de construction des images Docker.
