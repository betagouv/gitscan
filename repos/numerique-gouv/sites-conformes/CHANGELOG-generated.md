## Changelog : sites-conformes (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la préparation de la version 3.2.0 avec une packagification du projet et une organisation des sources.  Une nouvelle fonctionnalité majeure permet désormais le stockage des médias directement en base de données PostgreSQL, offrant une alternative à l'utilisation de S3. Des corrections de bugs ont également été apportées, notamment sur le front-end et dans la gestion des noms de champs de formulaire. L'ajout de Sentry permettra un meilleur suivi des erreurs en production.

### Évolutions fonctionnelles
- **Stockage des médias en PostgreSQL :**  Il est maintenant possible de stocker les médias (images, documents, etc.) directement dans la base de données PostgreSQL, offrant une alternative à l'utilisation de services de stockage externes comme S3. [#482](https://github.com/numerique-gouv/sites-conformes/issues/482)
- **Correction de bugs front-end :** Des corrections de bugs ont été implémentées sur l'interface utilisateur pour améliorer l'expérience utilisateur. [#486](https://github.com/numerique-gouv/sites-conformes/issues/486)
- **Correction du clean_name vide :**  Un bug empêchant le bon fonctionnement du nettoyage des noms de champs de formulaire a été résolu. [#492](https://github.com/numerique-gouv/sites-conformes/issues/492)

### Évolutions techniques
- **Packagification du projet :** Le projet a été packagé pour faciliter sa distribution et son installation. [#506](https://github.com/numerique-gouv/sites-conformes/issues/506) et [#514](https://github.com/numerique-gouv/sites-conformes/issues/514)
- **Organisation des sources :** Les sources du projet ont été réorganisées et renommées pour une meilleure structure.
- **Ajout de Sentry :** L'outil de surveillance des erreurs Sentry a été intégré pour améliorer la détection et le suivi des problèmes en production. [#445](https://github.com/numerique-gouv/sites-conformes/issues/445)
- **Mise à jour des dépendances Python :** Les dépendances Python du projet ont été mises à jour pour bénéficier des dernières corrections et améliorations. [#501](https://github.com/numerique-gouv/sites-conformes/issues/501)
- **Préparation de la version 3.2.0 :**  Plusieurs modifications ont été apportées pour préparer la sortie de la version 3.2.0, incluant des corrections automatiques et des ajustements de noms.

### Autres changements
- **Documentation mise à jour :** La documentation du projet a été mise à jour. [#511](https://github.com/numerique-gouv/sites-conformes/issues/511)
- **Changement de nom du dépôt :** Le nom du dépôt a été mis à jour. [#493](https://github.com/numerique-gouv/sites-conformes/issues/493)
- **Ajout de `demo` à `slugignore` :** Le mot `demo` a été ajouté à la liste des mots à ignorer lors de la génération des slugs.
