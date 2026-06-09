## Changelog : ecopass (30 derniers jours, au 8 juin 2026)

### Résumé
Ce mois-ci, l'équipe a principalement travaillé sur l'amélioration de l'importation et de l'exportation de données, ainsi que sur l'expérience utilisateur, notamment en ajoutant de l'aide contextuelle et en optimisant l'affichage des informations. Des corrections de bugs et des améliorations de performance ont également été apportées.

### Évolutions fonctionnelles
- Ajout de la gestion des composants multiples dans les fichiers CSV importés [#162](https://github.com/incubateur-ademe/ecopass/issues/162).
- Ajout de boutons d'aide contextuelle pour faciliter l'utilisation de la plateforme [#161](https://github.com/incubateur-ademe/ecopass/issues/161).
- Gestion des étiquettes complexes [#152](https://github.com/incubateur-ademe/ecopass/issues/152).
- Amélioration de l'affichage des images avec le GTIN et la comparaison [#153](https://github.com/incubateur-ademe/ecopass/issues/153).
- Les utilisateurs Bercy peuvent maintenant accéder aux données [#147](https://github.com/incubateur-ademe/ecopass/issues/147).
- Amélioration de la performance de la création de produits anonymisés.
- Ajout de la possibilité de tester la connexion à la base de données [#149](https://github.com/incubateur-ademe/ecopass/issues/149).
- Amélioration de la durabilité des exports [#156](https://github.com/incubateur-ademe/ecopass/issues/156).
- Correction de l'affichage du dernier lien actif [#157](https://github.com/incubateur-ademe/ecopass/issues/157).
- Correction de la couleur de l'étiquette de comparaison [#154](https://github.com/incubateur-ademe/ecopass/issues/154).

### Évolutions techniques
- Optimisation du streaming des produits lors des exports volumineux [#146](https://github.com/incubateur-ademe/ecopass/issues/146).
- Mise à jour des paquets, de Node et de pnpm [#145](https://github.com/incubateur-ademe/ecopass/issues/145).
- Correction d'un problème de "trim" flottant pour la quantité [#148](https://github.com/incubateur-ademe/ecopass/issues/148).
- Tri de l'API par nom [#151](https://github.com/incubateur-ademe/ecopass/issues/151).
- Correction de la taille et de la largeur des étiquettes simples [#163](https://github.com/incubateur-ademe/ecopass/issues/163) et [#164](https://github.com/incubateur-ademe/ecopass/issues/164).

### Autres changements
- Mise à jour de la documentation [#160](https://github.com/incubateur-ademe/ecopass/issues/160) et [#150](https://github.com/incubateur-ademe/ecopass/issues/150).
- Mise à jour du fichier README.
- Ajustement du timeout Matomo.
- Correction de la compatibilité avec pnpm 10 [#93e4b74](https://github.com/incubateur-ademe/ecopass/commit/93e4b74).
