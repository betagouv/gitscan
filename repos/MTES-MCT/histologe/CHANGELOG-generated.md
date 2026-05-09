## Changelog : histologe (30 derniers jours, au 06 mai 2026)

### Résumé
Ce mois-ci, les évolutions se concentrent sur l'amélioration de la qualité des données, la correction de bugs et l'accessibilité de l'application. Des améliorations ont été apportées à la synchronisation des données Esabora SCHS, à l'affichage des dates et heures, ainsi qu'à l'expérience utilisateur générale, notamment au niveau du tableau de bord et des formulaires. Des mises à jour techniques ont également été effectuées pour optimiser les performances et la sécurité.

### Évolutions fonctionnelles
- **Esabora SCHS :** Fiabilisation du mapping des réponses Esabora SCHS pour une meilleure intégration des données. [#5821](https://github.com/MTES-MCT/histologe/issues/5821)
- **Date et heure :** Affichage correct de la date et de l'heure des événements en tenant compte du fuseau horaire de l'utilisateur sur les emails et le tableau de bord. [#5778](https://github.com/MTES-MCT/histologe/issues/5785)
- **Visites :** Ajout de l'heure dans le suivi des visites programmées. [#5759](https://github.com/MTES-MCT/histologe/issues/5759)
- **Tableau de bord :** Amélioration de l'accessibilité du tableau de bord, notamment en permettant le zoom sur les avatars et les libellés des liens. [#5737](https://github.com/MTES-MCT/histologe/issues/5737) et [#5732](https://github.com/MTES-MCT/histologe/issues/5732)
- **Données photos :** Préservation des données EXIF des photos. [#5702](https://github.com/MTES-MCT/histologe/issues/5702)
- **Rappels d'événements :** Ajout d'emails de rappel d'événements liés au widget du tableau de bord. [#5683](https://github.com/MTES-MCT/histologe/issues/5683)
- **Affectation :** Rafraîchissement de la modale après une action AJAX. [#5691](https://github.com/MTES-MCT/histologe/issues/5691)
- **Fiche BO :** Affichage de la valeur structure déclarant dès qu'elle est renseignée. [#5699](https://github.com/MTES-MCT/histologe/issues/5703)
- **Chargement des données :** Amélioration du chargement des données après édition en back-office et messages flash AJAX. [#5546](https://github.com/MTES-MCT/histologe/issues/5695)

### Évolutions techniques
- **Mise à jour PHPUnit :** Mise à jour de PHPUnit de la version 9 vers la version 13. [#5766](https://github.com/MTES-MCT/histologe/issues/5766)
- **Refactoring :** Déplacement des méthodes liées aux statistiques vers un service dédié (query service). [#5711](https://github.com/MTES-MCT/histologe/issues/5711)
- **Mise à jour MySQL et Redis :** Mise à jour des versions de MySQL et Redis. [#5700](https://github.com/MTES-MCT/histologe/issues/5700)
- **Mise à jour PostCSS :** Mise à jour de la librairie PostCSS. [#5809](https://github.com/MTES-MCT/histologe/issues/5810)
- **Mise à jour Axios :** Mise à jour de la librairie Axios. [#5816](https://github.com/MTES-MCT/histologe/issues/5824)
- **Mise à jour phpspreadsheet :** Mise à jour de la librairie phpspreadsheet. [#5712](https://github.com/MTES-MCT/histologe/issues/5716)
- **Configuration CI :** Ajout d'un fichier d'environnement pour la CI. [#5670](https://github.com/MTES-MCT/histologe/issues/5717)
- **Nginx :** Mise à jour de la configuration Nginx. [#5739](https://github.com/MTES-MCT/histologe/issues/5739)

### Autres changements
- **Déconnexion OILHI :** Déconnexion de l'interconnexion avec OILHI. [#5688](https://github.com/MTES-MCT/histologe/issues/5688)
- **Corrections de bugs :** Correction de la pagination des connexions SI. [#5755](https://github.com/MTES-MCT/histologe/issues/5758)
- **Gestion des doublons Esabora SCHS :** Gestion de la resynchronisation en cas de doublon pour les visites Esabora SCHS. [#5725](https://github.com/MTES-MCT/histologe/issues/5725)
- **Ajout de phrases de contexte :** Ajout de phrases de contexte dans le back-office. [#5696](https://github.com/MTES-MCT/histologe/issues/5696)
- **Ajout de tests :** Ajout de tests sur la page de suivi usager. [#5709](https://github.com/MTES-MCT/histologe/issues/5709)
- **Optimisation du comptage :** Optimisation du comptage pour le panneau "Dossiers fermés par les communes". [#5735](https://github.com/MTES-MCT/histologe/issues/5736)
