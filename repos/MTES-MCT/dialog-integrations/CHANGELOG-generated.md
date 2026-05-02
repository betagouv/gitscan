## Changelog : dialog-integrations (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, le projet dialog-integrations a progressé significativement avec l'intégration de données pour les préfectures de Nantes et Rennes, ainsi que pour le département de la Sarthe. Des améliorations techniques ont été apportées pour optimiser le processus d'intégration et la qualité du code.

### Évolutions fonctionnelles
- Intégration des données des arrêtés préfectoraux pour Nantes [#11](https://github.com/MTES-MCT/dialog-integrations/pull/11).
- Intégration des données des arrêtés préfectoraux pour Rennes [#10](https://github.com/MTES-MCT/dialog-integrations/pull/10).
- Intégration des données des arrêtés préfectoraux pour la Sarthe [#5](https://github.com/MTES-MCT/dialog-integrations/pull/5).

### Évolutions techniques
- Amélioration du pipeline d'intégration continue (CI) pour éviter le déclenchement inutile des intégrations lors des *push* sur le dépôt.
- Refonte du processus de capture des sorties des scripts.
- Amélioration de la qualité du code avec des corrections de *linting* et ajout de typages.
- Mise à jour des dépendances du projet (nbconvert, uv).
- Fusion de la branche *main* dans les branches de fonctionnalités (co_rennes, co_nantes).

### Autres changements
- Mise à jour de la documentation README.
- Corrections mineures de formatage et suppression de lignes inutiles.
