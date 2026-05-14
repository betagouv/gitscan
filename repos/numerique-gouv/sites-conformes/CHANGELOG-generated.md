## Changelog : sites-conformes (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la flexibilité et de la robustesse de la plateforme. Les principales évolutions concernent l'ajout d'une alternative de stockage des médias en PostgreSQL, des corrections de bugs sur l'interface utilisateur, et des améliorations de l'internationalisation pour une meilleure adaptation aux différents contextes linguistiques.  Un déploiement en un clic sur Scalingo a également été mis en place pour faciliter le déploiement de l'application.

### Évolutions fonctionnelles
- **Stockage des médias :** Possibilité de stocker les médias directement dans la base de données PostgreSQL, offrant une alternative au stockage sur S3. [#482](https://github.com/numerique-gouv/sites-conformes/issues/482)
- **Correction de bugs front-end :** Résolution de plusieurs bugs affectant l'interface utilisateur. [#486](https://github.com/numerique-gouv/sites-conformes/issues/486)
- **Formulaires :** Correction d'un problème lié au nettoyage des noms de champs de formulaire, assurant un fonctionnement correct des formulaires. [#492](https://github.com/numerique-gouv/sites-conformes/issues/492)
- **Internationalisation des champs de formulaire :** Les champs de formulaire sont maintenant internationalisables. [#473](https://github.com/numerique-gouv/sites-conformes/issues/473) et [#464](https://github.com/numerique-gouv/sites-conformes/issues/464) et [#481](https://github.com/numerique-gouv/sites-conformes/issues/481)

### Évolutions techniques
- **Déploiement simplifié :** Mise en place d'un déploiement en un clic sur la plateforme Scalingo, facilitant le déploiement et la gestion de l'application. [#484](https://github.com/numerique-gouv/sites-conformes/issues/484)
- **Optimisation du tutoriel :** Amélioration du panneau du tutoriel pour une meilleure expérience utilisateur. [#473](https://github.com/numerique-gouv/sites-conformes/issues/473)
- **Header configurable :** Correction d'un bug concernant le header configurable. [#469](https://github.com/numerique-gouv/sites-conformes/issues/469)
- **Cache constant :** Modification du nom d'une variable pour améliorer la clarté du code lié au cache. [#469](https://github.com/numerique-gouv/sites-conformes/issues/469)

### Autres changements
- Mise à jour du nom du dépôt. [#493](https://github.com/numerique-gouv/sites-conformes/issues/493)
- Plusieurs mises à jour de dépendances Python ont été effectuées. [#501](https://github.com/numerique-gouv/sites-conformes/issues/501) et [#483](https://github.com/numerique-gouv/sites-conformes/issues/483) et [#464](https://github.com/numerique-gouv/sites-conformes/issues/464)
