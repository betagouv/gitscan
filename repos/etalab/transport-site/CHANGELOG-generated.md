## Changelog : transport-site (30 derniers jours)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration du support des données NeTEx, avec de nouvelles fonctionnalités pour la validation, l'extraction de métadonnées et la gestion des dates de validité. Des améliorations ont également été apportées à la consolidation des données IRVE et à la recherche de jeux de données. Enfin, des corrections et des optimisations diverses ont été réalisées pour améliorer la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **NeTEx :** Ajout d'un bouton de téléchargement toujours visible sur les ressources NeTEx [#5374](https://github.com/etalab/transport-site/issues/5374).
- **NeTEx :** Amélioration de l'affichage des erreurs XSD, regroupées par message pour une meilleure lisibilité [#5369](https://github.com/etalab/transport-site/issues/5369).
- **NeTEx :** Possibilité de télécharger le rapport de validation NeTEx [#5352](https://github.com/etalab/transport-site/issues/5352).
- **NeTEx :** Extraction des modes de transport et des réseaux [#5342](https://github.com/etalab/transport-site/issues/5342) et [#5351](https://github.com/etalab/transport-site/issues/5351).
- **NeTEx :** Ajout d'un flag indiquant l'absence de dates de validité et notification des ressources expirées [#5336](https://github.com/etalab/transport-site/issues/5336) et [#5337](https://github.com/etalab/transport-site/issues/5337).
- **IRVE :** Amélioration de la consolidation IRVE avec la remontée d'informations supplémentaires [#5321](https://github.com/etalab/transport-site/issues/5321) et la création d'un fichier dédoublonné [#5343](https://github.com/etalab/transport-site/issues/5343). Renommage du rapport de consolidation IRVE [#5359](https://github.com/etalab/transport-site/issues/5359).
- **Recherche :** Correction du tri des jeux de données (JDD) les plus récents [#5373](https://github.com/etalab/transport-site/issues/5373).
- **Recherche :** Amélioration de la recherche avec index en mémoire et facets [#5333](https://github.com/etalab/transport-site/issues/5333) et [#5340](https://github.com/etalab/transport-site/issues/5340).
- **Interface utilisateur :** Ajout d'un menu de navigation sur la page de détails des ressources [#5311](https://github.com/etalab/transport-site/issues/5311).
- **Géographie :** Ajout de la Suisse dans la liste des divisions administratives [#5367](https://github.com/etalab/transport-site/issues/5367).

### Évolutions techniques
- **Validation IRVE :** Autorisation de plusieurs espaces dans les coordonnées lors de la validation IRVE [#5318](https://github.com/etalab/transport-site/issues/5318).
- **Architecture :** Utilisation de jeux de données en mémoire pour la recherche, améliorant potentiellement la performance [#5345](https://github.com/etalab/transport-site/issues/5345).
- **Configuration :** Actualisation de la configuration ZFE [#5348](https://github.com/etalab/transport-site/issues/5348).
- **Unlock :** Désactivation du log de requêtes dans le plug TokenAuth pour améliorer la performance et la sécurité [#5314](https://github.com/etalab/transport-site/issues/5314).
- **Rapports :** Mise en place d'un rapport opérationnel avec un suivi global et détaillé [#5285](https://github.com/etalab/transport-site/issues/5285).

### Autres changements
- **Documentation :** Page de nouveautés mise à jour pour janvier 2026 [#5304](https://github.com/etalab/transport-site/issues/5304).
- **Code :** Nettoyage de code et suppression de code mort dans DatasetController [#5329](https://github.com/etalab/transport-site/issues/5329).
- **Code :** Correction d'une URL de ressource mal encodée [#5363](https://github.com/etalab/transport-site/issues/5363).
- **Code :** Suppression des PDC avec id_pdc_itinerance "non concerné" de la consolidation IRVE dédoublonnée [#5360](https://github.com/etalab/transport-site/issues/5360).
- **Code :** Divers refactorings et corrections [#5338](https://github.com/etalab/transport-site/issues/5338).
- **Code :** Nettoyage routinier [#5322](https://github.com/etalab/transport-site/issues/5322).
- **Code :** Correction d'un revert de la recherche par sous-type [#5324](https://github.com/etalab/transport-site/issues/5324).
- **Code :** Améliorations des extracteurs NeTEx [#5320](https://github.com/etalab/transport-site/issues/5320).
- **Code :** Correction d'un problème où la population était null dans order_datasets [#5328](https://github.com/etalab/transport-site/issues/5328).
- **Code :** Correction de warnings de compilation [#5344](https://github.com/etalab/transport-site/issues/5344).
