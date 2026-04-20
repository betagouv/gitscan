# Synthèse d'activité : anct-cartographie-nationale (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration des performances et de la stabilité de l'application de cartographie [cartographie](/repos/anct-cartographie-nationale/cartographie). Des optimisations ont été apportées au chargement des données, à la gestion des requêtes et au rendu de l'interface utilisateur. L'outil `mednum-cli` [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) a également été mis à jour pour améliorer sa connectivité à l'API de cartographie via CloudFront et corriger un problème de données. Ces améliorations se traduisent par une meilleure expérience utilisateur et une plus grande fiabilité des services.

## Sécurité
Aucun changement lié à la sécurité n'a été signalé durant cette période.

## Autres changements notables
Le dépôt [cartographie](/repos/anct-cartographie-nationale/cartographie) a subi une migration vers Node.js version 22, permettant une meilleure compatibilité avec les Web Streams.  Une refactorisation importante des routes et middlewares a été effectuée pour une meilleure organisation du code, avec l'adoption d'une API basée sur des pipes. L'implémentation d'un cache LRU pour les chunks de carte et l'utilisation de `Suspense` pour les états de chargement des routes principales visent à optimiser les performances de l'application.

## Dépôts les plus actifs
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Amélioration significative des performances, de la stabilité et de l'expérience utilisateur de l'application de cartographie.
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Optimisation de la connectivité à l'API de cartographie et correction d'un problème de données.
