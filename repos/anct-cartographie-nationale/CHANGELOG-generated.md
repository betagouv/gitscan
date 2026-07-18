# Synthèse d'activité : anct-cartographie-nationale (du 17/06 au 29/06)

## Résumé de l'activité
L'organisation a connu une semaine productive, axée sur l'amélioration des données et de l'expérience utilisateur.  La mise à jour des sources de données de [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) avec les nouvelles zones FRR et la source "francilin" permet une cartographie plus précise des zones d'inclusion numérique. Parallèlement, l'application [cartographie](/repos/anct-cartographie-nationale/cartographie) a bénéficié d'améliorations de la performance, de la gestion des erreurs et d'une modernisation de sa base de code.

## Sécurité
L'intégration de Sentry dans [cartographie](/repos/anct-cartographie-nationale/cartographie) permet une meilleure remontée des erreurs, tout en assurant la protection des données personnelles.

## Autres changements notables
[cartographie](/repos/anct-cartographie-nationale/cartographie) a subi un refactoring important vers des librairies plus modernes (@arckit/nextjs, @arckit/form, @arckit/daisyui) pour améliorer la maintenabilité et la qualité du code. De plus, la configuration des logs Nginx a été améliorée pour faciliter le débogage et l'intégration avec Grafana.

## Dépôts les plus actifs
- [mednum-cli](/repos/anct-cartographie-nationale/mednum-cli) : Mise à jour des sources de données et amélioration de la stabilité de la publication des données nationales.
- [cartographie](/repos/anct-cartographie-nationale/cartographie) : Amélioration de la recherche de lieux d'inclusion numérique, gestion du cache, intégration de Sentry et refactoring technique.
