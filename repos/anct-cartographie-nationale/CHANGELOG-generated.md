# Synthèse d'activité : anct-cartographie-nationale (derniers 7 jours)

## Résumé de l'activité
L'activité récente de l'organisation s'est concentrée sur l'amélioration de la performance et de la maintenabilité de la cartographie, ainsi que sur l'affinage des données utilisées par l'outil de médiation numérique. Le dépôt [cartographie](/repos/anct-cartographie-nationale/cartographie) a bénéficié d'une refactorisation importante de son architecture, intégrant des mécanismes de cache et de parallélisation pour optimiser les appels API. L'ajout de Matomo permet désormais de suivre l'utilisation des composants cartographiques. Le dépôt [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) a quant à lui amélioré la qualité de ses données en ajoutant des adresses officielles et en supprimant des sources obsolètes.

## Sécurité
Aucun changement lié à la sécurité n'a été identifié durant cette période.

## Autres changements notables
Le dépôt [cartographie](/repos/anct-cartographie-nationale/cartographie) a entrepris une refactorisation majeure vers une architecture basée sur les "abilities" et des bibliothèques partagées, visant à améliorer la modularité et la réutilisabilité du code. La migration vers une API basée sur des pipes et des middlewares simplifie également la gestion des routes et des pages. Le dépôt [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) a supprimé les gestionnaires de paquets Yarn et Pnpm pour simplifier la configuration du projet.

## Dépôts les plus actifs
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Refactorisation majeure de l'architecture, amélioration des performances et ajout de capacités d'analyse.
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Amélioration de la qualité des données et simplification de la configuration du projet.
