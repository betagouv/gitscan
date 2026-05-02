## Changelog : histologe (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, histologe a bénéficié d'améliorations significatives en termes d'expérience utilisateur, notamment au niveau de l'accessibilité et de la gestion des données. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la stabilité et la performance de l'application. Des évolutions ont été implémentées pour faciliter l'interconnexion avec d'autres services et améliorer la gestion des partenaires SCHS.

### Évolutions fonctionnelles

- Amélioration de l'affichage de la date et de l'heure des clubs en fonction du fuseau horaire de l'utilisateur sur les emails et le tableau de bord. [#5785](https://github.com/MTES-MCT/histologe/issues/5785)
- Ajout de l'heure dans le suivi des visites programmées. [#5759](https://github.com/MTES-MCT/histologe/issues/5759)
- Correction de la pagination des connexions SI. [#5758](https://github.com/MTES-MCT/histologe/issues/5758)
- Ajout d'un filtre pour les événements. [#5740](https://github.com/MTES-MCT/histologe/issues/5740)
- Amélioration de l'accessibilité du zoom sur l'avatar et le libellé du lien vers les dossiers sur le tableau de bord. [#5737](https://github.com/MTES-MCT/histologe/issues/5737)
- Préservation des données EXIF des photos. [#5702](https://github.com/MTES-MCT/histologe/issues/5702)
- Ajout de mails de rappel d'événements liés au widget du dashboard et modification du texte de la tuile dashboard. [#5683](https://github.com/MTES-MCT/histologe/issues/5683)
- Intégration du champ "autresOccupantsDesordre" et d'un filtre "provenance" dans le formulaire service secours. [#5632](https://github.com/MTES-MCT/histologe/issues/5632)
- Ajout de la possibilité de demander un arrêt de procédure. [#5640](https://github.com/MTES-MCT/histologe/issues/5640)
- Pagination des dernières actions sur le tableau de bord. [#5646](https://github.com/MTES-MCT/histologe/issues/5646)
- Ajout de qualifications pour le service secours des désordres. [#5659](https://github.com/MTES-MCT/histologe/issues/5659)
- Affichage d'un badge indiquant l'EPCI lié à la commune sur le tableau de bord. [#5682](https://github.com/MTES-MCT/histologe/issues/5682)
- Correction de l'affichage du validateur de numéros de téléphone sur la page de suivi des signalements. [#5661](https://github.com/MTES-MCT/histologe/issues/5661)
- Limitation à un seul envoi vers Santé Habitat pour les partenaires SCHS et autorisation de l'envoi de dossiers à Santé Habitat. [#5574](https://github.com/MTES-MCT/histologe/issues/5574)

### Évolutions techniques

- Mise à jour de Nginx. [#5739](https://github.com/MTES-MCT/histologe/issues/5739)
- Amélioration du passage d'un onglet à l'autre au clavier sur le tableau de bord. [#5732](https://github.com/MTES-MCT/histologe/issues/5732)
- Optimisation du comptage pour le panneau "Dossiers fermés par les communes". [#5736](https://github.com/MTES-MCT/histologe/issues/5736)
- Déplacement des méthodes liées aux statistiques vers un service dédié. [#5711](https://github.com/MTES-MCT/histologe/issues/5711)
- Mise à jour de MySQL et Redis. [#5700](https://github.com/MTES-MCT/histologe/issues/5700)
- Réorganisation des services dans des sous-dossiers pour une meilleure structure. [#5690](https://github.com/MTES-MCT/histologe/issues/5690)
- Mise à jour de la librairie Intervention\Image vers la version 4. [#5668](https://github.com/MTES-MCT/histologe/issues/5668)
- Mise à jour des paquets npm. [#5665](https://github.com/MTES-MCT/histologe/issues/5665)

### Autres changements

- Suppression de code mort. [#5673](https://github.com/MTES-MCT/histologe/issues/5673)
- Correction d'un bug empêchant l'édition des formulaires pour les profils BAILLEUR/BAILLEUR_OCCUPANT et remplacement du terme "Bailleur occupant". [#5652](https://github.com/MTES-MCT/histologe/issues/5652)
- Ajout de phrases de contexte pour améliorer la clarté. [#5696](https://github.com/MTES-MCT/histologe/issues/5696)
- Amélioration des chargements de données après édition dans le back-office et ajout de messages flash AJAX. [#5695](https://github.com/MTES-MCT/histologe/issues/5695)
- Déconnexion d'OILHI. [#5688](https://github.com/MTES-MCT/histologe/issues/5688)
- Correction d'un problème de rechargement du panneau après une erreur 404. [#5663](https://github.com/MTES-MCT/histologe/issues/5663)
- Correction des suivis pour les agents sur la page de suivi des signalements. [#5660](https://github.com/MTES-MCT/histologe/issues/5660)
