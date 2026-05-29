## Changelog : acces-cible (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la performance et de la stabilité de l'application, notamment en stabilisant l'import de fichiers CSV et en corrigeant des requêtes SQL inefficaces. De nouvelles fonctionnalités ont été ajoutées, comme le widget JDMA, et des améliorations de l'interface utilisateur ont été apportées avec l'utilisation de composants DSFR.

### Évolutions fonctionnelles
- Ajout d'un widget JDMA pour faciliter l'accès à certaines fonctionnalités. [#569](https://github.com/betagouv/acces-cible/issues/569)
- Stabilisation de l'import des fichiers CSV en utilisant un traitement en arrière-plan pour éviter les blocages. [#541](https://github.com/betagouv/acces-cible/issues/541)
- Normalisation des URLs des sites pour assurer leur cohérence. [#576](https://github.com/betagouv/acces-cible/issues/576)
- Configuration du bouton JDMA via des variables d'environnement pour une plus grande flexibilité. [#578](https://github.com/betagouv/acces-cible/issues/578)

### Évolutions techniques
- Correction de requêtes SQL N+1 pour améliorer les performances. [#538](https://github.com/betagouv/acces-cible/issues/538)
- Refactorisation du code lié au navigateur (browser) pour une meilleure maintenabilité. [#545](https://github.com/betagouv/acces-cible/issues/545)
- Utilisation du composant DSFR Side Menu pour améliorer l'interface utilisateur et assurer la cohérence avec le design system. [#571](https://github.com/betagouv/acces-cible/issues/571)
- Nettoyage du code mort et des dépendances inutilisées pour simplifier le projet. [#542](https://github.com/betagouv/acces-cible/issues/542)
- Mise à jour de Puma de la version 7.2.0 à la version 8.0.1. [#540](https://github.com/betagouv/acces-cible/issues/540)
- Mise à jour de plusieurs dépendances mineures. [#549](https://github.com/betagouv/acces-cible/issues/549)
- Mise à jour de erb de la version 6.0.3 à la version 6.0.4. [#546](https://github.com/betagouv/acces-cible/issues/546)

### Autres changements
- Ajout de migrations pour mettre à jour les URLs des sites en base de données. Plusieurs tentatives ont été faites pour assurer la bonne exécution de ces migrations. [#530](https://github.com/betagouv/acces-cible/issues/530), [#553](https://github.com/betagouv/acces-cible/issues/553), [#555](https://github.com/betagouv/acces-cible/issues/555), [#556](https://github.com/betagouv/acces-cible/issues/556), [#557](https://github.com/betagouv/acces-cible/issues/557), [#558](https://github.com/betagouv/acces-cible/issues/558)
- Correction d'une faute de frappe dans le fichier `queue.yml`. [#567](https://github.com/betagouv/acces-cible/issues/567)
- Suppression de la logique liée à `current` pour simplifier le code. [#573](https://github.com/betagouv/acces-cible/issues/573)
