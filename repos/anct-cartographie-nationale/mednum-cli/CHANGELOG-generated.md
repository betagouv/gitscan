## Changelog : mednum-cli (30 derniers jours, au 30 mars 2026)

### Résumé
Cette mise à jour apporte des améliorations concernant l'URL de l'API de cartographie nationale, la corrigeant pour utiliser CloudFront. De plus, une correction a été apportée pour exclure un lieu spécifique de la commune de Gonfreville l'Orcher. Enfin, les gestionnaires de paquets Yarn et Pnpm ont été supprimés des scripts du projet.

### Évolutions fonctionnelles
- Mise à jour de l'URL de l'API de cartographie nationale pour utiliser CloudFront. [#342](https://github.com/anct-cartographie-nationale/mednum-cli/issues/342)
- Correction d'un problème d'exclusion de lieux : le lieu "COMMUNE DE GONFREVILLE L ORCHER MAIRIE" est maintenant correctement exclu. [#341](https://github.com/anct-cartographie-nationale/mednum-cli/issues/341)

### Évolutions techniques
- Suppression de Yarn et Pnpm des scripts du fichier `package.json`, simplifiant ainsi la gestion des dépendances. [#340](https://github.com/anct-cartographie-nationale/mednum-cli/issues/340)
