## Changelog : st-home (30 derniers jours, au 22 juillet 2026)

### Résumé
Cette mise à jour apporte des corrections et améliorations concernant la robustesse du téléchargement des données SIRENE et DILA, l'affichage de la carte de conformité, ainsi que la gestion des adresses IP et de l'historique des RCPNT. Une nouvelle version du RCPNT (0.2.1) est également disponible avec son changelog.

### Évolutions fonctionnelles
- Correction de l'affichage du bouton "commune" sur la carte de conformité [#73](https://github.com/suitenumerique/st-home/issues/73).
- Amélioration de la classification SIRENE et corrections d'affichage dans l'interface utilisateur.
- Ajout d'une migration pour la table d'historique des RCPNT [#75](https://github.com/suitenumerique/st-home/issues/75).
- Nouvelle version du RCPNT (0.2.1) disponible avec son propre changelog.

### Évolutions techniques
- Amélioration de la robustesse du téléchargement des données SIRENE et du rapprochement DILA SIRET.
- Correction d'un contournement de la blocklist et gestion des erreurs GeoIP dans Caddy [#72](https://github.com/suitenumerique/st-home/issues/72).
- La défaillance du téléchargement GeoIP est désormais non fatale.

### Autres changements
- Ajout d'un changelog pour la nouvelle version du RCPNT (0.2.1).
