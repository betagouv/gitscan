## Changelog : karfur (30 derniers jours, au 23 juillet 2026)

### Résumé
Les dernières mises à jour de karfur se concentrent sur l'amélioration de l'expérience utilisateur, notamment en affichant des informations plus complètes sur les dispositifs et démarches, et en corrigeant des bugs liés à la recherche et aux favoris. Des améliorations techniques ont également été apportées pour faciliter la synchronisation des données et améliorer la robustesse de l'application.

### Évolutions fonctionnelles
- Affichage du nom du responsable ou du financeur principal sur les pages des dispositifs et démarches. [#3847](https://github.com/refugies-info/karfur/pull/3847)
- Possibilité de rendre le titre de la marque optionnel lors de la création ou modification d'un dispositif. [#3840](https://github.com/refugies-info/karfur/pull/3840)
- Correction du comptage incorrect du nombre de contributeurs sur une démarche. [#3845](https://github.com/refugies-info/karfur/pull/3845)
- Amélioration de la recherche sur les pages en langues autres que le français. [#3843](https://github.com/refugies-info/karfur/pull/3843)
- Correction d'un bug empêchant l'accès aux fiches et l'ajout de favoris sur certains navigateurs. [#3839](https://github.com/refugies-info/karfur/pull/3839)
- Correction de l'affichage des erreurs modales concernant les membres principaux. [#3839](https://github.com/refugies-info/karfur/pull/3839)
- Correction du surlignage des niveaux de français sur l'interface utilisateur. [#3835](https://github.com/refugies-info/karfur/pull/3835)
- Amélioration du maillage sémantique des mots-clés pour les démarches. [#3836](https://github.com/refugies-info/karfur/pull/3836)

### Évolutions techniques
- Amélioration de la copie de l'application construite pour inclure les chunks nécessaires au bon fonctionnement. [#3832](https://github.com/refugies-info/karfur/pull/3832)
- Ajout de secrets pour l'API Grist dans la configuration Cloud Build pour la synchronisation des opérateurs AGIR. [#3830](https://github.com/refugies-info/karfur/pull/3830)
- Implémentation de la synchronisation des opérateurs AGIR depuis Grist, avec gestion des erreurs et mise à jour des messages. [#3820](https://github.com/refugies-info/karfur/pull/3820)
- Normalisation des opérateurs AGIR et ajout de tests associés. [#3820](https://github.com/refugies-info/karfur/pull/3820)
- Publication du JSON des opérateurs sur Google Cloud Storage (GCS). [#3820](https://github.com/refugies-info/karfur/pull/3820)
- Ajout de la lecture des opérateurs depuis le JSON stocké sur GCS. [#3820](https://github.com/refugies-info/karfur/pull/3820)
- Amélioration de la gestion des erreurs de synchronisation des opérateurs AGIR. [#3820](https://github.com/refugies-info/karfur/pull/3820)

### Autres changements
- Ajout d'un hook pre-commit GitLeaks pour la détection de secrets.
- Correction de la référence de version de lodash dans le fichier pnpm-workspace.yaml.
- Amélioration des messages de synchronisation et ajustement du formatage du code pour la synchronisation AGIR.
- Ajout d'un champ "shortName" pour les webhooks.
- Ajout d'une couleur "short" pour les webhooks.
