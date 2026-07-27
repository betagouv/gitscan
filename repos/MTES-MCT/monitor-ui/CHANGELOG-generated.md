## Changelog : monitor-ui (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette version apporte des améliorations à l'interface utilisateur, notamment un nouveau composant de gestion de fichiers, des corrections de bugs pour améliorer la convivialité et la stabilité, ainsi que des optimisations de performance pour la recherche dans les arbres de données.

### Évolutions fonctionnelles
- Ajout d'un nouveau composant `FileUploader` pour la gestion des fichiers, incluant la possibilité de supprimer des fichiers par index et un affichage tronqué des noms de fichiers avec une ellipse. [#61865ba](https://github.com/MTES-MCT/monitor-ui/commit/61865ba91afb4e4559bd2c01264e37b8e8947853)
- Ajout d'un bouton de suppression standardisé pour les composants. [#b4662dc](https://github.com/MTES-MCT/monitor-ui/commit/b4662dc76324ac5e57b623be68a4a76afc6bcfa3)
- Amélioration de l'affichage des éléments tronqués dans le composant `CheckTreePicker` : affichage du label complet au survol et correction du problème de superposition avec l'icône d'expansion. [#32d4b06](https://github.com/MTES-MCT/monitor-ui/commit/32d4b069b7568236224803797327695429495216), [#e3535cf](https://github.com/MTES-MCT/monitor-ui/commit/e3535cf83258c1364349854159489f731583947f)
- Ajout d'une nouvelle icône "Attachment". [#2a11112](https://github.com/MTES-MCT/monitor-ui/commit/2a111124d00120436ff18521ce4e711ff7bde63a)

### Évolutions techniques
- Optimisation de la recherche dans les arbres de données du composant `CustomSearch` pour éviter une complexité quadratique. [#e99201f](https://github.com/MTES-MCT/monitor-ui/commit/e99201f782f3251832147800992a247890017961)
- Exportation de types pour une meilleure utilisation des composants. [#de4c952](https://github.com/MTES-MCT/monitor-ui/commit/de4c95252f19893030a1a6ce4923121f1c4ec8ea)
- Suppression du padding interne superflu dans certains composants. [#2ba134b](https://github.com/MTES-MCT/monitor-ui/commit/2ba134bf27379d6168171037432baf7c60354398)
- Exportation de la fonction `convertImagesToThumbnails`. [#bf1519d](https://github.com/MTES-MCT/monitor-ui/commit/bf1519db24be1f58d15750c7830b19926ace06c3)
- Exportation d'un hook pour une meilleure réutilisabilité. [#9796ab6](https://github.com/MTES-MCT/monitor-ui/commit/9796ab60f61ff0ca1252d088fc911ffc0b55b037)

### Autres changements
- Correction d'un bug empêchant le téléchargement de fichiers si le type MIME ne correspondait pas. [#a335ecf](https://github.com/MTES-MCT/monitor-ui/commit/a335ecfc76bc7296cc791707b2f19706625de247)
- Corrections de style et de padding pour améliorer l'apparence des composants. [#5a4ac95](https://github.com/MTES-MCT/monitor-ui/commit/5a4ac95638994adc995d7a06cd52a838822741cc)
- Mises à jour de version (24.55.0 à 24.56.0).
