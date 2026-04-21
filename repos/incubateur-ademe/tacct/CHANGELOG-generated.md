## Changelog : tacct (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, tacct a connu une importante phase de refactoring et de consolidation. L'application a été allégée en supprimant des fonctionnalités obsolètes (authentification, sandbox, anciens sites de baignade) et en simplifiant l'infrastructure. Des mises à jour de données ont été intégrées pour les indicateurs liés aux feux de forêt, à l'agriculture biologique, aux plans d'eau, au confort thermique, à l'arbovirose et aux moustiques tigres. L'interface utilisateur a également bénéficié d'améliorations, notamment au niveau des modales et des boutons.

### Évolutions fonctionnelles
- Amélioration de la modale des collections avec un slider fonctionnel [#a82ae2a2](https://github.com/incubateur-ademe/tacct/commit/a82ae2a2).
- Ajout d'une notice sur la page d'accueil [#9ed689b8](https://github.com/incubateur-ademe/tacct/commit/9ed689b8).
- Mise à jour des données relatives aux feux de forêt, incluant les surfaces en bio [#18a76aac](https://github.com/incubateur-ademe/tacct/commit/18a76aac) et [#d92ebbe8](https://github.com/incubateur-ademe/tacct/commit/d92ebbe8).
- Mise à jour des données concernant l'agriculture biologique [#e041c2b3](https://github.com/incubateur-ademe/tacct/commit/e041c2b3).
- Amélioration de l'affichage et de la réactivité des informations sur le moustique tigre [#9be9835c](https://github.com/incubateur-ademe/tacct/commit/9be9835c).
- Ajout d'une date d'affichage pour les notices [#58967f68](https://github.com/incubateur-ademe/tacct/commit/58967f68).
- Intégration des données relatives à l'arbovirose [#e0ddb640](https://github.com/incubateur-ademe/tacct/commit/e0ddb640) et [#70b036a8](https://github.com/incubateur-ademe/tacct/commit/70b036a8).

### Évolutions techniques
- Refactoring de l'application pour supprimer l'authentification, le mode sandbox et la page de login [#5f99525d](https://github.com/incubateur-ademe/tacct/commit/5f99525d).
- Suppression de dossiers et de fichiers inutiles [#ab91cb47](https://github.com/incubateur-ademe/tacct/commit/ab91cb47).
- Mise à jour de Prisma [#43490918](https://github.com/incubateur-ademe/tacct/commit/43490918).
- Mise à jour des packages et des dépendances [#dfd0b4a7](https://github.com/incubateur-ademe/tacct/commit/dfd0b4a7).
- Amélioration du processus de build et correction de problèmes liés à la configuration de l'environnement [#2dd2a501](https://github.com/incubateur-ademe/tacct/commit/2dd2a501), [#42cd56c0](https://github.com/incubateur-ademe/tacct/commit/42cd56c0) et [#e53620fe](https://github.com/incubateur-ademe/tacct/commit/e53620fe).
- Refactoring des noms de l'application tacct [#4e38b545](https://github.com/incubateur-ademe/tacct/commit/4e38b545).
- Correction d'un problème lié à la variable d'environnement `x-forwarded-host` [#5dcb8833](https://github.com/incubateur-ademe/tacct/commit/5dcb8833).

### Autres changements
- Ajout d'un nouveau bouton [#78a23220](https://github.com/incubateur-ademe/tacct/commit/78a23220).
- Correction de coquilles et de liens brisés [#7a879f38](https://github.com/incubateur-ademe/tacct/commit/7a879f38) et [#28b45844](https://github.com/incubateur-ademe/tacct/commit/28b45844).
- Ajout de tests E2E et Jest [#b60bafbe](https://github.com/incubateur-ademe/tacct/commit/b60bafbe).
- Correction d'un problème de z-index pour les modales [#3c2ed87d](https://github.com/incubateur-ademe/tacct/commit/3c2ed87d).
- Mise à jour de la base de données pour la qualité des sites de baignade [#c678cbff](https://github.com/incubateur-ademe/tacct/commit/c678cbff).
- Migration des données relatives au confort thermique [#c898ca8f](https://github.com/incubateur-ademe/tacct/commit/c898ca8f).
- Mise à jour du bucket RGA et de la table grand âge [#77a9f125](https://github.com/incubateur-ademe/tacct/commit/77a9f125).
- Ajout d'un iframe [#a451aab4](https://github.com/incubateur-ademe/tacct/commit/a451aab4).
