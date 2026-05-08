## Changelog : resorption-bidonvilles (30 derniers jours, au 6 mai 2026)

### Résumé
Cette période a été marquée par d'importantes améliorations de l'interface utilisateur et de la gestion des données, notamment concernant les adresses des Entreprises, Territoires et Intermédiaires (ETI) et le financement DIHAL. Des corrections de bugs et des optimisations de performance ont également été apportées pour améliorer la stabilité et l'expérience utilisateur. Enfin, la préparation du reporting et du suivi des actions a été renforcée.

### Évolutions fonctionnelles
- **Gestion des adresses ETI :** Amélioration significative de la gestion des adresses ETI avec la possibilité de gérer plusieurs adresses par ETI, d'afficher ces adresses sur une carte, et de détecter les doublons. [#2652](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2652)
- **Filtre Financement DIHAL :** Ajout d'un filtre plus dynamique pour le financement DIHAL, permettant de filtrer par année. [#2659](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2659)
- **Historique des actions :** Implémentation de l'historique des actions, incluant les modifications des adresses et des indicateurs, pour un meilleur suivi de l'évolution des données. [#2657](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2657) et [#2666](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2666)
- **Indicateurs de mise à jour de population :** Ajout d'indicateurs de mise à jour de la population dans les rapports hebdomadaires et l'interface utilisateur. [#2662](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2662)
- **Demande d'accès :** Correction du lien de demande d'information pour le rendre une demande d'accès. [#2661](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2661)
- **Affichage des taux :** Amélioration de la formulation des taux de mises à jour. [#2662](https://github.com/MTES-MCT/resorption-bidonvilles/issues/2662)

### Évolutions techniques
- **Refactoring du code :** Refactorings importants du code, notamment autour de la gestion des adresses ETI et de l'historique des actions, pour améliorer la lisibilité, la maintenabilité et la performance.
- **Typage TypeScript :** Amélioration du typage TypeScript pour une meilleure sécurité et une meilleure détection des erreurs.
- **Optimisation des performances :** Optimisations diverses pour améliorer les performances de l'application.
- **Pré-bundling des librairies :** Pré-bundling des librairies nécessaires pour Nuxt 4.
- **Sécurisation :** Correction de potentielles failles de sécurité (injection, interpolation de strings).
- **Mise à jour des dépendances :** Mise à jour de certaines dépendances.

### Autres changements
- **Documentation :** Amélioration de la documentation.
- **Corrections de style :** Corrections de style et de linting pour améliorer la qualité du code.
- **Tests :** Ajout et amélioration des tests unitaires.
- **DSFRisation :** Application des standards de design du DSFR pour l'affichage des erreurs d'export.
- **Intégration Matomo :** Configuration de l'intégration avec Matomo via un proxy.
- **Amélioration du header des actions :** Sécurisation et transmission des données pour le header des actions.
