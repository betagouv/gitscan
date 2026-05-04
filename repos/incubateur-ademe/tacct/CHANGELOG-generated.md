## Changelog : tacct (30 derniers jours, au 7 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur la mise à jour des données (incendies de forêt, agriculture biologique, qualité des sites de baignade, confort thermique) et sur des améliorations techniques de l'application, notamment concernant le build, la configuration et le refactoring du code. Des corrections de bugs ont également été apportées, notamment concernant l'affichage de la modale "collections".

### Évolutions fonctionnelles
- Correction d'un bug concernant le z-index de la modale "collections" [#1234](https://github.com/incubateur-ademe/tacct/issues/1234)
- Mise à jour des données relatives aux feux de forêt.
- Mise à jour des données relatives à l'agriculture biologique.
- Mise à jour des données relatives à la qualité des sites de baignade.
- Mise à jour des données relatives au confort thermique.
- Ajout d'une notice sur la page d'accueil.

### Évolutions techniques
- Refactoring du code pour supprimer les vieux sites de baignade.
- Refactoring du code pour renommer les noms de tacct.
- Refactoring du code pour supprimer des dossiers inutiles.
- Modification de la commande de build.
- Correction d'une erreur de configuration liée à `x-forwarded-host`.
- Mise à jour du bucket RGA et de la table "grand age".
- Refactoring des robots et du sitemap.

### Autres changements
- Ajout d'un iframe.
- Migration de la qualité des sites de baignade dans la base de données.
- Ajout d'un nouveau bouton (style).
