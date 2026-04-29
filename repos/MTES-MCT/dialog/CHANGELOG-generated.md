## Changelog : dialog (30 derniers jours, au 28 avril 2026)

### Résumé
Ce mois-ci, l'équipe a concentré ses efforts sur l'amélioration de l'importation et du traitement des données réglementaires, notamment via les flux Literalis et Datex. Des améliorations ont également été apportées à l'interface utilisateur, notamment pour la recherche et l'affichage des informations, ainsi que des corrections de bugs et des optimisations de performance.

### Évolutions fonctionnelles
- Ajout de la recherche dans le sélecteur d'organisations [#1824](https://github.com/MTES-MCT/dialog/issues/1824).
- Amélioration du rendu du filtre par organisation en augmentant sa largeur [#1827](https://github.com/MTES-MCT/dialog/issues/1827).
- Ajout de la fonctionnalité de desserte locale [#1817](https://github.com/MTES-MCT/dialog/issues/1817).
- Affichage de la source de l'arrêté [#1812](https://github.com/MTES-MCT/dialog/issues/1812).
- Affichage de l'heure de modification des arrêtés [#1813](https://github.com/MTES-MCT/dialog/issues/1813).
- Possibilité de modifier un arrêté après sa publication [#1793](https://github.com/MTES-MCT/dialog/issues/1793).
- Amélioration de la disponibilité du flux Datex [#1805](https://github.com/MTES-MCT/dialog/issues/1805).
- Implémentation d'une API pour récupérer les rues à proximité [#1809](https://github.com/MTES-MCT/dialog/issues/1809).
- Correction de l'import Literalis [#1792](https://github.com/MTES-MCT/dialog/issues/1792) et [#1773](https://github.com/MTES-MCT/dialog/issues/1773).
- Sur la carte, désélectionner toutes les couches sauf 'Circulation interdite' par défaut [#1787](https://github.com/MTES-MCT/dialog/issues/1787).

### Évolutions techniques
- Correction de la numérotation des Pull Requests inversée [#1822](https://github.com/MTES-MCT/dialog/issues/1822).
- Amélioration de l'administration des utilisateurs pour les environnements de test [#1815](https://github.com/MTES-MCT/dialog/issues/1815).
- Retour d'une erreur explicite lors d'un problème d'intersection sur l'API [#1814](https://github.com/MTES-MCT/dialog/issues/1814).
- Refactorisation de la recréation des index BDTOPO via une commande Symfony au lieu de migrations [#1806](https://github.com/MTES-MCT/dialog/issues/1806).
- Envoi de notifications d'intégration via Mattermost [#1797](https://github.com/MTES-MCT/dialog/issues/1797).
- Correction des problèmes de mémoire liés à la quantité de données DATEX [#1798](https://github.com/MTES-MCT/dialog/issues/1798).
- Traitement synchrone de la génération du Datex depuis la CI [#1794](https://github.com/MTES-MCT/dialog/issues/1794).
- Stream du flux de réponse Datex pour améliorer la performance [#1771](https://github.com/MTES-MCT/dialog/issues/1771).
- Configuration de la CI pour le nouveau flux Literalis [#1770](https://github.com/MTES-MCT/dialog/issues/1770).
- Implémentation d'un nouveau client Literalis WFS pour la communication [#1724](https://github.com/MTES-MCT/dialog/issues/1724).
- Correction d'une dépendance obsolète [#1763](https://github.com/MTES-MCT/dialog/issues/1763).
- Correction de la CI [#1767](https://github.com/MTES-MCT/dialog/issues/1767).
- POC de génération de fichiers statiques pour l'API des réglementations [#1772](https://github.com/MTES-MCT/dialog/issues/1772).

### Autres changements
- Documentation mise à jour.
- Nettoyage du code.
