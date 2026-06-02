## Changelog : savoirfR (30 derniers jours, au 1er juin 2026)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'intégration du module M6 et l'amélioration de l'expérience utilisateur, notamment en corrigeant des problèmes d'affichage et de compilation des exercices. Des optimisations ont également été apportées au pipeline d'intégration continue (CI) pour garantir une meilleure stabilité et compatibilité avec les dernières versions des outils utilisés.

### Évolutions fonctionnelles
- Intégration du module M6, incluant l'ajout d'images pour les corrections des stagiaires. [#8](https://github.com/MTES-MCT/savoirfR/issues/8)
- Amélioration de l'affichage de l'exercice 7 du module M6 en ajustant la hauteur de l'iframe.
- Corrections et améliorations suite aux tests d'utilisation du module M6 par les stagiaires.
- Correction du rendu d'images dans l'exercice 3 du module M6, lié à un problème de tiret dans le nom de fichier.

### Évolutions techniques
- Mise à jour des actions GitHub Checkout et Cache pour assurer la compatibilité avec Node.js 24.
- Correction d'un problème dans le CI où le token GitHub utilisé pour `tidytuesdayR::tt_load()` était parfois rejeté. La configuration a été revue pour utiliser un token personnel.
- Réactivation de l'installation de TinyTeX dans le CI.
- Optimisation du pipeline CI en simplifiant la copie de fichiers et en corrigeant des erreurs de compilation PDF.

### Autres changements
- Nettoyage de code dans le pipeline CI.
- Correction d'une faute de frappe dans le module M6.
