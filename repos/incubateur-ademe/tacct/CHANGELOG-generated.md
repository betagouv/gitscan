## Changelog : tacct (30 derniers jours, au 16 avril 2026)

### Résumé
Ce mois-ci, tacct a connu une importante phase de refactoring et de mise à jour des données. Plusieurs sources de données ont été mises à jour (incendies de forêt, agriculture biologique, feux de forêt, sites de baignade, confort thermique, grand âge, plans d'eau) et des améliorations ont été apportées à l'interface utilisateur, notamment au niveau des modales et des boutons. Des corrections de bugs et des optimisations de build ont également été réalisées.

### Évolutions fonctionnelles
- Mise à jour des données relatives aux **incendies de forêt** [#1699e4c2](https://github.com/incubateur-ademe/tacct/commit/1699e4c2).
- Mise à jour des données relatives à l'**agriculture biologique** [#e041c2b3](https://github.com/incubateur-ademe/tacct/commit/e041c2b3).
- Mise à jour des données relatives aux **feux de forêt** et aux **surfaces en agriculture biologique** [#18a76aac](https://github.com/incubateur-ademe/tacct/commit/18a76aac).
- Amélioration de la modale des **collections** (slider) [#a82ae2a2](https://github.com/incubateur-ademe/tacct/commit/a82ae2a2).
- Ajout de données concernant les **sites de baignade** et migration des données de qualité [#c678cbff](https://github.com/incubateur-ademe/tacct/commit/c678cbff).
- Mise à jour des données relatives au **confort thermique** [#c898ca8f](https://github.com/incubateur-ademe/tacct/commit/c898ca8f).
- Mise à jour des données relatives à la population **grand âge** [#77a9f125](https://github.com/incubateur-ademe/tacct/commit/77a9f125).
- Ajout d'un **iframe** pour l'intégration de contenu externe [#a451aab4](https://github.com/incubateur-ademe/tacct/commit/a451aab4).
- Amélioration de l'affichage et de la réactivité des informations concernant le **moustique tigre** [#9be9835c](https://github.com/incubateur-ademe/tacct/commit/9be9835c).
- Intégration des données **arbovirose** et **moustique tigre** [#70b036a8](https://github.com/incubateur-ademe/tacct/commit/70b036a8).
- Mise à jour des **sources des indicateurs** [#32455dc4](https://github.com/incubateur-ademe/tacct/commit/32455dc4).
- Mise à jour des données des **plans d'eau** [#f31537e2](https://github.com/incubateur-ademe/tacct/commit/f31537e2).
- Ajout de nouveaux noms pour tacct [#4e38b545](https://github.com/incubateur-ademe/tacct/commit/4e38b545).

### Évolutions techniques
- Refactoring du **robots.txt** et du **sitemap** pour améliorer le référencement [#4974eb40](https://github.com/incubateur-ademe/tacct/commit/4974eb40).
- Changement de la commande de **build** pour optimiser le processus [#b129b88b](https://github.com/incubateur-ademe/tacct/commit/b129b88b).
- Suppression de l'authentification, du sandbox et de la page de login, ainsi que mise à jour des modèles Prisma [#5f99525d](https://github.com/incubateur-ademe/tacct/commit/5f99525d).
- Suppression de dossiers inutiles et de code obsolète [#ab91cb47](https://github.com/incubateur-ademe/tacct/commit/ab91cb47).
- Correction d'une erreur de configuration liée à `x-forwarded-host` [#5dcb8833](https://github.com/incubateur-ademe/tacct/commit/5dcb8833).
- Mise à jour de la version de `pg` dans le build [#2dd2a501](https://github.com/incubateur-ademe/tacct/commit/2dd2a501).
- Suppression de la page de login des statistiques [#f2c1c49c](https://github.com/incubateur-ademe/tacct/commit/f2c1c49c).

### Autres changements
- Correction d'un bug lié au **z-index** d'une modale et des cookies [#3c2ed87d](https://github.com/incubateur-ademe/tacct/commit/3c2ed87d).
- Ajout d'un nouveau bouton avec un style amélioré [#78a23220](https://github.com/incubateur-ademe/tacct/commit/78a23220).
- Correction de liens de **redirection cassés** [#7a879f38](https://github.com/incubateur-ademe/tacct/commit/7a879f38).
- Correction de coquilles dans le texte [#28b45844](https://github.com/incubateur-ademe/tacct/commit/28b45844).
- Correction d'un bug lié à la recette **arbovirose** [#e0ddb640](https://github.com/incubateur-ademe/tacct/commit/e0ddb640).
- Fermeture de l'API Metabase [#0b37bd44](https://github.com/incubateur-ademe/tacct/commit/0b37bd44).
- Mise à jour de Prisma [#43490918](https://github.com/incubateur-ademe/tacct/commit/43490918).
