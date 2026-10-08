## Changelog : accessible-autocomplete (30 derniers jours, au 24 septembre 2026)

### Résumé
La version 3.0.2 a été publiée. Cette mise à jour corrige des problèmes d'affichage sur iOS et garantit que les éléments destinés à être masqués restent invisibles, même lorsque les politiques de sécurité (CSP) des sites web bloquent les styles en ligne.

### Évolutions fonctionnelles
- **Amélioration de la compatibilité avec les politiques de sécurité (CSP) :** les éléments visuellement cachés restent désormais correctement masqués lorsque la politique de sécurité du contenu bloque l'utilisation de styles en ligne ([#794](https://github.com/betagouv/accessible-autocomplete/pull/794)).
- **Correction de l'affichage sur iOS :** résolution d'un problème lié aux noms de propriétés CSS pour les suffixes d'options sur les appareils iOS ([#800](https://github.com/betagouv/accessible-autocomplete/pull/800)).

### Évolutions techniques
- **Optimisation du processus de déploiement :** alignement du processus de publication (release) sur celui de GOV.UK Frontend ([#695](https://github.com/betagouv/accessible-autocomplete/pull/695)).
