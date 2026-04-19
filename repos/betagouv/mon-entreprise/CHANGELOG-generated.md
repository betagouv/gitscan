## Changelog : mon-entreprise (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur la modernisation et la maintenance du simulateur, notamment avec la refactorisation du code, la mise à jour des règles de calcul (cotisations, impôts) pour 2026 et la préparation à la suppression du simulateur RGCP. Des améliorations ont également été apportées à l'expérience utilisateur, comme la correction de bugs et l'ajout d'informations plus claires.

### Évolutions fonctionnelles
- Suppression du simulateur RGCP.
- Amélioration de l'affichage des informations de l'entreprise sélectionnée.
- Correction de l'affichage des caisses de retraite PLR dans le simulateur.
- Ajout d'un bandeau rouge pour signaler la présence de règles obsolètes.
- Ajout d'un bandeau d'information pour les simulations en cours de chargement [#4433](https://github.com/betagouv/mon-entreprise/issues/4433).
- Correction du calcul des cotisations de début d'activité au régime micro-fiscal.
- Correction de l'affichage des professions libérales dans le simulateur.
- Ajout de liens vers le simulateur pour les indépendants depuis d'autres simulateurs.
- Ajout de la possibilité de choisir entre IR et IS pour les indépendants.
- Ajout d'un avertissement en cas de pension invalidité.
- Correction de la navigation entre les simulateurs indépendants.
- Correction de l'affichage des informations de l'entreprise.
- Correction de l'affichage des dividendes.

### Évolutions techniques
- Refactorisation importante du code, notamment pour la gestion des règles, des composants et du store.
- Mise à jour de la version de Node.js.
- Mise à jour des actions CI/CD.
- Amélioration de la performance du chargement des règles.
- Utilisation d'un modèle de règles par simulateur pour une meilleure organisation.
- Suppression de code commenté et de dépendances obsolètes.
- Amélioration des tests unitaires et des snapshots.
- Découplage du `safeSetSituation` du cache engine.
- Exportation du type `OrigineSimulation` pour une meilleure typage.
- Utilisation de `useOptionalEngine` pour une gestion plus flexible des moteurs de règles.
- Simplification de l'action `ajusteLaSituation` dans le store.

### Autres changements
- Mise à jour des plafonds de CA.
- Mise à jour des références exonérations.
- Mise à jour des taux de cotisation et des règles de calcul pour 2026.
- Correction de fautes de frappe et amélioration de la documentation.
- Ajout de traductions.
- Amélioration de la documentation interne.
- Mise à jour des dépendances (hors mises à jour automatiques).
- Correction du formatage Prettier.
