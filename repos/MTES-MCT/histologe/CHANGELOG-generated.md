## Changelog : histologe (30 derniers jours, au 2026-05-21)

### Résumé
Le mois écoulé a été marqué par des améliorations significatives en termes de sécurité, d'accessibilité et de performance de la plateforme histologe. Des corrections de vulnérabilités ont été apportées, l'accessibilité a été renforcée pour les utilisateurs et les API, et des optimisations ont été réalisées pour améliorer la réactivité de l'application, notamment au niveau de la liste des signalements et de l'export de données. Des améliorations ont également été apportées à la gestion des suivis et des notifications.

### Évolutions fonctionnelles
- Amélioration de la gestion des suivis : ajout de la date/heure des clubs en fonction de la timezone de l'utilisateur sur les mails et le dashboard [#5778](https://github.com/MTES-MCT/histologe/issues/5778).
- Ajout d'une confirmation lors de la suppression des notifications [#5800](https://github.com/MTES-MCT/histologe/issues/5800).
- Correction de la réouverture de la modale de sélection de bâtiment lors d'un changement d'adresse dans le back-office [#5839](https://github.com/MTES-MCT/histologe/issues/5839).
- Ajout de la possibilité de trier la liste des territoires par code postal [#5811](https://github.com/MTES-MCT/histologe/issues/5811).
- Amélioration de l'affichage des dates et heures des clubs dans les mails et le dashboard [#5778](https://github.com/MTES-MCT/histologe/issues/5778).
- Ajout de l'heure dans le suivi de visite programmée [#5759](https://github.com/MTES-MCT/histologe/issues/5759).
- Ajout et édition de documents [#5793](https://github.com/MTES-MCT/histologe/issues/5793).
- Ajout et édition de partenaires [#5781](https://github.com/MTES-MCT/histologe/issues/5781).
- Ajout et édition d'événements [#5823](https://github.com/MTES-MCT/histologe/issues/5823).
- Ajout de la gestion des utilisateurs API [#5826](https://github.com/MTES-MCT/histologe/issues/5826).
- Ajout de la gestion des services de secours, bailleurs et communes [#5832](https://github.com/MTES-MCT/histologe/issues/5832).
- Ajout de la gestion des accès pour les utilisateurs API [#5826](https://github.com/MTES-MCT/histologe/issues/5826).

### Évolutions techniques
- Mise à jour de Twig et Symfony pour corriger des vulnérabilités de sécurité [#5887](https://github.com/MTES-MCT/histologe/issues/5887).
- Montée de version de Doctrine [#5827](https://github.com/MTES-MCT/histologe/issues/5827).
- Mise à jour de PHPUnit de la version 9 à la version 13 [#5766](https://github.com/MTES-MCT/histologe/issues/5766).
- Suppression des persist et flush des managers d'entités pour optimiser les performances [#5757](https://github.com/MTES-MCT/histologe/issues/5757).
- Refactorisation du code pour déplacer la logique d'update et de nettoyage vers les classes Behaviour des repositories [#5762](https://github.com/MTES-MCT/histologe/issues/5762).
- Remplacement de phpspreadsheets par une alternative plus performante [#5836](https://github.com/MTES-MCT/histologe/issues/5836).
- Correction d'un bug lié à la conversion d'un tableau en chaîne de caractères pour l'envoi d'emails [#5853](https://github.com/MTES-MCT/histologe/issues/5853).
- Ajout d'un postmortem pour une vulnérabilité YesWeHack [#5847](https://github.com/MTES-MCT/histologe/issues/5847).
- Correction d'un problème d'environnement détecté par YesWeHack [#5838](https://github.com/MTES-MCT/histologe/issues/5838).
- Ajout de Lighthouse dans la CI pour l'audit de performance [#5789](https://github.com/MTES-MCT/histologe/issues/5789).
- Ajout de tests pour la pagination des connexions SI [#5755](https://github.com/MTES-MCT/histologe/issues/5755).
- Optimisation de la liste des signalements et de l'export de données (ajout du nom des documents et photos) [#5710](https://github.com/MTES-MCT/histologe/issues/5710).

### Autres changements
- Mise à jour des paquets npm [#5845](https://github.com/MTES-MCT/histologe/issues/5845), [#5894](https://github.com/MTES-MCT/histologe/issues/5894).
- Mise à jour de la collection Postman [#5830](https://github.com/MTES-MCT/histologe/issues/5830).
- Suppression du manager inutilisé [#5787](https://github.com/MTES-MCT/histologe/issues/5787).
- Correction de l'affichage des données EXIF pour éviter les plantages [#5820](https://github.com/MTES-MCT/histologe/issues/5820).
- Désactivation des boutons de soumission lors des requêtes AJAX [#5782](https://github.com/MTES-MCT/histologe/issues/5782).
- Ajustement du format du numéro de téléphone dans le tooltip des suivis [#5786](https://github.com/MTES-MCT/histologe/issues/5786).
- Correction de problèmes d'accessibilité [#5770](https://github.com/MTES-MCT/histologe/issues/5770), [#5807](https://github.com/MTES-MCT/histologe/issues/5807).
- Suppression du répertoire `test` du déploiement [#5818](https://github.com/MTES-MCT/histologe/issues/5818).
- Ajout de la gestion des messages de resynchronisation [#5754](https://github.com/MTES-MCT/histologe/issues/5754).
- Correction de la pagination des connexions SI [#5755](https://github.com/MTES-MCT/histologe/issues/5755).
- Mise à jour d'axios [#5816](https://github.com/MTES-MCT/histologe/issues/5816).
- Configuration de `innodb-buffer-pool-size` [#5791](https://github.com/MTES-MCT/histologe/issues/5791).
