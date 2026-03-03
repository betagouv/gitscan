## Changelog : histologe (30 derniers jours)

### Résumé
Les dernières mises à jour d'histologe améliorent l'expérience utilisateur et la gestion des signalements, notamment pour les agents de l'administration. Des corrections de bugs et des améliorations de l'interface ont été apportées, ainsi que des optimisations techniques pour la gestion des fichiers et l'intégration avec SISH. L'application continue d'évoluer pour faciliter la détection et la prise en charge du mal-logement.

### Évolutions fonctionnelles
- Ajout du choix de bâtiment pour les usagers saisissant une adresse manuellement dans le formulaire de signalement [#5341](https://github.com/MTES-MCT/histologe/issues/5341).
- Amélioration du filtre des signalements avec injonction [#5360](https://github.com/MTES-MCT/histologe/issues/5360).
- Ajout de la qualification "Saleté" dans la liste des signalements [#5371](https://github.com/MTES-MCT/histologe/issues/5371).
- Ajout du nom du partenaire ayant saisi un signalement professionnel dans la fiche signalement [#5380](https://github.com/MTES-MCT/histologe/issues/5380).
- Ajout de la donnée "Profil Occupant" dans le frontend et le backend [#5329](https://github.com/MTES-MCT/histologe/issues/5329).
- Possibilité d'ajouter des communes dans le back-office [#5367](https://github.com/MTES-MCT/histologe/issues/5367).
- Réorganisation des données et du design dans les détails de dossier du suivi usager (frontend) [#5324](https://github.com/MTES-MCT/histologe/issues/5324).
- Correction d'un bug empêchant l'affichage correct des valeurs pour la création de source [#5484](https://github.com/MTES-MCT/histologe/issues/5484).
- Correction d'un bug lié au filtre du code INSEE en Corse [#5502](https://github.com/MTES-MCT/histologe/issues/5502).
- Correction d'un bug lié à la date de réaffectation [#5464](https://github.com/MTES-MCT/histologe/issues/5464).
- Correction d'un bug Sentry lié à une exception Doctrine\ORM\NonUniqueResultException [#5476](https://github.com/MTES-MCT/histologe/issues/5476).
- Correction d'un bug empêchant l'affichage du premier bloc si déjà répondu [#5491](https://github.com/MTES-MCT/histologe/issues/5491).
- Correction d'un bug lié au tri des notifications [#5383](https://github.com/MTES-MCT/histologe/issues/5383).
- Correction d'un bug lié à l'envoi des événements Matomo [#5342](https://github.com/MTES-MCT/histologe/issues/5342).
- Correction d'un bug lié à la suppression d'un SA et à l'envoi du mail de notification [#5452](https://github.com/MTES-MCT/histologe/issues/5452).

### Évolutions techniques
- Mise en place d'un service Jobless pour l'exécution de la synchronisation des fichiers du bucket S3 [#5261](https://github.com/MTES-MCT/histologe/issues/5261).
- Organisation des nouveaux fichiers S3 par année/mois pour optimiser les synchronisations [#5331](https://github.com/MTES-MCT/histologe/issues/5331).
- Ajout de linter JS dans la CI [#5424](https://github.com/MTES-MCT/histologe/issues/5424).
- Mise à jour de Webpack vers la version 5.105.1 [#5407](https://github.com/MTES-MCT/histologe/issues/5407).
- Ajout d'informations sur le territoire pour l'accès à l'API [#5334](https://github.com/MTES-MCT/histologe/issues/5334).
- Suppression de données inutiles dans l'API [#5401](https://github.com/MTES-MCT/histologe/issues/5401).
- Suppression de l'option de données vides [#5439](https://github.com/MTES-MCT/histologe/issues/5439).
- Limitation du sélecteur de construction FO [#5450](https://github.com/MTES-MCT/histologe/issues/5450).
- Suppression du payload du log de requête HTTP [#5501](https://github.com/MTES-MCT/histologe/issues/5501).

### Autres changements
- Ajout d'un événement Matomo pour la démarche accélérée [#5366](https://github.com/MTES-MCT/histologe/issues/5366).
- Division du menu SA en deux parties [#5392](https://github.com/MTES-MCT/histologe/issues/5392).
- Ajout de skiplinks pour passer les filtres et la liste dans le back-office [#5377](https://github.com/MTES-MCT/histologe/issues/5377).
- Modification de la demande de poursuite de procédure [#5426](https://github.com/MTES-MCT/histologe/issues/5426).
- Mise à jour des dépendances Composer [#5350](https://github.com/MTES-MCT/histologe/issues/5350).
- Suppression des alertes immédiates dans les notifications [#5356](https://github.com/MTES-MCT/histologe/issues/5356).
- Correction de la notification "notify-visit" pour les partenaires externes [#5447](https://github.com/MTES-MCT/histologe/issues/5447).
- Améliorations diverses sur la gestion des e-mails en échec [#5373](https://github.com/MTES-MCT/histologe/issues/5373).
- Suppression des dépréciations [#5422](https://github.com/MTES-MCT/histologe/issues/5422).
- Mise à jour de npm minimatch [#5499](https://github.com/MTES-MCT/histologe/issues/5499).
- Ajout de la catégorie de suivi manquante [#5400](https://github.com/MTES-MCT/histologe/issues/5400).
- Ajout d'une route par service pour le service secours [#5344](https://github.com/MTES-MCT/histologe/issues/5344).
- Mise en place d'un formulaire multi-étape pour le formulaire service secours [#5398](https://github.com/MTES-MCT/histologe/issues/5398).
- Correction d'un bug lié à la disparition du sous-domaine dans le staging du service secours [#5425](https://github.com/MTES-MCT/histologe/issues/5425).
- Blocage des emails aux usagers lorsque le logement est vacant [#5310](https://github.com/MTES-MCT/histologe/issues/5310).
- Ajout de la possibilité de lier une contrainte à un email de partenaire [#5384](https://github.com/MTES-MCT/histologe/issues/5384).
- Correction de bugs sur les visites [#5435](https://github.com/MTES-MCT/histologe/issues/5435) et [#5434](https://github.com/MTES-MCT/histologe/issues/5434).
- Mise à jour de la documentation pour l'explicitation des données de la source de création de signalement [#5431](https://github.com/MTES-MCT/histologe/issues/5431).
- Correction du tri des tags par libellé dans la vue du signalement [#4981](https://github.com/MTES-MCT/histologe/issues/4981).
- Ajout de la possibilité de réinitialiser le formulaire dans une modale après une soumission réussie sans rechargement de la page [#5429](https://github.com/MTES-MCT/histologe/issues/5429).
- Ajout d'une URI à la liste bloquée en cas de maintenance [#5418](https://github.com/MTES-MCT/histologe/issues/5418).
- Suppression de l'autocomplétion du composant de recherche checkbox [#5406](https://github.com/MTES-MCT/histologe/issues/5406).
- Maintien du tri des notifications lors de la suppression [#5383](https://github.com/MTES-MCT/histologe/issues/5383).
- Ajout du décompte des visites dans le back-office [#5409](https://github.com/MTES-MCT/histologe/issues/5409).
- Mise à jour des dépendances mineures [#5480](https://github.com/MTES-MCT/histologe/issues/5480) et [#5382](https://github.com/MTES-MCT/histologe/issues/5382).
