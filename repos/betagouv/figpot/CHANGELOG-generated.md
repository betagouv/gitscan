## Changelog : figpot (30 derniers jours, au 27 mai 2026)

### Résumé
Les dernières améliorations de figpot se concentrent sur l'amélioration de la fidélité de la conversion Figma vers Penpot, en particulier pour les éléments de texte, les formes vectorielles, les gradients et les remplissages. Des corrections ont été apportées pour gérer des cas spécifiques rencontrés lors de la conversion, améliorant ainsi la qualité globale de la migration et de la synchronisation des designs.

### Évolutions fonctionnelles
- Amélioration de la conversion des textes :
    - Correction du calcul de la hauteur de ligne pour une meilleure correspondance avec Figma.
    - Gestion des espaces négatifs dans le texte pour un alignement correct.
    - Support des chemins de texte (text paths) convertis en vecteurs.
- Amélioration de la conversion des formes :
    - Correction de l'ordre des traits (strokes) pour une apparence correcte dans Penpot.
    - Gestion des arcs et des cercles, en les convertissant en vecteurs lorsque nécessaire.
    - Correction de problèmes de remplissage pour certains chemins Figma.
- Amélioration de la conversion des gradients :
    - Correction du mapping des gradients pour éviter les erreurs de valeur trop élevée.
    - Gestion correcte des gradients.
- Support des "slots" Figma.

### Évolutions techniques
- Gestion des erreurs : remplacement des exceptions par des notifications pour les types de nœuds non supportés, facilitant le débogage et l'identification des limitations.
- Correction d'un contournement (workaround) dans la logique de diff pour gérer les changements de type de nœud.
- Amélioration de la gestion des nœuds Figma potentiellement corrompus, avec un avertissement.

### Autres changements
- Mise à jour des polices Google.
- Support des variables de couleur.
