## Changelog : mutafriches (30 derniers jours, au 22 juillet 2026)

### Résumé
Ce mois-ci, l'application mutafriches a connu des améliorations significatives en termes de fonctionnalités et d'expérience utilisateur. Les principales évolutions concernent l'ajout de nouvelles pages (partenaires, résultats, données utilisées), l'intégration de services tiers (Zcal), et des corrections pour améliorer la précision des données et l'interface utilisateur.

### Évolutions fonctionnelles
- Ajout d'une page dédiée aux partenaires SCET et à la résolution d'IDU [#157](https://github.com/incubateur-ademe/mutafriches/issues/157).
- Réactivation de la fonctionnalité fret et de la comparaison avec Cartofriches [#159](https://github.com/incubateur-ademe/mutafriches/issues/159).
- Nouvelle page "Résultats" avec intégration de Zcal et suppression des références aux adresses mail de contact [#140](https://github.com/incubateur-ademe/mutafriches/issues/140), [#144](https://github.com/incubateur-ademe/mutafriches/issues/144).
- Ajout d'une page "Données utilisées" pour la transparence sur les sources de données [#137](https://github.com/incubateur-ademe/mutafriches/issues/137).
- Mise à jour de la page partenaires [#146](https://github.com/incubateur-ademe/mutafriches/issues/146).
- Amélioration du wording de la qualification manuelle [#151](https://github.com/incubateur-ademe/mutafriches/issues/151).
- Ajout d'un suivi du canal partenaire [#162](https://github.com/incubateur-ademe/mutafriches/issues/162).
- Correction de l'affichage des dates dans les statistiques [#161](https://github.com/incubateur-ademe/mutafriches/issues/161).
- Correction des statistiques de l'incubateur [#160](https://github.com/incubateur-ademe/mutafriches/issues/160).
- Ajout de la version de l'algorithme de provenance [#154](https://github.com/incubateur-ademe/mutafriches/issues/154).
- Correction de l'unité de distance (mètres/kilomètres) [#153](https://github.com/incubateur-ademe/mutafriches/issues/153).
- Ajout d'une documentation sur la source des données et possibilité de télécharger un PDF [#152](https://github.com/incubateur-ademe/mutafriches/issues/152).
- Ajout d'une version en label non cliquable dans le footer [#143](https://github.com/incubateur-ademe/mutafriches/issues/143) et ajout de la version dans le footer [#142](https://github.com/incubateur-ademe/mutafriches/issues/142).
- Raccourcissement des libellés "Paysage" et "Voie de desserte" dans l'interface utilisateur [#158](https://github.com/incubateur-ademe/mutafriches/issues/158).

### Évolutions techniques
- Refactoring de la page multisites et de la page diagnostic [#132](https://github.com/incubateur-ademe/mutafriches/issues/132).
- Mise en place d'un identifiant visiteur anonyme persistant pour la récurrence, ajout des pages juridiques et configuration du storage [#134](https://github.com/incubateur-ademe/mutafriches/issues/134).
- Utilisation d'imports locaux pour lovac [#149](https://github.com/incubateur-ademe/mutafriches/issues/149).
- Suppression des fixtures [#148](https://github.com/incubateur-ademe/mutafriches/issues/148).
- Préchargement des scripts via l'API [#147](https://github.com/incubateur-ademe/mutafriches/issues/147).
- Synchronisation de la documentation avec le code [#145](https://github.com/incubateur-ademe/mutafriches/issues/145).
- Correction d'un problème avec le "integrateur origin guard" [#156](https://github.com/incubateur-ademe/mutafriches/issues/156).
- Correction du schéma WFS de ZAER [#150](https://github.com/incubateur-ademe/mutafriches/issues/150).

### Autres changements
- Mise à jour de la dépendance TypeScript vers la version 6.0.3 [#90](https://github.com/incubateur-ademe/mutafriches/issues/90).
- Mise à jour de la dépendance Nodemailer vers la version 9.0.1 [#135](https://github.com/incubateur-ademe/mutafriches/issues/135).
- Correction des vulnérabilités identifiées par Dependabot et suppression des fixtures Excel [#141](https://github.com/incubateur-ademe/mutafriches/issues/141).
- Mise à jour des dépendances de sécurité [#136](https://github.com/incubateur-ademe/mutafriches/issues/136).
