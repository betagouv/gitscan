## Changelog : espace-membre-next (30 derniers jours, au 2026-05-21)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs, l'amélioration de l'accessibilité et l'ajout de nouvelles fonctionnalités pour la gestion des startups et des phases. Des efforts ont également été déployés pour moderniser la stack technique et améliorer la robustesse du système, notamment en corrigeant des problèmes liés à la synchronisation des emails et à la configuration de l'environnement de production.

### Évolutions fonctionnelles
- Amélioration de la recherche : Ajout d'un champ de recherche combiné pour les startups, facilitant leur identification et leur sélection. [#1324](https://github.com/betagouv/espace-membre-next/issues/1324)
- Gestion des phases : Mise à jour et amélioration de la gestion des phases, avec alignement des libellés sur beta.gouv.fr. [#1384](https://github.com/betagouv/espace-membre-next/issues/1384) et [#1304](https://github.com/betagouv/espace-membre-next/issues/1304)
- Gestion des événements startups : Correction des noms des événements pour les startups. [#1385](https://github.com/betagouv/espace-membre-next/issues/1385)
- Création d'emails : Correction d'un bug empêchant la création d'emails lorsque l'adresse email principale n'était pas définie. [#1342](https://github.com/betagouv/espace-membre-next/issues/1342)

### Évolutions techniques
- Accessibilité : Amélioration significative de l'accessibilité (RGAA) avec correction de plusieurs points :
    - Ajout de l'attribut `lang` sur la balise `<html>`. [#1361](https://github.com/betagouv/espace-membre-next/issues/1361)
    - Remplacement des labels orphelins par des labels FR. [#1363](https://github.com/betagouv/espace-membre-next/issues/1363)
    - Rendre les éléments `onClick` statiques accessibles au clavier. [#1364](https://github.com/betagouv/espace-membre-next/issues/1364)
    - Activation du preset recommandé jsx-a11y pour une meilleure conformité. [#1355](https://github.com/betagouv/espace-membre-next/issues/1355)
- Sécurité : Renforcement de la sécurité en appliquant une vérification d'authentification lors de la mise à jour des événements. [#1357](https://github.com/betagouv/espace-membre-next/issues/1357) et suppression d'un TODO lié à l'authentification. [#1354](https://github.com/betagouv/espace-membre-next/issues/1354)
- Modernisation : Migration du système de templating d'emails de MJML. [#1350](https://github.com/betagouv/espace-membre-next/issues/1350)
- Infrastructure : Augmentation du timeout pour la synchronisation des emails afin d'améliorer la fiabilité. [#1372](https://github.com/betagouv/espace-membre-next/issues/1372)
- Composants : Utilisation du composant `DataVisualization` au lieu d'un asset SVG supprimé. [#1351](https://github.com/betagouv/espace-membre-next/issues/1351)

### Autres changements
- Nettoyage : Suppression de code legacy lié aux emails. [#1375](https://github.com/betagouv/espace-membre-next/issues/1375) et renommage/documentation de la tâche de rappel de phase. [#1374](https://github.com/betagouv/espace-membre-next/issues/1374)
- Configuration : Suppression du fichier `.dotenv` et correction de problèmes liés à la configuration de l'environnement de production (ESM). [#1339](https://github.com/betagouv/espace-membre-next/issues/1339), [#1338](https://github.com/betagouv/espace-membre-next/issues/1338), [#1337](https://github.com/betagouv/espace-membre-next/issues/1337)
- Dépendances : Mise à jour de certaines dépendances. [#1331](https://github.com/betagouv/espace-membre-next/issues/1331)
- Correction de contraintes : Mise à jour des contraintes sur le nom des phases. [#1356](https://github.com/betagouv/espace-membre-next/issues/1356)
- Nettoyage du code : Suppression de code inutile. [#1383](https://github.com/betagouv/espace-membre-next/issues/1383)
