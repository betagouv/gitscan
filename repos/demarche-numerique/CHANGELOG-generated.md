# Synthèse d'activité : demarche-numerique (du 02/06 au 12/06)

## Résumé de l'activité
La semaine a été marquée par des améliorations significatives sur la plateforme [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr), notamment en termes d'expérience utilisateur avec l'ajout de bannières d'information, l'amélioration de l'affichage des badges et la gestion du code NAF 2025 pour les entreprises.  Des évolutions techniques importantes ont également été réalisées, avec une migration vers Rails 8.0 et l'implémentation de mesures de sécurité renforcées.  Enfin, une correction d'intégrité des données a été apportée au proxy [ds_proxy](/repos/demarche-numerique/ds_proxy) pour assurer la fiabilité des transferts de fichiers.

## Sécurité
- Correction de problèmes de sécurité liés à l'injection de code sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).

## Autres changements notables
- Mise à jour de Rails vers la version 8.0 sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Migration de composants HAML vers ERB sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Ajout d'un système de limitation de débit et d'un circuit breaker pour l'API Entreprise sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Utilisation de streaming pour les exports Excel afin de réduire la consommation de mémoire sur [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr).
- Correction d'un bug où l'en-tête `content-md5` était altéré lors du proxyage sur [ds_proxy](/repos/demarche-numerique/ds_proxy).

## Dépôts les plus actifs
- [demarche.numerique.gouv.fr](/repos/demarche-numerique/demarche.numerique.gouv.fr) : Amélioration continue de la plateforme avec de nouvelles fonctionnalités et des optimisations techniques.
- [ds_proxy](/repos/demarche-numerique/ds_proxy) : Correction d'un bug critique lié à l'intégrité des données lors du proxyage.
