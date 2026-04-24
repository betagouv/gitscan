## Changelog : dialog (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de la gestion des arrêtés (affichage de la source, modification après publication), l'optimisation des performances (gestion des données DATEX, import Literalis) et l'ajout de nouvelles fonctionnalités (recherche de rues proches, notifications Mattermost). Des corrections de bugs et des améliorations techniques ont également été apportées pour stabiliser et moderniser la plateforme.

### Évolutions fonctionnelles
- Affichage de la source de l'arrêté sur l'interface utilisateur. [#1812](https://github.com/MTES-MCT/dialog/issues/1812)
- Possibilité de modifier un arrêté après sa publication. [#1793](https://github.com/MTES-MCT/dialog/issues/1793)
- Ajout d'une fonctionnalité pour récupérer les rues à proximité. [#1809](https://github.com/MTES-MCT/dialog/issues/1809)
- Sur la carte, désélectionner toutes les couches par défaut, sauf 'Circulation interdite'. [#1787](https://github.com/MTES-MCT/dialog/issues/1787)
- Amélioration de la disponibilité du service Datex. [#1805](https://github.com/MTES-MCT/dialog/issues/1805)
- Envoi de notifications d'intégration via Mattermost. [#1797](https://github.com/MTES-MCT/dialog/issues/1797)
- Affichage de l'heure de modification des arrêtés. [#1813](https://github.com/MTES-MCT/dialog/issues/1813)

### Évolutions techniques
- Refonte du processus de création des index BDTOPO en utilisant une commande Symfony au lieu des migrations. [#1806](https://github.com/MTES-MCT/dialog/issues/1806)
- Optimisation du traitement et de la synchronisation de la génération du Datex via la CI. [#1794](https://github.com/MTES-MCT/dialog/issues/1794)
- Correction des problèmes de mémoire liés à la quantité de données DATEX. [#1798](https://github.com/MTES-MCT/dialog/issues/1798)
- Amélioration de la gestion des erreurs lors d'un problème d'intersection sur l'API. [#1814](https://github.com/MTES-MCT/dialog/issues/1814)
- Stream du flux de réponse Datex pour améliorer les performances. [#1771](https://github.com/MTES-MCT/dialog/issues/1771)
- Mise en place d'un nouveau client pour la communication WFS Literalis. [#1724](https://github.com/MTES-MCT/dialog/issues/1724)
- Correction de l'import Literalis. [#1792](https://github.com/MTES-MCT/dialog/issues/1792) et [#1773](https://github.com/MTES-MCT/dialog/issues/1773)
- Correction des dépréciations. [#1763](https://github.com/MTES-MCT/dialog/issues/1763)
- Amélioration de la configuration de la CI. [#1767](https://github.com/MTES-MCT/dialog/issues/1767) et [#1770](https://github.com/MTES-MCT/dialog/issues/1770)

### Autres changements
- Amélioration de l'administration des utilisateurs pour les environnements de test. [#1815](https://github.com/MTES-MCT/dialog/issues/1815)
- POC pour la génération de fichiers statiques pour l'API des réglementations. [#1772](https://github.com/MTES-MCT/dialog/issues/1772)
