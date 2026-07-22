# Synthèse d'activité : anct-cartographie-nationale (du 29 juin 2026 au 10 juillet 2026)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration des données utilisées par les outils de cartographie et sur la stabilité et l'observabilité de l'application principale.  [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) a été mis à jour avec de nouvelles sources de données et des corrections, tandis que [cartographie](/repos/anct-cartographie-nationale/cartographie) bénéficie d'un filtrage amélioré, d'une meilleure gestion des erreurs et d'une instrumentation accrue pour faciliter le diagnostic et la maintenance. Ces améliorations visent à fournir des données plus précises et une expérience utilisateur plus fiable.

## Sécurité
Aucun changement lié à la sécurité n'a été identifié dans les changelogs de cette période.

## Autres changements notables
- Refactorisation du cache des lieux dans [cartographie](/repos/anct-cartographie-nationale/cartographie) pour une meilleure gestion et performance.
- Amélioration de l'observabilité de [cartographie](/repos/anct-cartographie-nationale/cartographie) avec l'ajout de logs structurés, la corrélation avec Sentry et l'ajout de logs d'accès Nginx au format JSON.

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Mise à jour des sources de données (FRR, QPV, francilin) et amélioration de la stabilité de la publication des données.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Ajout de filtres par source de données, amélioration de la gestion des erreurs et refactorisation du cache pour une meilleure performance et observabilité.
