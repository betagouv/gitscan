## Changelog : histologe (30 derniers jours, au 22 mai 2026)

### Résumé
Les dernières semaines ont été marquées par des améliorations de sécurité, d'accessibilité et de performance sur la plateforme Histologe. Des corrections de vulnérabilités ont été apportées, et l'interface utilisateur a été optimisée pour une meilleure expérience, notamment au niveau des formulaires et des notifications. Plusieurs évolutions techniques ont également été réalisées pour moderniser le code et améliorer la robustesse de l'application.

### Évolutions fonctionnelles
- Amélioration de l'affichage de la date et de l'heure des clubs en fonction du fuseau horaire de l'utilisateur dans les emails et le tableau de bord [#5778](https://github.com/MTES-MCT/histologe/issues/5778).
- Ajout d'une confirmation lors de la suppression des notifications [#5800](https://github.com/MTES-MCT/histologe/issues/5800).
- Correction de la réouverture de la modale de sélection de bâtiment lors d'un changement d'adresse dans l'interface administrateur [#5839](https://github.com/MTES-MCT/histologe/issues/5839).
- Ajout de la possibilité de trier la liste des territoires par code postal [#5811](https://github.com/MTES-MCT/histologe/issues/5811).
- Amélioration de l'affichage des noms des documents et des photos dans la liste des signalements et lors de l'export [#5710](https://github.com/MTES-MCT/histologe/issues/5710).
- Ajout de la gestion des événements [#5823](https://github.com/MTES-MCT/histologe/issues/5823).
- Ajout et édition des partenaires [#5781](https://github.com/MTES-MCT/histologe/issues/5781).
- Ajout et édition des documents [#5793](https://github.com/MTES-MCT/histologe/issues/5793).
- Correction de la conversion d'array en string pour l'envoi d'emails [#5853](https://github.com/MTES-MCT/histologe/issues/5853).
- Ajout de la reprise de commande dossier rejet [#5877](https://github.com/MTES-MCT/histologe/issues/5877).

### Évolutions techniques
- Mise à jour de Twig et Symfony pour corriger des vulnérabilités de sécurité [#5887](https://github.com/MTES-MCT/histologe/issues/5887).
- Remplacement de `phpspreadsheets` par une alternative plus maintenue [#5836](https://github.com/MTES-MCT/histologe/issues/5836).
- Montée de version de Doctrine [#5827](https://github.com/MTES-MCT/histologe/issues/5827).
- Mise à jour de PHPUnit de la version 9 à la version 13 [#5766](https://github.com/MTES-MCT/histologe/issues/5766).
- Suppression des persist et flush des managers d'entités pour optimiser les performances [#5757](https://github.com/MTES-MCT/histologe/issues/5757).
- Déplacement de la logique d'update et de nettoyage vers des classes Behaviour dans plusieurs repositories [#5762](https://github.com/MTES-MCT/histologe/issues/5762).
- Ajout de Lighthouse dans la CI pour des tests de performance et d'accessibilité [#5789](https://github.com/MTES-MCT/histologe/issues/5789).
- Correction d'un problème d'environnement relevé par YesWeHack [#5838](https://github.com/MTES-MCT/histologe/issues/5838).
- Ajout d'un postmortem pour la vulnérabilité YesWeHack [#5847](https://github.com/MTES-MCT/histologe/issues/5847).

### Autres changements
- Suppression de la route de gestion des images du firewall principal [#5891](https://github.com/MTES-MCT/histologe/issues/5891).
- Mise à jour des paquets npm [#5845](https://github.com/MTES-MCT/histologe/issues/5845), [#5893](https://github.com/MTES-MCT/histologe/issues/5893).
- Mise à jour de PostCSS [#5809](https://github.com/MTES-MCT/histologe/issues/5809).
- Mise à jour de Axios [#5816](https://github.com/MTES-MCT/histologe/issues/5816).
- Amélioration de la configuration innodb-buffer-pool-size [#5791](https://github.com/MTES-MCT/histologe/issues/5791).
- Désactivation des boutons submit lors des soumissions AJAX pour éviter les doubles envois [#5782](https://github.com/MTES-MCT/histologe/issues/5782).
- Ajustement du format du numéro de téléphone dans le tooltip des suivis [#5786](https://github.com/MTES-MCT/histologe/issues/5786).
- Correction de l'accessibilité sur plusieurs formulaires [#5770](https://github.com/MTES-MCT/histologe/issues/5770) et [#5807](https://github.com/MTES-MCT/histologe/issues/5807).
- Suppression du manager inutilisé [#5787](https://github.com/MTES-MCT/histologe/issues/5787).
- Mise à jour de la collection Postman [#5830](https://github.com/MTES-MCT/histologe/issues/5830).
- Ignorer le répertoire test dans le déploiement [#5818](https://github.com/MTES-MCT/histologe/issues/5818).
