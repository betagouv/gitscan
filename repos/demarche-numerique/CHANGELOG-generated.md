# Synthèse d'activité : demarche-numerique (du 02/06 au 12/06)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) avec des évolutions significatives pour les professionnels, notamment l'ajout d'un bouton ProConnect et une migration vers la version 4 de l'API Entreprise pour une meilleure gestion des données d'établissement. Des corrections de bugs et des améliorations de l'expérience utilisateur ont également été apportées.  Parallèlement, une correction importante a été déployée sur [ds_proxy](/repos/demarche-numerique/ds_proxy) pour garantir l'intégrité des données lors du proxyage des requêtes.

## Sécurité
Aucune modification liée à la sécurité n'a été signalée durant cette période.

## Autres changements notables
- Refactorisation majeure de [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) pour la migration vers l'API Entreprise v4, incluant la gestion des données d'établissement et le code NAF 2025.
- Amélioration de la performance et optimisation du code de [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) avec la réduction des requêtes N+1 et l'utilisation de circuit breakers.
- Correction d'un bug d'altération d'en-tête HTTP dans [ds_proxy](/repos/demarche-numerique/ds_proxy) affectant l'intégrité des fichiers.

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Amélioration significative de la plateforme avec des fonctionnalités pour les professionnels et une migration vers une nouvelle version de l'API Entreprise.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Correction d'un bug critique concernant l'intégrité des données lors du proxyage.
