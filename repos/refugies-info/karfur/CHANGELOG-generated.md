## Changelog : karfur (30 derniers jours, au 2026-05-24)

### Résumé
Ce mois-ci, les améliorations se concentrent sur la correction de bugs et l'amélioration de la stabilité de l'application, notamment suite à des régressions de production le 22 mai. Des corrections de typographie et des ajustements d'interface ont également été apportés pour améliorer l'expérience utilisateur.

### Évolutions fonctionnelles
- Correction d'une coquille sur la page "Mission" [#3746](https://github.com/refugies-info/karfur/pull/3746).
- Correction de l'affichage du compteur de bénévoles sur la page "Traduire" [#3736](https://github.com/refugies-info/karfur/pull/3736) : le compteur affiche désormais correctement 0 lorsque nécessaire.
- Correction de problèmes de traductions dupliquées lors de la validation [#3735](https://github.com/refugies-info/karfur/pull/3735).
- Correction d'un problème empêchant l'affichage correct des nombres sur la page "Traduire" pour certaines langues.

### Évolutions techniques
- Correction de plusieurs régressions ayant causé des erreurs 500 en production le 22 mai [#3745](https://github.com/refugies-info/karfur/pull/3745).
- Amélioration de la gestion des erreurs sur le serveur : extraction typée du statut des erreurs.
- Correction de la marge supérieure des accordéons sur la fiche RCO [#3742](https://github.com/refugies-info/karfur/pull/3742).
- Amélioration de la robustesse de la fonction `deleteLineBreaks` en gérant les entrées `undefined` et ajout de tests unitaires correspondants.

### Autres changements
- Aucun changement significatif à signaler.
