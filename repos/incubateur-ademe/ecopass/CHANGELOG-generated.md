## Changelog : ecopass (30 derniers jours, au 01 juin 2026)

### Résumé
Les dernières mises à jour d'ecopass se concentrent sur l'amélioration de la performance, la correction de bugs visuels et fonctionnels, ainsi que l'ajout de fonctionnalités pour répondre aux besoins spécifiques des utilisateurs, notamment l'accès aux données pour les utilisateurs Bercy et l'amélioration des exports massifs.

### Évolutions fonctionnelles
- Amélioration de la gestion des étiquettes complexes, permettant une meilleure représentation des informations sur les produits. [#152](https://github.com/incubateur-ademe/ecopass/issues/152)
- Les utilisateurs de Bercy peuvent désormais accéder aux données. [#147](https://github.com/incubateur-ademe/ecopass/issues/147) et [#144](https://github.com/incubateur-ademe/ecopass/issues/144)
- Correction de l'affichage de la couleur de l'étiquette de comparaison. [#154](https://github.com/incubateur-ademe/ecopass/issues/154)
- Correction de l'affichage de l'image avec le GTIN et la comparaison. [#153](https://github.com/incubateur-ademe/ecopass/issues/153)
- Amélioration de la performance lors de la création de produits anonymisés.
- Correction d'un bug lié à l'arrondi des quantités flottantes. [#148](https://github.com/incubateur-ademe/ecopass/issues/148)
- Amélioration de la gestion des exports massifs de produits, notamment en utilisant un système de streaming pour les gros fichiers. [#146](https://github.com/incubateur-ademe/ecopass/issues/146)
- L'ordre des éléments dans l'API a été modifié pour être trié par nom. [#151](https://github.com/incubateur-ademe/ecopass/issues/151)

### Évolutions techniques
- Mise à jour des paquets, de Node.js et de pnpm. [#145](https://github.com/incubateur-ademe/ecopass/issues/145)
- Ajout d'un test de connexion pour faciliter le diagnostic des problèmes de connectivité. [#149](https://github.com/incubateur-ademe/ecopass/issues/149)
- Correction de problèmes de compatibilité avec pnpm 10. [#93e4b74](https://github.com/incubateur-ademe/ecopass/commit/93e4b74)

### Autres changements
- Mise à jour de la documentation. [#150](https://github.com/incubateur-ademe/ecopass/issues/150)
- Mise à jour du fichier README.
- Ajustement du timeout de Matomo.
