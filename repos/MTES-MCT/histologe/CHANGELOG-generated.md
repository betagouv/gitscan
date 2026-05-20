## Changelog : histologe (30 derniers jours, au 19 mai 2026)

### Résumé
Ce mois-ci, histologe a bénéficié d'améliorations significatives en termes d'accessibilité, de performance et de correction de vulnérabilités de sécurité. Des corrections ont été apportées à l'interface utilisateur pour faciliter l'utilisation, notamment dans les formulaires et les tableaux de bord. Des optimisations ont été réalisées sur la gestion des données et des fichiers, et des mesures de sécurité ont été mises en place suite à un audit.

### Évolutions fonctionnelles
- Amélioration de la gestion des événements avec l'ajout de filtres. [#5713](https://github.com/MTES-MCT/histologe/issues/5713)
- Ajout de la date et de l'heure dans le suivi des visites programmées. [#5759](https://github.com/MTES-MCT/histologe/issues/5759)
- Amélioration de l'affichage des dates des photos en préservant les données EXIF. [#5702](https://github.com/MTES-MCT/histologe/issues/5702)
- Ajout d'une confirmation pour vider les notifications. [#5800](https://github.com/MTES-MCT/histologe/issues/5800)
- Correction de la réouverture de la modale de sélection de bâtiment lors d'un changement d'adresse. [#5839](https://github.com/MTES-MCT/histologe/issues/5839)
- Correction de la conversion array to string pour l'envoi de mails. [#5853](https://github.com/MTES-MCT/histologe/issues/5853)
- Ajout de la reprise de commande dossier rejet. [#5877](https://github.com/MTES-MCT/histologe/issues/5877)
- Amélioration de l'affichage du nom des documents et des photos dans l'export des signalements. [#5710](https://github.com/MTES-MCT/histologe/issues/5710)

### Évolutions techniques
- Remplacement de phpspreadsheets par une alternative. [#5836](https://github.com/MTES-MCT/histologe/issues/5836)
- Suppression des persist et flush des managers d'entités pour optimiser les performances. [#5757](https://github.com/MTES-MCT/histologe/issues/5757)
- Montée de version de Doctrine. [#5827](https://github.com/MTES-MCT/histologe/issues/5827)
- Mise à jour de PHPUnit de 9 vers 13. [#5766](https://github.com/MTES-MCT/histologe/issues/5766)
- Déplacement de méthodes vers des classes Behaviour pour une meilleure organisation du code. [#5762](https://github.com/MTES-MCT/histologe/issues/5762)
- Correction d'un problème lié à l'environnement variable relevé par YesWeHack. [#5838](https://github.com/MTES-MCT/histologe/issues/5838)
- Ajout d'un postmortem suite à une vulnérabilité YesWeHack. [#5847](https://github.com/MTES-MCT/histologe/issues/5847)
- Mise à jour des paquets npm. [#5846](https://github.com/MTES-MCT/histologe/issues/5846)
- Mise à jour de PostCSS. [#5809](https://github.com/MTES-MCT/histologe/issues/5809)
- Ajout de Lighthouse dans la CI pour l'audit de performance. [#5789](https://github.com/MTES-MCT/histologe/issues/5789)

### Autres changements
- Améliorations de l'accessibilité pour les utilisateurs API, les services de secours, les bailleurs et les communes. [#5826](https://github.com/MTES-MCT/histologe/issues/5826), [#5832](https://github.com/MTES-MCT/histologe/issues/5832), [#5807](https://github.com/MTES-MCT/histologe/issues/5807)
- Améliorations de l'accessibilité sur le tableau de bord (zoom sur l'avatar, libellé des liens). [#5737](https://github.com/MTES-MCT/histologe/issues/5737)
- Mise à jour de la collection Postman. [#5831](https://github.com/MTES-MCT/histologe/issues/5831)
- Suppression du manager. [#5787](https://github.com/MTES-MCT/histologe/issues/5787)
- Correction de la pagination des connexions SI. [#5758](https://github.com/MTES-MCT/histologe/issues/5758)
- Ajout de la gestion du message de resynchronisation. [#5756](https://github.com/MTES-MCT/histologe/issues/5756)
- Désactivation des boutons submit lors des soumissions AJAX. [#5782](https://github.com/MTES-MCT/histologe/issues/5782)
- Ajustement du format du numéro de téléphone dans le tooltip des suivis. [#5786](https://github.com/MTES-MCT/histologe/issues/5786)
- Correction de bugs divers et amélioration de la qualité du code.
