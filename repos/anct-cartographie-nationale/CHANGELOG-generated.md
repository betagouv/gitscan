# Synthèse d'activité : anct-cartographie-nationale (du 16/06 au 29/06)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration des données utilisées pour la cartographie des lieux d'inclusion numérique et sur la modernisation de l'application web.  [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) a été mis à jour avec de nouvelles sources de données (Francilin) et des corrections de zonage (remplacement ZRR par FRR, mise à jour QPV).  L'application [cartographie](/repos/anct-cartographie-nationale/cartographie) a bénéficié d'un filtre par source de données, d'une meilleure gestion du cache et d'une intégration de Sentry pour le suivi des erreurs. Ces améliorations se traduisent par une meilleure qualité des données et une expérience utilisateur plus stable et fiable.

## Sécurité
L'intégration de Sentry dans [cartographie](/repos/anct-cartographie-nationale/cartographie) inclut un filtrage des données sensibles, renforçant ainsi la sécurité des informations remontées en cas d'erreur.

## Autres changements notables
[cartographie](/repos/anct-cartographie-nationale/cartographie) a entrepris une migration vers des bibliothèques plus modernes (@arckit/nextjs, @arckit/form, @arckit/daisyui) pour standardiser et moderniser sa base de code.  La configuration des logs Nginx a été modifiée pour émettre au format JSON et corrélée avec Sentry via un `request_id`, facilitant ainsi le débogage et la surveillance.

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Mise à jour des sources de données et amélioration de la publication des données nationales.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Amélioration de la recherche, intégration de Sentry, modernisation du code et amélioration de la journalisation.
