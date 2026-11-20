## Changelog : Dossier-Facile-Frontend (30 derniers jours, au 19 novembre 2026)

### Résumé
Ce mois-ci, les évolutions se sont concentrées sur l'amélioration de l'expérience utilisateur (ajustements des attestations et de l'interface) et sur un travail important de mise en conformité avec les normes d'accessibilité. La robustesse technique a également été renforcée par des mises à jour de sécurité et une optimisation des processus de déploiement et de tests.

### Évolutions fonctionnelles
- Ajout d'une modale de demande de vérification [#2103](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2103).
- Amélioration des attestations auto-générées : modification de la formulation, limitation à 500 caractères et correction du formatage des nombres [#2102](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2102), [#2095](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2095).
- Optimisations de l'interface utilisateur : correction de l'affichage du footer sur mobile, harmonisation des espacements et des polices dans les paramètres, et mise à jour des libellés de partage [#2091](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2091), [#2098](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2098).
- Correction d'un problème lié à la messagerie [#2099](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2099).

### Évolutions techniques
- Accessibilité (a11y) : Amélioration de la sémantique et de la navigation pour l'ensemble de l'application (SPA, header, page de partage) [#2081](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2081), [#2084](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2084), [#2096](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2096), [#2064](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2064).
- CI/CD et Infrastructure : Mise en place d'un workflow de release [#2101](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2101), mise à jour de Node 22 et des GitHub Actions [#2082](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2082), et correction de vulnérabilités via Vite [#2105](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2105).
- Tests : Stabilisation des tests de bout en bout (E2E) via la correction de sélecteurs et l'ajustement de la gestion des notifications d'échec [#2085](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2085), [#2092](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2092).

### Autres changements
- Nettoyage du projet avec la suppression de Storybook [#2104](https://github.com/MTES-MCT/Dossier-Facile-Frontend/issues/2104).
