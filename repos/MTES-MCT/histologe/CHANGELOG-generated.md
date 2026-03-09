## Changelog : histologe (30 derniers jours)

### Résumé
Ce changelog résume les améliorations apportées à histologe au cours des 30 derniers jours. Les mises à jour incluent des corrections de bugs, des améliorations de l'interface utilisateur, de nouvelles fonctionnalités pour faciliter le suivi des signalements et des optimisations techniques pour améliorer la performance et la stabilité de l'application.

### Évolutions fonctionnelles

- Correction d'un bug empêchant la sauvegarde du début des désordres. [#5515](https://github.com/MTES-MCT/histologe/issues/5515)
- Correction de l'image manquante sur la page 404. [#5517](https://github.com/MTES-MCT/histologe/issues/5517)
- Nettoyage du contenu de requête dans les emails d’erreur pour une meilleure lisibilité. [#5507](https://github.com/MTES-MCT/histologe/issues/5507)
- Correction d'un bug de filtre du code INSEE, notamment pour la Corse. [#5502](https://github.com/MTES-MCT/histologe/issues/5502)
- Masquage du premier bloc si déjà répondu. [#5493](https://github.com/MTES-MCT/histologe/issues/5493)
- Correction d'un problème de valeur pour la création de source dans l'interface d'administration. [#5484](https://github.com/MTES-MCT/histologe/issues/5484)
- Ajout du filtre code INSEE à la liste des signalements. [#5468](https://github.com/MTES-MCT/histologe/issues/5468)
- Ajout de la date de réaffectation. [#5465](https://github.com/MTES-MCT/histologe/issues/5465)
- Ajout de données explicites pour la source de création de signalement. [#5431](https://github.com/MTES-MCT/histologe/issues/5431)
- Revue des notifications tiers déclarant pro. [#5462](https://github.com/MTES-MCT/histologe/issues/5462)
- Modification des informations de l'agence dans le suivi usager. [#5355](https://github.com/MTES-MCT/histologe/issues/5355)
- Correction du mail de notification lors de la suppression d'un SA (Super Administrateur). [#5452](https://github.com/MTES-MCT/histologe/issues/5452)
- Limitation du sélecteur de bâtiment dans le frontend. [#5451](https://github.com/MTES-MCT/histologe/issues/5451)
- Utilisation d'un formulaire multi-étape pour le formulaire service secours. [#5398](https://github.com/MTES-MCT/histologe/issues/5398)
- Correction d'un bug lié à la notification de visite pour les partenaires externes. [#5447](https://github.com/MTES-MCT/histologe/issues/5447)
- Réinitialisation du formulaire dans une modale après une soumission réussie sans rechargement de page. [#5439](https://github.com/MTES-MCT/histologe/issues/5439)
- Corrections de bugs sur les visites. [#5437](https://github.com/MTES-MCT/histologe/issues/5437)
- Blocage des emails aux usagers lorsque le logement est vacant. [#5310](https://github.com/MTES-MCT/histologe/issues/5310)
- Améliorations diverses sur la gestion des e-mails en échec. [#5373](https://github.com/MTES-MCT/histologe/issues/5373)
- Modification de la demande de poursuite de procédure. [#5427](https://github.com/MTES-MCT/histologe/issues/5427)
- Ajout du nouveau système de messages de confirmation / erreur pour les visites. [#5265](https://github.com/MTES-MCT/histologe/issues/5265)
- Ajout de skiplinks pour passer les filtres et la liste dans l'interface d'administration. [#5377](https://github.com/MTES-MCT/histologe/issues/5377)
- Amélioration du filtre signalement injonction. [#5385](https://github.com/MTES-MCT/histologe/issues/5385)
- Ajout du choix de bâtiment pour les usagers qui saisissent une adresse à la main. [#5341](https://github.com/MTES-MCT/histologe/issues/5341)
- Ajout du nom du partenaire qui a saisi le signalement pro. [#5380](https://github.com/MTES-MCT/histologe/issues/5380)
- Ajout de la qualification "Saleté". [#5371](https://github.com/MTES-MCT/histologe/issues/5371)
- Division en deux du menu SA (Super Administrateur). [#5392](https://github.com/MTES-MCT/histologe/issues/5392)
- Automatisation de l'envoi du rappel au bailleur sans réponse. [#5366](https://github.com/MTES-MCT/histologe/issues/5366)

### Évolutions techniques

- Exécution de la synchronisation des fichiers bucket S3 via un service jobless. [#5261](https://github.com/MTES-MCT/histologe/issues/5261)
- Ajout des linter JS dans la CI (Continuous Integration). [#5424](https://github.com/MTES-MCT/histologe/issues/5424)
- Mise à jour de Webpack en 5.105.1. [#5407](https://github.com/MTES-MCT/histologe/issues/5407)
- Suppression de données inutiles dans la configuration de l'API. [#5438](https://github.com/MTES-MCT/histologe/issues/5438)
- Suppression de l'autocomplete de la recherche checkbox component. [#5408](https://github.com/MTES-MCT/histologe/issues/5408)

### Autres changements

- Suppression d'options de données vides. [#5462](https://github.com/MTES-MCT/histologe/issues/5462)
- Ajout de communes. [#5367](https://github.com/MTES-MCT/histologe/issues/5367)
- Suppression de dépréciations. [#5422](https://github.com/MTES-MCT/histologe/issues/5422)
- Mise à jour de dépendances mineures. [#5393](https://github.com/MTES-MCT/histologe/issues/5393) et [#5433](https://github.com/MTES-MCT/histologe/issues/5433)
- Ajout d'un événement Matomo. [#5366](https://github.com/MTES-MCT/histologe/issues/5366)
- Ajout d'une contrainte de lien à l'email du partenaire. [#5395](https://github.com/MTES-MCT/histologe/issues/5395)
- Ajout de la catégorie "suivi" manquante. [#5417](https://github.com/MTES-MCT/histologe/issues/5417)
