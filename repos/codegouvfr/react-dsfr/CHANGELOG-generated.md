## Changelog : react-dsfr (30 derniers jours, au 30 mai 2026)

### Résumé
Cette mise à jour apporte une correction importante concernant le composant `Alert`, permettant de supprimer l'attribut `role` lorsqu'il est explicitement défini à `undefined`. Cette modification offre plus de flexibilité aux développeurs pour personnaliser l'accessibilité du composant en fonction de leurs besoins spécifiques.

### Évolutions fonctionnelles
- Correction du composant `Alert` : L'attribut `role` est maintenant correctement supprimé lorsque `role={undefined}` est spécifié, offrant un contrôle plus fin sur l'accessibilité. [#490](https://github.com/codegouvfr/react-dsfr/issues/490)

### Évolutions techniques
- Aucune évolution technique significative à signaler.

### Autres changements
- Mise à jour de la version du package.
