## Changelog : dialog (30 derniers jours, au 18 mai 2026)

### Résumé
Ce mois-ci, les améliorations se concentrent sur l'importation et le traitement des données réglementaires, notamment via le nouveau flux Literalis et l'optimisation du traitement des données DATEX. Des corrections ont également été apportées pour améliorer la stabilité et la performance de l'application. Enfin, des améliorations de l'interface utilisateur ont été réalisées, notamment sur la carte.

### Évolutions fonctionnelles
- Amélioration de l'importation des données Literalis, avec correction de bugs et configuration de la CI pour le nouveau flux. [#1724](https://github.com/MTES-MCT/dialog/issues/1724), [#1770](https://github.com/MTES-MCT/dialog/issues/1770), [#1773](https://github.com/MTES-MCT/dialog/issues/1773), [#1792](https://github.com/MTES-MCT/dialog/issues/1792)
- Sur la carte, la sélection par défaut est maintenant uniquement 'Circulation interdite', améliorant l'expérience utilisateur. [#1787](https://github.com/MTES-MCT/dialog/issues/1787)
- Envoi de notifications d'intégration via Mattermost pour une meilleure communication. [#1797](https://github.com/MTES-MCT/dialog/issues/1797)

### Évolutions techniques
- Optimisation du traitement des données DATEX pour résoudre les problèmes de mémoire liés à la quantité de données. [#1798](https://github.com/MTES-MCT/dialog/issues/1798)
- Streaming de la réponse DATEX pour une meilleure performance. [#1771](https://github.com/MTES-MCT/dialog/issues/1771)
- Correction de la CI pour assurer le bon fonctionnement des pipelines. [#1767](https://github.com/MTES-MCT/dialog/issues/1767)
- Correction d'une utilisation de fonction dépréciée. [#1763](https://github.com/MTES-MCT/dialog/issues/1763)
- POC de génération de fichier statique pour l'API des réglementations. [#1772](https://github.com/MTES-MCT/dialog/issues/1772)
