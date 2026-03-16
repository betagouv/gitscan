## Changelog : histologe (30 derniers jours)

### Résumé
Les dernières mises à jour d'histologe se concentrent sur l'amélioration de l'expérience utilisateur, notamment dans les formulaires et le suivi des signalements. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. Des améliorations ont été apportées à l'API et à la gestion des emails.

### Évolutions fonctionnelles
- [BO - Signalement] Affichage des informations du bailleur même si le profil de l'occupant n'est pas défini. [#5543](https://github.com/MTES-MCT/histologe/issues/5543)
- [FO - Suivi usager] Possibilité d'éditer la situation du foyer. [#5473](https://github.com/MTES-MCT/histologe/issues/5473)
- [FO - Suivi signalement] Possibilité d'éditer les compléments d'adresse et la géolocalisation. [#5518](https://github.com/MTES-MCT/histologe/issues/5518)
- [BO - Communes] Possibilité d'éditer le code INSEE d'une commune. [#5520](https://github.com/MTES-MCT/histologe/issues/5520)
- [BO - Form Pro] Revue des notifications pour les tiers déclarant professionnels. [#5405](https://github.com/MTES-MCT/histologe/issues/5405)
- [FO - Formulaire police] Socle desordres implémenté. [#5533](https://github.com/MTES-MCT/histologe/issues/5533)
- [FO - Suivi usager - Détails dossier] Possibilité de modifier les informations de l'agence et de l'assurance. [#5355](https://github.com/MTES-MCT/histologe/issues/5355) & [#5458](https://github.com/MTES-MCT/histologe/issues/5458)
- [BO - Visites] Passage au nouveau système de messages de confirmation/erreur pour les visites. [#5265](https://github.com/MTES-MCT/histologe/issues/5265)
- [FO - Formulaire service secours] Utilisation d'un formulaire multi-étape. [#5398](https://github.com/MTES-MCT/histologe/issues/5398)
- [API] Ajout d'un filtre sur le code INSEE dans la liste des signalements. [#5468](https://github.com/MTES-MCT/histologe/issues/5468)

### Évolutions techniques
- [API RIAL] Ajout d'une variable d'environnement pour activer/désactiver l'API RIAL. [#5553](https://github.com/MTES-MCT/histologe/issues/5553)
- Ajout d'une option pour désactiver Clamav par défaut. [#5516](https://github.com/MTES-MCT/histologe/issues/5516)
- Ajout des linter JS dans la CI. [#5424](https://github.com/MTES-MCT/histologe/issues/5424)
- Suppression des dépréciations. [#5422](https://github.com/MTES-MCT/histologe/issues/5422)
- Suppression de la payload des logs HTTP. [#5503](https://github.com/MTES-MCT/histologe/issues/5503)
- Mise à jour des dépendances npm. [#5499](https://github.com/MTES-MCT/histologe/issues/5499) & [#5478](https://github.com/MTES-MCT/histologe/issues/5478)

### Autres changements
- Correction de bugs divers liés à l'affichage des dates, aux emails, et à la gestion des visites.
- Amélioration de la gestion des e-mails en échec. [#5373](https://github.com/MTES-MCT/histologe/issues/5373)
- Correction d'un bug lié au filtre code INSEE en Corse. [#5502](https://github.com/MTES-MCT/histologe/issues/5502)
- Ajout de la gestion des territoires pour le bailleur. [#5479](https://github.com/MTES-MCT/histologe/issues/5479)
- Suppression de données vides. [#5439](https://github.com/MTES-MCT/histologe/issues/5439)
- Correction de l'image manquante sur la page 404. [#5517](https://github.com/MTES-MCT/histologe/issues/5517)
- Gestion de la fermeture de procédure par l'usager. [#5460](https://github.com/MTES-MCT/histologe/issues/5460)
- Contrôle lors de l'ajout de tiers. [#5413](https://github.com/MTES-MCT/histologe/issues/5413)
- Ajout de sous-titres explicatifs au dashboard. [#5495](https://github.com/MTES-MCT/histologe/issues/5495)
- Correction de l'affichage des infos bailleurs. [#5543](https://github.com/MTES-MCT/histologe/issues/5543)
- Correction de l'affichage de la date de notification du bailleur. [#5530](https://github.com/MTES-MCT/histologe/issues/5530)
- Ajout d'une référence temporaire pour l'interconnexion SAS import. [#5540](https://github.com/MTES-MCT/histologe/issues/5540)
- Correction du mail de notification lors de la suppression d'un SA. [#5452](https://github.com/MTES-MCT/histologe/issues/5452)
- Correction de la gestion des notifications pour les partenaires affectables. [#5470](https://github.com/MTES-MCT/histologe/issues/5470)
- Blocage des emails aux usagers lorsque le logement est vacant. [#5310](https://github.com/MTES-MCT/histologe/issues/5310)
- Ajout de la boite de dialogue d'installation PWA personnalisée. [#5510](https://github.com/MTES-MCT/histologe/issues/5510)
- Correction des doublons incluant l'injonction. [#5542](https://github.com/MTES-MCT/histologe/issues/5542) & [#5537](https://github.com/MTES-MCT/histologe/issues/5537)
