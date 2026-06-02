## Changelog : acces-cible (30 derniers jours, au 01 juin 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la stabilisation de l'import de données CSV, l'optimisation des performances et l'amélioration de l'interface utilisateur. Une nouvelle fonctionnalité permet d'ajouter un widget JDMA pour faciliter l'accès à cet outil. Plusieurs corrections de bugs et améliorations techniques ont également été apportées pour améliorer la robustesse et la maintenabilité de l'application.

### Évolutions fonctionnelles
- Ajout d'un widget JDMA pour faciliter l'accès à l'outil de diagnostic d'accessibilité. [#569](https://github.com/betagouv/acces-cible/issues/569)
- Stabilisation de l'import des fichiers CSV en utilisant un traitement en arrière-plan pour éviter les blocages. [#541](https://github.com/betagouv/acces-cible/issues/541)
- Normalisation des URLs des sites pour éviter les problèmes de comparaison et de redirection. [#576](https://github.com/betagouv/acces-cible/issues/576)
- Configuration du bouton JDMA via des variables d'environnement pour une plus grande flexibilité. [#578](https://github.com/betagouv/acces-cible/issues/578)

### Évolutions techniques
- Correction de requêtes SQL N+1 pour améliorer les performances de l'application. [#538](https://github.com/betagouv/acces-cible/issues/538)
- Refactorisation du code lié au navigateur pour une meilleure maintenabilité. [#545](https://github.com/betagouv/acces-cible/issues/545)
- Utilisation du composant DSFR Side Menu pour harmoniser l'interface utilisateur. [#571](https://github.com/betagouv/acces-cible/issues/571)
- Nettoyage du code mort et des dépendances inutilisées pour simplifier la base de code. [#542](https://github.com/betagouv/acces-cible/issues/542)
- Correction d'une faute de frappe dans le fichier `queue.yml`. [#567](https://github.com/betagouv/acces-cible/issues/567)

### Autres changements
- Ajout de migrations pour compléter les URLs des sites en base de données. Plusieurs tentatives ont été faites pour assurer la bonne exécution de cette migration. [#530](https://github.com/betagouv/acces-cible/issues/530), [#553](https://github.com/betagouv/acces-cible/issues/553), [#555](https://github.com/betagouv/acces-cible/issues/555), [#556](https://github.com/betagouv/acces-cible/issues/556), [#557](https://github.com/betagouv/acces-cible/issues/557), [#558](https://github.com/betagouv/acces-cible/issues/558)
- Mise à jour de la dépendance Puma vers la version 8.0.1. [#540](https://github.com/betagouv/acces-cible/issues/540)
- Mise à jour de plusieurs dépendances mineures. [#549](https://github.com/betagouv/acces-cible/issues/549)
- Mise à jour de la dépendance Erb vers la version 6.0.4. [#546](https://github.com/betagouv/acces-cible/issues/546)
