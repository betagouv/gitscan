## Changelog : figpot (30 derniers jours, au 28 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent principalement sur la fidélité de la conversion Figma vers Penpot, notamment en corrigeant des problèmes liés au rendu du texte, des formes, des gradients et des couleurs.  L'objectif est d'améliorer la qualité de la migration et de la synchronisation des designs entre les deux plateformes.

### Évolutions fonctionnelles
- Amélioration de la conversion des textes : correction du calcul de la hauteur de ligne et gestion des espaces négatifs pour un rendu plus précis dans Penpot.
- Support des nœuds de "slot" Figma.
- Support des nœuds de chemin de texte Figma, convertis en vecteurs.
- Gestion améliorée des dégradés, avec correction des valeurs excessives et d'un mapping incorrect.
- Les couleurs définies via des variables alias sont maintenant correctement converties.
- Correction de problèmes de remplissage pour certains chemins Figma.

### Évolutions techniques
- Correction de l'ordre des traits (strokes) pour correspondre à Penpot.
- Gestion des erreurs lors de la récupération de nœuds texte Figma potentiellement corrompus.
- Contournement d'un problème lié aux types de nœuds non supportés lors de la comparaison (diff).
- Forçage de la conversion des arcs en vecteurs plutôt qu'en objets "cercle" Penpot.
- Correction de bugs liés aux chemins avec des traits supplémentaires.

### Autres changements
- Mise à jour des polices Google.
- Amélioration de la gestion des types de nœuds non supportés : affichage d'une notification au lieu d'une erreur.
- Ajustement de la hauteur des caractères ("cap height") pour un meilleur positionnement du texte.
