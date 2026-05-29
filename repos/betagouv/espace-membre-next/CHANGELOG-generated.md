## Changelog : espace-membre-next (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la gestion des phases de vie des projets, la correction de problèmes d'accessibilité et de sécurité, ainsi que l'ajout de nouvelles fonctionnalités de recherche et de synchronisation des données. Des améliorations techniques ont également été apportées pour moderniser le code et l'infrastructure.

### Évolutions fonctionnelles
- **Phases de projets :** Refonte de la gestion des phases de vie des projets, incluant un renommage de "perennisation" en "consolidation" et une harmonisation des libellés avec beta.gouv.fr [#1392, #1384, #1304].
- **Recherche :** Ajout d'un champ de recherche combiné pour les startups, facilitant leur identification et leur sélection [#1324].
- **Synchronisation des données :** Ajout d'une table `matrix_accounts` et d'un script de synchronisation associé [#1373].
- **Gestion des emails :** Correction d'un bug empêchant la création d'emails lorsque l'adresse email principale n'était pas définie [#1342].
- **Amélioration de la détection Tchap :** Optimisation de la détection de Tchap pour une meilleure efficacité [#1393].
- **Evénements startups :** Correction des noms des événements affichés [#1385].

### Évolutions techniques
- **Sécurité :** Renforcement de la sécurité en appliquant une vérification d'authentification lors de la mise à jour des événements [#1357].
- **Accessibilité :** Améliorations significatives de l'accessibilité (RGAA) :
    - Ajout de l'attribut `lang` sur la balise `<html>` [#1361].
    - Remplacement des labels orphelins par des éléments avec la classe `fr-label` [#1363].
    - Rendre les éléments `onClick` statiques accessibles au clavier [#1364].
    - Activation du preset recommandé jsx-a11y pour une meilleure conformité RGAA [#1355, #1365].
- **Modernisation du code :** Suppression de code obsolète lié aux emails et nettoyage de l'environnement [#1375, #1383].
- **Composants DSFR :** Utilisation du composant `DataVisualization` au lieu d'un asset SVG supprimé [#1351].
- **Migration MJML :** Migration vers MJML pour la gestion des templates d'emails [#1350].
- **Timeout dimail-sync :** Augmentation du timeout pour la synchronisation dimail [#1372].

### Autres changements
- **Documentation :** Mise à jour de la documentation pour la gestion des phases [#1374].
- **Nettoyage de code :** Suppression d'un TODO lié à l'authentification dans `validateNewMember` [#1354].
- **Contraintes phases :** Mise à jour des contraintes de nom des phases [#1356].
