## Changelog : karfur (30 derniers jours, au 16 juillet 2026)

### Résumé
Les dernières mises à jour de karfur se concentrent sur l'intégration et la synchronisation des données des opérateurs AGIR depuis Grist, ainsi que sur des corrections de bugs et des améliorations de l'interface utilisateur. Des améliorations ont également été apportées à la gestion des fiches et des favoris.

### Évolutions fonctionnelles
- Possibilité de rendre le titre de la marque optionnel sur les dispositifs.
- Amélioration de l'accessibilité et de l'affichage des niveaux de français sur les fiches.
- Surlignage des adresses e-mail sur les fiches RCO.
- Correction d'un bug empêchant l'accès et l'ajout de fiches aux favoris [#3839](https://github.com/refugies-info/karfur/issues/3839).
- Correction d'un bug empêchant l'affichage du responsable principal dans une modale.
- Mise à jour du texte sur la page "Mission et Impact".
- Correction d'un problème de création d'agents sur Letta/Letta Code [#3823](https://github.com/refugies-info/karfur/issues/3823).

### Évolutions techniques
- Intégration de la synchronisation des opérateurs AGIR depuis Grist avec gestion des erreurs et mise à jour des messages.
- Ajout de la publication du JSON des opérateurs sur GCS.
- Ajout d'un déclenchement admin pour la synchronisation des opérateurs AGIR.
- Amélioration de la copie de l'application construite pour inclure les chunks nécessaires au build Docker.
- Ajout de secrets pour l'API Grist dans la configuration Cloud Build.
- Amélioration de la gestion des erreurs de synchronisation AGIR.
- Lecture des opérateurs depuis le JSON GCS.
- Normalisation des opérateurs AGIR et ajout de tests associés.
- Ajout de documents de synchronisation des opérateurs AGIR depuis Grist.
- Correction du typage pour les favoris.

### Autres changements
- Mise à jour de la documentation sur la synchronisation des opérateurs AGIR.
- Suppression de logs de console inutiles.
- Suppression d'une div vide inutile.
- Clarification des clés de traduction.
- Tri des résultats par `algoliaIds`.
- Correction de la syntaxe des diagrammes Mermaid dans la documentation.
