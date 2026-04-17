## Changelog : impactco2 (30 derniers jours, au 15 avril 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs et l'amélioration de l'expérience utilisateur, notamment au niveau des étiquettes d'information et de l'intégration de contenu externe via des iframes. De nouvelles statistiques ont été ajoutées et des ajustements ont été faits pour améliorer la gestion du temps d'engagement dans les simulateurs.

### Évolutions fonctionnelles
- Correction de l'adresse du Bioparc.
- Amélioration de l'accessibilité des étiquettes d'information ([#876](https://github.com/incubateur-ademe/impactco2/issues/876)).
- Ajustement de la hauteur des boutons sur les étiquettes animées de livraison.
- Modification de la formulation des mentions légales sur les étiquettes.
- Ajout de nouvelles statistiques ([#873](https://github.com/incubateur-ademe/impactco2/issues/873)).
- Gestion du temps d'engagement en fonction du simulateur utilisé.
- Mise en cache des données de la FAQ ([#871](https://github.com/incubateur-ademe/impactco2/issues/871)).
- Correction du zoom sur les logos du footer.

### Évolutions techniques
- Optimisation de l'appel à Google Maps pour qu'il soit effectué côté serveur ([#874](https://github.com/incubateur-ademe/impactco2/issues/874)).
- Suppression du rendu côté serveur (SSR) pour la page Notion.
- Ajout de gestion d'erreur (Error Boundary) aux composants Notion.
- Suppression d'une vérification inutile.
- Mise à jour de la librairie npm ([#875](https://github.com/incubateur-ademe/impactco2/issues/875)).
- Mise à jour de la librairie iframe resizer.

### Autres changements
- Ajout de tests pour le Bioparc.
- Correction de problèmes de rendu excessif dans l'adresse.
- Ajustement de la largeur maximale des étiquettes grises ([#877](https://github.com/incubateur-ademe/impactco2/issues/877)).
- Amélioration de la formulation d'une petite note d'avertissement sur les étiquettes.
