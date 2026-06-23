## Changelog : acces-cible (30 derniers jours, au 22 juin 2026)

### Résumé
Cette version apporte des améliorations significatives à l'import de données CSV, notamment en stabilisant le processus et en évitant les doublons de tags. De plus, un nouveau widget JDMA a été intégré et la configuration de ce dernier est désormais gérée via des variables d'environnement. Des optimisations ont également été apportées à la gestion des tests et à l'image Docker.

### Évolutions fonctionnelles
- Ajout d'un widget JDMA pour une fonctionnalité non précisée. [#569](https://github.com/betagouv/acces-cible/issues/569)
- Amélioration de la gestion des imports CSV : traitement en arrière-plan pour une meilleure stabilité et éviter les blocages. [#541](https://github.com/betagouv/acces-cible/issues/541)
- Correction d'un bug empêchant la normalisation correcte de l'URL des sites. [#576](https://github.com/betagouv/acces-cible/issues/576)
- Éviter la création de tags en doublon lors de l'import de fichiers CSV. [#577](https://github.com/betagouv/acces-cible/issues/577)
- Configuration du bouton JDMA désormais possible via des variables d'environnement. [#578](https://github.com/betagouv/acces-cible/issues/578)

### Évolutions techniques
- Refonte de l'image Docker pour utiliser le Dockerfile principal. [#547](https://github.com/betagouv/acces-cible/issues/547)
- Amélioration du mocking des tests Axe pour une meilleure fiabilité. [#586](https://github.com/betagouv/acces-cible/issues/586)
- Suppression d'une version personnalisée de la gem Omniauth au profit d'une version standard. [#587](https://github.com/betagouv/acces-cible/issues/587)
- Refactoring du navigateur utilisé pour les tests. [#545](https://github.com/betagouv/acces-cible/issues/545)
- Suppression de la logique liée à la colonne `current` et à la colonne `url` de la table `audits`. [#580](https://github.com/betagouv/acces-cible/issues/580), [#582](https://github.com/betagouv/acces-cible/issues/582), [#573](https://github.com/betagouv/acces-cible/issues/573)
