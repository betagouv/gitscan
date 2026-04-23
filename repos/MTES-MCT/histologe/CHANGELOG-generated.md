## Changelog : histologe (30 derniers jours, au 17 avril 2026)

### Résumé
Ce mois-ci, l'équipe a continué d'améliorer l'application histologe, en se concentrant sur l'expérience utilisateur, notamment dans les formulaires de signalement et de service secours. Des corrections de bugs et des optimisations ont été apportées, ainsi que des améliorations techniques pour la gestion des données et l'infrastructure. Des fonctionnalités ont été ajoutées pour faciliter le travail des agents et des partenaires, notamment concernant la gestion des EPCI et l'envoi de dossiers à Santé Habitat.

### Évolutions fonctionnelles
- Amélioration du formulaire "Service Secours" : ajout de qualifications, d'un bouton d'annulation pour réinitialiser la saisie, et intégration du champ "autresOccupantsDesordre" ainsi qu'un filtre de provenance [#5632](https://github.com/MTES-MCT/histologe/issues/5632).
- Ajout d'un badge dans le back-office pour indiquer l'EPCI lié à la commune [#5682](https://github.com/MTES-MCT/histologe/issues/5682).
- Possibilité de définir des EPCI sur le périmètre des partenaires [#5587](https://github.com/MTES-MCT/histologe/issues/5587).
- Amélioration de l'affichage de la valeur "structure déclarant" dans le back-office dès qu'elle est renseignée [#5699](https://github.com/MTES-MCT/histologe/issues/5699).
- Ajout de la conclusion de visite "Suspicion d'insalubrité" dans le back-office [#5603](https://github.com/MTES-MCT/histologe/issues/5603).
- Correction de la validation de plusieurs champs dans le formulaire de signalement (front-office) [#5583](https://github.com/MTES-MCT/histologe/issues/5583).
- Possibilité pour les RT de supprimer les documents uploadés par un partenaire, même sans valeur "uploadedBy" [#5588](https://github.com/MTES-MCT/histologe/issues/5588).
- Ajout d'une fonctionnalité pour arrêter une procédure dans la démarche accélérée [#5640](https://github.com/MTES-MCT/histologe/issues/5640).
- Limitation à un seul envoi vers Santé Habitat et autorisation pour les partenaires SCHS d'envoyer des dossiers [#5574](https://github.com/MTES-MCT/histologe/issues/5574).
- Amélioration de l'affichage des infobulles dans le back-office [#5658](https://github.com/MTES-MCT/histologe/issues/5658).
- Correction du validateur de numéros de téléphone dans le suivi de signalement (front-office) [#5661](https://github.com/MTES-MCT/histologe/issues/5661).

### Évolutions techniques
- Mise à jour de la librairie Intervention\Image à la version 4 [#5657](https://github.com/MTES-MCT/histologe/issues/5657).
- Suppression de code mort pour améliorer la maintenabilité [#5673](https://github.com/MTES-MCT/histologe/issues/5673).
- Amélioration de l'accessibilité de l'espace documentaire [#5677](https://github.com/MTES-MCT/histologe/issues/5677).
- Refactorisation des requêtes pour le dashboard du back-office vers un query service [#5646](https://github.com/MTES-MCT/histologe/issues/5646).
- Mise à jour des paquets npm [#5665](https://github.com/MTES-MCT/histologe/issues/5665) et [#5642](https://github.com/MTES-MCT/histologe/issues/5642).
- Correction d'un problème de rechargement de panel après une erreur 404 [#5662](https://github.com/MTES-MCT/histologe/issues/5662).
- Correction d'un problème avec le referrerPolicy pour résoudre une erreur leaflet [#5609](https://github.com/MTES-MCT/histologe/issues/5609).
- Ajout de tests fonctionnels et création d'une factory spécifique pour le service secours [#5633](https://github.com/MTES-MCT/histologe/issues/5633).

### Autres changements
- Correction de bugs mineurs et améliorations de l'interface utilisateur [#5691](https://github.com/MTES-MCT/histologe/issues/5691), [#5617](https://github.com/MTES-MCT/histologe/issues/5617).
- Correction de l'édition des profils Bailleurs/Bailleurs Occupants et remplacement du wording "Bailleur occupant" [#5652](https://github.com/MTES-MCT/histologe/issues/5652).
- Changement de l'ordre d'affichage des photos [#5602](https://github.com/MTES-MCT/histologe/issues/5602).
- Gestion de la mise à vide d'un mail occupant via l'édition front-office [#5645](https://github.com/MTES-MCT/histologe/issues/5645).
- Correction d'un bug dans l'édition du champ "infoProcedureBailMoyen" [#5610](https://github.com/MTES-MCT/histologe/issues/5610).
- Finalisation de l'affichage après enregistrement du formulaire police [#5552](https://github.com/MTES-MCT/histologe/issues/5552).
- Finalisation de l'étape récapitulatif avant soumission du formulaire police [#5591](https://github.com/MTES-MCT/histologe/issues/5591).
- Suppression des jobs_event après 1 mois [#5509](https://github.com/MTES-MCT/histologe/issues/5509).
- Normalisation des données et suppression des champs en doublon [#5601](https://github.com/MTES-MCT/histologe/issues/5601).
- Ajout d'un lien pour supprimer le filtre "MySignalementsOnlyFilter" [#5611](https://github.com/MTES-MCT/histologe/issues/5611).
- Pagination des dernières actions dans le dashboard du back-office [#5606](https://github.com/MTES-MCT/histologe/issues/5606).
- Correction de l'export CSV du header [#5634](https://github.com/MTES-MCT/histologe/issues/5634).
