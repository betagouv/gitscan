## Changelog : dialog-integrations (30 derniers jours, au 27 avril 2026)

### Résumé
Ce mois-ci, le projet dialog-integrations a progressé significativement avec l'intégration de données pour les préfectures de Rennes et Nantes, ainsi que des améliorations sur l'intégration des données de la Sarthe. Des corrections et des optimisations ont été apportées pour assurer la stabilité et la fiabilité du système, notamment au niveau des tests et de l'intégration continue.

### Évolutions fonctionnelles
- Intégration des données de la préfecture de Rennes [#10](https://github.com/MTES-MCT/dialog-integrations/pull/10).
- Intégration des données de la préfecture de Nantes [#11](https://github.com/MTES-MCT/dialog-integrations/pull/11).
- Intégration des données de la Sarthe [#5](https://github.com/MTES-MCT/dialog-integrations/pull/5).
- Correction d'un problème d'identifiant pour Brest.

### Évolutions techniques
- Amélioration du workflow d'intégration continue pour éviter les déclenchements inutiles.
- Mise à jour des paquets (nbconvert, uv) via Dependabot [#12](https://github.com/MTES-MCT/dialog-integrations/pull/12), [#9](https://github.com/MTES-MCT/dialog-integrations/pull/9), [#3](https://github.com/MTES-MCT/dialog-integrations/pull/3).
- Amélioration de la qualité du code avec l'ajout de typage et l'utilisation de linters.
- Configuration de l'environnement pour utiliser toutes les variables d'environnement et activer les notifications.
- Fusion de la branche `main` dans les branches de fonctionnalité (Rennes, Nantes).

### Autres changements
- Mise à jour de la documentation README.
- Corrections de formatage et de style de code.
- Suppression d'une ligne superflue.
