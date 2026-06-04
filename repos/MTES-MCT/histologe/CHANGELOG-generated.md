## Changelog : histologe (30 derniers jours, au 03 juin 2026)

### Résumé
Ce mois-ci, l'équipe a travaillé sur l'amélioration de l'accessibilité de l'application, la correction de bugs et l'optimisation des performances. Des améliorations ont été apportées à l'interface utilisateur, notamment pour la gestion des signalements et des notifications. Des mises à jour de sécurité et des refactorings techniques ont également été réalisés pour assurer la stabilité et la pérennité de la plateforme.

### Évolutions fonctionnelles
- [BO - Liste signalements] Les étiquettes et partenaires dans la liste des signalements sont maintenant triés par ordre alphabétique, insensible à la casse. [#5916](https://github.com/MTES-MCT/histologe/issues/5916)
- [Signalement] L'occupation du logement est maintenant déterminée de manière plus systématique et affichée correctement dans la fiche signalement. [#5909](https://github.com/MTES-MCT/histologe/issues/5909)
- [BO - Signalement] Ajout d'un message informatif pour les logements vacants lors de l'ajout d'un suivi. [#5897](https://github.com/MTES-MCT/histologe/issues/5897)
- [FO - Signalement] Possibilité d'enregistrer le nom du travailleur social. [#5867](https://github.com/MTES-MCT/histologe/issues/5867)
- [Démarche accélérée - FO Bailleur] Les bailleurs peuvent maintenant envoyer un suivi et des documents pendant la procédure. [#5819](https://github.com/MTES-MCT/histologe/issues/5819)
- [BO - Notifications] Ajout d'une confirmation avant de vider les notifications. [#5800](https://github.com/MTES-MCT/histologe/issues/5800)
- [BO - Signalement] Correction de la réouverture de la modale de sélection de bâtiment lors d'un changement d'adresse. [#5839](https://github.com/MTES-MCT/histologe/issues/5839)
- [BO - Liste Signalements] La liste des signalements est maintenant ancrée. [#5868](https://github.com/MTES-MCT/histologe/issues/5868)
- Amélioration de l'accessibilité pour les utilisateurs API. [#5826](https://github.com/MTES-MCT/histologe/issues/5826)
- Amélioration de l'accessibilité pour l'ajout et l'édition d'événements. [#5823](https://github.com/MTES-MCT/histologe/issues/5823)
- Diverses corrections d'accessibilité dans l'interface. [#5807](https://github.com/MTES-MCT/histologe/issues/5807) et [#5770](https://github.com/MTES-MCT/histologe/issues/5770)

### Évolutions techniques
- Refactorisation de `JobEventRepository` et `SignalementDraftRepository`. [#5914](https://github.com/MTES-MCT/histologe/issues/5914)
- Mise à jour des dépendances Composer. [#5912](https://github.com/MTES-MCT/histologe/issues/5912)
- Remplacement du lib php cron par le composant symfony scheduler. [#5863](https://github.com/MTES-MCT/histologe/issues/5863)
- Suppression ou limitation de l'utilisation des contextes de suivi. [#5884](https://github.com/MTES-MCT/histologe/issues/5884) et [#5843](https://github.com/MTES-MCT/histologe/issues/5843)
- Mise à jour de Twig et Symfony pour corriger des vulnérabilités de sécurité (CVE). [#5887](https://github.com/MTES-MCT/histologe/issues/5887)
- Suppression des persist et flush des managers d'entités pour optimiser les performances. [#5757](https://github.com/MTES-MCT/histologe/issues/5757)
- Montée de version de Doctrine. [#5827](https://github.com/MTES-MCT/histologe/issues/5827)
- Remplacement de phpspreadsheets dans tout le code. [#5836](https://github.com/MTES-MCT/histologe/issues/5836)
- Ajout de Lighthouse dans la CI pour l'audit de performance. [#5789](https://github.com/MTES-MCT/histologe/issues/5789)

### Autres changements
- Mise à jour de la documentation de l'API. [#5929](https://github.com/MTES-MCT/histologe/issues/5929)
- Correction d'une synchronisation erronée du messenger doctrine. [#5921](https://github.com/MTES-MCT/histologe/issues/5921)
- Ajout d'un plugin heatmap. [#5870](https://github.com/MTES-MCT/histologe/issues/5870)
- Correction du tri par code postal sur la liste des territoires. [#5811](https://github.com/MTES-MCT/histologe/issues/5811)
- Suppression de la route de gestion des images du firewall main. [#5891](https://github.com/MTES-MCT/histologe/issues/5891)
- Ajout d'un postmortem pour une vulnérabilité YesWeHack. [#5847](https://github.com/MTES-MCT/histologe/issues/5847)
- Correction d'un problème de conversion array to string pour l'envoi de mails. [#5853](https://github.com/MTES-MCT/histologe/issues/5853)
- Amélioration de l'historique des affectations. [#5875](https://github.com/MTES-MCT/histologe/issues/5875)
- Correction d'un blocage sur le parcours Parc public. [#5854](https://github.com/MTES-MCT/histologe/issues/5854)
- Mise à jour de la collection Postman. [#5831](https://github.com/MTES-MCT/histologe/issues/5831)
- Correction d'un problème lié aux données EXIF. [#5820](https://github.com/MTES-MCT/histologe/issues/5820)
- Suppression d'un manager inutile. [#5787](https://github.com/MTES-MCT/histologe/issues/5787)
- Suppression d'une commande temporaire. [#5885](https://github.com/MTES-MCT/histologe/issues/5885)
