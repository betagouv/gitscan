## Changelog : histologe (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, histologe a bénéficié d'améliorations significatives sur les formulaires de signalement et de suivi, notamment pour les cas de service secours et d'injonction aux bailleurs. Des corrections de bugs et des optimisations ont également été apportées pour améliorer l'expérience utilisateur et la stabilité de la plateforme, en particulier dans le back-office.

### Évolutions fonctionnelles
- **Formulaire Service Secours :**
    - Ajout de qualifications pour les signalements de service secours. [#5653](https://github.com/MTES-MCT/histologe/pull/5653)
    - Possibilité de filtrer les adresses de la BAN par département. [#5599](https://github.com/MTES-MCT/histologe/issues/5599)
    - Ajout d'un bouton d'annulation pour réinitialiser la saisie. [#5607](https://github.com/MTES-MCT/histologe/issues/5607)
    - Intégration du champ `autresOccupantsDesordre` et d'un filtre de provenance. [#5632](https://github.com/MTES-MCT/histologe/issues/5632)
- **Formulaire Police :** Finalisation des étapes de saisie et de récapitulatif. [#5548](https://github.com/MTES-MCT/histologe/issues/5548), [#5591](https://github.com/MTES-MCT/histologe/issues/5591)
- **Suivi Signalement :**
    - Correction du validateur de numéros de téléphone. [#5661](https://github.com/MTES-MCT/histologe/issues/5661)
    - Ajout et retrait de filtres dans la liste des signalements (back-office). [#5598](https://github.com/MTES-MCT/histologe/issues/5598)
    - Ajout de la conclusion de visite "Suspicion d'insalubrité". [#5603](https://github.com/MTES-MCT/histologe/issues/5603)
    - Edition du type et de la composition du logement. [#5569](https://github.com/MTES-MCT/histologe/issues/5569)
- **Back-Office :**
    - Affichage d'un badge indiquant l'EPCI lié à la commune. [#5682](https://github.com/MTES-MCT/histologe/issues/5682)
    - Pagination des dernières actions dans le dashboard. [#5646](https://github.com/MTES-MCT/histologe/issues/5646)
    - Possibilité pour les RT de supprimer les documents uploadés par un partenaire. [#5588](https://github.com/MTES-MCT/histologe/issues/5588)
- **SCHS / Santé Habitat :** Limitation à un seul envoi vers Santé Habitat et autorisation pour les partenaires SCHS. [#5574](https://github.com/MTES-MCT/histologe/issues/5574)
- **Démarche Accélérée :** Ajout de la demande d'arrêt de procédure et clôture bailleur. [#5640](https://github.com/MTES-MCT/histologe/issues/5640), [#5535](https://github.com/MTES-MCT/histologe/issues/5535)

### Évolutions techniques
- Mise à jour de la librairie `Intervention\Image` vers la version 4. [#5657](https://github.com/MTES-MCT/histologe/pull/5657)
- Amélioration de l'architecture pour déplacer les requêtes vers un `queryservice`. [#5646](https://github.com/MTES-MCT/histologe/issues/5646)
- Suppression de code mort. [#5673](https://github.com/MTES-MCT/histologe/pull/5673)
- Correction d'un problème de rechargement de panel après une erreur 404. [#5662](https://github.com/MTES-MCT/histologe/issues/5662)
- Ajout de tests fonctionnels pour le service secours. [#5633](https://github.com/MTES-MCT/histologe/issues/5633)

### Autres changements
- Correction de l'affichage de la valeur structure déclarant dans la fiche BO dès qu'elle est renseignée. [#5699](https://github.com/MTES-MCT/histologe/issues/5699)
- Correction de bugs liés à l'édition des formulaires (FO) pour les profils bailleur/occupant. [#5652](https://github.com/MTES-MCT/histologe/issues/5652)
- Correction de l'archivage des brouillons et de la gestion des adresses libres inconnues dans le formulaire pro. [#5667](https://github.com/MTES-MCT/histologe/issues/5667)
- Correction de l'affichage des infobulles dans le back-office. [#5658](https://github.com/MTES-MCT/histologe/issues/5658)
- Ajout d'un suivi initial en création des signalements INJONCTION_BAILLEUR. [#5577](https://github.com/MTES-MCT/histologe/issues/5577)
- Suppression d'une référence superflue sur le FO en INJONCTION_CLOSED. [#5586](https://github.com/MTES-MCT/histologe/issues/5586)
- Mise à jour des paquets npm. [#5665](https://github.com/MTES-MCT/histologe/pull/5665)
- Amélioration de l'accessibilité de l'espace documentaire. [#5677](https://github.com/MTES-MCT/histologe/issues/5677)
- Correction de l'affichage des noms dans le module service secours. [#5691](https://github.com/MTES-MCT/histologe/issues/5691)
- Correction d'une contrainte d'invariant fiscal dans l'édition FO. [#5691](https://github.com/MTES-MCT/histologe/issues/5691)
- Ajout d'un paramètre `findAllList`. [#5685](https://github.com/MTES-MCT/histologe/issues/5685)
