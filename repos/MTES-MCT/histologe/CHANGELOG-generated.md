## Changelog : histologe (30 derniers jours, au 05 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans le back-office, notamment en termes d'accessibilité et de performance. Des corrections de bugs et des optimisations techniques ont également été apportées, ainsi que des améliorations concernant l'interconnexion avec d'autres systèmes et la gestion des données.

### Évolutions fonctionnelles
- Ajout de l'heure dans le suivi de visite programmée dans le back-office. [#5759](https://github.com/MTES-MCT/histologe/issues/5759)
- Amélioration de l'affichage de la date et de l'heure des clubs en fonction du fuseau horaire de l'utilisateur, dans les emails et le tableau de bord. [#5778](https://github.com/MTES-MCT/histologe/issues/5778)
- Ajout de filtres pour les événements. [#5713](https://github.com/MTES-MCT/histologe/issues/5713)
- Affichage de la valeur du déclarant structure dès qu'elle est renseignée dans la fiche du back-office. [#5699](https://github.com/MTES-MCT/histologe/issues/5699)
- Ajout de mails de rappel d'évènement lié au widget du dashboard et modification du texte de la tuile dashboard. [#5683](https://github.com/MTES-MCT/histologe/issues/5683)
- Affichage d'un badge indiquant l'EPCI lié à la commune dans le back-office (signalement). [#5682](https://github.com/MTES-MCT/histologe/issues/5682)
- Correction de la pagination des connexions dans le SI. [#5755](https://github.com/MTES-MCT/histologe/issues/5755)
- Gestion de la resynchronisation des messages en cas de doublon. [#5754](https://github.com/MTES-MCT/histologe/issues/5754)

### Évolutions techniques
- Mise à jour de PHPUnit de la version 9 à la version 13. [#5766](https://github.com/MTES-MCT/histologe/issues/5766)
- Mise à jour de PostCSS. [#5809](https://github.com/MTES-MCT/histologe/issues/5809)
- Mise à jour de MySQL et Redis. [#5700](https://github.com/MTES-MCT/histologe/issues/5700)
- Déplacement des méthodes liées aux statistiques vers un service dédié (query service) pour une meilleure organisation du code. [#5711](https://github.com/MTES-MCT/histologe/issues/5711)
- Amélioration de la gestion des chargements de données après édition dans le back-office et utilisation de messages flash AJAX. [#5546](https://github.com/MTES-MCT/histologe/issues/5546)
- Mise à jour de la librairie phpspreadsheet. [#5712](https://github.com/MTES-MCT/histologe/issues/5712)
- Mise à jour de la dépendance `follow-redirects` npm. [#5730](https://github.com/MTES-MCT/histologe/issues/5730)
- Ajout d'un fichier d'environnement CI. [#5670](https://github.com/MTES-MCT/histologe/issues/5670)
- Optimisation du comptage pour le panneau "Dossiers fermés par les communes". [#5735](https://github.com/MTES-MCT/histologe/issues/5735)
- Activation de la synchronisation pour les SCHS connectés à Santé Habitat. [#5684](https://github.com/MTES-MCT/histologe/issues/5684)

### Autres changements
- Améliorations de l'accessibilité du tableau de bord (passage d'onglet au clavier, zoom sur l'avatar). [#5732](https://github.com/MTES-MCT/histologe/issues/5732), [#5734](https://github.com/MTES-MCT/histologe/issues/5734), [#5737](https://github.com/MTES-MCT/histologe/issues/5737)
- Correction de l'archivage des brouillons et gestion des adresses libres inconnues dans les formulaires pro. [#5667](https://github.com/MTES-MCT/histologe/issues/5667)
- Correction d'un bug concernant la contrainte d'invariant fiscal lors de l'édition dans le front-office et affichage du nom du service de secours. [#5691](https://github.com/MTES-MCT/histologe/issues/5691)
- Déconnexion d'OILHI. [#5688](https://github.com/MTES-MCT/histologe/issues/5688)
- Ajout de phrases de contexte dans le back-office. [#5696](https://github.com/MTES-MCT/histologe/issues/5696)
- Amélioration de l'accessibilité de l'espace documentaire. [#5677](https://github.com/MTES-MCT/histologe/issues/5677)
- Préserver les données exif des photos. [#5702](https://github.com/MTES-MCT/histologe/issues/5702)
- Contrôle de la date à partir des données exif pour éviter les plantages. [#5801](https://github.com/MTES-MCT/histologe/issues/5801)
