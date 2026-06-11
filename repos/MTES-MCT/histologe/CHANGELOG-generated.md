## Changelog : histologe (30 derniers jours, au 10 juin 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans le traitement des signalements et des démarches accélérées. Des corrections de bugs et des améliorations de sécurité ont également été apportées, ainsi que des optimisations techniques pour une meilleure performance et maintenabilité du code.

### Évolutions fonctionnelles
- Amélioration de l'affichage de l'occupation du logement dans la fiche signalement ([#5909](https://github.com/MTES-MCT/histologe/issues/5909)).
- Ajout d'un message informatif pour les logements vacants lors de l'ajout d'un suivi ([#5897](https://github.com/MTES-MCT/histologe/issues/5897)).
- Possibilité d'enregistrer le nom du travailleur social dans le signalement ([#5867](https://github.com/MTES-MCT/histologe/issues/5867)).
- Suppression du blocage sur le parcours "Parc public" si le bailleur n'a pas été prévenu ou l'a été trop récemment ([#5854](https://github.com/MTES-MCT/histologe/issues/5854)).
- Le bailleur peut désormais envoyer un suivi et des documents pendant la procédure de démarche accélérée ([#5819](https://github.com/MTES-MCT/histologe/issues/5819)).
- Ajout de liserets pour améliorer la lisibilité du récapitulatif de signalement ([#5865](https://github.com/MTES-MCT/histologe/issues/5865)).
- Amélioration de l'historique des affectations ([#5875](https://github.com/MTES-MCT/histologe/issues/5875)).
- Ajout de types de partenaires ([#5913](https://github.com/MTES-MCT/histologe/issues/5913)).
- Correction de l'export des utilisateurs non-RT dans l'annuaire ([#5925](https://github.com/MTES-MCT/histologe/issues/5925)).
- Liste des signalements triée par étiquette et partenaire, sans tenir compte de la casse ([#5916](https://github.com/MTES-MCT/histologe/issues/5916)).
- Ancrage de la liste des signalements dans le back-office ([#5868](https://github.com/MTES-MCT/histologe/issues/5868)).

### Évolutions techniques
- Refactorisation de `JobEventRepository` et `SignalementDraftRepository` ([#5914](https://github.com/MTES-MCT/histologe/issues/5914)).
- Mise à jour des dépendances Composer ([#5912](https://github.com/MTES-MCT/histologe/issues/5912)).
- Remplacement de la librairie PHP Cron par le composant Symfony Scheduler ([#5863](https://github.com/MTES-MCT/histologe/issues/5863)).
- Mise à jour de Twig et Symfony pour corriger des vulnérabilités de sécurité ([#5887](https://github.com/MTES-MCT/histologe/issues/5887)).
- Suppression de la route de gestion des images du firewall principal pour des raisons de sécurité ([#5891](https://github.com/MTES-MCT/histologe/issues/5891)).
- Suppression ou limitation de l'utilisation des contextes de suivi et des types de suivi ([#5884](https://github.com/MTES-MCT/histologe/issues/5884) et [#5843](https://github.com/MTES-MCT/histologe/issues/5843)).
- Correction de fixtures ([#5874](https://github.com/MTES-MCT/histologe/issues/5874)).
- Activation du plugin heatmap ([#5870](https://github.com/MTES-MCT/histologe/issues/5870)).

### Autres changements
- Autorisation des scripts du plugin Matomo depuis stats.beta.gouv.fr ([#5938](https://github.com/MTES-MCT/histologe/issues/5938)).
- Mise à jour de la documentation de l'API ([#5928](https://github.com/MTES-MCT/histologe/issues/5928)).
- Correction de la synchronisation des erreurs messenger doctrine ([#5921](https://github.com/MTES-MCT/histologe/issues/5921)).
- Amélioration de l'accessibilité de la liste des signalements ([#5900](https://github.com/MTES-MCT/histologe/issues/5900)).
- Précision sur les liens des démarches accélérées pour l'accessibilité ([#5896](https://github.com/MTES-MCT/histologe/issues/5896)).
- Correction de la conversion array to string pour l'envoi de mails ([#5853](https://github.com/MTES-MCT/histologe/issues/5853)).
- Diverses modifications de contenu dans le front et back-office ([#5862](https://github.com/MTES-MCT/histologe/issues/5862)).
- Suppression d'exceptions ajoutées lors du passage à phpstan2 ([#5813](https://github.com/MTES-MCT/histologe/issues/5813)).
- Suppression d'une commande temporaire ([#5880](https://github.com/MTES-MCT/histologe/issues/5880)).
- Ajout de la commande sish reprise commande dossier rejet ([#5877](https://github.com/MTES-MCT/histologe/issues/5877)).
