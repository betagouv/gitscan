## Changelog : complements-alimentaires (30 derniers jours, au 14 mai 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'amélioration de la gestion des visas, notamment avec l'ajout d'une fonctionnalité d'approbation automatique et une interface utilisateur dédiée. Des mises à jour de dépendances ont également été effectuées pour assurer la sécurité et la stabilité du projet. Enfin, des améliorations ont été apportées à l'export des données et à la gestion des images.

### Évolutions fonctionnelles
- **Visa automatique :** Implémentation d'une fonctionnalité d'approbation automatique des visas, incluant une interface utilisateur pour la configuration et le suivi. ([#2884](https://github.com/betagouv/complements-alimentaires/pull/2884))
- **Export des données :** Ajout de l'adresse email de l'entreprise aux exports de la recherche avancée.
- **Gestion des images :** Correction de problèmes liés à l'affichage des images. ([#2871](https://github.com/betagouv/complements-alimentaires/pull/2871))
- **Composition PDF :** Amélioration de la composition des PDF, incluant l'ajout d'un compteur de pages et le remplacement du symbole micro par un "u". ([#2854](https://github.com/betagouv/complements-alimentaires/pull/2854))
- **Données Open Data :** Correction de problèmes liés à l'export des données en Open Data. ([#2855](https://github.com/betagouv/complements-alimentaires/pull/2855))

### Évolutions techniques
- **Mises à jour de dépendances :** Plusieurs dépendances ont été mises à jour vers leurs dernières versions stables, notamment Django, Pandas, lxml, cryptography, et les dépendances frontend (Vue.js, PostCSS, etc.) pour améliorer la sécurité et les performances.
- **Suppression de notebooks :** Suppression des fichiers notebooks, car les données sont désormais gérées via Metabase et la base de données. ([#2872](https://github.com/betagouv/complements-alimentaires/pull/2872))
- **Refactoring des tests :** Refactorisation des tests pour une meilleure granularité et maintenabilité.

### Autres changements
- **Documentation :** Mise à jour de la documentation (README).
- **Nettoyage de code :** Suppression de code obsolète et amélioration de la lisibilité du code.
- **Configuration :** Modifications de la configuration pour améliorer la stabilité et la performance.
