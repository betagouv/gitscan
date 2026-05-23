## Changelog : figpot (30 derniers jours, au 22 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la fidélité de la conversion Figma vers Penpot, notamment au niveau du rendu du texte, des formes, des gradients et des couleurs. Plusieurs corrections ont été apportées pour gérer des cas spécifiques et améliorer la compatibilité entre les deux plateformes.

### Évolutions fonctionnelles
- Amélioration de la conversion des textes : correction du calcul de la hauteur de ligne et gestion des espaces négatifs pour un rendu plus précis dans Penpot.
- Gestion des chemins (paths) : correction de problèmes liés aux remplissages et aux traits, assurant une conversion plus fidèle des formes complexes.
- Support des nœuds de texte sur un chemin (text path nodes) : conversion des textes sur un chemin en vecteurs pour une compatibilité avec Penpot.
- Support des slots Figma : gestion des nœuds de slot Figma lors de la conversion.
- Support des variables de couleur : correction de la conversion des couleurs via des alias de variables.

### Évolutions techniques
- Correction de l'ordre des traits (strokes) pour correspondre à Penpot.
- Gestion des erreurs : remplacement des exceptions par des notifications pour les types de nœuds non supportés, améliorant la robustesse du convertisseur.
- Contournement d'un problème lié aux changements de logique de transformation qui pouvaient causer des erreurs de comparaison (diff).
- Forçage de la conversion des arcs en vecteurs plutôt qu'en objets "cercle" Penpot.
- Correction de la gestion des gradients : amélioration du mapping des gradients et gestion des valeurs trop élevées.

### Autres changements
- Mise à jour des polices Google.
- Ajout d'un avertissement pour les nœuds de texte sur un chemin qui pourraient être corrompus par l'API Figma (reconstruction automatique en vecteur).
