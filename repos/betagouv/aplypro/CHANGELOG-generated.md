## Changelog : aplypro (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, les évolutions d'aplypro se concentrent sur l'amélioration de la gestion des adresses, la correction de bugs liés aux paiements MASA et à l'envoi de données à RNVP, ainsi que des améliorations de l'interface utilisateur et de la logique métier pour la gestion des élèves et des PFMP. Plusieurs corrections mineures et optimisations ont également été apportées.

### Évolutions fonctionnelles
- **Gestion des adresses :** Amélioration de la correction d'adresses avec l'intégration de `ASP::AdresseCorrectionRequest` [#1941]. Correction de plusieurs bugs liés aux mises à jour d'adresses [#1944].
- **Paiements MASA :** Déblocage des paiements MASA [#1933].
- **PFMP :** Affichage des messages d'erreur sur le formulaire de rectification d'une PFMP [#1933].
- **Informations élève :** Ajout d'informations complémentaires sur la page de détail de l'élève et modification de la présentation visuelle [#1933].
- **Gestion des doublons RNVP :** Correction d'un problème d'envoi de doublons de données à RNVP [#1933].
- **Gestion de la double scolarité :** Prise en charge de la double scolarité d'un élève dans une même classe [#1923].
- **Abrogation des DA :** Modification de la logique et de l'affichage du bouton d'abrogation des DA.

### Évolutions techniques
- **API RNVP :** Correction des bugs liés à l'appel à l'API RNVP [#1922].
- **Refactoring :** Renommage de méthodes pour une meilleure lisibilité et suppression de l'opérateur bang sur `merge_date_range`.
- **Tests :** Ajout de tests unitaires pour FREGATA et SYGNE. Correction de tests existants.
- **Dépendances :** Mise à jour de plusieurs dépendances : `addressable` [#1940], `rack-session` [#1939], `rack` [#1936].
- **Optimisation :** Amélioration de la gestion des appels batch à RNVP pour les grands nombres d'élèves.

### Autres changements
- **Documentation :** Traductions des messages d'erreur en français.
- **Nettoyage de code :** Suppression de code obsolète et correction de problèmes de style avec Rubocop.
- **Version :** Mise à jour de la version de l'application à 2.9.1 et 2.9.2.
