## Changelog : histologe (30 derniers jours, au 12 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans le back-office et en front-office, notamment au niveau de la gestion des signalements et de l'accessibilité. Des corrections de sécurité et des optimisations techniques ont également été apportées.

### Évolutions fonctionnelles
- Amélioration de l'affichage de l'occupation du logement dans la fiche signalement du back-office [#5909](https://github.com/MTES-MCT/histologe/issues/5909).
- Ajout d'un message informatif pour les logements vacants lors de l'ajout d'un suivi dans le back-office [#5897](https://github.com/MTES-MCT/histologe/issues/5897).
- Possibilité d'enregistrer le nom du travailleur social en front-office [#5867](https://github.com/MTES-MCT/histologe/issues/5867).
- Suppression du blocage du parcours "Parc public" si le bailleur n'a pas été prévenu ou l'a été trop récemment [#5854](https://github.com/MTES-MCT/histologe/issues/5854).
- Amélioration de l'historique des affectations [#5851](https://github.com/MTES-MCT/histologe/issues/5851).
- Ajout de type partenaire [#5905](https://github.com/MTES-MCT/histologe/issues/5905).
- Correction de l'export des utilisateurs non-RT dans l'annuaire du back-office [#5925](https://github.com/MTES-MCT/histologe/issues/5925).
- Ajout d'étiquettes et de partenaires triés alphabétiquement (sans tenir compte de la casse) dans la liste des signalements du back-office [#5916](https://github.com/MTES-MCT/histologe/issues/5916).
- Amélioration de l'accessibilité de la liste des signalements [#5900](https://github.com/MTES-MCT/histologe/issues/5900) et des liens "démarche accélérée" [#5901](https://github.com/MTES-MCT/histologe/issues/5901).
- Ancrage de la liste des signalements dans le back-office [#5868](https://github.com/MTES-MCT/histologe/issues/5868).
- Activation du plugin heatmap [#5718](https://github.com/MTES-MCT/histologe/issues/5870).
- Correction de la suppression de la qualification [#5999](https://github.com/MTES-MCT/histologe/issues/5999).

### Évolutions techniques
- Refactorisation de `JobEventRepository` et `SignalementDraftRepository` [#5914](https://github.com/MTES-MCT/histologe/issues/5914).
- Mise à jour des dépendances Composer [#5912](https://github.com/MTES-MCT/histologe/issues/5912).
- Mise à jour de Twig et Symfony pour corriger des vulnérabilités de sécurité [#5887](https://github.com/MTES-MCT/histologe/issues/5887).
- Remplacement de la librairie PHP Cron par le composant Symfony Scheduler [#5863](https://github.com/MTES-MCT/histologe/issues/5863).
- Suppression de la route de gestion des images du firewall main [#5891](https://github.com/MTES-MCT/histologe/issues/5891).
- Suppression ou limitation de l'utilisation des contextes de suivi et des types de suivi [#5884](https://github.com/MTES-MCT/histologe/issues/5884) et [#5843](https://github.com/MTES-MCT/histologe/issues/5843).
- Correction d'une synchronisation d'erreur messenger doctrine [#5921](https://github.com/MTES-MCT/histologe/issues/5921).

### Autres changements
- Mise à jour de la documentation de l'API [#5928](https://github.com/MTES-MCT/histologe/issues/5928).
- Autorisation des scripts du plugin Matomo depuis stats.beta.gouv.fr [#5938](https://github.com/MTES-MCT/histologe/issues/5958).
- Mise à jour de TinyMCE [#5955](https://github.com/MTES-MCT/histologe/issues/5956).
- Mise à jour des paquets npm [#5964](https://github.com/MTES-MCT/histologe/issues/5965) et [#5893](https://github.com/MTES-MCT/histologe/issues/5894).
- Correction des fixtures [#5874](https://github.com/MTES-MCT/histologe/issues/5874).
- Ajout de sish reprise commande dossier rejet [#5877](https://github.com/MTES-MCT/histologe/issues/5879).
- Suppression d'une commande temporaire [#5880](https://github.com/MTES-MCT/histologe/issues/5885).
