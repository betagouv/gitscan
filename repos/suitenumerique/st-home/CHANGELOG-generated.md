## Changelog : st-home (30 derniers jours, au 24 juillet 2026)

### Résumé
Cette mise à jour apporte des améliorations à la robustesse de l'application, notamment dans le traitement des données SIRENE et DILA SIRET, ainsi que des corrections d'affichage et de sécurité. L'intégration avec Grist a été complètement supprimée.

### Évolutions fonctionnelles
- Correction de l'affichage du bouton "commune" sur la carte de conformité. [#73](https://github.com/suitenumerique/st-home/issues/73)
- Amélioration de la classification SIRENE et corrections d'interface utilisateur pour le module RPNT. [#73](https://github.com/suitenumerique/st-home/issues/73)
- Ajout d'une migration pour la table d'historique RCPNT. [#73](https://github.com/suitenumerique/st-home/issues/73)
- Nouvelle version changelog pour le module RPNT (0.2.1).

### Évolutions techniques
- Suppression complète de l'intégration Grist (inscription et code résiduel).
- Amélioration de la robustesse du téléchargement SIRENE et de la correspondance DILA SIRET.
- Correction d'un contournement de la liste noire et gestion des erreurs de géolocalisation dans Caddy. [#72](https://github.com/suitenumerique/st-home/issues/72)
- Rendre le téléchargement de la base de données GeoIP fatal en cas d'échec. [#75](https://github.com/suitenumerique/st-home/issues/75)

### Autres changements
- Aucun changement significatif à signaler.
