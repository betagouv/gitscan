## Changelog : histologe (30 derniers jours, au 29 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans le back-office (BO) et le front-office (FO), notamment en termes d'accessibilité, de gestion des données et de correction de bugs. Des améliorations techniques ont également été apportées pour optimiser les performances et la stabilité de la plateforme.

### Évolutions fonctionnelles
- **Tableau de bord (BO):**
    - Ajout de l'heure dans le suivi de visite programmée [#5759](https://github.com/MTES-MCT/histologe/issues/5759).
    - Amélioration de l'accessibilité, notamment pour le zoom sur les avatars et le passage entre les onglets au clavier [#5737](https://github.com/MTES-MCT/histologe/issues/5737), [#5734](https://github.com/MTES-MCT/histologe/issues/5734), [#5732](https://github.com/MTES-MCT/histologe/issues/5732).
    - Pagination des dernières actions et déplacement des requêtes vers un query service [#5646](https://github.com/MTES-MCT/histologe/issues/5646).
    - Ajout d'une catégorie "Affectation en attente" [#5606](https://github.com/MTES-MCT/histologe/issues/5606).
    - Affichage d'un badge indiquant l'EPCI lié à la commune sur la page de signalement [#5682](https://github.com/MTES-MCT/histologe/issues/5682).
- **Formulaire (FO):**
    - Intégration du champ "autresOccupantsDesordre" et d'un filtre "provenance" pour le formulaire service secours [#5632](https://github.com/MTES-MCT/histologe/issues/5632).
    - Correction du validateur de numéros de téléphone [#5661](https://github.com/MTES-MCT/histologe/issues/5661).
    - Possibilité pour les RT de supprimer les documents uploadés par un partenaire [#5588](https://github.com/MTES-MCT/histologe/issues/5588).
    - Gestion de la mise à vide d'un mail occupant via l'édition FO [#5645](https://github.com/MTES-MCT/histologe/issues/5645).
    - Correction d'un bug bloquant l'édition FO pour les profils BAILLEUR/BAILLEUR\_OCCUPANT [#5652](https://github.com/MTES-MCT/histologe/issues/5652).
- **Autres:**
    - Ajout de mails de rappel d'évènement lié au widget du dashboard et modification du texte de la tuile dashboard [#5683](https://github.com/MTES-MCT/histologe/issues/5683).
    - Affichage de la valeur structure déclarant dès qu'elle est renseignée dans la fiche BO [#5699](https://github.com/MTES-MCT/histologe/issues/5699).
    - Ajout de qualifications pour le service secours desordres [#5653](https://github.com/MTES-MCT/histologe/issues/5653).
    - Gestion de la synchronisation des visites avec Esabora SCHS, incluant la gestion du partenaire par défaut et la resynchronisation en cas de doublon [#5725](https://github.com/MTES-MCT/histologe/issues/5725).
    - Ajout d'un filtre pour les événements [#5713](https://github.com/MTES-MCT/histologe/issues/5713).
    - Affichage de la date/heure des clubs en fonction de la timezone de l'utilisateur sur les mails et le dashboard [#5778](https://github.com/MTES-MCT/histologe/issues/5778).

### Évolutions techniques
- **Infrastructure:**
    - Mise à jour de MySQL et Redis [#5700](https://github.com/MTES-MCT/histologe/issues/5700).
    - Mise à jour de Nginx [#5739](https://github.com/MTES-MCT/histologe/issues/5739).
- **Architecture:**
    - Déplacement des méthodes de statistiques vers un query service [#5711](https://github.com/MTES-MCT/histologe/issues/5711).
    - Réorganisation des services dans des sous-dossiers [#5690](https://github.com/MTES-MCT/histologe/issues/5690).
- **Performances:**
    - Optimisation du calcul du nombre de dossiers fermés par les communes [#5735](https://github.com/MTES-MCT/histologe/issues/5735).
    - Amélioration des chargements de données après édition BO [#5546](https://github.com/MTES-MCT/histologe/issues/5546).
- **Dépendances:**
    - Mise à jour de phpspreadsheet [#5712](https://github.com/MTES-MCT/histologe/issues/5712).
    - Mise à jour de Intervention\Image à la version 4 [#5657](https://github.com/MTES-MCT/histologe/issues/5657).
    - Mise à jour des paquets npm [#5665](https://github.com/MTES-MCT/histologe/issues/5665).
    - Mise à jour de follow-redirects [#5730](https://github.com/MTES-MCT/histologe/issues/5730).

### Autres changements
- Ajout d'un fichier d'environnement CI [#5670](https://github.com/MTES-MCT/histologe/issues/5670).
- Suppression de code mort [#5673](https://github.com/MTES-MCT/histologe/issues/5673).
- Préservation des données exif des photos [#5702](https://github.com/MTES-MCT/histologe/issues/5702).
- Suppression des jobs_event après 1 mois [#5509](https://github.com/MTES-MCT/histologe/issues/5509).
- Correction d'un bug empêchant le rechargement du panel après une erreur 404 [#5662](https://github.com/MTES-MCT/histologe/issues/5662).
- Déconnexion de OILHI [#5688](https://github.com/MTES-MCT/histologe/issues/5688).
- Activation de la synchronisation pour les SCHS connectés à Santé Habitat [#5684](https://github.com/MTES-MCT/histologe/issues/5684).
