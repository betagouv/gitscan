## Changelog : histologe (30 derniers jours, au 16 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans le back-office (BO) et en front-office (FO), avec des corrections de bugs, des améliorations d'accessibilité et des optimisations techniques. Des mises à jour de sécurité ont également été appliquées.

### Évolutions fonctionnelles
- Possibilité de fermer des signalements en masse à partir d'un fichier CSV [#5980](https://github.com/MTES-MCT/histologe/issues/5980)
- Correction d'un bug empêchant la suppression des qualifications [#5999](https://github.com/MTES-MCT/histologe/issues/5999)
- Amélioration de l'export des utilisateurs dans l'annuaire du back-office [#5925](https://github.com/MTES-MCT/histologe/issues/5925)
- Détermination plus systématique de l'occupation du logement et correction de l'affichage dans la fiche signalement du back-office [#5909](https://github.com/MTES-MCT/histologe/issues/5909)
- Ajout d'un type de partenaire [#5905](https://github.com/MTES-MCT/histologe/issues/5905)
- Possibilité d'enregistrer le nom du travailleur social dans le front-office [#5867](https://github.com/MTES-MCT/histologe/issues/5867)
- Suppression du blocage du parcours "Parc public" si le bailleur n'a pas été prévenu récemment [#5854](https://github.com/MTES-MCT/histologe/issues/5854)
- Amélioration de l'historique des affectations [#5851](https://github.com/MTES-MCT/histologe/issues/5851)
- Ajout d'un message informatif pour les logements vacants lors de l'ajout d'un suivi [#5897](https://github.com/MTES-MCT/histologe/issues/5897)
- Ajout d'une fonctionnalité pour ancrer la liste des signalements dans le back-office [#5868](https://github.com/MTES-MCT/histologe/issues/5868)
- Précision sur les liens "démarche accélérée" pour l'accessibilité [#5901](https://github.com/MTES-MCT/histologe/issues/5901)
- Amélioration de l'accessibilité de la liste des signalements [#5900](https://github.com/MTES-MCT/histologe/issues/5900)

### Évolutions techniques
- Refactorisation de `JobEventRepository` et `SignalementDraftRepository` [#5914](https://github.com/MTES-MCT/histologe/issues/5914)
- Mise à jour des dépendances Composer [#5912](https://github.com/MTES-MCT/histologe/issues/5912)
- Remplacement de la librairie PHP Cron par le composant Symfony Scheduler [#5863](https://github.com/MTES-MCT/histologe/issues/5863)
- Mise à jour de Twig et Symfony pour corriger des vulnérabilités de sécurité (#5887)
- Suppression ou limitation de l'utilisation des contextes de suivi [#5884](https://github.com/MTES-MCT/histologe/issues/5884)
- Suppression de la route de gestion des images du firewall main [#5891](https://github.com/MTES-MCT/histologe/issues/5891)
- Activation du plugin heatmap [#5870](https://github.com/MTES-MCT/histologe/issues/5870)
- Ajout d'une commande pour fermer les dossiers à partir d'un CSV [#6020](https://github.com/MTES-MCT/histologe/issues/6020)

### Autres changements
- Mise à jour de la documentation de l'API [#5928](https://github.com/MTES-MCT/histologe/issues/5928)
- Autorisation des scripts du plugin Matomo depuis stats.beta.gouv.fr [#5938](https://github.com/MTES-MCT/histologe/issues/5938)
- Mise à jour de TinyMCE [#5955](https://github.com/MTES-MCT/histologe/issues/5955)
- Mise à jour des paquets npm [#5893](https://github.com/MTES-MCT/histologe/issues/5893) et [#5965](https://github.com/MTES-MCT/histologe/issues/5965)
- Suppression d'une commande temporaire [#5880](https://github.com/MTES-MCT/histologe/issues/5880)
- Ajout d'une commande sish reprise pour les dossiers rejetés [#5877](https://github.com/MTES-MCT/histologe/issues/5877)
