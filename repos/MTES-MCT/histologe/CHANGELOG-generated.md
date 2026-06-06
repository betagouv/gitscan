## Changelog : histologe (30 derniers jours, au 4 juin 2026)

### Résumé
Ce mois-ci, histologe a bénéficié d'une série d'améliorations axées sur l'expérience utilisateur, la sécurité et la stabilité technique. Les agents de l'administration bénéficieront d'une meilleure gestion des signalements, d'une accessibilité accrue et de corrections de bugs importants. Des mises à jour de sécurité ont également été appliquées pour protéger les données sensibles.

### Évolutions fonctionnelles
- Amélioration de l'export des utilisateurs dans l'annuaire ([#5925](https://github.com/MTES-MCT/histologe/issues/5925)).
- Mise à jour de la documentation de l'API ([#5928](https://github.com/MTES-MCT/histologe/issues/5928)).
- Affichage plus précis de l'occupation du logement dans les signalements ([#5909](https://github.com/MTES-MCT/histologe/issues/5909)).
- Ajout du nom du travailleur social lors de l'enregistrement d'un signalement ([#5867](https://github.com/MTES-MCT/histologe/issues/5867)).
- Possibilité pour les bailleurs d'envoyer des suivis et des documents pendant la procédure de démarche accélérée ([#5819](https://github.com/MTES-MCT/histologe/issues/5819)).
- Amélioration de la gestion des affectations dans l'historique des signalements ([#5851](https://github.com/MTES-MCT/histologe/issues/5851)).
- Correction du blocage du parcours "Parc public" lorsque le bailleur n'est pas prévenu ou l'a été trop récemment ([#5854](https://github.com/MTES-MCT/histologe/issues/5854)).
- Ajout de liserets pour améliorer la lisibilité du récapitulatif de signalement ([#5865](https://github.com/MTES-MCT/histologe/issues/5865)).
- Ajout de messages d'information pour les logements vacants lors de l'ajout de suivi ([#5897](https://github.com/MTES-MCT/histologe/issues/5897)).
- Amélioration de l'accessibilité de la liste des signalements ([#5900](https://github.com/MTES-MCT/histologe/issues/5900)).
- Amélioration de l'accessibilité pour les utilisateurs API, services secours, bailleurs et communes ([#5826](https://github.com/MTES-MCT/histologe/issues/5826), [#5832](https://github.com/MTES-MCT/histologe/issues/5832), [#5823](https://github.com/MTES-MCT/histologe/issues/5823)).
- Correction de la réouverture de la modale de sélection de bâtiment lors d'un changement d'adresse ([#5839](https://github.com/MTES-MCT/histologe/issues/5839)).
- Ajout d'étiquettes et de partenaires triés alphabétiquement dans la liste des signalements ([#5916](https://github.com/MTES-MCT/histologe/issues/5916)).
- Ancrage de la liste des signalements ([#5868](https://github.com/MTES-MCT/histologe/issues/5868)).

### Évolutions techniques
- Refactorisation de `JobEventRepository` et `SignalementDraftRepository` ([#5914](https://github.com/MTES-MCT/histologe/issues/5914)).
- Mise à jour des dépendances Composer ([#5912](https://github.com/MTES-MCT/histologe/issues/5912)).
- Remplacement du lib php cron par le composant symfony scheduler ([#5863](https://github.com/MTES-MCT/histologe/issues/5863)).
- Remplacement de phpspreadsheets par d'autres librairies ([#5836](https://github.com/MTES-MCT/histologe/issues/5836)).
- Mise à jour de Twig et Symfony pour corriger des vulnérabilités de sécurité ([#5887](https://github.com/MTES-MCT/histologe/issues/5887)).
- Suppression ou limitation de l'utilisation des contextes de suivi ([#5884](https://github.com/MTES-MCT/histologe/issues/5884), [#5843](https://github.com/MTES-MCT/histologe/issues/5843)).
- Suppression de la route de gestion des images du firewall main ([#5891](https://github.com/MTES-MCT/histologe/issues/5891)).
- Ajout d'un postmortem pour une vulnérabilité YesWeHack ([#5847](https://github.com/MTES-MCT/histologe/issues/5847)).
- Correction d'une erreur d'environnement relevée par YesWeHack ([#5838](https://github.com/MTES-MCT/histologe/issues/5838)).
- Mise à jour des packages npm ([#5845](https://github.com/MTES-MCT/histologe/issues/5845)).
- Correction de fixtures ([#5874](https://github.com/MTES-MCT/histologe/issues/5874)).

### Autres changements
- Mise à jour de la collection Postman ([#5830](https://github.com/MTES-MCT/histologe/issues/5830)).
- Suppression du manager ([#5787](https://github.com/MTES-MCT/histologe/issues/5787)).
- Correction de conversion array to string pour l'envoi de mails ([#5853](https://github.com/MTES-MCT/histologe/issues/5853)).
- Diverses modifications de contenu ([#5862](https://github.com/MTES-MCT/histologe/issues/5862)).
- Suppression d'exceptions ajoutées lors du passage à phpstan2 ([#5813](https://github.com/MTES-MCT/histologe/issues/5813)).
