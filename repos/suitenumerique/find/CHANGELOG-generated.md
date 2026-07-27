## Changelog : find (30 derniers jours, au 06 juillet 2026)

### Résumé
Ce changelog présente les récentes améliorations apportées à Find, axées sur la configuration du déploiement via Helm et des ajustements techniques pour l'environnement local.  Aucune nouvelle fonctionnalité visible pour l'utilisateur n'a été introduite durant cette période.

### Évolutions fonctionnelles
*   Ajout de la possibilité de spécifier un `secretName` existant lors de l'utilisation du chart Helm, offrant plus de flexibilité pour la gestion des secrets. [#34583e](https://github.com/suitenumerique/find/commit/034583e)

### Évolutions techniques
*   Mise à jour de la version de Python à 3.14. [58553aa](https://github.com/suitenumerique/find/commit/58553aa)
*   Modification des ports exposés des conteneurs pour l'environnement local. [025e6d0](https://github.com/suitenumerique/find/commit/025e6d0)
*   Annulation de la suppression du service `dockerize` et de l'unification des index de recherche avec la portée du service. [3483ca1](https://github.com/suitenumerique/find/commit/3483ca1) et [bec4fd9](https://github.com/suitenumerique/find/commit/bec4fd9)
