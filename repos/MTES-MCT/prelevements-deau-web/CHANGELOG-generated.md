## Changelog : prelevements-deau-web (30 derniers jours, au 25 mars 2026)

### Résumé
Cette mise à jour apporte des améliorations significatives à l'interface utilisateur, notamment une refonte des menus et des corrections concernant l'affichage des images sur les pages de tags.  L'infrastructure a également été améliorée avec l'ajout de déploiements automatisés sur Scaleway et l'intégration de Sentry pour la surveillance des erreurs.

### Évolutions fonctionnelles
- **Menus :** Refonte complète des menus de l'application ([#389](https://github.com/MTES-MCT/prelevements-deau-web/pull/389)).
- **Pages de tags :** Correction de l'affichage des images sur les pages de tags, notamment la pagination et la suppression d'images inutiles ([#432](https://github.com/MTES-MCT/prelevements-deau-web/pull/432)).
- **Composant UserbarPageAPILinkItem :** Mise à jour du composant pour améliorer son fonctionnement ([#462](https://github.com/MTES-MCT/prelevements-deau-web/pull/462)).
- **En-têtes :** Correction d'un problème lié aux en-têtes ([#459](https://github.com/MTES-MCT/prelevements-deau-web/pull/459)).

### Évolutions techniques
- **Déploiement :** Ajout d'actions pour le déploiement automatisé sur Scaleway.
- **Surveillance des erreurs :** Intégration de Sentry pour la surveillance et la gestion des erreurs.
- **Makefile :** Suppression du Makefile, probablement remplacé par d'autres outils de gestion de tâches.
- **Migrations :** Génération et application de nouvelles migrations de base de données.

### Autres changements
-  Aucun autre changement significatif à signaler.
