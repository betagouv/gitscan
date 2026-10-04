## Changelog : ecopass (30 derniers jours, au 01/10/2026)

### Résumé
Ce mois-ci, la plateforme a bénéficié de nombreuses améliorations visant à enrichir l'information disponible pour les utilisateurs (détails produits, paramètres de calcul) et à fluidifier les processus de déclaration. L'expérience utilisateur a été optimisée, notamment sur mobile et via de nouveaux outils de recherche et d'exportation, tout en renforçant la stabilité du système.

### Évolutions fonctionnelles
- **Nouvelles fonctionnalités**
  - Gestion des délégations ([#233](https://github.com/incubateur-ademe/ecopass/issues/233)).
  - Recherche de produits au sein des lots ([#219](https://github.com/incubateur-ademe/ecopass/issues/219)).
  - Exportation de fichiers au format SVG ([#212](https://github.com/incubateur-ademe/ecopass/issues/212)).
  - Introduction de la gestion de la masse des produits ([#220](https://github.com/incubateur-ademe/ecopass/issues/220)).
  - Amélioration de la sélection des matériaux ([#222](https://github.com/incubateur-ademe/ecopass/issues/222)).
  - Ajout d'un sélecteur de pays dans les formulaires ([#225](https://github.com/incubateur-ademe/ecopass/issues/225)).

- **Enrichissement de l'information et de l'expérience utilisateur**
  - Ajout de détails contextuels sur les produits déclarés ([#236](https://github.com/incubateur-ademe/ecopass/issues/236)), les produits déclarables ([#224](https://github.com/incubateur-ademe/ecopass/issues/224)), les paramètres de calcul ([#231](https://github.com/incubateur-ademe/ecopass/issues/231)) et les résultats du Design System ([#223](https://github.com/incubateur-ademe/ecopass/issues/223)).
  - Optimisation de l'interface de déclaration pour une utilisation sur mobile ([#228](https://github.com/incubateur-ademe/ecopass/issues/228)).
  - Simplification des formulaires : le champ prix est désormais optionnel ([#226](https://github.com/incubateur-ademe/ecopass/issues/226)) et la date de naissance n'est plus requise.
  - Ajout d'informations légales et de précisions sur FranceConnect ([#213](https://github.com/incubateur-ademe/ecopass/issues/213)).

- **Corrections et ajustements**
  - Correction de l'exportation CSV et de la gestion des lots sans GTIN ([#237](https://github.com/incubateur-ademe/ecopass/issues/237)).
  - Résolution de problèmes d'affichage sur les menus déroulants et les composants UI ([#227](https://github.com/incubateur-ademe/ecopass/issues/227), [#229](https://github.com/incubateur-ademe/ecopass/issues/229)).
  - Correction de l'affichage des masses de produits ([#230](https://github.com/incubateur-ademe/ecopass/issues/230)).
  - Ajustement des droits d'accès : l'exportation est désormais accessible à tous et l'accès au Design System est limité aux citoyens ([#214](https://github.com/incubateur-ademe/ecopass/issues/214)).

### Évolutions techniques
- **Optimisation des performances et de la stabilité**
  - Mise en place d'un export par lots pour améliorer la gestion des gros volumes de données ([#208](https://github.com/incubateur-ademe/ecopass/issues/208)).
  - Résolution d'un problème de consommation de mémoire (RAM) sur la vue liste des produits ([#221](https://github.com/incubateur-ademe/ecopass/issues/221)).
  - Amélioration de l'observabilité via l'ajout de logs sur les fonctions serveur et les routes API ([#211](https://github.com/incubateur-ademe/ecopass/issues/211)).
  - Correction de la procédure de build.
  - Ajustement du délai de déconnexion automatique (logout timeout).

### Autres changements
- Nettoyage du code (suppression des `console.log`).
- Mise à jour des textes de l'interface et des noms de marques.
