## Changelog : histologe (30 derniers jours, au 13 mai 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application histologe, en se concentrant sur l'expérience utilisateur, notamment sur les formulaires de signalement et de service secours, ainsi que sur l'amélioration de la gestion des données et des visualisations. Des corrections de bugs et des optimisations techniques ont également été apportées pour garantir la stabilité et la performance de la plateforme.

### Évolutions fonctionnelles
- **Formulaire Service Secours :**
    - Ajout d'un bouton "Annuler" pour réinitialiser la saisie. [#5607](https://github.com/MTES-MCT/histologe/issues/5607)
    - Possibilité de filtrer les adresses de la BAN par département. [#5599](https://github.com/MTES-MCT/histologe/issues/5599)
    - Ajout des nouvelles données sur les autres pages, API et exports. [#5557](https://github.com/MTES-MCT/histologe/issues/5557)
    - Ajout de qualifications pour le service secours desordres. [#5653](https://github.com/MTES-MCT/histologe/issues/5653)
- **Formulaire Police :** Finalisation des étapes 5 et récapitulatif avant soumission. [#5548](https://github.com/MTES-MCT/histologe/issues/5548) et [#5591](https://github.com/MTES-MCT/histologe/issues/5591)
- **Suivi Usager :**
    - Possibilité d'éditer les informations générales sur le logement. [#5482](https://github.com/MTES-MCT/histologe/issues/5482)
    - Edition du type et de la composition du logement. [#5569](https://github.com/MTES-MCT/histologe/issues/5569)
- **Signalement :**
    - Affichage d'un badge indiquant l'EPCI lié à la commune. [#5682](https://github.com/MTES-MCT/histologe/issues/5682)
    - Ajout de la conclusion de visite "Suspicion d'insalubrité". [#5603](https://github.com/MTES-MCT/histologe/issues/5603)
    - Création de visites pendant l'import de signalements par CSV. [#5565](https://github.com/MTES-MCT/histologe/issues/5565)
- **Dashboard (BO) :**
    - Pagination des dernières actions. [#5646](https://github.com/MTES-MCT/histologe/issues/5646)
    - Catégorie "Affectation en attente". [#5606](https://github.com/MTES-MCT/histologe/issues/5606)
- **SCHS / Santé Habitat :** Limitation à un seul envoi vers Santé Habitat et autorisation pour les partenaires SCHS. [#564](https://github.com/MTES-MCT/histologe/issues/5574)
- **Fiche BO :** Affichage de la valeur structure déclarant dès qu'elle est renseignée. [#5699](https://github.com/MTES-MCT/histologe/issues/5699)

### Évolutions techniques
- Mise à jour de la librairie Intervention\Image vers la version 4. [#5657](https://github.com/MTES-MCT/histologe/issues/5657)
- Mise à jour des paquets npm. [#5665](https://github.com/MTES-MCT/histologe/issues/5665) et [#5624](https://github.com/MTES-MCT/histologe/issues/5624)
- Suppression de code mort. [#5673](https://github.com/MTES-MCT/histologe/issues/5673)
- Normalisation des données : suppression des champs faisant doublon. [#5601](https://github.com/MTES-MCT/histologe/issues/5601)
- Amélioration de la visualisation des modifications. [#5573](https://github.com/MTES-MCT/histologe/issues/5573)
- Ajout d'une factory spécifique pour Service secours et ajout de tests fonctionnels. [#5633](https://github.com/MTES-MCT/histologe/issues/5633)
- Correction d'un problème de rechargement de panel après une erreur 404. [#5662](https://github.com/MTES-MCT/histologe/issues/5662)
- Correction d'un problème d'accessibilité dans l'espace documentaire. [#5677](https://github.com/MTES-MCT/histologe/issues/5677)
- Ajout de `referrerPolicy` pour corriger une erreur Leaflet. [#5609](https://github.com/MTES-MCT/histologe/issues/5609)

### Autres changements
- Documentation : Mock des services BAN et RnB pour éviter les plantages de C/I. [#5566](https://github.com/MTES-MCT/histologe/issues/5566)
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Mise à jour des dépendances. [#5706](https://github.com/MTES-MCT/histologe/issues/5706) et [#5708](https://github.com/MTES-MCT/histologe/issues/5708)
- Correction de l'affichage des infobulles. [#5658](https://github.com/MTES-MCT/histologe/issues/5658)
- Ajout et retrait de filtres sur la liste des signalements. [#5598](https://github.com/MTES-MCT/histologe/issues/5598)
- Correction du validateur de numéros de téléphone. [#5661](https://github.com/MTES-MCT/histologe/issues/5661)
- Correction de l'archivage de draft et gestion adresse libre inconnue. [#5667](https://github.com/MTES-MCT/histologe/issues/5667)
- Correction d'un bug empêchant l'édition pour les profils Bailleurs. [#5652](https://github.com/MTES-MCT/histologe/issues/5652)
- Ajout de suivi initial en création des signalements INJONCTION_BAILLEUR. [#5577](https://github.com/MTES-MCT/histologe/issues/5577)
- Suppression de la référence supliqué sur le FO en INJONCTION_CLOSED. [#5586](https://github.com/MTES-MCT/histologe/issues/5586)
- Changement de l'ordre d'affichage des photos. [#5602](https://github.com/MTES-MCT/histologe/issues/5602)
- Gestion de la mise à vide d'un mail occupant via l'édition FO. [#5645](https://github.com/MTES-MCT/histologe/issues/5645)
- Correction d'un bug sur le champ infoProcedureBailMoyen. [#5610](https://github.com/MTES-MCT/histologe/issues/5610)
- Intégration du champ autresOccupantsDesordre et d'un filtre provenance. [#5632](https://github.com/MTES-MCT/histologe/issues/5632)
- Ajout d'une demande d'arrêt de procédure. [#5640](https://github.com/MTES-MCT/histologe/issues/5640)
- Suppression de job_event après 1 mois. [#5509](https://github.com/MTES-MCT/histologe/issues/5509)
- Ajout de la possibilité pour les RT de supprimer les documents uploadés par un partenaire. [#5588](https://github.com/MTES-MCT/histologe/issues/5588)
- Ajout de liens pour supprimer le filtre MySignalementsOnlyFilter. [#5611](https://github.com/MTES-MCT/histologe/issues/5611)
- Correction de l'export CSV. [#5634](https://github.com/MTES-MCT/histologe/issues/5634)
- Correction de plusieurs validations de champs. [#5583](https://github.com/MTES-MCT/histologe/issues/5583)
