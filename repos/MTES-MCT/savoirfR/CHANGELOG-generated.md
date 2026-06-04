## Changelog : savoirfR (30 derniers jours, au 2026-06-01)

### Résumé
Ce mois-ci, les efforts de développement se sont concentrés sur l'intégration et l'amélioration du module M6, notamment grâce aux retours d'un stagiaire. Des corrections ont été apportées à l'affichage des images et à la compilation des exercices, ainsi que des ajustements au pipeline CI pour assurer une meilleure stabilité et compatibilité.

### Évolutions fonctionnelles
- Intégration du module M6, finalisant ainsi le développement de cette fonctionnalité. [#8](https://github.com/MTES-MCT/savoirfR/issues/8)
- Amélioration de la hauteur de l'iframe dans l'exercice 7 du module M6 pour une meilleure expérience utilisateur.
- Ajout des images nécessaires pour les corrections du stagiaire dans le module M6.
- Correction de l'affichage d'une image spécifique (fromage d'automne) dans l'exercice 3 du module M6.

### Évolutions techniques
- Mise à jour des actions GitHub (checkout et cache) pour assurer la compatibilité avec Node.js 24.
- Correction d'un problème dans le pipeline CI lié à l'utilisation du token GitHub, qui causait des erreurs lors du chargement de données.
- Réactivation de l'installation de TinyTeX dans le pipeline CI.
- Amélioration du pipeline CI pour la compilation des exercices en PDF et résolution de problèmes de cache.
- Nettoyage de la copie de fichiers dans le pipeline CI, améliorant ainsi l'efficacité.

### Autres changements
- Correction d'une faute de frappe dans le module M6.
