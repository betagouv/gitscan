## Changelog : impactco2 (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs et l'amélioration de l'expérience utilisateur, notamment au niveau des étiquettes d'information et de l'intégration de contenu externe via des iframes. De nouvelles statistiques ont également été ajoutées et la gestion du temps d'engagement dans les simulateurs a été affinée.

### Évolutions fonctionnelles
- Correction de l'adresse du Bioparc.
- Amélioration de l'accessibilité des étiquettes d'information. [#876](https://github.com/incubateur-ademe/impactco2/issues/876)
- Ajustement de la hauteur des boutons sur les étiquettes d'information animées pour la livraison.
- Modification de la formulation des mentions légales sur les étiquettes.
- Correction de la largeur maximale des étiquettes grises. [#877](https://github.com/incubateur-ademe/impactco2/issues/877)
- Ajout de nouvelles statistiques. [#873](https://github.com/incubateur-ademe/impactco2/issues/873)
- Gestion du temps d'engagement dans les simulateurs en fonction du contexte.
- Mise en cache des données de la FAQ pour une meilleure performance. [#871](https://github.com/incubateur-ademe/impactco2/issues/871)

### Évolutions techniques
- Optimisation de l'appel à la carte (callgmap) pour une exécution côté serveur. [#874](https://github.com/incubateur-ademe/impactco2/issues/874)
- Suppression du rendu côté serveur (SSR) pour le contenu de Notion.
- Ajout d'une gestion des erreurs (error boundary) aux composants Notion pour une meilleure robustesse.
- Correction de valeurs dans le checker d'iframes.
- Suppression d'une vérification inutile.

### Autres changements
- Mise à jour de npm. [#875](https://github.com/incubateur-ademe/impactco2/issues/875)
- Ajout de tests pour le Bioparc.
- Correction du zoom sur les logos du footer.
