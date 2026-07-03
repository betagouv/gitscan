# Synthèse d'activité : anct-cartographie-nationale (du 17/06 au 29/06)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration des données utilisées pour la cartographie des lieux d'inclusion numérique et sur la modernisation de l'application web.  [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) a été mis à jour avec de nouvelles sources de données (Francilin) et des corrections de zonage (remplacement ZRR par FRR, mise à jour QPV). L'application [cartographie](/repos/anct-cartographie-nationale/cartographie) a bénéficié d'un filtre par source de données, d'une meilleure gestion du cache et de l'intégration de Sentry pour le suivi des erreurs. Ces améliorations visent à fournir des données plus précises et une expérience utilisateur plus stable et performante.

## Sécurité
L'intégration de Sentry dans [cartographie](/repos/anct-cartographie-nationale/cartographie) inclut un filtrage des données sensibles lors de la remontée des erreurs, améliorant ainsi la sécurité des données utilisateurs.

## Autres changements notables
[cartographie](/repos/anct-cartographie-nationale/cartographie) a entrepris une modernisation technique significative avec l'adoption de nouvelles bibliothèques (@arckit/nextjs, @arckit/form, @arckit/daisyui) et l'émission des logs Nginx au format JSON pour une meilleure intégration avec Grafana. Ces changements visent à améliorer la maintenabilité et l'observabilité de l'application.

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Mise à jour des sources de données et amélioration de la stabilité de la publication des données nationales.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Amélioration de l'interface utilisateur avec un filtre par source de données, intégration d'un outil de suivi des erreurs et modernisation de la base de code.
