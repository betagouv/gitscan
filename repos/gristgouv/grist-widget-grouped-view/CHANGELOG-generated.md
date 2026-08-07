## Changelog : grist-widget-grouped-view (30 derniers jours, au 6 août 2026)

### Résumé
Cette mise à jour majeure améliore considérablement l'ergonomie et l'accessibilité du widget. Les utilisateurs bénéficient désormais d'une interface mieux adaptée à l'intégration dans Grist, avec une gestion du défilement optimisée par groupe, une détection automatique de la langue et de nouvelles options de personnalisation visuelle.

### Évolutions fonctionnelles
- **Internationalisation** : Support du français et de l'anglais avec détection automatique de la langue du navigateur.
- **Navigation et affichage** :
  - Amélioration du défilement : le défilement se fait désormais par groupe plutôt qu'au niveau global, avec une barre d'outils fixe (sticky).
  - Possibilité de configurer la hauteur maximale des groupes (entre 80 et 600px).
- **Personnalisation** :
  - Ajout d'un sélecteur de couleur par groupe.
  - Nouveau panneau de réglages incluant différents formats pour les valeurs booléennes.
  - Affichage conditionnel de la section des booléens (visible uniquement si une colonne booléenne est affichée).
- **Corrections de formatage** : Correction de l'affichage des années (ex: 2025 au lieu de 2 025).

### Évolutions techniques
- **Accessibilité et conformité** : Mise en conformité avec les standards W3C et les critères d'accessibilité WCAG 2.1 AA.
- **Optimisation du layout** : Refonte du CSS et de la gestion des hauteurs pour garantir un comportement stable et un défilement fluide à l'intérieur des iframes Grist.
- **Refactoring** : 
  - Amélioration de la sémantique HTML.
  - Optimisation de la gestion des clés de groupe vides via l'utilisation de `Symbol`.

### Autres changements
- Nettoyage du dépôt (suppression de fichiers de test).
- Mise à jour de la documentation (README).
