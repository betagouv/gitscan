## Changelog : histologe (30 derniers jours, au 23 avril 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de l'expérience utilisateur dans le back-office (BO) et le front-office (FO), notamment au niveau des formulaires, des tableaux de bord et des signalements. Des corrections de bugs et des optimisations techniques ont également été apportées pour améliorer la performance et la stabilité de la plateforme. L'intégration avec Santé Habitat a été améliorée, et des mises à jour de sécurité ont été effectuées.

### Évolutions fonctionnelles
- Ajout de l'heure dans le suivi de visite programmée dans le BO. [#5759](https://github.com/MTES-MCT/histologe/issues/5759)
- Correction de la pagination des connexions SI dans le BO. [#5758](https://github.com/MTES-MCT/histologe/issues/5758)
- Gestion de la resynchronisation des messages, notamment pour Esabora SCHS. [#5756](https://github.com/MTES-MCT/histologe/issues/5756)
- Ajout d'un filtre pour les événements dans le BO. [#5740](https://github.com/MTES-MCT/histologe/issues/5740)
- Amélioration de l'accessibilité du zoom sur l'avatar et le libellé des dossiers dans le BO. [#5737](https://github.com/MTES-MCT/histologe/issues/5737)
- Préservation des données EXIF des photos. [#5702](https://github.com/MTES-MCT/histologe/issues/5702)
- Amélioration de l'accessibilité du tableau de bord dans le BO (passage d'onglet au clavier, etc.). [#5734](https://github.com/MTES-MCT/histologe/issues/5734) et [#5732](https://github.com/MTES-MCT/histologe/issues/5732)
- Ajout de mails de rappel d'événements liés au widget du dashboard. [#5683](https://github.com/MTES-MCT/histologe/issues/5683)
- Ajout de badges indiquant l'EPCI lié à la commune dans le BO. [#5682](https://github.com/MTES-MCT/histologe/issues/5682)
- Ajout de phrases de contexte dans le BO pour une meilleure compréhension. [#5696](https://github.com/MTES-MCT/histologe/issues/5696)
- Possibilité pour les RT de supprimer les documents uploadés par un partenaire (cas Esabora). [#5636](https://github.com/MTES-MCT/histologe/issues/5636)
- Ajout d'un bouton annuler pour réinitialiser la saisie dans le formulaire service secours. [#5607](https://github.com/MTES-MCT/histologe/issues/5607)
- Amélioration des données affichées sur les pages du service secours. [#5557](https://github.com/MTES-MCT/histologe/issues/5557)
- Ajout de la catégorie "Affectation en attente" au dashboard du BO. [#5606](https://github.com/MTES-MCT/histologe/issues/5606)
- Possibilité de définir des EPCI sur le périmètre des partenaires. [#5636](https://github.com/MTES-MCT/histologe/issues/5636)

### Évolutions techniques
- Mise à jour de MySQL et Redis. [#5700](https://github.com/MTES-MCT/histologe/issues/5700)
- Déplacement des méthodes de calcul de statistiques vers un query service. [#5711](https://github.com/MTES-MCT/histologe/issues/5711)
- Mise à jour de la librairie Intervention\Image vers la version 4. [#5657](https://github.com/MTES-MCT/histologe/issues/5657)
- Mise à jour des paquets npm. [#5665](https://github.com/MTES-MCT/histologe/issues/5665)
- Optimisation du calcul du nombre de dossiers fermés par les communes. [#5736](https://github.com/MTES-MCT/histologe/issues/5736)
- Création d'une factory spécifique pour le service secours et ajout de tests fonctionnels. [#5633](https://github.com/MTES-MCT/histologe/issues/5633)
- Suppression de code mort. [#5673](https://github.com/MTES-MCT/histologe/issues/5673)
- Normalisation des données et suppression des champs en doublon. [#5601](https://github.com/MTES-MCT/histologe/issues/5601)
- Mise en place d'un fichier d'environnement CI. [#5717](https://github.com/MTES-MCT/histologe/issues/5717)
- Mise à jour de phpspreadsheet. [#5716](https://github.com/MTES-MCT/histologe/issues/5716)
- Réorganisation des services dans des sous-dossiers. [#5690](https://github.com/MTES-MCT/histologe/issues/5690)
- Mise à jour de la dépendance `follow-redirects` en npm. [#5730](https://github.com/MTES-MCT/histologe/issues/5730)
- Mise à jour de la dépendance `picomatch` en npm. [#5624](https://github.com/MTES-MCT/histologe/issues/5624)
- Amélioration de la gestion de la déconnexion OILHI. [#5688](https://github.com/MTES-MCT/histologe/issues/5688)

### Autres changements
- Correction de bugs mineurs et améliorations de l'interface utilisateur.
- Ajout de tests unitaires et fonctionnels.
- Amélioration de la documentation.
- Correction de la validation des numéros de téléphone dans le FO. [#5661](https://github.com/MTES-MCT/histologe/issues/5661)
- Correction de l'affichage des infobulles dans le BO. [#5658](https://github.com/MTES-MCT/histologe/issues/5658)
- Correction de l'archivage des brouillons et de la gestion des adresses libres inconnues. [#5674](https://github.com/MTES-MCT/histologe/issues/5674)
- Correction d'un bug empêchant l'édition du formulaire FO pour certains profils. [#5644](https://github.com/MTES-MCT/histologe/issues/5644)
- Correction d'un bug d'affichage du nom du service secours. [#5691](https://github.com/MTES-MCT/histologe/issues/5691)
- Correction d'un problème de rafraîchissement de la modale après un flash ajax. [#5695](https://github.com/MTES-MCT/histologe/issues/5695)
- Correction d'un problème de chargement des données après édition dans le BO. [#5695](https://github.com/MTES-MCT/histologe/issues/5695)
- Suppression des jobs évènements après 1 mois. [#5647](https://github.com/MTES-MCT/histologe/issues/5647)
- Correction d'un problème d'export CSV. [#5635](https://github.com/MTES-MCT/histologe/issues/5635)
- Correction d'un problème lié à leaflet et au referrerPolicy. [#5617](https://github.com/MTES-MCT/histologe/issues/5617)
- Correction de l'affichage des données sur le suivi usager. [#5660](https://github.com/MTES-MCT/histologe/issues/5660)
- Correction de l'affichage de la valeur du déclarant dans la fiche BO. [#5703](https://github.com/MTES-MCT/histologe/issues/5703)
- Limitation de l'envoi vers Santé Habitat à un seul par SCHS. [#5686](https://github.com/MTES-MCT/histologe/issues/5686)
- Autorisation des partenaires SCHS à envoyer des dossiers à Santé Habitat. [#5686](https://github.com/MTES-MCT/histologe/issues/5686)
